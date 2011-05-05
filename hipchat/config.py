from configobj import ConfigObj

class HipChatConfig(object): pass

token = 0

def init_cfg(config_fname):
    cfg = ConfigObj(config_fname)
    global token
    token = cfg['token']
