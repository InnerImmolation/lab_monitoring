import os
import json
from monitoring.Monitoring import Monitoring


class Export(Monitoring):
    def __init__(self, interval, type):
        Monitoring.__init__(self, interval)
        self.type = str(type)
    def exportResult(self):
        if self.type == 'json':
            with open('data.json', 'w') as outfile:
                json.dump(self.getResult, outfile)
            print('Export in {}\\data.json'.format(os.path.abspath(os.curdir)))
        elif self.type == 'txt':
            with open('data.txt', 'w') as outfile:
                outfile.write(self.buildTxt())
            print('Export in {}\\data.txt'.format(os.path.abspath(os.curdir)))
