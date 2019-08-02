## TTVcloud SDK for Python

### 安装
require python verion >= 2.7

```
    pip install ttvcloud
```

### AK/SK设置
- 在代码里显示调用VodService的方法set_ak/set_sk

- 在当前环境变量中分别设置 VCLOUD_ACCESSKEY="your ak"  VCLOUD_SECRETKEY = "your sk"

- json格式放在～/.vcloud/config中，格式为：{"ak":"your ak","sk":"your sk"}

以上优先级依次降低，建议在代码里显示设置，以便问题排查

### API

#### 上传

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
[get_poster_url]()

#### 更多示例参见 example



###Change log

#### 0.0.5
- 去掉image X 相关
- 增加封面图上传接口
- getUploadAuthToken/getPlayAuthToken/RedirectPlay支持X-Amz-Expires参数
- 代码格式优化