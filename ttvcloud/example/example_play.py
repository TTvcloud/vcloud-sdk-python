# coding:utf-8
from ttvcloud.VodService import VodService

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    params = dict()
    params['video_id'] = 'your video id'
    resp = vod_service.get_play_auth_token(params)
    print resp

    print '*' * 100

    # https://vcloud.bytedance.net/docs/4/2918/
    params = dict()
    params['video_id'] = 'your video id'
    resp = vod_service.get_play_info(params)
    if not resp['ResponseMetadata'].has_key('Error'):
        print resp['Result']['Data']['PlayInfoList'][0]['MainPlayUrl']
        print resp['Result']['Data']['PlayInfoList'][0]['BackupPlayUrl']

    print '*' * 100

    params = dict()
    params['Vid'] = 'your video id'
    params['Ssl'] = '1'
    resp = vod_service.get_origin_video_play_info(params)
    if not resp['ResponseMetadata'].has_key('Error'):
        print resp['Result']['MainPlayUrl']
        print resp['Result']['BackupPlayUrl']

    print '*' * 100

    params = dict()
    params['Vid'] = 'your video id'
    resp = vod_service.get_redirect_play(params)
    print resp



