from ...tl.mtproto_request import MTProtoRequest


class ResPQ(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    resPQ#05162463 nonce:int128 server_nonce:int128 pq:string server_public_key_fingerprints:Vector<long> = ResPQ"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x5162463
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x786986b8

    def __init__(self, nonce, server_nonce, pq, server_public_key_fingerprints):
        """
        :param nonce: Telegram type: "int128".
        :param server_nonce: Telegram type: "int128".
        :param pq: Telegram type: "string".
        :param server_public_key_fingerprints: Telegram type: "long". Must be a list.

        Constructor for ResPQ: Instance of ResPQ.
        """
        super().__init__()

        self.nonce = nonce
        self.server_nonce = server_nonce
        self.pq = pq
        self.server_public_key_fingerprints = server_public_key_fingerprints

    def to_dict(self):
        return {
            'nonce': self.nonce,
            'server_nonce': self.server_nonce,
            'pq': self.pq,
            'server_public_key_fingerprints': [] if self.server_public_key_fingerprints is None else self.server_public_key_fingerprints[:],
        }

    def on_send(self, writer):
        writer.write_int(ResPQ.constructor_id, signed=False)
        writer.write_large_int(self.nonce, bits=128)
        writer.write_large_int(self.server_nonce, bits=128)
        writer.tgwrite_string(self.pq)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.server_public_key_fingerprints))
        for server_public_key_fingerprints_item in self.server_public_key_fingerprints:
            writer.write_long(server_public_key_fingerprints_item)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ResPQ(None, None, None, None)

    def on_response(self, reader):
        self.nonce = reader.read_large_int(bits=128)
        self.server_nonce = reader.read_large_int(bits=128)
        self.pq = reader.tgread_string()
        reader.read_int()  # Vector's constructor ID
        self.server_public_key_fingerprints = []  # Initialize an empty list
        server_public_key_fingerprints_len = reader.read_int()
        for _ in range(server_public_key_fingerprints_len):
            server_public_key_fingerprints_item = reader.read_long()
            self.server_public_key_fingerprints.append(server_public_key_fingerprints_item)

    def __repr__(self):
        return 'resPQ#05162463 nonce:int128 server_nonce:int128 pq:string server_public_key_fingerprints:Vector<long> = ResPQ'

    def __str__(self):
        return '(resPQ (ID: 0x5162463) = (nonce={}, server_nonce={}, pq={}, server_public_key_fingerprints={}))'.format(str(self.nonce), str(self.server_nonce), str(self.pq), None if not self.server_public_key_fingerprints else [str(_) for _ in self.server_public_key_fingerprints])
