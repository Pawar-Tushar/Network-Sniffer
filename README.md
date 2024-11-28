# SecureNet Analyzer

**SecureNet Analyzer** is a powerful Python-based network traffic monitoring and security tool designed for network administrators, cybersecurity professionals, and penetration testers. This tool provides real-time packet capture, live host detection, vulnerability analysis, and secure user authentication to ensure robust network security.

---

## Overview

**SecureNet Analyzer** captures and analyzes network traffic, detects live devices on the network, and helps identify potential vulnerabilities and threats. Leveraging the **Scapy** library for packet crafting, it offers real-time packet analysis, live host detection using ARP requests, custom packet creation, and secure user authentication with SHA-256 hashing for login security.

The tool is ideal for network monitoring, device enumeration, and testing the resilience of your network against various cyber threats.

---

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation Instructions](#installation-instructions)
4. [Usage Examples](#usage-examples)
5. [Security Considerations](#security-considerations)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [Legal Disclaimer](#legal-disclaimer)
9. [License](#license)
10. [Acknowledgements](#acknowledgements)
11. [Conclusion](#conclusion)
12. [Contact](#contact)

---

## Features

- **Packet Capture and Analysis**: Capture and analyze network traffic from any network interface. Extract detailed information including IPs, ports, protocols, and payloads.
- **Live Host Detection**: Detect live devices on your network using ARP requests, and map IP and MAC addresses.
- **Packet Creation and Sending**: Craft custom packets and send them to specified addresses for network testing and vulnerability assessment.
- **SHA-256 Authentication**: Implement secure user authentication with password hashing using SHA-256.
- **Data Export**: Export captured packets in **PCAP** and **TXT** formats for further analysis and sharing.
- **Vulnerability Detection**: Analyze packets to detect unusual traffic patterns and potential security issues.

---

## Requirements

- **Python 3**: Ensure you have Python 3 or later installed.
- **Scapy Library**: This tool requires Scapy for network packet crafting.


---

## Installation Instructions

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/Pawar-Tushar/SecureNet-Analyzer.git

2. **Navigate to the project directory:**
    ```bash
    cd SecureNet-Analyzer
    ```

3. **Install the required dependencies using pip**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the Application**:
    ```bash
    python Main.py  [option] [arguments]
    ```

### Ensure Privileges:
Since the tool requires access to network interfaces, make sure to run the script with elevated privileges:

- **On Linux/macOS:**
    ```bash
    sudo python main.py
    ```

- **On Windows:** Ensure you run the command prompt or PowerShell as **Administrator**.

---

## Usage Examples

The tool operates via the command line interface (CLI). Below are some basic commands and examples:

### Options:
- `-c` or `--capture`: Start packet capture and analysis.
- `-lh` or `--live-host`: Perform live host detection on the network.

### Common Arguments:
- `--i [interface]`: Specify the network interface to capture packets from (e.g., eth0, Wi-Fi).
- `--pc [number]`: Specify the number of packets to capture.
- `--a`: Analyze captured packets in real-time.
- `--s`: Save captured packets.
- `--p [filename]`: Save captured packets in PCAP format.
- `--t [filename]`: Save captured packets in TXT format.
- `--f [filter]`: Define a filter condition (e.g., 'src host 192.168.1.1 and tcp').
- `--ip [IP address]`: Specify an IP address for live host detection.

### Example 1: Start Packet Capture
```bash
python Main.py c --i Wi-Fi --pc 10 --a --s --p captured_traffic.pcap 
```

### Example 2: Live Host Detection
```bash
python Main.py lh --ip 192.168.1.1
```
## Security Considerations

- **Password Storage**: Passwords are securely stored using SHA-256 hashing and never stored in plain text.
- **Network Monitoring**: Use the tool responsibly only on networks where you have explicit permission to capture and analyze traffic. Unauthorized traffic analysis may be illegal and unethical.
- **ARP Spoofing**: The tool uses ARP requests for live host detection, which could trigger ARP spoofing alerts on certain networks. Ensure the tool is used in authorized environments.

---

## Troubleshooting

- **Permission Issues**: If you are unable to capture packets, ensure you are running the tool with the appropriate permissions (e.g., using **sudo** on Linux/macOS).
- **Missing Dependencies**: If the tool fails to run due to missing dependencies, verify that you have installed all required packages as outlined in the installation instructions.
- **Network Interface Not Detected**: If the network interface is not detected, verify it is available by running **ifconfig** (Linux/macOS) or **ipconfig** (Windows) to check available interfaces.

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your improvements or bug fixes. When submitting changes, please ensure:

- Code is well-documented.
- Any new features are accompanied by clear explanations and examples.
- Tests are provided for new functionalities (if applicable).

---

## Legal Disclaimer

The use of code contained in this repository, either in part or in its entirety, for engaging with targets without prior, explicit mutual consent is **illegal**. It is the **end user's responsibility** to comply with all applicable **local, state, and federal laws**.

The developers assume **no liability** and are **not responsible** for any misuse or damages caused by the use of any code contained in this repository. This applies in any event, whether **accidental** or **intentional**, if the code is utilized by a threat actor or unauthorized entity to **compromise** the security, privacy, confidentiality, integrity, and/or availability of systems or associated resources. In this context, **"compromise"** refers to the **exploitation of known or unknown vulnerabilities** in systems, including, but not limited to, weaknesses in **security controls** (human- or electronically-enabled).

The developers explicitly endorse the use of this code only in **educational environments** for the purpose of learning or teaching cybersecurity concepts and in **authorized penetration testing engagements**, where the system owner has given **explicit consent**. The goal should be to identify and mitigate vulnerabilities and protect systems from potential exploitation by malicious agents, as outlined in the respective threat models.
Before using this tool, ensure you have **written authorization** and adhere to all relevant laws and ethical guidelines.
**It is crucial that this tool is used ethically and legally. Unauthorized use could result in severe consequences under law.**

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **Scapy**: For providing powerful functionality for packet crafting and sending.
- **Python 3.x**: For the simplicity and flexibility it offers for network programming.
- **Wireshark**: For being a trusted tool for analyzing PCAP files, which you can use alongside this tool.

---

## Conclusion

**SecureNet Analyzer** is a robust and versatile tool designed for network security monitoring, packet analysis, and vulnerability detection. Whether you are a network administrator, a cybersecurity professional, or a penetration tester, this tool will provide valuable insights into network behavior, enhance security monitoring, and assist with identifying potential threats and vulnerabilities.

## Contact

For any queries or issues, feel free to reach out via GitHub Issues or email me at [tusharpawar@749963.com].




