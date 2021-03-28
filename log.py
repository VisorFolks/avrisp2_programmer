log_level = 0

def set_level(level):
    global log_level
    log_level = level
    return

def l1(info):
    if(log_level >= 0):
        print("INFO: " + info)
    return

def l2(info):
    if(log_level >= 1):
        print("INFO: " + info)
    return

def errexit(info):
    print("Error: " + info)
    exit(-1)