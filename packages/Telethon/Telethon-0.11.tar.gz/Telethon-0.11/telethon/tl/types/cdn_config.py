from ...tl.mtproto_request import MTProtoRequest


class CdnConfig(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    cdnConfig#5725e40a public_keys:Vector<CdnPublicKey> = CdnConfig"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x5725e40a
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xecda397c

    def __init__(self, public_keys):
        """
        :param public_keys: Telegram type: "CdnPublicKey". Must be a list.

        Constructor for CdnConfig: Instance of CdnConfig.
        """
        super().__init__()

        self.public_keys = public_keys

    def to_dict(self):
        return {
            'public_keys': [] if self.public_keys is None else [None if x is None else x.to_dict() for x in self.public_keys],
        }

    def on_send(self, writer):
        writer.write_int(CdnConfig.constructor_id, signed=False)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.public_keys))
        for public_keys_item in self.public_keys:
            public_keys_item.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return CdnConfig(None)

    def on_response(self, reader):
        reader.read_int()  # Vector's constructor ID
        self.public_keys = []  # Initialize an empty list
        public_keys_len = reader.read_int()
        for _ in range(public_keys_len):
            public_keys_item = reader.tgread_object()
            self.public_keys.append(public_keys_item)

    def __repr__(self):
        return 'cdnConfig#5725e40a public_keys:Vector<CdnPublicKey> = CdnConfig'

    def __str__(self):
        return '(cdnConfig (ID: 0x5725e40a) = (public_keys={}))'.format(None if not self.public_keys else [str(_) for _ in self.public_keys])
