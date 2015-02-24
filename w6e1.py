__author__ = 'rafael'

from onepk_helper import NetworkDevice

rtr1 = {'ip': '50.242.94.227', 'username': 'pyclass', 'password': '88newclass',
        'pin_file': 'device_name', 'port': 12345}


def main():
    '''Create an onep object, establish a connection with an element, 
    and return its system name, product ID, and serial number.''' 
    rtr1_obj = NetworkDevice(**rtr1)
    rtr1_obj.establish_session()
    print 'Stats for {}:'.format(rtr1_obj.net_element.properties.sys_name)
    print 'Product ID: {}'.format(rtr1_obj.net_element.properties.product_id)
    print 'Serial No.: {}'.format(rtr1_obj.net_element.properties.SerialNo)
    rtr1_obj.disconnect()


if __name__ == "__main__":
    main()
