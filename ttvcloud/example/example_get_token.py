# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    space_name = 'your space_name'
    vid = 'your video id'

    params = dict()
    params['video_id'] = vid
    # set expires time of the play auth token, defalut is 15min(900),
    # set if if you know the params' meaning exactly.
    params['X-Amz-Expires'] = '60'
    resp = vod_service.get_play_auth_token(params)
    print(resp)

    print('*' * 100)

    params = dict()
    params['SpaceName'] = space_name
    # set expires time of the upload token, defalut is 15min(900),
    # set if if you know the params' meaning exactly.
    params['X-Amz-Expires'] = '60'

    resp = vod_service.get_upload_auth_token(params)
    print(resp)
