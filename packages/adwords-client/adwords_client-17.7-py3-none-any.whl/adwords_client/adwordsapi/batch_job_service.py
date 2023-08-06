import logging
from collections import OrderedDict

import googleads

from . import common as cm

logger = logging.getLogger(__name__)


class BatchJobHelper(googleads.adwords.BatchJobHelper, cm.SudsFactory):

    def __init__(self, service):
        request_builder = BatchJobHelper.GetRequestBuilder(client=service.client)
        response_parser = BatchJobHelper.GetResponseParser()
        super().__init__(request_builder=request_builder, response_parser=response_parser)
        self.suds_client = service.suds_client
        self.operations = OrderedDict()     # Should honor the operation type insertion order
        self.last_operation = None
        self.upload_helper = self.GetIncrementalUploadHelper(service.batch_job[0].uploadUrl.url)
        self._last_temporary_id = 0

    def __getitem__(self, op_type, item):
        return self.operations[op_type][item]

    def add_operation(self, operation):
        if operation['xsi_type'] in self.operations:
            self.operations[operation['xsi_type']].append(operation)
        else:
            self.operations[operation['xsi_type']] = [operation]
        self.last_operation = operation

    def get_temporary_id(self):
        """
        Get next Temporary ID for adwords objects on this BatchJobService operations

        Dependent operations are applied in the order they appear in your upload.
        Therefore, when using temporary IDs, make sure the operation that creates a parent object
        comes before the operations that create its child objects.
        See: https://developers.google.com/adwords/api/docs/guides/batch-jobs?#using_temporary_ids
        """
        # TODO: Protect this with locks?
        self._last_temporary_id -= 1
        return self._last_temporary_id

    def add_biddable_adgroup_criterion_operation(self,
                                                 adgroup_id,
                                                 operator,
                                                 xsi_type,
                                                 criteria_id=None,
                                                 criterion_params={},
                                                 **kwargs):
        criterion = {'xsi_type': xsi_type}
        if criteria_id:
            criterion['id'] = criteria_id
        for key in criterion_params:
            criterion[key] = criterion_params[key]

        operand = {
            'xsi_type': 'BiddableAdGroupCriterion',
            'criterion': criterion,
            'adGroupId': adgroup_id,
        }
        for key in kwargs:
            operand[key] = kwargs[key]

        operation = {
            'xsi_type': 'AdGroupCriterionOperation',
            'operand': operand,
            'operator': operator
        }
        self.add_operation(operation)

    def add_adgroup_operation(self, campaign_id, adgroup_id, operator):
        operation = {
            'xsi_type': 'AdGroupOperation',
            'operand': {
                'xsi_type': 'AdGroup',
                'campaignId': campaign_id,
                'id': adgroup_id,
            },
            'operator': operator,
        }
        self.add_operation(operation)

    def add_bidding_strategy_configuration(self, xsi_type, value):
        if 'biddingStrategyConfiguration' not in self.last_operation['operand']:
            bidding_strategy = {'xsi_type': 'BiddingStrategyConfiguration', 'bids': []}
            self.last_operation['operand']['biddingStrategyConfiguration'] = bidding_strategy
        bid_type = {'xsi_type': xsi_type}
        bid_type['bid'] = {'xsi_type': 'Money'}
        bid_type['bid']['microAmount'] = value
        self.last_operation['operand']['biddingStrategyConfiguration']['bids'].append(bid_type)

    def add_campaign_label_operation(self, campaign_id, operator, label_id):
        operation = {
            'xsi_type': 'CampaignLabelOperation',
            'operator': operator,
            'operand': {'xsi_type': 'CampaignLabel',
                        'campaignId': campaign_id,
                        'labelId': label_id}
        }
        self.add_operation(operation)

    def upload_operations(self, is_last=False):
        fail_counter = 0
        done = True
        while done:
            try:
                if is_last:
                    logger.info('Uploading final data...')
                else:
                    logger.info('Uploading intermediate data...')
                self.upload_helper.UploadOperations(list(self.operations.values()), is_last=is_last)
                self.operations = {}
                self.last_operation = None
                done = False
            except Exception as e:
                fail_counter += 1
                if fail_counter > 2:
                    logger.error('Problem uploading the data, failure...')
                    raise e
                logger.error('Problem uploading the data, retrying...')


class BatchJobOperations(cm.SudsFactory):
    def __init__(self, service):
        self.suds_client = service.suds_client
        self.operations = []

    def __getitem__(self, item):
        return self.operations[item]

    def add_batch_job_operation(self, operator, id_=None, status=None):
        batch_job = self.get_object('BatchJob', 'cm')
        batch_job.id = id_
        batch_job.status = status

        operation = self.get_object('BatchJobOperation', 'cm')
        operation.operator = operator
        operation.operand = batch_job
        self.operations.append(operation)


class BatchJobService(cm.BaseService):
    def __init__(self, client):
        super().__init__(client, 'BatchJobService')
        self.batch_job = None
        self.helper = None

    def get_wholeoperation_id(self):
        try:
            return self.batch_job[0].id
        except IndexError:
            raise RuntimeError('No operations queued. No "whole operation" id created')

    def prepare_mutate(self):
        self.helper = BatchJobOperations(self.service)
        self.ResultProcessor = cm.SimpleReturnValue

    def prepare_job(self, client_customer_id=None):
        self.prepare_mutate()
        self.helper.add_batch_job_operation('ADD')
        self.batch_job = self.mutate(client_customer_id)
        self.helper = BatchJobHelper(self)

    def cancel_jobs(self, jobs):
        result = {}
        for client_id in jobs:
            self.prepare_mutate()
            for job in jobs[client_id]:
                if job['status'] not in ['DONE', 'CANCELING', 'CANCELED']:
                    self.helper.add_batch_job_operation('SET', job['id'], 'CANCELING')
            result[client_id] = self.mutate(client_id) if len(self.helper.operations) > 0 else None
        return result

        self.helper = BatchJobOperations(self.service)
        self.helper.add_batch_job_operation('SET')
        self.ResultProcessor = cm.SimpleReturnValue
        return

    def get_status(self, batch_job_id, client_customer_id=None):
        self.prepare_get()
        self.helper.add_fields('DownloadUrl', 'Id', 'ProcessingErrors', 'ProgressStats', 'Status')
        self.helper.add_predicate('Id', 'EQUALS', [batch_job_id])
        return next(iter(self.get(client_customer_id)))

    def get_multiple_status(self, jobs):
        result = {}
        for client_id in jobs:
            self.prepare_get()
            self.helper.add_fields('DownloadUrl', 'Id', 'ProcessingErrors', 'ProgressStats', 'Status')
            self.helper.add_predicate('Id', 'IN', [job for job in jobs[client_id]])
            result[client_id] = list(self.get(client_id))
        return result
