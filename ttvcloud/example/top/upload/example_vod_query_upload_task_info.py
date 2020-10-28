# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService
from ttvcloud.vod.top.model.request.UrlUploadQueryRequest import UrlUploadQueryRequest
from ttvcloud.vod.top.model.response.QueryDataResponse import QueryDataResponse
import json

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    vod_service.set_ak('your ak')
    vod_service.set_sk('your sk')

    jobId = 'url jobId'

    jobIds = [jobId]
    comma = ','
    s = comma.join(jobIds)

    params = dict()
    params['JobIds'] = s

    url_upload_query_request = UrlUploadQueryRequest(jobIds)

    resp = vod_service.query_upload_task_info(url_upload_query_request)
    print(json.dumps(resp))

    url_upload_query_response = QueryDataResponse(resp)
    print(json.dumps(url_upload_query_response, default=lambda obj: obj.__dict__))
