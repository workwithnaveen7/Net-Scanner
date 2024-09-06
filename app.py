from flask import Flask, render_template, request
import subprocess
import xml.etree.ElementTree as ET
from jinja2 import Template

app = Flask(__name__)

def parse_nmap_results(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    hosts_info = []
    for host in root.findall('host'):
        address = host.find('address').attrib['addr']
        host_info = {'address': address, 'ports': []}
        for port in host.find('ports').findall('port'):
            port_info = {
                'portid': port.attrib['portid'],
                'protocol': port.attrib['protocol'],
                'state': port.find('state').attrib['state'],
                'service': port.find('service').attrib.get('name', 'unknown')
            }
            host_info['ports'].append(port_info)
        hosts_info.append(host_info)
    
    return hosts_info

def generate_html_report(hosts_info, template_file, output_file):
    with open(template_file, 'r') as file:
        template_content = file.read()
    template = Template(template_content)

    report_html = template.render(hosts=hosts_info)

    with open(output_file, 'w') as file:
        file.write(report_html)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']
    output_file = "scans/scan_results.xml"
    

    subprocess.run(['nmap', '-oX', output_file, target])
    

    hosts_info = parse_nmap_results(output_file)
    if hosts_info:
        generate_html_report(hosts_info, "templates/report_template.html", "templates/report.html")
    else:
        return render_template('index.html', error="No hosts found in scan results.")
    
    return render_template('report.html', hosts=hosts_info)

if __name__ == "__main__":
    app.run(debug=True)
