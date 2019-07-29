# coding:utf-8
import hashlib
import hmac
import urllib


class Util(object):
    @staticmethod
    def norm_uri(path):
        return urllib.quote(path).replace('%2F', '/').replace('+', '%20')

    @staticmethod
    def norm_query(params):
        query = ''
        for key in sorted(params.keys()):
            query = query + urllib.quote(key, safe='-_.~') + '=' + urllib.quote(params[key],
                                                                                safe='-_.~') + '&'
        query = query[:-1]
        return query.replace('+', '%20')

    @staticmethod
    def hmac_sha1(key, content):
        return hmac.new(key, content, hashlib.sha1).digest()

    @staticmethod
    def hmac_sha256(key, content):
        return hmac.new(key, content, hashlib.sha256).digest()

    @staticmethod
    def sha256(content):
        return hashlib.sha256(content).hexdigest()

    @staticmethod
    def to_hex(content):
        lst = []
        for ch in content:
            hv = hex(ord(ch)).replace('0x', '')
            if len(hv) == 1:
                hv = '0' + hv
            lst.append(hv)
        return reduce(lambda x, y: x + y, lst)
