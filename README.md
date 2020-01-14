## TTVcloud SDK for Python

[![Build Status](https://travis-ci.org/TTvcloud/vcloud-sdk-python.svg?branch=master)](https://travis-ci.org/TTvcloud/vcloud-sdk-python)

### 安装
require python verion >= 2.7

```
    pip install --user ttvcloud
```

如果已经安装ttvcloud包，则用下面命令升级即可
```
    pip install --upgrade ttvcloud
```


### AK/SK设置
- 在代码里显示调用VodService的方法set_ak/set_sk

- 在当前环境变量中分别设置 VCLOUD_ACCESSKEY="your ak"  VCLOUD_SECRETKEY = "your sk"

- json格式放在～/.vcloud/config中，格式为：{"ak":"your ak","sk":"your sk"}

以上优先级依次降低，建议在代码里显示设置，以便问题排查

### 地域Region设置
- 目前已开放三个地域设置，分别为
  ```
  - cn-north-1 (默认)
  - ap-singapore-1
  - us-east-1
  ```
- 默认为cn-north-1，如果需要调用其它地域服务，请在初始化函数getInstance中传入指定地域region，例如：
  ```
  vod_service = VodService('us-east-1')
  ```
- 注意：IAM模块目前只开放cn-north-1区域

### API

#### 获取sts2签名

[sign_sts2]()
```
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')

    statement = Statement.new_allow_statement(['iam:*'], [])
    inline_policy = Policy([statement])
    
    # 60 * 60 (设定有效期一小时)
    resp = vod_service.sign_sts2(inline_policy, 60 * 60)
    print(resp)

```

#### 上传

- 通过指定url地址上传

[upload_media_by_url](https://open.bytedance.com/docs/4/4652/)

- 服务端直接上传

上传视频包括 [apply_upload](https://open.bytedance.com/docs/4/2915/) 和 [commit_upload](https://open.bytedance.com/docs/4/2916/) 两步

上传封面图包括 [apply_upload](https://open.bytedance.com/docs/4/2915/) 和 [modify_video_info](https://open.bytedance.com/docs/4/4367/) 两步


为方便用户使用，封装方法 upload_video 和 upload_poster， 一步上传



#### 转码
[start_transcode](https://open.bytedance.com/docs/4/1670/)


#### 发布
[set_video_publish_status](https://open.bytedance.com/docs/4/4709/)


#### 播放：
[get_play_info](https://open.bytedance.com/docs/4/2918/)

[get_origin_video_play_info](https://open.bytedance.com/docs/4/11148/)

[get_redirect_play](https://open.bytedance.com/docs/4/9205/)

#### 封面图:
[get_poster_url](https://open.bytedance.com/docs/4/5335/)

#### token相关
[get_upload_auth_token](https://open.bytedance.com/docs/4/6275/)

[get_play_auth_token](https://open.bytedance.com/docs/4/6275/)

PS: 上述两个接口和 [get_redirect_play](https://open.bytedance.com/docs/4/9205/) 接口中均含有 X-Amz-Expires 这个参数

关于这个参数的解释为：设置返回的playAuthToken或uploadToken或follow 302地址的有效期，目前服务端默认该参数为15min（900s），如果用户认为该有效期过长，可以传递该参数来控制过期时间
。

#### 更多示例参见 example