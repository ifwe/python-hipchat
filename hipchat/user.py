import hipchat.config
import json

from urllib import urlencode
from urllib2 import urlopen, Request

def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc


def call_hipchat(cls, ReturnType, url, data=True, **kw):
    auth = [('format', 'json'), ('auth_token', hipchat.config.token)]
    if not data:
        auth.extend(kw.items())
    req = Request(url=url + '?%s' % urlencode(auth))
    if data:
        req.add_data(urlencode(kw.items()))
    print ReturnType
    return ReturnType(json.load(urlopen(req)))
                     

class HipChatObject(object):
    def __init__(self, jsono):
        self.jsono = jsono
        print jsono
        for k, v in jsono[self.sort].iteritems():
            setattr(self, k, v)

    def __str__(self):
        return json.dumps(self.jsono)


class UserDeleteStatus(HipChatObject):
    sort = 'delete'
    def __init__(self, jsono):
        self.jsono = jsono
        self.deleted = jsono.get('deleted')


class User(HipChatObject):
    sort = 'user'


User.create = classmethod(partial(call_hipchat, User, url="https://api.hipchat.com/v1/users/create", data=True))
User.delete = \
    classmethod(partial(call_hipchat, 
                        ReturnType=UserDeleteStatus, 
                        url="https://api.hipchat.com/v1/users/delete", 
                        data=True))
User.list_all = \
    classmethod(partial(call_hipchat, 
                        ReturnType=lambda x: map(User, map(lambda y: {'user': y}, x['users'])), 
                        url="https://api.hipchat.com/v1/users/list", 
                        data=False))
User.show = classmethod(partial(call_hipchat, User, url="https://api.hipchat.com/v1/users/show", data=False))
User.update = classmethod(partial(call_hipchat, User, url="https://api.hipchat.com/v1/users/update", data=True))
