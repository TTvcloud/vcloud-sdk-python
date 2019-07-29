# coding:utf-8
from ttvcloud.VodService import VodService

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    # https://vcloud.bytedance.net/docs/4/4709/
    body = dict()
    body['Vid'] = 'your vid'
    body['SpaceName'] = 'your space_name'
    body['Status'] = 'Published'
    # body['Status'] = 'Blocked'

    resp = vod_service.set_video_publish_status(body)
    print resp