# Net-Scanner

Net-Scanner is a user-friendly web-based network scanning tool that leverages Nmap to identify open ports and services on target URLs. Designed for simplicity and efficiency, it provides a straightforward interface for users to perform network scans and view results directly in their browser.

## Features

- **Network Scanning**: Performs scans using Nmap to discover open ports and services.
- **Detailed Reports**: Generates comprehensive scan reports in HTML format.
- **User-Friendly Interface**: Simple and intuitive web interface for entering scan targets and viewing results.

## Usage

1. **Run the Flask application:**

    ```bash
    python app.py
    ```

2. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:5000
    ```

3. **Enter the target URL and click "Start Scan".** The application will perform a scan and display the results on a new page.

![netscanner_image](https://github.com/user-attachments/assets/d60c7a8c-58fb-4b2d-9d16-a22886c271ff)

After scanning a target, you will see a detailed report showing the open ports and services. Here is a sample report:

![netscanner_report](https://github.com/user-attachments/assets/aeda72f3-17f3-4e67-adfb-09baa813400d)

