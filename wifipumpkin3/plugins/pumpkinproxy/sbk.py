from wifipumpkin3.plugins.pumpkinproxy.base import BasePumpkin
from bs4 import BeautifulSoup


class sbk(BasePumpkin):
    meta = {
        "_name": "sbk",
        "_version": "1.1",
        "_description": "TEST 1.",
        "_author": "by Maintainer",
    }

    @staticmethod
    def getName():
        return sbk.meta["_name"]

    def __init__(self):
        for key, value in self.meta.items():
            self.__dict__[key] = value
        self.ConfigParser = False
    def handleResponse(self, request, data):

        print('---------------------------- TEST ------------------- ')
        print('---------------------------- TEST ------------------- ')

        print(request)
        print('---------------------------- TEST ------------------- ')
        
        return data
    

    #def handleHeader(self, request, key, value):
