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

    def __init__(self):
        self.service_info = EditService.get_service_info()
        self.api_info = EditService.get_api_info()
        super(EditService, self).__init__(self.service_info, self.api_info)

    @staticmethod
    def get_service_info():
        service_info = ServiceInfo("open.bytedanceapi.com", {'Accept': 'application/json'},
                                   Credentials('', '', 'edit', 'cn-north-1'), 5000, 5000)
        return service_info

    @staticmethod
    def get_api_info():
        api_info = {"SubmitDirectEditTaskAsync": ApiInfo("POST", "/", {"Action": "SubmitDirectEditTaskAsync",
                                                                       "Version": "2018-01-01"}, {}, {}),
                    "GetDirectEditResult": ApiInfo("POST", "/",
                                                   {"Action": "GetDirectEditResult", "Version": "2018-01-01"}, {}, {}),
                    "SubmitDirectEditTaskSync": ApiInfo("POST", "/",
                                                        {"Action": "SubmitDirectEditTaskSync", "Version": "2018-01-01"},
                                                        {}, {})
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