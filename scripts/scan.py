import subprocess

def run_nmap_scan(target):
    scan_file = "scans/scan_results.xml"
    nmap_command = ["nmap", "-oX", scan_file, target]
    subprocess.run(nmap_command)
    return scan_file
