# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    params = dict()
    params['TemplateId'] = 'your template id'

    body = dict()
    body['Vid'] = 'your vid'
    body['Priority'] = 0
    body['Input'] = {}

    resp = vod_service.start_transcode(params, body)
    print(resp)
