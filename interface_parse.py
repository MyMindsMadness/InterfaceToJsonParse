import json

config_dict = {"interface": {}}

with open ('Show_Run_Interface.txt', 'r') as file:
    for line in file:
        line = line.strip()
        #print (line)
        if line.startswith("interface"):
            interface_name = line.split()[1]
            config_dict["interface"][interface_name] = {}
            current_interface = interface_name
        elif "no switchport" in line:
            config_dict["interface"][current_interface]["switchport"] = False
        elif "ip address" in line:
            iplist = line.split(" ")
            ip = iplist[2]
            sm = iplist[3]
            config_dict["interface"][current_interface]["ip"] = ip
            config_dict["interface"][current_interface]["mask"] = sm
        elif "helper-address" in line:
            helperlist = line.split(" ")
            helper = helperlist[2]
            config_dict["interface"][current_interface]["ip helper"] = helper
        elif "duplex" in line:
            duplexmode = line[7:]
            config_dict["interface"][current_interface]["duplex"] = duplexmode
        elif "speed" in line:
            speedmode = line[6:]
            config_dict["interface"][current_interface]["speed"] = speedmode
        elif "ipv6 address" in line:
            if "/" in line:
                gualist = line.split(" ")
                config_dict["interface"][current_interface]["ipv6"] = gualist[2]
            elif "link-local" in line:
                linklocallist = line.split(" ")
                config_dict["interface"][current_interface]["ipv6 link local"] = linklocallist[2]
        


with open ('output.json', 'w') as outfile:
    outfile.write(json.dumps(config_dict, indent=4))