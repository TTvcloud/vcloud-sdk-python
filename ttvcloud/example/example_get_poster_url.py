# coding:utf-8
import sys
import time

from ttvcloud.Const import *
from ttvcloud.ImgUrlOption import ImgUrlOption
from ttvcloud.VodService import VodService

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    vod_service.set_ak('your ak')
    vod_service.set_sk('your sk')

    # set fallback weights if necessary
    fallback_weights = {'v1.test.com': 10, 'v3.test.com': 5}
    resp = vod_service.set_fallback_domain_weights(fallback_weights)
    if not resp:
        print 'set fallback weights error'
        sys.exit(-1)

    space_name = 'your space_name'
    vid = 'your vid'

    resp = vod_service.get_domain_weights(space_name)
    print resp

    print '*' * 100

    for i in range(20):
        resp = vod_service.get_domain_info(space_name)
        print resp
        time.sleep(1)

    print '*' * 100

    uri = 'your uri'

    option = ImgUrlOption()
    option.set_https()
    option.set_vod_tpl_smart_crop(600, 392)
    option.set_format(FORMAT_AWEBP)

    resp = vod_service.get_poster_url(space_name, uri, option)
    print resp

    print '*' * 100

    option = ImgUrlOption()
    option.set_https()
    option.set_format(FORMAT_AWEBP)
    option.set_vod_tpl_sig()
    option.set_sig_key('your sig')
    option.set_kv({'from': 'my测试'})

    resp = vod_service.get_image_url(space_name, uri, option)
    print resp
