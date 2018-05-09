# coding:utf-8

import requests
import config
import uuid
import logging
import os


url = "http://222.24.62.120/CheckCode.aspx"

headers = {
 'User-Agent':'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1',
 'referer': url,
 'accept-language':"zh-CN,zh;q=0.8,en;q=0.6",
 'accept-encoding':'gzip, deflate, sdch, br',
 'accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}


def get_image():
    r = requests.get(url, headers=headers)
    return r.content


def save_image(num=100, path=config.DATA_PATH):
    for i in range(num):
        p = os.path.join(path, "{name}.gif".format(name=str(uuid.uuid1()).replace(" ", "")))
        with open(p, "wb") as f:
            f.write(get_image())
            logging.debug("{i} download done!".format(**vars()))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    handlers=[logging.FileHandler(config.LOG_FILE),
                              logging.StreamHandler()])

    save_image()