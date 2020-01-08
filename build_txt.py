import b2h
import collections
#data1 =  {'cpu': '{"user": 2.1, "system": 2.5, "idle": 94.8, "interrupt": 0.6, "dpc": 0.0}', 'mem_usage': '{"total": 33730158592, "used": 17661227008, "free": 16068931584, "percent": 52.4, "sin": 0, "sout": 0}', 'virtual_mem_usage': '{"total": 16550289408, "available": 722100224, "percent": 95.6, "used": 15828189184, "free": 722100224}', 'disk i/o': '{"read_count": 3002836, "write_count": 2976320, "read_bytes": 73050704384, "write_bytes": 154726665216, "read_time": 3372, "write_time": 3254}', 'network io stats': '{"bytes_sent": 58969786, "bytes_recv": 262722055, "packets_sent": 202260, "packets_recv": 892811, "errin": 0, "errout": 0, "dropin": 0, "dropout": 0}', 'network interfaces': {'VirtualBox Host-Only Network': '{"family": 23, "address": "fe80::fc40:ecca:1267:6c3e", "netmask": null, "broadcast": null, "ptp": null}', 'Ethernet': '{"family": 23, "address": "fe80::a049:9a63:3ab8:9966", "netmask": null, "broadcast": null, "ptp": null}', 'Loopback Pseudo-Interface 1': '{"family": 23, "address": "::1", "netmask": null, "broadcast": null, "ptp": null}'}}
#'\t{}: {}'.format(x.capitalize(), b2h.bytes2human(tr.get(x)) if isinstance(tr.get(x), int) else tr.get(x))

def tree(tr):
  if type(tr) is collections.OrderedDict:
    return '\n'.join(list(map(lambda x: '\t{}:{}'.format(x.capitalize(),  b2h.bytes2human(tr.get(x)) if isinstance(tr.get(x), int) else tr.get(x)), tr.keys())))
  if(type(tr) == dict):
    return '\n'.join(list(map(lambda x: '{}: \n{}'.format(x.capitalize(), tree(tr[x])), tr.keys())))

