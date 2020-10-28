from Base import BaseResponse
from QueryDataResponse import SourceInfo


class UploadVideoResponse(BaseResponse):
    def __init__(self, resp):
        BaseResponse.__init__(self, resp)
        self.vid = ""
        self.poster_uri = ""
        self.callback_args = ""
        self.source_info = SourceInfo()
        self.encryption = Encryption()
        if 'Error' not in resp['ResponseMetadata']:
            data = resp['Result']['Data']
            self.vid = data.get('Vid')
            self.poster_uri = data.get('PosterUri')
            self.callback_args = data.get('CallbackArgs')
            if 'SourceInfo' in data:
                source_info = data['SourceInfo']
                self.source_info.store_uri = source_info.get('StoreUri')
                self.source_info.md5 = source_info.get('Md5')
                self.source_info.width = source_info.get('Width')
                self.source_info.height = source_info.get('Height')
                self.source_info.duration = source_info.get('Duration')
                self.source_info.bitrate = source_info.get('Bitrate')
                self.source_info.format = source_info.get('Format')
                self.source_info.size = source_info.get('Size')
                self.source_info.file_type = source_info.get('FileType')
            if 'Encryption' in data:
                encryption = data['Encryption']
                self.encryption.uri = encryption.get('Uri')
                self.encryption.secret_key = encryption.get('SecretKey')
                self.encryption.algorithm = encryption.get('Algorithm')
                self.encryption.version = encryption.get('Version')
                self.encryption.source_md5 = encryption.get('SourceMd5')


class Encryption:
    def __init__(self):
        self.uri = ""
        self.secret_key = ""
        self.algorithm = ""
        self.version = ""
        self.source_md5 = ""
        self.extra = dict()
