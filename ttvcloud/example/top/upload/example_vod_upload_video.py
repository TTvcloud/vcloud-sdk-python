# coding:utf-8
from __future__ import print_function

import json

from ttvcloud.const.Const import *
from ttvcloud.vod.VodService import VodService

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    vod_service.set_ak('AKLTNDQ2YTRlNTBiYTg1NDcyNmE3MDA1MTUzNzc5MWMwNmI')
    vod_service.set_sk('1ZOtyBZ89VERZdOfiUrPf24a3tTjRo1XIJbzccVHMrBvZo1jEn60LjClP2t05qWz')

    space_name = 'james-test'
    file_path = '/Users/bytedance/Downloads/objects.mp4'

    function_list = list()

    get_meta_function = {'Name': 'GetMeta'}
    function_list.append(get_meta_function)

    snapshot_function_input = {'SnapshotTime': 2.3}
    snapshot_function = {'Name': 'Snapshot', 'Input': snapshot_function_input}
    function_list.append(snapshot_function)

    resp = vod_service.upload_video_tob(space_name, file_path, function_list,
                                        callback_args='my callback args')

    print(json.dumps(resp))
