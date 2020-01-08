import psutil
import build_txt
import json
def monitoring(interval, type):
    result = {}
    result['cpu'] = psutil.cpu_times_percent(interval)._asdict()
    result['mem_usage'] = psutil.swap_memory()._asdict()
    result['virtual_mem_usage'] = psutil.virtual_memory()._asdict()
    result['disk i/o'] = psutil.disk_io_counters()._asdict()
    result['network io stats'] = psutil.net_io_counters()._asdict()
    result['network interfaces'] = {}
    network_interfaces = psutil.net_if_addrs()
    for interface in network_interfaces:
        result['network interfaces'][interface] = {}
        for interface_param in network_interfaces[interface]:
            result['network interfaces'][interface] = interface_param._asdict()
    if type == 'json':
        with open('data.json', 'w') as outfile:
            json.dump(result, outfile)
    elif type == 'txt':
        with open('data.txt', 'w') as outfile:
            outfile.write(build_txt.tree(result))
    return result
monitoring(1, 'json')
