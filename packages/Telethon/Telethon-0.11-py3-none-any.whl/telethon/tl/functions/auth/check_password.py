from ....tl.mtproto_request import MTProtoRequest


class CheckPasswordRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    auth.checkPassword#0a63011e password_hash:bytes = auth.Authorization"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xa63011e
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xb9e04e39

    def __init__(self, password_hash):
        """
        :param password_hash: Telegram type: "bytes".

        :returns auth.Authorization: Instance of Authorization.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.password_hash = password_hash

    def to_dict(self):
        return {
            'password_hash': self.password_hash,
        }

    def on_send(self, writer):
        writer.write_int(CheckPasswordRequest.constructor_id, signed=False)
        writer.tgwrite_bytes(self.password_hash)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return CheckPasswordRequest(None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'auth.checkPassword#0a63011e password_hash:bytes = auth.Authorization'

    def __str__(self):
        return '(auth.checkPassword (ID: 0xa63011e) = (password_hash={}))'.format(str(self.password_hash))
