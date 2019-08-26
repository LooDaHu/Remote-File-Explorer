import socket
import re


def get_local_adr():
    address_set = socket.getaddrinfo(socket.gethostname(), None, family=2)
    for address in address_set:
        if re.match("192.168.", address[4][0]):
            local_network_addr = address[4][0]
            return local_network_addr
    return "ADDRESS_NOT_FOUND"
