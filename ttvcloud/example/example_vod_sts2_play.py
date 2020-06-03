# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService
from ttvcloud.Policy import *

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    sts2 = vod_service.get_video_play_auth([], [], [])
    print(sts2)

    sts2 = vod_service.get_video_play_auth_with_expired_time([], [], [], 60 * 60)
    print(sts2)
