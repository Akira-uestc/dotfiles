import time

import requests as rq

post_url_ip = "172.25.249.69"  # post_url的ip
post_data_queryString = "userip=100.66.199.32&wlanacname=&nasip=171.88.130.251&wlanparameter=08-26-ae-3a-c9-0d&url=http://123.123.123.123/&userlocation=ethtrunk/3:411.1021"  # post_data的queryString字段
post_data_userId = "19982076259"  # post_data的userId字段
post_data_password = "42ec653fc30c627c25cbd13d5dce8d55c014f6b6ee2739e43a9ab40544f37c55dd79d1d8b5cd39ebb938a796b75e03fde81487f70ff882a2ab639e2db0115a7528399c62998e4bb518a995eee677ef401bd7cb2de5778c00c767d7741dbbdcc06818cff955d9203f42555e80c44bc562a469046ee2c059ff43aa016536219785"  # post_data的password字段


header = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en,ru;q=0.9,ja;q=0.8,zh-CN;q=0.7,zh;q=0.6,ko;q=0.5,zh-TW;q=0.4",
    "Connection": "keep-alive",
    "Content-Length": "580",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}
post_data = {
    "userId": post_data_userId,
    "password": post_data_password,
    "queryString": post_data_queryString,
    "passwordEncrypt": "true",
}
post_url = "http://" + post_url_ip + "/eportal/InterFace.do?method=login"


def login():
    z = rq.post(url=post_url, data=post_data, headers=header)
    # print(z.content.decode("utf-8").split(",")[1])
    response = z.content.decode("utf-8")
    if "success" in response:
        return True
    return False


if __name__ == "__main__":
    time.sleep(10)
    for i in range(0, 10):
        time.sleep(6)
        login()
