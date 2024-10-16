import socket
from http.client import responses

from app.utils.header import (DnsHeader,)
import app.models

import struct


def create_header(qdcount = 0):
    return DnsHeader(
        id = 1234,
        qr = 1,
        opcode=0,
        aa=0,
        tc = 0,
        rd = 0,
        ra = 0,
        z = 0,
        rcode = 0,
        qdcount = qdcount,
        ancount=0,
        nscount=0,
        arcount=0
    )


def pack_dns_message(message: DnsHeader) -> bytes:
    flags = (
        message.qr << 15
        | message.opcode << 11
        | message.aa << 10
        | message.tc << 9
        | message.rd << 8
        | message.ra << 7
        | message.z << 4
        | message.rcode
    )
    return struct.pack(
        ">HHHHHH",
        message.id,
        flags,
        message.qdcount,
        message.ancount,
        message.nscount,
        message.arcount
    )

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    #
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("127.0.0.1", 2053))

    while True:
        try:
            buf, source = udp_socket.recvfrom(512)

            buf_data = DnsHeader.from_bytes(data = buf[:12])
            print(f"Received data from {source}: {buf_data}")
            question_section = buf[12:]
            header = create_header(1)
            # response = header.to_bytes()
            response = pack_dns_message(header)
            response = response + question_section
            udp_socket.sendto(response, source)
        except Exception as e:
            print(f"Error receiving data: {e}")
            break


if __name__ == "__main__":
    main()
# ,dsoflm