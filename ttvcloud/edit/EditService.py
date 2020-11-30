# coding:utf-8
import json
import threading

from ttvcloud.ApiInfo import ApiInfo
from ttvcloud.Credentials import Credentials
from ttvcloud.ServiceInfo import ServiceInfo
from ttvcloud.base.Service import Service


class EditService(Service):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(EditService, "_instance"):
            with EditService._instance_lock:
                if not hasattr(EditService, "_instance"):
                    EditService._instance = object.__new__(cls)
        return EditService._instance

    def __init__(self, region='cn-north-1'):
        self.service_info = EditService.get_service_info(region)
        self.api_info = EditService.get_api_info()
        super(EditService, self).__init__(self.service_info, self.api_info)

    @staticmethod
    def get_service_info(region):
        service_info_map = {
            'cn-north-1': ServiceInfo("open.bytedanceapi.com", {'Accept': 'application/json'},
                                      Credentials('', '', 'edit', 'cn-north-1'), 5, 5),
            'ap-singapore-1': ServiceInfo("open.ap-singapore-1.bytedanceapi.com", {'Accept': 'application/json'},
                                          Credentials('', '', 'edit', 'ap-singapore-1'), 5, 5),
            'us-east-1': ServiceInfo("open.us-east-1.bytedanceapi.com", {'Accept': 'application/json'},
                                     Credentials('', '', 'edit', 'us-east-1'), 5, 5),
        }
        service_info = service_info_map.get(region, None)
        if not service_info:
            raise Exception('Cant find the region, please check it carefully')

        return service_info

    @staticmethod
    def get_api_info():
        api_info = {"SubmitDirectEditTaskAsync": ApiInfo("POST", "/", {"Action": "SubmitDirectEditTaskAsync",
                                                                       "Version": "2018-01-01"}, {}, {}),
                    "SubmitDirectEditTaskSync": ApiInfo("POST", "/", {"Action": "SubmitDirectEditTaskSync",
                                                                      "Version": "2018-01-01"}, {}, {}),
                    "GetDirectEditResult": ApiInfo("POST", "/", {"Action": "GetDirectEditResult",
                                                                 "Version": "2018-01-01"}, {}, {}),
                    "SubmitTemplateTaskAsync": ApiInfo("POST", "/", {"Action": "SubmitTemplateTaskAsync",
                                                                     "Version": "2018-01-01"}, {}, {})
                    }
        return api_info

    def submit_direct_edit_task_async(self, body):
        res = self.json('SubmitDirectEditTaskAsync', {}, body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json

    def submit_direct_edit_task_sync(self, body):
        res = self.json('SubmitDirectEditTaskSync', {}, body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json

    def get_direct_edit_result(self, body):
        res = self.json('GetDirectEditResult', {}, body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json

    def submit_template_task_async(self, body):
        res = self.json('SubmitTemplateTaskAsync', {}, body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
