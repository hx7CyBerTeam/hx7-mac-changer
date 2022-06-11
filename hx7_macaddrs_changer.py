# # # # # # # # # # # # # # #
#        hx7 scripts        #
# # # # # ------- # # # # # #
#    mac address changer    #
# # # # # # # # # # # # # # #

import subprocess

interface = input("> Enter InterFace : ")
new_mac = input("> Enter A New MAC Address : ")

print("[+] Changing MAC Address For " + interface + " To " + new_mac)

subprocess.call(" ifconfig " + interface + " down ", shell=True)
subprocess.call(" ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call(" ifconfig " + interface + " up ", shell=True)
