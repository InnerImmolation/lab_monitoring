import collections
import psutil
from monitoring import b2h


def list_interfaces(interfaces):
    result = {}
    list(map(lambda x: result.update({x : list(map(lambda y: y._asdict(), interfaces[x]))}), interfaces))
    return result

class Monitoring:
    def __init__(self, interval):
        self.interval = int(interval)
        self.result = dict(cpu=psutil.cpu_times_percent(self.interval)._asdict(),
                           mem_usage=psutil.swap_memory()._asdict(),
                           disk_io=psutil.disk_io_counters()._asdict(),
                           network_io_stats=psutil.net_io_counters()._asdict(),
                           network_interfaces=list_interfaces(psutil.net_if_addrs()))
    @property
    def getResult(self):
        return self.result
    @property
    def buildTxt(self):
        def tree(tr):
            if type(tr) == list:
                for item in tr:
                    return tree(item)
            if type(tr) is collections.OrderedDict:
                return '\n'.join(list(map(lambda x: '\t{}:{}'.format(x.capitalize(), b2h.bytes2human(tr.get(x)) if isinstance(tr.get(x),int) else tr.get(x)), tr.keys())))
            if type(tr) == dict:
                return '\n'.join(list(map(lambda x: '{}: \n{}'.format(x.capitalize(), tree(tr[x])), tr.keys())))
        return tree(self.getResult)
