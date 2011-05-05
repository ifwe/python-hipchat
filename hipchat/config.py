from configobj import ConfigObj

token = 0

def init_cfg(config_fname):
    cfg = ConfigObj(config_fname)
    global token
    token = cfg['token']
