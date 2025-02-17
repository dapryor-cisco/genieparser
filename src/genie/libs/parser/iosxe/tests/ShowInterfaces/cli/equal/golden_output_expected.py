expected_output = {
    "Port-channel12": {
        "flow_control": {"send": False, "receive": False},
        "err_disabled": False,
        "suspended": False,
        "type": "EtherChannel",
        "counters": {
            "out_buffer_failure": 0,
            "out_underruns": 0,
            "in_giants": 0,
            "in_throttles": 0,
            "in_frame": 0,
            "in_ignored": 0,
            "last_clear": "1d23h",
            "out_interface_resets": 2,
            "in_mac_pause_frames": 0,
            "out_collision": 0,
            "rate": {
                "out_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "in_rate": 2000,
                "in_rate_pkts": 2,
            },
            "in_watchdog": 0,
            "out_deferred": 0,
            "out_mac_pause_frames": 0,
            "in_pkts": 961622,
            "in_multicast_pkts": 4286699522,
            "in_runts": 0,
            "out_unknown_protocl_drops": 0,
            "in_no_buffer": 0,
            "out_buffers_swapped": 0,
            "out_lost_carrier": 0,
            "out_errors": 0,
            "in_errors": 0,
            "in_octets": 72614643,
            "in_crc_errors": 0,
            "out_no_carrier": 0,
            "in_with_dribble": 0,
            "in_broadcast_pkts": 944818,
            "out_pkts": 39281,
            "out_late_collision": 0,
            "out_octets": 6235318,
            "in_overrun": 0,
            "out_babble": 0,
        },
        "auto_negotiate": True,
        "phys_address": "0057.d2ff.422a",
        "keepalive": 10,
        "output_hang": "never",
        "txload": "1/255",
        "oper_status": "up",
        "arp_type": "arpa",
        "rxload": "1/255",
        "duplex_mode": "full",
        "link_type": "auto",
        "queues": {
            "input_queue_size": 0,
            "total_output_drop": 0,
            "input_queue_drops": 0,
            "input_queue_max": 2000,
            "output_queue_size": 0,
            "input_queue_flushes": 0,
            "output_queue_max": 0,
            "queue_strategy": "fifo",
        },
        "encapsulations": {
            "encapsulation": "qinq virtual lan",
            "first_dot1q": "10",
            "second_dot1q": "20",
        },
        "last_input": "never",
        "last_output": "1d22h",
        "line_protocol": "up",
        "mac_address": "0057.d2ff.422a",
        "connected": True,
        "port_channel": {
            "port_channel_member": True,
            "port_channel_member_intfs": ["GigabitEthernet1/0/2"],
        },
        "arp_timeout": "04:00:00",
        "bandwidth": 1000000,
        "port_speed": "1000mb/s",
        "enabled": True,
        "mtu": 1500,
        "delay": 10,
        "reliability": "255/255",
    },
    "GigabitEthernet1/0/1": {
        "flow_control": {"send": False, "receive": False},
        "err_disabled": False,
        "suspended": False,
        "type": "Gigabit Ethernet",
        "counters": {
            "out_buffer_failure": 0,
            "out_underruns": 0,
            "in_giants": 0,
            "in_throttles": 0,
            "in_frame": 0,
            "in_ignored": 0,
            "last_clear": "1d02h",
            "out_interface_resets": 2,
            "in_mac_pause_frames": 0,
            "out_collision": 0,
            "rate": {
                "out_rate_pkts": 0,
                "load_interval": 30,
                "out_rate": 0,
                "in_rate": 0,
                "in_rate_pkts": 0,
            },
            "in_watchdog": 0,
            "out_deferred": 0,
            "out_mac_pause_frames": 0,
            "in_pkts": 12127,
            "in_multicast_pkts": 4171,
            "in_runts": 0,
            "out_unknown_protocl_drops": 0,
            "in_no_buffer": 0,
            "out_buffers_swapped": 0,
            "out_lost_carrier": 0,
            "out_errors": 0,
            "in_errors": 0,
            "in_octets": 2297417,
            "in_crc_errors": 0,
            "out_no_carrier": 0,
            "in_with_dribble": 0,
            "in_broadcast_pkts": 4173,
            "out_pkts": 12229,
            "out_late_collision": 0,
            "out_octets": 2321107,
            "in_overrun": 0,
            "out_babble": 0,
        },
        "phys_address": "0057.d2ff.428c",
        "keepalive": 10,
        "output_hang": "never",
        "txload": "1/255",
        "description": "desc",
        "oper_status": "down",
        "arp_type": "arpa",
        "rxload": "1/255",
        "duplex_mode": "auto",
        "queues": {
            "input_queue_size": 0,
            "total_output_drop": 0,
            "input_queue_drops": 0,
            "input_queue_max": 375,
            "output_queue_size": 0,
            "input_queue_flushes": 0,
            "output_queue_max": 40,
            "queue_strategy": "fifo",
        },
        "ipv4": {"10.1.1.1/24": {"prefix_length": "24", "ip": "10.1.1.1"}},
        "encapsulations": {"encapsulation": "arpa"},
        "last_input": "never",
        "last_output": "04:39:18",
        "line_protocol": "down",
        "mac_address": "0057.d2ff.428c",
        "connected": False,
        "port_channel": {"port_channel_member": False},
        "media_type": "10/100/1000BaseTX",
        "bandwidth": 768,
        "port_speed": "1000mb/s",
        "enabled": False,
        "arp_timeout": "04:00:00",
        "mtu": 1500,
        "delay": 3330,
        "reliability": "255/255",
    },
    "GigabitEthernet3": {
        "flow_control": {"send": False, "receive": False},
        "type": "CSR vNIC",
        "auto_negotiate": True,
        "duplex_mode": "full",
        "link_type": "auto",
        "media_type": "RJ45",
        "port_speed": "1000mbps",
        "counters": {
            "out_buffer_failure": 0,
            "out_underruns": 0,
            "in_giants": 0,
            "in_throttles": 0,
            "in_frame": 0,
            "in_ignored": 0,
            "last_clear": "never",
            "out_interface_resets": 1,
            "in_mac_pause_frames": 0,
            "out_collision": 0,
            "in_crc_errors": 0,
            "rate": {
                "out_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "in_rate": 0,
                "in_rate_pkts": 0,
            },
            "in_watchdog": 0,
            "out_deferred": 0,
            "out_mac_pause_frames": 0,
            "in_pkts": 6,
            "in_multicast_pkts": 0,
            "in_runts": 0,
            "in_no_buffer": 0,
            "out_buffers_swapped": 0,
            "out_errors": 0,
            "in_errors": 0,
            "in_octets": 480,
            "out_unknown_protocl_drops": 0,
            "out_no_carrier": 0,
            "out_lost_carrier": 0,
            "in_broadcast_pkts": 0,
            "out_pkts": 28,
            "out_late_collision": 0,
            "out_octets": 7820,
            "in_overrun": 0,
            "out_babble": 0,
        },
        "phys_address": "5254.00ff.0e7e",
        "keepalive": 10,
        "output_hang": "never",
        "txload": "1/255",
        "reliability": "255/255",
        "arp_type": "arpa",
        "rxload": "1/255",
        "queues": {
            "input_queue_size": 0,
            "total_output_drop": 0,
            "input_queue_drops": 0,
            "input_queue_max": 375,
            "output_queue_size": 0,
            "input_queue_flushes": 0,
            "output_queue_max": 40,
            "queue_strategy": "fifo",
        },
        "ipv4": {
            "192.168.154.1/24": {"prefix_length": "24", "ip": "192.168.154.1"},
            "unnumbered": {"interface_ref": "Loopback0"},
        },
        "encapsulations": {"encapsulation": "arpa"},
        "last_output": "00:00:27",
        "line_protocol": "up",
        "mac_address": "5254.00ff.0e7e",
        "oper_status": "up",
        "port_channel": {"port_channel_member": False},
        "arp_timeout": "04:00:00",
        "bandwidth": 1000000,
        "enabled": True,
        "mtu": 1500,
        "delay": 10,
        "last_input": "never",
    },
    "Loopback0": {
        "queues": {
            "input_queue_size": 0,
            "total_output_drop": 0,
            "input_queue_drops": 0,
            "input_queue_max": 75,
            "output_queue_size": 0,
            "input_queue_flushes": 0,
            "output_queue_max": 0,
            "queue_strategy": "fifo",
        },
        "mtu": 1514,
        "encapsulations": {"encapsulation": "loopback"},
        "last_output": "never",
        "type": "Loopback",
        "line_protocol": "up",
        "oper_status": "up",
        "keepalive": 10,
        "output_hang": "never",
        "txload": "1/255",
        "counters": {
            "out_buffer_failure": 0,
            "out_underruns": 0,
            "in_giants": 0,
            "in_throttles": 0,
            "in_frame": 0,
            "in_ignored": 0,
            "last_clear": "1d04h",
            "out_interface_resets": 0,
            "out_collision": 0,
            "rate": {
                "out_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "in_rate": 0,
                "in_rate_pkts": 0,
            },
            "in_pkts": 0,
            "in_multicast_pkts": 0,
            "in_runts": 0,
            "in_no_buffer": 0,
            "out_buffers_swapped": 0,
            "out_errors": 0,
            "in_errors": 0,
            "in_octets": 0,
            "in_crc_errors": 0,
            "out_unknown_protocl_drops": 0,
            "in_broadcast_pkts": 0,
            "out_pkts": 72,
            "out_octets": 5760,
            "in_overrun": 0,
            "in_abort": 0,
        },
        "reliability": "255/255",
        "bandwidth": 8000000,
        "port_channel": {"port_channel_member": False},
        "enabled": True,
        "ipv4": {"192.168.154.1/24": {"prefix_length": "24", "ip": "192.168.154.1"}},
        "rxload": "1/255",
        "delay": 5000,
        "last_input": "1d02h",
    },
    "Vlan100": {
        "type": "Ethernet SVI",
        "counters": {
            "out_buffer_failure": 0,
            "out_underruns": 0,
            "in_giants": 0,
            "in_throttles": 0,
            "in_frame": 0,
            "in_ignored": 0,
            "last_clear": "1d04h",
            "out_interface_resets": 0,
            "rate": {
                "out_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "in_rate": 0,
                "in_rate_pkts": 0,
            },
            "in_pkts": 50790,
            "in_multicast_pkts": 0,
            "in_runts": 0,
            "in_no_buffer": 0,
            "out_buffers_swapped": 0,
            "out_errors": 0,
            "in_errors": 0,
            "in_octets": 3657594,
            "in_crc_errors": 0,
            "out_unknown_protocl_drops": 0,
            "in_broadcast_pkts": 0,
            "out_pkts": 72,
            "out_octets": 5526,
            "in_overrun": 0,
        },
        "phys_address": "0057.d2ff.4279",
        "queues": {
            "input_queue_size": 0,
            "total_output_drop": 0,
            "input_queue_drops": 0,
            "input_queue_max": 375,
            "output_queue_size": 0,
            "input_queue_flushes": 0,
            "output_queue_max": 40,
            "queue_strategy": "fifo",
        },
        "txload": "1/255",
        "reliability": "255/255",
        "arp_type": "arpa",
        "rxload": "1/255",
        "output_hang": "never",
        "ipv4": {"192.168.234.1/24": {"prefix_length": "24", "ip": "192.168.234.1"}},
        "encapsulations": {"encapsulation": "arpa"},
        "last_output": "1d03h",
        "line_protocol": "up",
        "mac_address": "0057.d2ff.4279",
        "oper_status": "up",
        "port_channel": {"port_channel_member": False},
        "arp_timeout": "04:00:00",
        "bandwidth": 1000000,
        "enabled": True,
        "mtu": 1500,
        "delay": 10,
        "last_input": "never",
    },
    "GigabitEthernet1/0/2": {
        "flow_control": {"send": False, "receive": False},
        "err_disabled": False,
        "suspended": False,
        "type": "Gigabit Ethernet",
        "counters": {
            "out_buffer_failure": 0,
            "out_underruns": 0,
            "in_giants": 0,
            "in_throttles": 0,
            "in_frame": 0,
            "in_ignored": 0,
            "last_clear": "1d02h",
            "out_interface_resets": 5,
            "in_mac_pause_frames": 0,
            "out_collision": 0,
            "rate": {
                "out_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "in_rate": 3000,
                "in_rate_pkts": 5,
            },
            "in_watchdog": 0,
            "out_deferred": 0,
            "out_mac_pause_frames": 0,
            "in_pkts": 545526,
            "in_multicast_pkts": 535961,
            "in_runts": 0,
            "out_unknown_protocl_drops": 0,
            "in_no_buffer": 0,
            "out_buffers_swapped": 0,
            "out_lost_carrier": 0,
            "out_errors": 0,
            "in_errors": 0,
            "in_octets": 41210298,
            "in_crc_errors": 0,
            "out_no_carrier": 0,
            "in_with_dribble": 0,
            "in_broadcast_pkts": 535996,
            "out_pkts": 23376,
            "out_late_collision": 0,
            "out_octets": 3642296,
            "in_overrun": 0,
            "out_babble": 0,
        },
        "phys_address": "0057.d2ff.422a",
        "keepalive": 10,
        "output_hang": "never",
        "txload": "1/255",
        "oper_status": "up",
        "arp_type": "arpa",
        "media_type": "10/100/1000BaseTX",
        "rxload": "1/255",
        "duplex_mode": "full",
        "queues": {
            "input_queue_size": 0,
            "total_output_drop": 0,
            "input_queue_drops": 0,
            "input_queue_max": 2000,
            "output_queue_size": 0,
            "input_queue_flushes": 0,
            "output_queue_max": 40,
            "queue_strategy": "fifo",
        },
        "encapsulations": {"encapsulation": "arpa"},
        "last_input": "never",
        "last_output": "00:00:02",
        "line_protocol": "up",
        "mac_address": "0057.d2ff.422a",
        "connected": True,
        "port_channel": {
            "port_channel_member": True,
            "port_channel_int": "Port-channel12",
        },
        "arp_timeout": "04:00:00",
        "bandwidth": 1000000,
        "port_speed": "1000mb/s",
        "enabled": True,
        "mtu": 1500,
        "delay": 10,
        "reliability": "255/255",
    },
    "GigabitEthernet0/0/4": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "bandwidth": 1000000,
        "auto_negotiate": True,
        "counters": {
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_mac_pause_frames": 0,
            "in_multicast_pkts": 0,
            "in_no_buffer": 0,
            "in_octets": 0,
            "in_overrun": 0,
            "in_pkts": 0,
            "in_runts": 0,
            "in_throttles": 0,
            "in_watchdog": 0,
            "last_clear": "never",
            "out_babble": 0,
            "out_collision": 0,
            "out_deferred": 0,
            "out_errors": 0,
            "out_interface_resets": 1,
            "out_late_collision": 0,
            "out_lost_carrier": 0,
            "out_mac_pause_frames": 0,
            "out_no_carrier": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "delay": 10,
        "duplex_mode": "full",
        "link_type": "auto",
        "port_speed": "1000mbps",
        "media_type": "unknown",
        "enabled": False,
        "encapsulations": {"encapsulation": "arpa"},
        "flow_control": {"receive": False, "send": False},
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "down",
        "mac_address": "380e.4dff.dc72",
        "phys_address": "380e.4dff.dc72",
        "mtu": 1500,
        "oper_status": "down",
        "output_hang": "never",
        "port_channel": {"port_channel_member": False},
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 375,
            "input_queue_size": 0,
            "output_queue_max": 40,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "txload": "1/255",
        "type": "BUILT-IN-2T+6X1GE",
    },
}
