
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
        :param Watermark: 水印贴片标签。默认值：空。
        :type Watermark: str
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
        self.Watermark = None
        self.Base64 = None
        self.Ssl = None

    def _deserialize(self, params):
        self.Vid = params.get("Vid")
        self.Format = params.get("Format")
        self.Codec = params.get("Codec")
        self.Definition = params.get("Definition")
        self.FileType = params.get("FileType")
        self.Watermark = params.get("Watermark")
        self.Base64 = params.get("Base64")
        self.Ssl = params.get("Ssl")
