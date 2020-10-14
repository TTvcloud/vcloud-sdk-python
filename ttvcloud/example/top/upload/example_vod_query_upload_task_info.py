# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService
import json

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    vod_service.set_ak('AKLTNDQ2YTRlNTBiYTg1NDcyNmE3MDA1MTUzNzc5MWMwNmI')
    vod_service.set_sk('1ZOtyBZ89VERZdOfiUrPf24a3tTjRo1XIJbzccVHMrBvZo1jEn60LjClP2t05qWz')

    jobId = '6c9823276b844b619024e3a5367b7d08'

    jobIds = [jobId]
    comma = ','
    s = comma.join(jobIds)

    params = dict()
    params['JobIds'] = s

    resp = vod_service.query_upload_task_info(params)
    print(json.dumps(resp))
