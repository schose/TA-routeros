# Technology Add-On for Mikrotik Routeros

The Splunk Technology Add-On for Mikrotik RouterOS provides extractions and CIM normalization for Mikrotik RouterOS devices.
CIM Datamodels network traffic, name resolution (DNS) and DHCP are used.

## Activation of Loging Using Mikrotik RouterOS

To activate logging of RouterOS events activate Syslog logging. Use a Syslog Server or activate a UDP input on Splunk Forwarder.

To activate Logging
<ul>
<li>start the router
<li>bla
<li>bla
</ul>


As soon as configured the logfile will be created and look similar to this:
<pre>
Dec 15 23:59:59 192.168.61.1 firewall,info forward: in:bridge-batchworks(ether4) out:ether1, src-mac 68:05:ca:2b:3d:1a, proto UDP, 192.168.61.198:59870->172.217.16.78:443, len 1378
Dec 15 23:59:36 192.168.61.1 dns,packet id:5e6b rd:1 tc:0 aa:0 qr:1 ra:1 QUERY 'name error'
Dec 15 23:59:36 192.168.61.1 dns query from 192.168.61.198: #3463 _kerberos._tcp.dc._msdcs.bwlab.loc. UNKNOWN (33)
Dec 15 22:58:18 192.168.61.1 dhcp,info dhcp-public deassigned 192.168.63.196 from 6C:8D:C1:2C:67:B3
</pre>

## Installation and Deployment of TA-routeros

Download this TA and place it in etc/apps on your Searchhead, Indexers and Universal Forwarders (Syslog servers).

here is an example inputs.conf
<pre>
[monitor:///var/log/cases/routeros/*/*.log]
index = batchworks
sourcetype = routeros
host_segment = 5
disabled = 0
</pre>


Verify the data input and extraction works by searching for

<pre>
sourcetype=routeros tag=network tag=communicate
</pre>