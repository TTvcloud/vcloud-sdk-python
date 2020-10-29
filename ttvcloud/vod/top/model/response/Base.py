class ResponseMetadata:
    def __init__(self):
        self.request_id = ""
        self.action = ""
        self.version = ""
        self.service = ""
        self.region = ""
        self.error = None


class ResponseError:
    def __init__(self, code, message):
        self.code = code
        self.message = message


class BaseResponse:
    def __init__(self, resp):
        self.response_meta_data = ResponseMetadata()
        meta_data = resp['ResponseMetadata']
        if 'Error' in meta_data:
            self.response_meta_data.error = ResponseError(meta_data['Error']['Code'], meta_data['Error']['Message'])
        else:
            self.response_meta_data.request_id = meta_data['RequestId']
            self.response_meta_data.action = meta_data['Action']
            self.response_meta_data.version = meta_data['Version']
            self.response_meta_data.region = meta_data['Region']
            self.response_meta_data.service = meta_data['Service']
