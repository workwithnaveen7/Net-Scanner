from jinja2 import Template

def generate_html_report(hosts_info, template_file, output_file):
    with open(template_file, 'r') as file:
        template = Template(file.read())

    report_html = template.render(hosts=hosts_info)

    with open(output_file, 'w') as file:
        file.write(report_html)
