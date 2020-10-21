# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService
from ttvcloud.vod.Models import VodGetPlayInfoRequest, VodGetOriginVideoPlayInfoRequest

if __name__ == '__main__':
    vod_service = VodService()
    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')
    try:
        vid = 'v0c2c369007abu04ru8riko30uo9n73g'
        req = VodGetPlayInfoRequest()
        req.Vid = vid
        resp = vod_service.get_play_info(req)
    except Exception:
        raise
    else:
        print(resp)
        print(resp.PlayInfoList[0].MainPlayUrl)
        print(resp.PlayInfoList[0].BackupPlayUrl)

    print('*' * 100)

    try:
        vid = 'v0c2c369007abu04ru8riko30uo9n73g'
        req = VodGetOriginVideoPlayInfoRequest()
        req.Vid = vid
        req.Ssl = '1'
        resp = vod_service.get_origin_video_play_info(req)
    except Exception:
        raise
    else:
        print(resp)
        print(resp.MainPlayUrl)
        print(resp.BackupPlayUrl)

    print('*' * 100)
