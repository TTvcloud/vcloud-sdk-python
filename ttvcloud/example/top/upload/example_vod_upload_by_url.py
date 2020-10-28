# coding:utf-8
from __future__ import print_function

import json

from ttvcloud.vod.VodService import VodService
from ttvcloud.vod.top.model.request.UrlUploadRequest import UrlUploadRequest, UrlSet
from ttvcloud.vod.top.model.response.UrlUploadResponse import *

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    vod_service.set_ak('your ak')
    vod_service.set_sk('your sk')

    space_name = 'your space name'
    url = 'video url'

    request = UrlUploadRequest(space_name)
    url_set = UrlSet(url)
    request.add_url_set(url_set)
    resp = vod_service.upload_video_by_url_tob(request)
    print(json.dumps(resp))
    url_upload_response = UrlUploadResponse(resp)
    print(json.dumps(url_upload_response, default=lambda obj: obj.__dict__))
