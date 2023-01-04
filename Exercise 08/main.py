"""
main.py
By: Abhinav Tyagi
Date: 02NOV22
"""

"""
calling class for devices.py
"""

from devices import Firewall, Switch, LoadBalancer

#Firewall instance
firewall69=Firewall("firewall69")
#configure
firewall69.configure_firewall()
#verify crc
firewall69.calc_crc("data")

#Switch instance
switch12=Switch("switch12")
#configure
switch12.configure_switch()
#verify crc
switch12.calc_crc("data")

#Load Balancer instance
loadbalancer28=LoadBalancer("loadbalancer28")
#configure
loadbalancer28.configure_load_balancer()
#verify crc
loadbalancer28.calc_crc("data")