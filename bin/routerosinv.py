import json
import sys
from routeros import login

SCHEME = """<scheme>
    <title>Mikrotik Routeros</title>
    <description>Get data from Mikrotik RouterOS</description>
    <use_external_validation>false</use_external_validation>
    <use_single_instance>false</use_single_instance>
    <endpoint>
        <args>
            <arg name="name">
                <title>Connection Name</title>
                <description>e.g. Name or Location of the RouterOS device</description>
                <validation>is_string('name')</validation>
            </arg>
            
            <arg name="ROUTEROS_IP">
                <title>ROUTEROS_IP</title>
                <description>IP OR FQDN of your RouterOS Device</description>
            </arg>
            
            <arg name="ROUTEROS_PORT">
                <title>ROUTEROS_PORT</title>
                <data_type>number</data_type>
                <description>Port where your RouterOS Device is reachable - default: 8291</description>
                <validation>is_port('ROUTEROS_PORT')</validation>
            </arg>
                        
        </args>
    </endpoint>
</scheme>
"""

def do_scheme():

    print SCHEME

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
    val_dataa = get_validation_data()
    #logging.debug("validate: using fritzbox %s on port %d", val_data["FB_IP"], val_data["FB_PORT"])

def usage():
    print "usage: %s [--scheme|--validate-arguments]"
    sys.exit(2)


#print json.perfdata

if __name__ == '__main__':

    if len(sys.argv) > 1:
        if sys.argv[1] == "--scheme":
            do_scheme()
#        elif sys.argv[1] == "--validate-arguments":
#            validate_arguments()
        elif sys.argv[1] == "--test":
            #print 'No tests for the scheme present'
            do_scheme()
        else:
            usage()

    else:
        routeros = login('admin', '', '192.168.109.3')
        mikdata = routeros('/system/resource/print')

        #print mikdata

        perfdata = {
            "uptime": mikdata[0]["uptime"],
            "architecture-name": mikdata[0]["architecture-name"],
            "version": mikdata[0]["version"],
            "cpu-frequency": mikdata[0]["cpu-frequency"],
            "free-memory":  mikdata[0]["free-memory"],
            "total-memory":  mikdata[0]["total-memory"],
            "free-hdd-space":  mikdata[0]["free-hdd-space"],
            "total-hdd-space": mikdata[0]["total-hdd-space"],
            "architecture-name":  mikdata[0]["architecture-name"],
            "board-name": mikdata[0]["board-name"]
        }

        json_perfdata = json.dumps(perfdata)
        print perfdata
