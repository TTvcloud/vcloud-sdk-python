# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService
import json

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    vod_service.set_ak('your ak')
    vod_service.set_sk('your sk')

    space_name = 'your space name'

    params = dict()
    form = dict()

    session = ''

    form['SessionKey'] = session
    form['SpaceName'] = space_name
    form['Functions'] = '[{"Name": "GetMeta"},{"Name":"Snapshot","Input":{"SnapshotTime": 2.0}}]'
    resp = vod_service.commit_upload_info(params, form)
    print(json.dumps(resp))
