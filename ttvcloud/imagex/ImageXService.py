# coding:utf-8

from __future__ import print_function

import json
import os

from ttvcloud.ApiInfo import ApiInfo
from ttvcloud.Credentials import Credentials
from ttvcloud.ServiceInfo import ServiceInfo
from ttvcloud.base.Service import Service
from ttvcloud.const.Const import *
from ttvcloud.util.Util import *
from ttvcloud.Policy import *

IMAGEX_HOST_CN = "imagex.bytedanceapi.com"
IMAGEX_HOST_VA = "imagex.us-east-1.bytedanceapi.com"
IMAGEX_HOST_SG = "imagex.ap-singapore-1.bytedanceapi.com"

IMAGEX_INNER_HOST_CN = "imagex.byted.org"
IMAGEX_INNER_HOST_VA = "imagex.us-east-1.byted.org"
IMAGEX_INNER_HOST_SG = "imagex.ap-singapore-1.byted.org"

IMAGEX_SERVICE_NAME = "ImageX"
IMAGEX_API_VERSION = "2018-08-01"

ResourceServiceIdTRN = "trn:ImageX:*:*:ServiceId/%s"

service_info_map = {
    REGION_CN_NORTH1: ServiceInfo(
        IMAGEX_HOST_CN,
        {'Accept': 'application/json'},
        Credentials('', '', IMAGEX_SERVICE_NAME, REGION_CN_NORTH1),
        5000, 5000, "https"),
    REGION_AP_SINGAPORE1: ServiceInfo(
        IMAGEX_HOST_SG,
        {'Accept': 'application/json'},
        Credentials('', '', IMAGEX_SERVICE_NAME, REGION_AP_SINGAPORE1),
        5000, 5000, "https"),
    REGION_US_EAST1: ServiceInfo(
        IMAGEX_HOST_VA,
        {'Accept': 'application/json'},
        Credentials('', '', IMAGEX_SERVICE_NAME, REGION_US_EAST1),
        5000, 5000, "https"),
    INNER_REGION_CN_NORTH1: ServiceInfo(
        IMAGEX_INNER_HOST_CN,
        {'Accept': 'application/json'},
        Credentials('', '', IMAGEX_SERVICE_NAME, REGION_CN_NORTH1),
        5000, 5000),
    INNER_REGION_AP_SINGAPORE1: ServiceInfo(
        IMAGEX_INNER_HOST_SG,
        {'Accept': 'application/json'},
        Credentials('', '', IMAGEX_SERVICE_NAME, REGION_AP_SINGAPORE1),
        5000, 5000),
    INNER_REGION_US_EAST1: ServiceInfo(
        IMAGEX_INNER_HOST_VA,
        {'Accept': 'application/json'},
        Credentials('', '', IMAGEX_SERVICE_NAME, REGION_US_EAST1),
        5000, 5000),
}

api_info = {
    "ApplyImageUpload":
        ApiInfo("GET", "/", {"Action": "ApplyImageUpload", "Version": IMAGEX_API_VERSION}, {}, {}),
    "CommitImageUpload":
        ApiInfo("POST", "/", {"Action": "CommitImageUpload", "Version": IMAGEX_API_VERSION}, {}, {}),
    "UpdateImageUploadFiles":
        ApiInfo("POST", "/", {"Action": "UpdateImageUploadFiles", "Version": IMAGEX_API_VERSION}, {}, {}),
    "PreviewImageUploadFile":
        ApiInfo("GET", "/", {"Action": "PreviewImageUploadFile", "Version": IMAGEX_API_VERSION}, {}, {})
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
        res = self.get('ApplyImageUpload', params, doseq=1)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json

    def commit_upload(self, params, body):
        res = self.json('CommitImageUpload', params, body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json

    # 上传本地图片文件
    def upload_image(self, service_id, file_paths, keys=[], space_name="", functions=[]):
        img_datas = []
        for p in file_paths:
            if not os.path.isfile(p):
                raise Exception("no such file on file path %s" % p)
            in_file = open(p, "rb")
            img_datas.append(in_file.read())
            in_file.close()
        return self.upload_image_data(service_id, img_datas, keys, space_name, functions)

    # 上传图片二进制数据
    def upload_image_data(self, service_id, img_datas, keys=[], space_name="", functions=[]):
        apply_upload_request = {
            'ServiceId': service_id,
            'UploadNum': len(img_datas),
            'StoreKeys': keys,
            'SpaceName': space_name
        }
        resp = self.apply_upload(apply_upload_request)
        if 'Error' in resp['ResponseMetadata']:
            raise Exception(resp['ResponseMetadata'])

        result = resp['Result']
        reqid = result['RequestId']
        addr = result['UploadAddress']
        if len(addr['UploadHosts']) == 0:
            raise Exception("no upload host found, reqid %s" % reqid)
        elif len(addr['StoreInfos']) != len(img_datas):
            raise Exception(
                "store info len %d != upload num %d, reqid %s" % (
                    len(result['StoreInfos']), len(img_datas), reqid))

        session_key = addr['SessionKey']
        host = addr['UploadHosts'][0]
        self.do_upload(img_datas, host, addr['StoreInfos'])

        commit_upload_request = {
            'ServiceId': service_id,
            'SpaceName': space_name
        }
        commit_upload_body = {
            'SessionKey': session_key,
            'Functions': functions,
        }
        resp = self.commit_upload(commit_upload_request, json.dumps(commit_upload_body))
        if 'Error' in resp['ResponseMetadata']:
            raise Exception(resp['ResponseMetadata'])
        return resp['Result']

    def do_upload(self, img_datas, host, store_infos):
        idx = 0
        for d in img_datas:
            oid = store_infos[idx]['StoreUri']
            auth = store_infos[idx]['Auth']
            url = 'http://{}/{}'.format(host, oid)
            headers = {'Content-CRC32': hex(crc32(d) & 0xFFFFFFFF)[2:], 'Authorization': auth}
            upload_status, resp = self.put_data(url, d, headers)
            if not upload_status:
                raise Exception("upload %s error %s" % (url, resp))
            idx += 1

    # 获取临时上传凭证
    def get_upload_auth_token(self, params):
        apply_token = self.get_sign_url('ApplyImageUpload', params)
        commit_token = self.get_sign_url('CommitImageUpload', params)

        ret = {'Version': 'v1', 'ApplyUploadToken': apply_token, 'CommitUploadToken': commit_token}
        data = json.dumps(ret)
        if sys.version_info[0] == 3:
            return base64.b64encode(data.encode('utf-8')).decode('utf-8')
        else:
            return base64.b64encode(data.decode('utf-8'))

    # 获取上传临时密钥
    def get_upload_auth(self, service_ids, expire=60*60):
        actions = ['ImageX:ApplyImageUpload', 'ImageX:CommitImageUpload']
        resources = []
        if len(service_ids) == 0:
            resources.append(ResourceServiceIdTRN % '*')
        else:
            for sid in service_ids:
                resources.append(ResourceServiceIdTRN % sid)

        statement = Statement.new_allow_statement(actions, resources)
        inline_policy = Policy([statement])
        return self.sign_sts2(inline_policy, expire)

    # 更新图片URL：action为0表示刷新，为1表示禁用，为2表示解禁
    def update_image_urls(self, service_id, urls, action=0):
        if action < 0 or action > 2:
            raise Exception("update action should be [0,2], %d" % action)

        query = {
            'ServiceId': service_id
        }
        body = {
            'Action': action,
            'ImageUrls': urls
        }
        res = self.json("UpdateImageUploadFiles", query, json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        if 'Error' in res_json['ResponseMetadata']:
            raise Exception(res_json['ResponseMetadata'])
        return res_json['Result']

    # 获取图片信息
    def get_image_info(self, service_id, store_uri):
        query = {
            'ServiceId': service_id,
            'StoreUri': store_uri,
        }
        res = self.get('PreviewImageUploadFile', query)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        if 'Error' in res_json['ResponseMetadata']:
            raise Exception(res_json['ResponseMetadata'])
        return res_json['Result']
