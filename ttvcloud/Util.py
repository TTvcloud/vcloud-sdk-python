# coding:utf-8
import hashlib
import hmac
import sys
from functools import reduce

try:
    from urllib import quote
except:
    from urllib.parse import quote


class Util(object):
    @staticmethod
    def norm_uri(path):
        return quote(path).replace('%2F', '/').replace('+', '%20')

    @staticmethod
    def norm_query(params):
        query = ''
        for key in sorted(params.keys()):
            query = query + quote(key, safe='-_.~') + '=' + quote(params[key],
                                                                  safe='-_.~') + '&'
        query = query[:-1]
        return query.replace('+', '%20')

    @staticmethod
    def hmac_sha256(key, content):
        # type(key) == <class 'bytes'>
        if sys.version_info[0] == 3:
            return hmac.new(key, bytes(content, encoding='utf-8'), hashlib.sha256).digest()
        else:
            return hmac.new(key, content, hashlib.sha256).digest()

    @staticmethod
    def sha256(content):
        # type(content) == <class 'str'>
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    @staticmethod
    def to_hex(content):
        lst = []
        for ch in content:
            if sys.version_info[0] == 3:
                hv = hex(ch).replace('0x', '')
            else:
                hv = hex(ord(ch)).replace('0x', '')
            if len(hv) == 1:
                hv = '0' + hv
            lst.append(hv)
        return reduce(lambda x, y: x + y, lst)
