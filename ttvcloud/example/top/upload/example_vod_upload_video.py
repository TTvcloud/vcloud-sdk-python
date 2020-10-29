# coding:utf-8
from __future__ import print_function

import json

from ttvcloud.const.Const import *
from ttvcloud.vod.VodService import VodService
from ttvcloud.vod.top.model.request.UploadVideoRequest import UploadVideoRequest
from ttvcloud.vod.top.model.response.UploadVideoResponse import UploadVideoResponse
from ttvcloud.vod.top.model.functions.Functions import Function

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    vod_service.set_ak('your ak')
    vod_service.set_sk('your sk')

    space_name = 'your space'
    file_path = 'file path'

    get_meta_function = Function.get_meta_func()
    snapshot_function = Function.get_snapshot_func(2.3)

    upload_video_reqeust = UploadVideoRequest()
    upload_video_reqeust.set_space_name(space_name)
    upload_video_reqeust.set_file_path(file_path)
    upload_video_reqeust.set_callback_args("my callback args")
    upload_video_reqeust.add_function(get_meta_function)
    upload_video_reqeust.add_function(snapshot_function)

    resp = vod_service.upload_video_tob(upload_video_reqeust)
    print(json.dumps(resp))

    upload_video_response = UploadVideoResponse(resp)
    print(json.dumps(upload_video_response, default=lambda obj: obj.__dict__))
