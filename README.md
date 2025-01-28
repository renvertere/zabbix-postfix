<div id="top"></div>

<h1 align="center">Zabbix Postfix Monitoring Solution</h1>

<br />
<div align="center">

[![YAML][yaml-shield]][yaml-url]
[![Python][python-shield]][python-url]
[![Github Actions][github-actions-shield]][github-actions-url]

![Release Pipeline][test-pipline-badge]

</div>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/renvertere/zabbix-postfix">
    <img src="resources/img/zabbix_logo.svg" alt="Logo" width="420" height="120">
    <br >
    <img src="resources/img/postfix_logo.svg" alt="Logo" width="420" height="120">
  </a>

  <h3 align="center">Zabbix Postfix Monitoring Solution</h3>

  <p align="center">
    This repository houses the required scripts and configuration to implement Zabbix monitoring for the Postfix mail server.
    <br />
    <a href="https://github.com/renvertere/zabbix-postfix"><strong>Explore the documentation »</strong></a>
    <br />
    <br />
    <a href="https://github.com/renvertere/zabbix-postfix">View Demo</a>
    ·
    <a href="https://github.com/renvertere/zabbix-postfix/issues">Report Bug</a>
    ·
    <a href="https://github.com/renvertere/zabbix-postfix/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Disclaimer](#disclaimer)
- [Getting Started](#getting-started)
  - [Deployment Steps](#deployment-steps)
- [Usage](#usage)
  - [Monitoring Metrics in Zabbix](#monitoring-metrics-in-zabbix)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)
- [References](#references)

<!-- ABOUT THE PROJECT -->
## About The Project

The Zabbix Postfix Monitoring Solution enables monitoring of key Postfix metrics through custom Zabbix user parameters and sudoers configuration. It allows you to monitor Postfix server status, version, and mail queue details, providing essential insights into the Postfix environment.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Zabbix](https://www.zabbix.com/)
* [Postfix](http://www.postfix.org/)
* [Linux](https://www.linux.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- DISCLAIMER -->
## Disclaimer

This project is provided "as is" without any warranties or support. The authors disclaim any liability for damages arising from its use. Compatibility has been tested with Zabbix 6.0 LTS on Ubuntu (22.04/20.04), but functionality on other systems cannot be guaranteed.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To set up this monitoring solution, you need to upload the Postfix template to the zabbix server, configure custom Zabbix user parameters and adjust the sudoers file to grant necessary permissions on the target host.

### Deployment Steps

1. **Clone the repository**
2. **Load the template `resources/zabbix/template/template_app_postfix.yaml` on to your Zabbix server**
3. **Copy the User Parameters Configuration**
4. **Update the Sudoers File**
5. **Restart the Zabbix Agent**

<br />

#### Run on Target Host (Postfix Server)

   ```bash
   git clone git@github.com:renvertere/zabbix-postfix.git
   cd zabbix-postfix
   sudo cp -Rvf resources/zabbix/userparameter/userparameter_postfix.conf /etc/zabbix/zabbix_agent2.d/plugins.d
   systemctl restart zabbix-agent2
   ```

<p align="right">(<a href="#top">back to top</a>)</p> <!-- USAGE EXAMPLES -->

## Usage
Once the template has been applied against a target host, the Zabbix Postfix Monitoring Solution will start collecting data from the Postfix server and making it available for monitoring in Zabbix.

## Monitoring Metrics in Zabbix
- Postfix Version: Displays the version of Postfix installed on the server.
- Postfix Startup Status: Indicates whether Postfix is enabled to start at boot.
- Total Mail Queue Count: Shows the total number of emails currently in the Postfix mail queue.
- Custom Mail Queue Counts: Monitors specific file counts within Postfix queues based on custom filters.
<p align="right">(<a href="#top">back to top</a>)</p> <!-- ROADMAP -->

## Roadmap
- [x] Develop custom user parameters for Postfix monitoring.
- [x] Configure Zabbix sudoers to allow necessary command execution.
- [x] Extend monitoring to include more detailed Postfix metrics.
- [x] Provide additional alerting and reporting capabilities.

See the open issues for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p> <!-- CONTRIBUTING -->

## Contributing
[![Contributors][contributors-shield]][contributors-url]

Contributions are welcome! Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

<p align="right">(<a href="#top">back to top</a>)</p> <!-- LICENSE -->

## License
Distributed under the MIT License. See LICENSE.md for more information.

<p align="right">(<a href="#top">back to top</a>)</p> <!-- CONTACT -->

## Contact
Ren - @renvertere

Project Link: https://github.com/renvertere/zabbix-postfix

<p align="right">(<a href="#top">back to top</a>)</p> <!-- ACKNOWLEDGMENTS -->

## Acknowledgments
- Zabbix
- Postfix
- Linux
<p align="right">(<a href="#top">back to top</a>)</p> <!-- MARKDOWN LINKS & IMAGES --> <!-- FOOTER --> <footer> DevOps: Repetitio. Conventio. Duplicatio. Creatio ad perfectionem redacta.</footer> 


<!-- MARKDOWN LINKS & IMAGES -->
[yaml-shield]: https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515
[yaml-url]: https://github.com/renvertere/zabbix-postfix
[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://github.com/renvertere/zabbix-postfix
[github-actions-shield]: https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white
[github-actions-url]: https://github.com/renvertere/zabbix-postfix/actions
[test-pipline-badge]: https://github.com/renvertere/zabbix-postfix/actions/workflows/release-ci.yml/badge.svg
[contributors-shield]: https://img.shields.io/github/contributors/renvertere/zabbix-postfix.svg?style=for-the-badge
[contributors-url]: https://github.com/renvertere/zabbix-postfix/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/renvertere/zabbix-postfix.svg?style=for-the-badge
[forks-url]: https://github.com/renvertere/zabbix-postfix/network/members
[stars-shield]: https://img.shields.io/github/stars/renvertere/zabbix-postfix.svg?style=for-the-badge
[stars-url]: https://github.com/renvertere/zabbix-postfix/stargazers
[issues-shield]: https://img.shields.io/github/issues/renvertere/zabbix-postfix.svg?style=for-the-badge
[issues-url]: https://github.com/renvertere/zabbix-postfix/issues
[license-shield]: https://img.shields.io/github/license/renvertere/zabbix-postfix.svg?style=for-the-badge
[license-url]: https://github.com/renvertere/zabbix-postfix/blob/main/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/renvertere-80349925/
[product-screenshot]: resources/img/zabbix_logo.png