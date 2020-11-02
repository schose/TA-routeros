# Technology Add-On for Mikrotik RouterOS

The Splunk Technology Add-On for Mikrotik RouterOS provides extractions and CIM normalization for Mikrotik RouterOS devices.
CIM data models network traffic, name resolution (DNS), DHCP and authentication are used.

## Activation of logging using Mikrotik RouterOS

To activate logging of RouterOS events activate Syslog logging. Use a Syslog server or activate a UDP input on Splunk Forwarder.

To activate logging use the CLI

- create a logging action
/system logging action
add name=syslogbw remote=1.2.3.4 remote-port=5200 src-address=2.3.4.5 target=remote

- create a logging profile
/system logging
set 0 topics=info,!firewall
add action=syslog topics=info
add action=syslog topics=warning
add action=syslog topics=critical
add action=syslog topics=error
add action=syslog topics=dns,!debug

## Firewall logging

You need to enable logging for every rule you want to analyse. To do so specify a rulename and an action. Action needs to be "drop" or "accept".
use "log=yes log-prefix="rulename drop|accept" when creating a rule.

Here is an example for a drop rule:
add action=drop chain=input connection-nat-state=!dstnat connection-state=new in-interface=ether1 log=yes log-prefix="input_wan drop"

This is an example for a forward rule:
add action=accept chain=forward dst-address=0.0.0.0/0 in-interface=mynet log=yes log-prefix="fwd_bw_internet accept" out-interface=ether1 src-address=192.168.1.0/24

## Installation and Deployment of TA-routeros

Download this TA and place it in etc/apps on your Searchhead, Indexers and Universal Forwarders (Syslog servers).

Here is an example inputs.conf:
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