# coding:utf-8
from ttvcloud.Const import *
from ttvcloud.VodService import VodService

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    space_name = 'your space_name'
    file_path = 'your file_path'
    url = 'your url'

    resp = vod_service.get_upload_auth_token(space_name)
    print resp

    print '*' * 100

    # https://vcloud.bytedance.net/docs/4/2915/
    # https://vcloud.bytedance.net/docs/4/2916/

    function_list = list()

    get_meta_function = {'Name': 'GetMeta'}
    function_list.append(get_meta_function)

    snapshot_function_input = {'SnapshotTime': 2.3}
    snapshot_function = {'Name': 'Snapshot', 'Input': snapshot_function_input}
    function_list.append(snapshot_function)

    resp = vod_service.upload(space_name, file_path, FILE_TYPE_VIDEO, function_list)
    print resp

    print '*' * 100
    # https://vcloud.bytedance.net/docs/4/4652/
    params = dict()
    params['SpaceName'] = space_name
    params['Format'] = UPLOAD_FORMAT_MP4
    params['SourceUrls'] = [url]
    resp = vod_service.upload_media_by_url(params)
    print resp
