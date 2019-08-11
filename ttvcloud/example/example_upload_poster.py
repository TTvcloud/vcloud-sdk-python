# coding:utf-8
from __future__ import print_function

from ttvcloud.const.Const import *
from ttvcloud.vod.VodService import VodService

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    space_name = 'your space_name'
    file_path = 'your file_path'
    vid = 'your vid'

    resp = vod_service.upload_poster(vid, space_name, file_path, FILE_TYPE_IMAGE)
    print(resp)
