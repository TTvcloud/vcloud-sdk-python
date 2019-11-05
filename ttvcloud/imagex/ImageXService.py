# coding:utf-8

from __future__ import print_function

import json
import os

from ttvcloud.ApiInfo import ApiInfo
from ttvcloud.Credentials import Credentials
from ttvcloud.ServiceInfo import ServiceInfo
from ttvcloud.base.Service import Service
from ttvcloud.const.Const import *
from ttvcloud.util.Util import Util

IMAGEX_HOST_CN = "imagex.bytedanceapi.com"
IMAGEX_HOST_VA = "imagex.us-east-1.bytedanceapi.com"
IMAGEX_HOST_SG = "imagex.ap-singapore-1.bytedanceapi.com"

IMAGEX_SERVICE_NAME = "ImageX"
IMAGEX_API_VERSION = "2018-08-01"

service_info_map = {
    REGION_CN_NORTH1: ServiceInfo(
        IMAGEX_HOST_CN,
        {'Accept': 'application/json'},
        Credentials('', '', IMAGEX_SERVICE_NAME, REGION_CN_NORTH1),
        5000, 5000),
    REGION_AP_SINGAPORE1: ServiceInfo(
        IMAGEX_HOST_SG,
        {'Accept': 'application/json'},
        Credentials('', '', IMAGEX_SERVICE_NAME, REGION_AP_SINGAPORE1),
        5000, 5000),
    REGION_US_EAST1: ServiceInfo(
        IMAGEX_HOST_VA,
        {'Accept': 'application/json'},
        Credentials('', '', IMAGEX_SERVICE_NAME, REGION_US_EAST1),
        5000, 5000),
}

api_info = {
    "ApplyUploadImageFile":
        ApiInfo("GET", "/", {"Action": "ApplyUploadImageFile", "Version": IMAGEX_API_VERSION}, {}, {}),
    "CommitUploadImageFile":
        ApiInfo("POST", "/", {"Action": "CommitUploadImageFile", "Version": IMAGEX_API_VERSION}, {}, {}),
}


class ImageXService(Service):
    def __init__(self, region='cn-north-1'):
        self.service_info = ImageXService.get_service_info(region)
        self.api_info = ImageXService.get_api_info()
        super(ImageXService, self).__init__(self.service_info, self.api_info)

    @staticmethod
    def get_service_info(region):
        service_info = service_info_map.get(region, None)
        if not service_info:
            raise Exception('Cant find the region %s, please check it carefully' % region)
        return service_info

    @staticmethod
    def get_api_info():
        return api_info

    # upload
    def apply_upload(self, params):
        res = self.get('ApplyUploadImageFile', params, doseq=1)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json

    def commit_upload(self, params, body):
        res = self.json('CommitUploadImageFile', params, body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json

    def upload_image(self, service_id, file_paths, keys):
        for p in file_paths:
            if not os.path.isfile(p):
                raise Exception("no such file on file path %s" % p)

        apply_upload_request = {'ServiceId': service_id, 'UploadNum': len(file_paths), 'StoreKeys': keys}
        resp = self.apply_upload(apply_upload_request)
        if 'Error' in resp['ResponseMetadata']:
            raise Exception(resp['ResponseMetadata'])

        result = resp['Result']
        if len(result['UploadHosts']) == 0:
            raise Exception("no upload host found")
        elif len(result['StoreInfos']) != len(file_paths):
            raise Exception("store info len %d != upload num %d" % (len(result['StoreInfos']), len(file_paths)))

        session_key = result['SessionKey']
        host = result['UploadHosts'][0]
        self.do_upload(file_paths, host, result['StoreInfos'])

        commit_upload_request = {'ServiceId': service_id, 'SessionKey': session_key}
        resp = self.commit_upload(commit_upload_request, "")
        if 'Error' in resp['ResponseMetadata']:
            raise Exception(resp['ResponseMetadata'])
        return resp['Result']

    def do_upload(self, file_paths, host, store_infos):
        idx = 0
        for p in file_paths:
            oid = store_infos[idx]['StoreUri']
            auth = store_infos[idx]['Auth']
            url = 'http://{}/{}'.format(host, oid)
            headers = {'Content-CRC32': hex(Util.crc32(p))[2:], 'Authorization': auth}
            upload_status, resp = self.put(url, p, headers)
            if not upload_status:
                raise Exception("upload %s error" % url)
            idx += 1
