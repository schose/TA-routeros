from __future__ import print_function
import xml
import time
import sys
import socket
import threading
import subprocess
import logging
import xml.dom.minidom, xml.sax.saxutils
import datetime
import json
import sys
import logging
from librouteros import connect


# set up logging suitable for splunkd comsumption
logging.root
#logging.root.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logging.root.addHandler(handler)

#from Queue import Queue

SCHEME = """<scheme>
    <title>Mikrotik Routeros Interface Stats</title>
    <description>Get data from Mikrotik RouterOS</description>
    <use_external_validation>false</use_external_validation>
    <use_single_instance>false</use_single_instance>
    <endpoint>
        <args>
            <arg name="name">
                <title>Connection Name</title>
                <description>e.g. Name or Location of the RouterOS device</description>
            </arg>
            
            <arg name="ROUTEROS_IP">
                <title>Routeros IP</title>
                <description>IP OR FQDN of your RouterOS Device</description>
            </arg>
            
            <arg name="ROUTEROS_PORT">
                <title>Routeros Port</title>
                <data_type>number</data_type>
                <description>Port where your RouterOS API Port is reachable - default: 8728 - this is not winbox port!!!</description>
            </arg>

            <arg name="ROUTEROS_USERNAME">
                <title>Username</title>
                <description>Username for your RouterOS Device</description>
            </arg>

            <arg name="ROUTEROS_PASSWORD">
                <title>Password</title>
                <description>Password for your RouterOS Device</description>
            </arg>
        </args>
    </endpoint>
</scheme>
"""

def do_scheme():

    print(SCHEME)

def get_validation_data():
    val_data = {}

    # read everything from stdin
    val_str = sys.stdin.read()

    # parse the validation XML
    doc = xml.dom.minidom.parseString(val_str)
    root = doc.documentElement

    #logging.debug("XML: found items")

    item_node = root.getElementsByTagName("configuration")[0]
    if item_node:
        logging.debug("XML: found configuration")

        name = item_node.getAttribute("name")
        val_data["stanza"] = name

        params_node = item_node.getElementsByTagName("param")
        for param in params_node:
            name = param.getAttribute("name")
            logging.debug("Found param %s" % name)
            if name and param.firstChild and \
                            param.firstChild.nodeType == param.firstChild.TEXT_NODE:
                val_data[name] = param.firstChild.data

    return val_data


def validate_arguments():
    #logging.debug("before validate function")
    #val_data = get_validation_data()
    #val_dataa = get_validation_data()
    testme = ()
    #logging.debug("validate: using routeros device %s on port %s using username %s password %s ", \
# val_dataa["ROUTEROS_IP"], val_dataa["ROUTEROS_PORT"], val_dataa["ROUTEROS_USERNAME"], \
# val_dataa["ROUTEROS_PASSWORD"])

def usage():
    print("usage: %s [--scheme|--validate-arguments]")
    sys.exit(2)

def getdata():
    val_data = get_validation_data()

    ROUTEROS_IP = val_data["ROUTEROS_IP"]
    ROUTEROS_PORT = int(val_data["ROUTEROS_PORT"])
    ROUTEROS_USERNAME = val_data["ROUTEROS_USERNAME"]
    ROUTEROS_PASSWORD = val_data["ROUTEROS_PASSWORD"]
 
    logging.info("run: using routeros device %s on port %s using username ", ROUTEROS_IP, ROUTEROS_PORT, ROUTEROS_USERNAME)

#    routeros = login(ROUTEROS_USERNAME, ROUTEROS_PASSWORD, ROUTEROS_IP)

    routeros = connect(username=ROUTEROS_USERNAME, password=ROUTEROS_PASSWORD, host=ROUTEROS_IP)
    mikdata = routeros('/interface/getall')
    
    json_perfdatanic = json.dumps(mikdata)
    print(json_perfdatanic)

    # outfile = "/opt/splunk/etc/apps/TA-routeros/bin/out.json"
    # file = open(outfile,"w")

    # for lineout in mikdata:
    #     file.write(lineout) 

    #file.write(mikdata)
#    file.close()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        if sys.argv[1] == "--scheme":
            do_scheme()
        elif sys.argv[1] == "--validate-arguments":
            validate_arguments()
        elif sys.argv[1] == "--test":
            #print 'No tests for the scheme present'
            do_scheme()
        else:
            usage()

    else:
        getdata()

