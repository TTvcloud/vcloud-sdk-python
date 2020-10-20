# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService
from ttvcloud.vod.Models import VodGetPlayInfoRequest

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    vid = 'your vid'

    req = VodGetPlayInfoRequest()
    req.Vid = vid
    resp = vod_service.get_play_info(req)
    if not ('Error' in resp['ResponseMetadata']):
        print(resp['Result']['Data']['PlayInfoList'][0]['MainPlayUrl'])
        print(resp['Result']['Data']['PlayInfoList'][0]['BackupPlayUrl'])

    print('*' * 100)

    req = VodGetPlayInfoRequest()
    req.Vid = vid
    req.Ssl = '1'
    resp = vod_service.get_origin_video_play_info(req)
    if not ('Error' in resp['ResponseMetadata']):
        print(resp['Result']['MainPlayUrl'])
        print(resp['Result']['BackupPlayUrl'])

    print('*' * 100)
