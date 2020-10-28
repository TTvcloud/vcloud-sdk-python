from Base import BaseResponse


class QueryDataResponse(BaseResponse):
    def __init__(self, resp):
        BaseResponse.__init__(self, resp)
        self.video_info_list = []
        self.not_exist_job_ids = []
        if 'Error' not in resp['ResponseMetadata']:
            data = resp['Result']['Data']
            video_info_list = data['VideoInfoList']
            self.not_exist_job_ids = data['NotExistJobIds']
            for v in video_info_list:
                u = URLSet()
                u.request_id = v['RequestId']
                u.job_id = v['JobId']
                u.state = v['State']
                u.vid = v['Vid']
                u.space_name = v['SpaceName']
                u.account_id = v['AccountId']
                u.source_info.store_uri = v.get('StoreUri')
                u.source_info.md5 = v.get('Md5')
                u.source_info.width = v.get('Width')
                u.source_info.height = v.get('Height')
                u.source_info.duration = v.get('Duration')
                u.source_info.bitrate = v.get('Bitrate')
                u.source_info.format = v.get('Format')
                u.source_info.size = v.get('Size')
                u.source_info.file_type = v.get('FileType')
                self.video_info_list.append(u)


class URLSet:
    def __init__(self):
        self.request_id = ""
        self.job_id = ""
        self.source_url = ""
        self.state = ""
        self.vid = ""
        self.space_name = ""
        self.account_id = ""
        self.source_info = SourceInfo()
        self.extra = None


class SourceInfo:
    def __init__(self):
        self.store_uri = ""
        self.md5 = ""
        self.width = ""
        self.height = ""
        self.duration = ""
        self.bitrate = ""
        self.format = ""
        self.size = ""
        self.file_type = ""
        self.extra = None
