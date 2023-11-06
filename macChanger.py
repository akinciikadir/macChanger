import subprocess  #Harici komutları veya işletim sistemi komutlarını çalıştırmak ve kontrol etmek için kullanılır.
import optparse



def get_user_inputs():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface")
    parse_object.add_option("-m","--macAdress",dest="macAdress")

    return parse_object.parse_args()
def change_mac_adress(user_interface,user_macadress):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_macadress])
    subprocess.call(["ifconfig",user_interface,"up"])

print("macChanger started!")
(user_input,argument)=get_user_inputs()
change_mac_adress(user_input.interface,user_input.macAdress)



