import requests


def get_output(adr, api, uuid, remote_uuid):
    addr = adr + "api/protected_instance/outputlog"
    param = {
        "uuid": uuid,
        "remote_uuid": remote_uuid,
        "apikey": api,
    }
    try:
        response = requests.get(url=addr, params=param)
        # print(response.status_code)

    except:
        return -1
    else:
        return response.text


# if __name__=='__main__':
#     outputGet(r'http://mc.rjack.cn:23333/',r'c34b1a982fbc45fc8c62e2a95d9ab39e',r'e72b16a852fd4843a5ebe6ed9e268949',r'd1b6e8dac1804fa8b51c74b4ce66764b')
