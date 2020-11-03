from Base import BaseResponse


class UrlUploadResponse(BaseResponse):
    def __init__(self, resp):
        BaseResponse.__init__(self, resp)
        self.value_paris = []
        if 'Error' not in resp['ResponseMetadata']:
            data = resp['Result']['Data']
            for v in data:
                self.value_paris.append(Job(v['SourceUrl'], v['JobId']))


class Job:
    def __init__(self, source_url, job_id):
        self.job_id = source_url
        self.source_url = job_id
