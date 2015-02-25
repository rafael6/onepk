__author__ = 'rafael'

from onepk_helper import NetworkDevice
from onep.vty import VtyService

rtr1 = {'ip': '50.242.94.227', 'username': 'pyclass', 'password': '88newclass',
        'pin_file': 'pynet-rtr1-pin.txt', 'port': 15002}
rtr2 = {'ip': '50.242.94.227', 'username': 'pyclass', 'password': '88newclass',
        'pin_file': 'pynet-rtr2-pin.txt', 'port': 8002}


def set_command(vty, cmd):
    """
    :param vty: OnePK VtyService object
    :param cmd: CLI command
    :return:CLI command output
    """
    cli = vty.write(cmd)
    return cli
    

def main():
    """
    reate an onep object, establish a connection with an element
    :return: output of the show version CLI command
    """
    for rtr in (rtr1, rtr2):
        rtr_obj = NetworkDevice(**rtr)
        rtr_obj.establish_session()
        vty_service = VtyService(rtr_obj.net_element)
        vty_service.open()
        print 'Stats for {}:'.format(rtr_obj.net_element.properties.sys_name)
        set_command(vty_service, 'terminal length 0')
        print set_command(vty_service, 'show version')
        rtr_obj.disconnect()


if __name__ == "__main__":
    main()
