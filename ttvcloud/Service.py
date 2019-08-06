# coding: utf-8
import json
import os
from collections import OrderedDict

import requests

from ttvcloud.Request import Request
from ttvcloud.SignerV4 import SignerV4


class Service(object):
    def __init__(self, service_info, api_info):
        self.service_info = service_info
        self.api_info = api_info
        self.session = requests.session()
        self.init()

    def init(self):
        if 'VCLOUD_ACCESSKEY' in os.environ and 'VCLOUD_SECRETKEY' in os.environ:
            self.service_info.set_ak(os.environ['VCLOUD_ACCESSKEY'])
            self.service_info.set_sk(os.environ['VCLOUD_SECRETKEY'])
        else:

            path = os.environ['HOME'] + '/.vcloud/config'
            if os.path.isfile(path):
                with open(path, 'r') as f:
                    j = json.load(f)
                    if 'ak' in j:
                        self.service_info.credentials.set_ak(j['ak'])
                    if 'sk' in j:
                        self.service_info.credentials.set_sk(j['sk'])

    def set_ak(self, ak):
        self.service_info.credentials.set_ak(ak)

    def set_sk(self, sk):
        self.service_info.credentials.set_sk(sk)

    def get_sign_url(self, api, params):
        if not (api in self.api_info):
            raise Exception("no such api")
        api_info = self.api_info[api]

        mquery = self.merge(api_info.query, params)
        r = Request()
        r.set_method(api_info.method)
        r.set_path(api_info.path)
        r.set_query(mquery)

        return SignerV4.sign_url(r, self.service_info.credentials)

    def get(self, api, params):
        if not (api in self.api_info):
            raise Exception("no such api")
        api_info = self.api_info[api]

        r = self.prepare_request(api_info, params)

        SignerV4.sign(r, self.service_info.credentials)

        url = r.build()
        resp = self.session.get(url, headers=r.headers,
                                timeout=(self.service_info.connection_timeout, self.service_info.socket_timeout))
        if resp.status_code == 200:
            return resp.text
        else:
            return ''

    def post(self, api, params, form):
        if not (api in self.api_info):
            raise Exception("no such api")
        api_info = self.api_info[api]
        r = self.prepare_request(api_info, params)
        r.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        r.form = self.merge(api_info.form, form)

        SignerV4.sign(r, self.service_info.credentials)

        url = r.build()
        resp = self.session.post(url, headers=r.headers, data=r.form,
                                 timeout=(self.service_info.connection_timeout, self.service_info.socket_timeout))
        if resp.status_code == 200:
            return resp.text
        else:
            return ''

    def json(self, api, params, body):
        if not (api in self.api_info):
            raise Exception("no such api")
        api_info = self.api_info[api]
        r = self.prepare_request(api_info, params)
        r.headers['Content-Type'] = 'application/json'
        r.body = body

        SignerV4.sign(r, self.service_info.credentials)

        url = r.build()
        resp = self.session.post(url, headers=r.headers, data=r.body,
                                 timeout=(self.service_info.connection_timeout, self.service_info.socket_timeout))
        if resp.status_code == 200:
            return resp.text
        else:
            return ''

    def put(self, url, file_path, headers):
        with open(file_path, 'rb') as f:
            resp = self.session.put(url, headers=headers, data=f)
            if resp.status_code == 200:
                return True, resp.text
            else:
                return False, resp.text

    def prepare_request(self, api_info, params):
        for key in params:
            if type(params[key]) == int or type(params[key]) == float:
                params[key] = str(params[key])
            elif type(params[key]) == list:
                params[key] = ','.join(params[key])

        connection_timeout = self.service_info.connection_timeout
        socket_timeout = self.service_info.socket_timeout

        r = Request()
        r.set_method(api_info.method)
        r.set_connection_timeout(connection_timeout)
        r.set_socket_timeout(socket_timeout)

        mheaders = self.merge(api_info.header, self.service_info.header)
        mheaders['Host'] = self.service_info.host
        r.set_headers(mheaders)

        mquery = self.merge(api_info.query, params)
        r.set_query(mquery)

        r.set_host(self.service_info.host)
        r.set_path(api_info.path)

        return r

    def merge(self, param1, param2):
        od = OrderedDict()
        for key in param1:
            od[key] = param1[key]

        for key in param2:
            od[key] = param2[key]

        return od
