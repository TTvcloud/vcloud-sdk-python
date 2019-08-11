# coding:utf-8
from ttvcloud.const.Const import *


class ImgUrlOption(object):
    def __init__(self):
        self.isHttps = False
        self.format = ''
        self.sig_key = ''
        self.tpl = ''
        self.width = 0
        self.height = 0
        self.kv = {}

    def set_https(self):
        self.isHttps = True

    def set_format(self, format):
        self.format = format

    def set_sig_key(self, sig_key):
        self.sig_key = sig_key

    def set_kv(self, kv):
        self.kv = kv

    def set_vod_tpl_sig(self):
        self.tpl = VOD_TPL_SIG

    def set_vod_tpl_obj(self):
        self.tpl = VOD_TPL_OBJ

    def set_vod_tpl_noop(self):
        self.tpl = VOD_TPL_NOOP

    def set_vod_tpl_center_crop(self, width, height):
        self.width = width
        self.height = height
        self.tpl = VOD_TPL_CENTER_CROP

    def set_vod_tpl_smart_crop(self, width, height):
        self.width = width
        self.height = height
        self.tpl = VOD_TPL_SMART_CROP

    def set_vod_tpl_resize(self, width, height):
        self.width = width
        self.height = height
        self.tpl = VOD_TPL_RESIZE
