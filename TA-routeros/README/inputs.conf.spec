[routerosinv://default]
ROUTEROS_IP = 192.168.101.1
* This is the routeros ip or fqdn
ROUTEROS_PORT= 8219
* This is the routeros port
ROUTEROS_USERNAME= admin
* This is the routeros uzsername
ROUTEROS_PASSWORD= admin
* This is the routeros password
interval = 300
* how often routeros in queried in seconds
sourcetype=routeros:inventory
* sourcetype to use

[routerosint://default]
ROUTEROS_IP = 192.168.101.1
* This is the routeros ip or fqdn
ROUTEROS_PORT= 8219
* This is the routeros port
ROUTEROS_USERNAME= admin
* This is the routeros uzsername
ROUTEROS_PASSWORD= admin
* This is the routeros password
interval = 300
* how often routeros in queried in seconds
sourcetype=routeros:interfaces
* sourcetype to use

[routerosperf://default]
ROUTEROS_IP = 192.168.101.1
* This is the routeros ip or fqdn
ROUTEROS_PORT= 8219
* This is the routeros port
ROUTEROS_USERNAME= admin
* This is the routeros uzsername
ROUTEROS_PASSWORD= admin
* This is the routeros password
interval = 300
* how often routeros in queried in seconds
sourcetype=routeros:interfaces
* sourcetype to use
