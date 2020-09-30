# coding:utf-8
from __future__ import print_function

from ttvcloud.const.Const import *
from ttvcloud.vod.VodService import VodService
import json

if __name__ == '__main__':
    print(123)
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    vod_service.set_ak('AKLTNDQ2YTRlNTBiYTg1NDcyNmE3MDA1MTUzNzc5MWMwNmI')
    vod_service.set_sk('1ZOtyBZ89VERZdOfiUrPf24a3tTjRo1XIJbzccVHMrBvZo1jEn60LjClP2t05qWz')

    space_name = 'james-test'
    url = 'your url'

    params = dict()
    params['SpaceName'] = space_name
    params['URLSets'] = UPLOAD_FORMAT_MP4

    url_sets = []
    url_set = dict()
    url_set['SourceUrl'] = 'https://stream7.iqilu.com/10339/upload_transcode/202002/18/20200218114723HDu3hhxqIT.mp4'
    url_sets.append(url_set)
    print(json.dumps(url_sets))

    resp = vod_service.upload_video_by_url(params)
    print(resp)
