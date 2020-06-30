# coding:utf-8
from __future__ import print_function

from ttvcloud.imagex.ImageXService import ImageXService

if __name__ == '__main__':
    imagex_service = ImageXService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    imagex_service.set_ak('ak')
    imagex_service.set_sk('sk')

    resp = imagex_service.get_image_info('service id', 'image uri')
    print(resp)
