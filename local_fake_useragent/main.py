# -*- coding: utf-8 -*-
# @Author: Mehaei
# @Date:   2019-09-27 17:46:15
# @Last Modified by:   Mehaei
# @Last Modified time: 2022-06-21 11:06:17
import random
from local_fake_useragent.featured_ua import ua_list
from local_fake_useragent.errors import CustomHeaderFormatError, BrowserNotExistsError


class LocalUserAgent(object):
    BROWER = tuple(ua_list.keys())

    def __init__(self, browser=None, add_custom_header=None):
        """
        The local version randomly returns request headers
        :param browser: Specify the browser, return the request header
        :param add_custom_header: Add custom request headers， ie: {"a":["b","c]}
        """
        if add_custom_header:
            LocalUserAgent.check_custom_header(add_custom_header)
            LocalUserAgent.add_custom_header(add_custom_header)
        if browser and browser not in LocalUserAgent.BROWER:
            raise BrowserNotExistsError("Brower %s Not Found, Supported Browsers: %s" % (browser ,LocalUserAgent.BROWER))
        self.browser = browser

    @property
    def rget(self):
        """
        Randomly return request headers
        :return: requests headers
        """
        if self.browser:
            return random.choice(ua_list[self.browser])
        return random.choice(ua_list[random.choice(LocalUserAgent.BROWER)])

    @staticmethod
    def add_custom_header(headers):
        """
        Add custom request headers， ie: {"a":["b","c]}
        :param headers: Custom request headers
        :return: None
        """
        for key, value in headers.items():
            if key in LocalUserAgent.BROWER:
                ua_list[key].extend(list(value))
            else:
                ua_list[key] = value
        LocalUserAgent.BROWER = tuple(ua_list.keys())

    @staticmethod
    def check_custom_header(headers):
        """
        Check custom request headers， ie: {"a":["b","c]}
        :param headers: Custom request headers
        :return: None
        """
        if not isinstance(headers, dict):
            raise CustomHeaderFormatError("Custom headers require a dictionary type")

        for key, value in headers.items():
            if not isinstance(key, str):
                raise CustomHeaderFormatError("Custom headers key must be a string type")

            if not isinstance(value, (list, set, tuple)):
                raise CustomHeaderFormatError("Custom headers value must be a collection type")

            for hvalue in value:
                if not hvalue:
                    raise CustomHeaderFormatError("Custom headers cannot contain null values")
                if not isinstance(hvalue, str):
                    raise CustomHeaderFormatError("Custom headers list must be a string type")


if __name__ == "__main__":
    # 获取所有浏览器的随机请求头
    # u = LocalUserAgent()

    # 获取chrome的随机请求头
    u = LocalUserAgent("chrome")

    c = {
        "0": ["a", "b"]
    }
    # 添加自定义请求头
    # u = LocalUserAgent("0", add_custom_header=c)

    print(u.rget)

    # 支持的浏览器
    print(LocalUserAgent.BROWER)