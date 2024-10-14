import struct

class DnsHeader:
    def __init__(
        self,
        id: int,
        qr: int,
        opcode: int,
        aa: int,
        tc: int,
        rd: int,
        ra: int,
        z: int,
        rcode: int,
        qdcount: int,
        ancount: int,
        nscount: int,
        arcount: int,
    ):
        self.id = id
        self.qr = qr
        self.opcode = opcode
        self.aa = aa
        self.tc = tc
        self.rd = rd
        self.ra = ra
        self.z = z
        self.rcode = rcode
        self.qdcount = qdcount
        self.ancount = ancount
        self.nscount = nscount
        self.arcount = arcount

    def to_bytes(self):
        flags = (
            self.qr << 15
            | self.opcode << 11
            | self.aa << 10
            | self.tc << 9
            | self.rd << 8
            | self.ra << 7
            | self.z << 4
            | self.rcode
        )
        return struct.pack(
            "!6H",
            self.id,
            flags,
            self.qdcount,
            self.ancount,
            self.nscount,
            self.arcount
           )

    @staticmethod
    def from_bytes(data):
        decoded_response = struct.unpack("!6H", data)
        return decoded_response

    def __str__(self):
        return f"id ={self.id}, qr ={self.qr}, opcode ={self.opcode}, aa={self.aa}, tc={self.tc}, rd={self.rd}, ra={self.ra}, z={self.z}, rcode={self.rcode}, qdcount={self.qdcount}, ancount={self.ancount}, nscount={self.nscount}, arcount={self.arcount}) "