__author__ = 'rafael'

from onepk_helper import NetworkDevice
from onep.interfaces import NetworkInterface, InterfaceFilter

rtr1 = {'ip': '50.242.94.227', 'username': 'pyclass', 'password': '88newclass',
        'pin_file': 'pynet-rtr1-pin.txt', 'port': 15002}
rtr2 = {'ip': '50.242.94.227', 'username': 'pyclass', 'password': '88newclass',
        'pin_file': 'pynet-rtr2-pin.txt', 'port': 8002}


def get_intstat(obj):
    """
    :param obj:
    :return:interface list
    """
    a_filter = InterfaceFilter(None, NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ETHERNET)
    intf_list = obj.net_element.get_interface_list(a_filter)
    return intf_list


def main():
    """
    Create an onep object and establish a connection with an element.
    :return:system name and interface FastEthernet4 stats.
    """
    for rtr in (rtr1, rtr2):
        rtr_obj = NetworkDevice(**rtr)
        rtr_obj.establish_session()
        print 'Stats for {}:'.format(rtr_obj.net_element.properties.sys_name)
        for i in get_intstat(rtr_obj):
            if 'FastEthernet4' in i.name:
                print i.get_statistics()
        rtr_obj.disconnect()


if __name__ == "__main__":
    main()
    
