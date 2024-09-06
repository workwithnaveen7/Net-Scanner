import xml.etree.ElementTree as ET

def parse_nmap_results(scan_file):
    tree = ET.parse(scan_file)
    root = tree.getroot()
    hosts_info = []

    for host in root.findall('host'):
        host_info = {}
        address = host.find('address').get('addr')
        host_info['address'] = address

        ports = []
        for port in host.findall('./ports/port'):
            port_info = {
                'portid': port.get('portid'),
                'protocol': port.get('protocol'),
                'state': port.find('state').get('state'),
                'service': port.find('service').get('name')
            }
            ports.append(port_info)

        host_info['ports'] = ports
        hosts_info.append(host_info)

    return hosts_info
