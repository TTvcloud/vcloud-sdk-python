class VodPlayInfo:
    def __init__(self):
        """
        :param FileID: 流文件ID
        :type FileID: str
        :param Md5: 文件Hash校验值
        :type Md5: str
        :param FileType: 流文件类型
        :type FileType: str
        :param Format: 封装格式，可选值：mp4,dash,hls。默认值：mp4。
        :type Format: str
        :param Codec: 编码类型，可选值：h264,h265。默认值：h264。
        :type Codec: str
        :param Definition: 视频流清晰度，默认返回全部清晰度，可选值：240p，360p，480p，540p，720p，1080p。默认值：空。
        :type Definition: str
        :param MainPlayUrl: 主播放地址
        :type MainPlayUrl: str
        :param BackupPlayUrl: 备播放地址
        :type BackupPlayUrl: str
        :param Bitrate: 码率(Kbps)
        :type Bitrate: float
        :param Width: 宽
        :type Width: long
        :param Height: 高
        :type Height: long
        :param Size: 文件大小
        :type Size: long
        :param Quality: 质量
        :type Quality: str
        :param LogoType: 水印类型
        :type LogoType: str
        :param PlayAuthID: 加密密钥ID
        :type PlayAuthID: str
        :param PlayAuth: 加密密钥
        :type PlayAuth: str
        :param P2pVerifyUrl: P2P播放校验文件地址
        :type P2pVerifyUrl: str
        :param PreloadInterval: 预加载间隔
        :type PreloadInterval: long
        :param PreloadMaxStep: 预加载最大步长
        :type PreloadMaxStep: long
        :param PreloadMinStep: 预加载最小步长
        :type PreloadMinStep: long
        :param PreloadSize: 预加载大小
        :type PreloadSize: long
        :param InitRange: Dash分片信息
        :type InitRange: str
        :param IndexRange: Dash分片信息
        :type IndexRange: str
        :param CheckInfo: 劫持校验信息
        :type CheckInfo: str
        """
        self.FileID = None
        self.Md5 = None
        self.FileType = None
        self.Format = None
        self.Codec = None
        self.Definition = None
        self.MainPlayUrl = None
        self.BackupPlayUrl = None
        self.Bitrate = None
        self.Width = None
        self.Height = None
        self.Size = None
        self.Quality = None
        self.LogoType = None
        self.PlayAuthID = None
        self.PlayAuth = None
        self.P2pVerifyURL = None
        self.PreloadInterval = None
        self.PreloadMaxStep = None
        self.PreloadMinStep = None
        self.PreloadSize = None
        self.InitRange = None
        self.IndexRange = None
        self.CheckInfo = None

    def _deserialize(self, params):
        self.FileID = params.get("FileID")
        self.Md5 = params.get("Md5")
        self.FileType = params.get("FileType")
        self.Format = params.get("Format")
        self.Codec = params.get("Codec")
        self.Definition = params.get("Definition")
        self.MainPlayUrl = params.get("MainPlayUrl")
        self.BackupPlayUrl = params.get("BackupPlayUrl")
        self.Bitrate = params.get("Bitrate")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Size = params.get("Size")
        self.Quality = params.get("Quality")
        self.LogoType = params.get("LogoType")
        self.PlayAuthID = params.get("PlayAuthID")
        self.PlayAuth = params.get("PlayAuth")
        self.P2pVerifyURL = params.get("P2pVerifyURL")
        self.PreloadInterval = params.get("PreloadInterval")
        self.PreloadMaxStep = params.get("PreloadMaxStep")
        self.PreloadMinStep = params.get("PreloadMinStep")
        self.PreloadSize = params.get("PreloadSize")
        self.InitRange = params.get("InitRange")
        self.IndexRange = params.get("IndexRange")
        self.CheckInfo = params.get("CheckInfo")

class VodAdaptiveInfo:
    def __init__(self):
        """
        :param MainPlayUrl: mpd主链接
        :type MainPlayUrl: str
        :param BackupPlayUrl: mpd备链接
        :type BackupPlayUrl: str
        :param AdaptiveType: 动态格式类型segment_base(对应format=mpd) / segment_template(对应format=dash)
        :type AdaptiveType: str
        """
        self.MainPlayUrl = None
        self.BackupPlayUrl = None
        self.AdaptiveType = None

    def _deserialize(self, param):
        self.MainPlayUrl = param.get("MainPlayUrl")
        self.BackupPlayUrl = param.get("BackupPlayUrl")
        self.AdaptiveType = param.get("AdaptiveType")


class VodGetPlayInfoRequest:
    def __init__(self):
        """
        :param Vid: 视频ID
        :type Vid: str
        :param Format: 封装格式，可选值：mp4,dash,hls。默认值：mp4。
        :type Format: str
        :param Codec: 编码类型，可选值：h264,h265。默认值：h264。
        :type Codec: str
        :param Definition: 视频流清晰度，默认返回全部清晰度，可选值：240p，360p，480p，540p，720p，1080p。默认值：空。
        :type Definition: str
        :param FileType: 流文件类型，可选值：加密视频流evideo，加密音频流传eaudio，非加密视频流video，普通音频音频流audio。默认值：video。
        :type FileType: str
        :param LogoType: 水印贴片标签。默认值：空。
        :type LogoType: str
        :param Base64: 播放地址是否base64编码，可选值： "0"-否，"1"-是。默认值："0"。
        :type Base64: str
        :param Ssl: 返回https播放地址，可选值："1"-是；"0"-否。默认值："0"-否。
        :type Ssl: str
        """
        self.Vid = None
        self.Format = None
        self.Codec = None
        self.Definition = None
        self.FileType = None
        self.LogoType = None
        self.Base64 = None
        self.Ssl = None

    def _deserialize(self, params):
        self.Vid = params.get("Vid")
        self.Format = params.get("Format")
        self.Codec = params.get("Codec")
        self.Definition = params.get("Definition")
        self.FileType = params.get("FileType")
        self.LogoType = params.get("LogoType")
        self.Base64 = params.get("Base64")
        self.Ssl = params.get("Ssl")


class VodGetPlayInfoResponse:
    def __init__(self):
        """
        :param Vid: 视频ID
        :type Vid: str
        :param Status: 视频状态
        :type Status: long
        :param PosterUrl: 封面图
        :type PosterUrl: str
        :param Duration: 视频时长(单位：s)
        :type Duration: float
        :param FileType: 媒体类型(video/audio)
        :type FileType: str
        :param EnableAdaptive: 是否关键帧对齐
        :type EnableAdaptive: bool
        :param PlayInfoList: 播放流列表
        :type PlayInfoList: []VodPlayInfo
        :param TotalCount: 列表数量
        :type TotalCount: int
        :param AdaptiveInfo: dash视频播放信息
        :type AdaptiveInfo: bool
        """
        self.Vid = None
        self.Status = None
        self.PosterUrl = None
        self.Duration = None
        self.FileType = None
        self.EnableAdaptive = None
        self.TotalCount = None
        self.PlayInfoList = None
        self.AdaptiveInfo = None

    def _deserialize(self, params):
        self.Vid = params.get("Vid")
        self.Status = params.get("Status")
        self.PosterUrl = params.get("PosterUrl")
        self.Duration = params.get("Duration")
        self.FileType = params.get("FileType")
        self.EnableAdaptive = params.get("EnableAdaptive")
        self.TotalCount = params.get("TotalCount")
        self.AdaptiveInfo = params.get("AdaptiveInfo")
        if params.get("PlayInfoList") is not None:
            self.PlayInfoList = list()
            for row in params.get("PlayInfoList"):
                if row is None:
                    continue
                re_row = VodPlayInfo()
                re_row._deserialize(row)
                self.PlayInfoList.append(re_row)
        if params.get("AdaptiveInfo") is not None:
            self.AdaptiveInfo = VodAdaptiveInfo()
            self.AdaptiveInfo._deserialize(params.get("AdaptiveInfo"))


class VodGetOriginVideoPlayInfoRequest:
    def __init__(self):
        """
        :param Vid: 视频ID
        :type Vid: str
        :param Base64: 播放地址是否base64编码，可选值： "0"-否，"1"-是。默认值："0"。
        :type Base64: str
        :param Ssl: 返回https播放地址，可选值："1"-是；"0"-否。默认值："0"-否。
        :type Ssl: str
        """
        self.Vid = None
        self.Base64 = None
        self.Ssl = None

    def _deserialize(self, params):
        self.Vid = params.get("Vid")
        self.Base64 = params.get("Base64")
        self.Ssl = params.get("Ssl")


class VodGetOriginVideoPlayInfoResponse:
    def __init__(self):
        """
        :param Duration: 视频时长(单位：s)
        :type Duration: float
        :param FileType: 媒体类型(video/audio)
        :type FileType: str
        :param Format: 封装格式，可选值：mp4,dash,hls。默认值：mp4。
        :type Format: str
        :param Codec: 编码类型，可选值：h264,h265。默认值：h264。
        :type Codec: str
        :param MainPlayUrl: 主播放地址
        :type MainPlayUrl: str
        :param BackupPlayUrl: 备播放地址
        :type BackupPlayUrl: str
        :param Bitrate: 码率(Kbps)
        :type Bitrate: float
        :param Width: 宽
        :type Width: long
        :param Height: 高
        :type Height: long
        :param Size: 文件大小
        :type Size: long
        :param Md5: 校验Hash
        :type Md5: str
        """
        self.Duration = None
        self.FileType = None
        self.Format = None
        self.Codec = None
        self.MainPlayUrl = None
        self.BackupPlayUrl = None
        self.Bitrate = None
        self.Width = None
        self.Height = None
        self.Size = None
        self.Md5 = None

    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        self.FileType = params.get("FileType")
        self.Format = params.get("Format")
        self.Codec = params.get("Codec")
        self.MainPlayUrl = params.get("MainPlayUrl")
        self.BackupPlayUrl = params.get("BackupPlayUrl")
        self.Bitrate = params.get("Bitrate")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Size = params.get("Size")
        self.Md5 = params.get("Md5")
