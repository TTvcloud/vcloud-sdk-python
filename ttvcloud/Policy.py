# coding:utf-8
import json
try:
    from ttvcloud.Encoder import JSONEncoder
except:
    from ttvcloud.EncoderV3 import JSONEncoder


class ComplexEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Statement):
            return {'Effect_1': o.effect,
                    'Action_2': o.action,
                    'Resource_3': o.resource}
        if isinstance(o, InnerToken):
            return {
                'LTAccessKeyId_1': o.lt_access_key_id,
                'AccessKeyId_2': o.access_key_id,
                'SignedSecretAccessKey_3': o.signed_secret_access_key,
                'ExpiredTime_4': o.expired_time,
                'PolicyString_5': o.policy_string,
                'Signature_6': o.signature
            }
        if isinstance(o, Policy):
            return {
                'Statement_1': [item for item in o.statements]
            }
        return JSONEncoder.default(self, o)


class Policy(object):
    def __init__(self, statements):
        self.statements = statements


class Statement(object):
    def __init__(self):
        self.effect = ''
        self.action = []
        self.resource = []
        self.condition = ''

    @staticmethod
    def new_allow_statement(actions, resources):
        s = Statement()
        s.effect = "Allow"
        s.action = actions
        s.resource = resources
        return s

    @staticmethod
    def new_deny_statement(actions, resources):
        s = Statement()
        s.effect = "Deny"
        s.action = actions
        s.resource = resources
        return s


class SecurityToken2(object):
    def __init__(self):
        self.access_key_id = ''
        self.secret_access_key = ''
        self.session_token = ''
        self.expired_time = ''

    def __str__(self):
        return json.dumps({
            'AccessKeyId': self.access_key_id,
            'SecretAccessKey': self.secret_access_key,
            'SessionToken': self.session_token,
            'ExpiredTime': self.expired_time
        })


class InnerToken(object):
    def __init__(self):
        self.lt_access_key_id = ''
        self.access_key_id = ''
        self.signed_secret_access_key = ''
        self.expired_time = 0
        self.policy_string = ''
        self.signature = ''
