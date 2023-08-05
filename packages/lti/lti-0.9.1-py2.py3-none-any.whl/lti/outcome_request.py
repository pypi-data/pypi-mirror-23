from collections import defaultdict
from lxml import etree, objectify

import requests
from requests_oauthlib import OAuth1
from requests_oauthlib.oauth1_auth import SIGNATURE_TYPE_AUTH_HEADER

from .outcome_response import OutcomeResponse
from .utils import InvalidLTIConfigError

REPLACE_REQUEST = 'replaceResult'
DELETE_REQUEST = 'deleteResult'
READ_REQUEST = 'readResult'

VALID_ATTRIBUTES = [
    'operation',
    'score',
    'result_data',
    'outcome_response',
    'message_identifier',
    'lis_outcome_service_url',
    'lis_result_sourcedid',
    'consumer_key',
    'consumer_secret',
    'post_request'
]


class OutcomeRequest(object):
    '''
    Class for consuming & generating LTI Outcome Requests.

    Outcome Request documentation:
        http://www.imsglobal.org/LTI/v1p1/ltiIMGv1p1.html#_Toc319560472

    This class can be used both by Tool Providers and Tool Consumers, though
    they each use it differently. The TP will use it to POST an OAuth-signed
    request to the TC. A TC will use it to parse such a request from a TP.
    '''
    def __init__(self, opts=defaultdict(lambda: None)):
        # Initialize all our accessors to None
        for attr in VALID_ATTRIBUTES:
            setattr(self, attr, None)

        # Store specified options in our accessors
        for (key, val) in opts.items():
            if key in VALID_ATTRIBUTES:
                setattr(self, key, val)
            else:
                raise InvalidLTIConfigError(
                    "Invalid outcome request option: {}".format(key)
                )

    @staticmethod
    def from_post_request(post_request):
        '''
        Convenience method for creating a new OutcomeRequest from a request
        object.

        post_request is assumed to be a Django HttpRequest object
        '''
        request = OutcomeRequest()
        request.post_request = post_request
        request.process_xml(post_request.body)
        return request

    def post_replace_result(self, score, result_data=None):
        '''
        POSTs the given score to the Tool Consumer with a replaceResult.

        OPTIONAL:
            result_data must be a dictionary
            Note: ONLY ONE of these values can be in the dict at a time,
            due to the Canvas specification.

            'text' : str text
            'url' : str url
        '''
        self.operation = REPLACE_REQUEST
        self.score = score
        self.result_data = result_data
        if result_data is not None:
            if len(result_data) > 1:
                error_msg = ('Dictionary result_data can only have one entry. '
                             '{0} entries were found.'.format(len(result_data)))
                raise InvalidLTIConfigError(error_msg)
            elif 'text' not in result_data and 'url' not in result_data:
                error_msg = ('Dictionary result_data can only have the key '
                             '"text" or the key "url".')
                raise InvalidLTIConfigError(error_msg)
            else:
                return self.post_outcome_request()
        else:
            return self.post_outcome_request()

    def post_delete_result(self):
        '''
        POSTs a deleteRequest to the Tool Consumer.
        '''
        self.operation = DELETE_REQUEST
        return self.post_outcome_request()

    def post_read_result(self):
        '''
        POSTS a readResult to the Tool Consumer.
        '''
        self.operation = READ_REQUEST
        return self.post_outcome_request()

    def is_replace_request(self):
        '''
        Check whether this request is a replaceResult request.
        '''
        return self.operation == REPLACE_REQUEST

    def is_delete_request(self):
        '''
        Check whether this request is a deleteResult request.
        '''
        return self.operation == DELETE_REQUEST

    def is_read_request(self):
        '''
        Check whether this request is a readResult request.
        '''
        return self.operation == READ_REQUEST

    def was_outcome_post_successful(self):
        return self.outcome_response and self.outcome_response.is_success()

    def post_outcome_request(self, **kwargs):
        '''
        POST an OAuth signed request to the Tool Consumer.
        '''
        if not self.has_required_attributes():
            raise InvalidLTIConfigError(
                'OutcomeRequest does not have all required attributes')

        header_oauth = OAuth1(self.consumer_key, self.consumer_secret,
                              signature_type=SIGNATURE_TYPE_AUTH_HEADER,
                              force_include_body=True, **kwargs)

        headers = {'Content-type': 'application/xml'}
        resp = requests.post(self.lis_outcome_service_url, auth=header_oauth,
                             data=self.generate_request_xml(),
                             headers=headers)
        outcome_resp = OutcomeResponse.from_post_response(resp, resp.content)
        self.outcome_response = outcome_resp
        return self.outcome_response

    def process_xml(self, xml):
        '''
        Parse Outcome Request data from XML.
        '''
        root = objectify.fromstring(xml)
        self.message_identifier = str(
            root.imsx_POXHeader.imsx_POXRequestHeaderInfo.
            imsx_messageIdentifier)
        try:
            result = root.imsx_POXBody.replaceResultRequest
            self.operation = REPLACE_REQUEST
            # Get result sourced id from resultRecord
            self.lis_result_sourcedid = result.resultRecord.\
                sourcedGUID.sourcedId
            self.score = str(result.resultRecord.result.
                             resultScore.textString)
        except:
            pass

        try:
            result = root.imsx_POXBody.deleteResultRequest
            self.operation = DELETE_REQUEST
            # Get result sourced id from resultRecord
            self.lis_result_sourcedid = result.resultRecord.\
                sourcedGUID.sourcedId
        except:
            pass

        try:
            result = root.imsx_POXBody.readResultRequest
            self.operation = READ_REQUEST
            # Get result sourced id from resultRecord
            self.lis_result_sourcedid = result.resultRecord.\
                sourcedGUID.sourcedId
        except:
            pass

    def has_required_attributes(self):
        return self.consumer_key is not None\
            and self.consumer_secret is not None\
            and self.lis_outcome_service_url is not None\
            and self.lis_result_sourcedid is not None\
            and self.operation is not None

    def generate_request_xml(self):
        root = etree.Element(
            'imsx_POXEnvelopeRequest',
            xmlns='http://www.imsglobal.org/services/ltiv1p1/xsd/imsoms_v1p0')

        header = etree.SubElement(root, 'imsx_POXHeader')
        header_info = etree.SubElement(header, 'imsx_POXRequestHeaderInfo')
        version = etree.SubElement(header_info, 'imsx_version')
        version.text = 'V1.0'
        message_identifier = etree.SubElement(header_info,
                                              'imsx_messageIdentifier')
        message_identifier.text = self.message_identifier
        body = etree.SubElement(root, 'imsx_POXBody')
        request = etree.SubElement(body, '%s%s' % (self.operation,
                                                   'Request'))
        record = etree.SubElement(request, 'resultRecord')

        guid = etree.SubElement(record, 'sourcedGUID')

        sourcedid = etree.SubElement(guid, 'sourcedId')
        sourcedid.text = self.lis_result_sourcedid

        if self.score is not None:
            result = etree.SubElement(record, 'result')
            result_score = etree.SubElement(result, 'resultScore')
            language = etree.SubElement(result_score, 'language')
            language.text = 'en'
            text_string = etree.SubElement(result_score, 'textString')
            text_string.text = self.score.__str__()

        if self.result_data:
            resultData = etree.SubElement(result, 'resultData')
            if 'text' in self.result_data:
                resultDataText = etree.SubElement(resultData, 'text')
                resultDataText.text = self.result_data['text']
            elif 'url' in self.result_data:
                resultDataURL = etree.SubElement(resultData, 'url')
                resultDataURL.text = self.result_data['url']

        return etree.tostring(root, xml_declaration=True, encoding='utf-8')
