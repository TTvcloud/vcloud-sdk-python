# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    vid = 'your vid'

    params = dict()
    params['video_id'] = vid
    resp = vod_service.get_play_info(params)
    if not ('Error' in resp['ResponseMetadata']):
        print(resp['Result']['Data']['PlayInfoList'][0]['MainPlayUrl'])
        print(resp['Result']['Data']['PlayInfoList'][0]['BackupPlayUrl'])

    print('*' * 100)

    params = dict()
    params['Vid'] = vid
    params['Ssl'] = '1'
    resp = vod_service.get_origin_video_play_info(params)
    if not ('Error' in resp['ResponseMetadata']):
        print(resp['Result']['MainPlayUrl'])
        print(resp['Result']['BackupPlayUrl'])

    print('*' * 100)

    params = dict()
    params['Vid'] = vid
    # set expires time of the redirect play url, defalut is 15min(900),
    # set if if you know the params' meaning exactly.
    params['X-Amz-Expires'] = '60'
    resp = vod_service.get_redirect_play(params)
    print(resp)
