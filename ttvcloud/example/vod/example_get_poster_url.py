# coding:utf-8
from __future__ import print_function

import sys
import time

from ttvcloud.const.Const import *
from ttvcloud.vod.ImgUrlOption import ImgUrlOption
from ttvcloud.vod.VodService import VodService

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    space_name = 'your space_name'
    uri = 'your uri'

    # set fallback weights if necessary
    fallback_weights = {'v1.test.com': 10, 'v3.test.com': 5}
    resp = vod_service.set_fallback_domain_weights(fallback_weights)
    if not resp:
        print('set fallback weights error')
        sys.exit(-1)

    resp = vod_service.get_domain_weights(space_name)
    print(resp)

    print('*' * 100)

    for i in range(20):
        resp = vod_service.get_domain_info(space_name)
        print(resp)
        time.sleep(1)

    print('*' * 100)

    option = ImgUrlOption()
    option.set_https()
    option.set_vod_tpl_smart_crop(600, 392)
    option.set_format(FORMAT_AWEBP)

    resp = vod_service.get_poster_url(space_name, uri, option)
    print(resp)
