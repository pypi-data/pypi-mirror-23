from ...tl.mtproto_request import MTProtoRequest


class InputPeerUser(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputPeerUser#7b8e7de6 user_id:int access_hash:long = InputPeer"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x7b8e7de6
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xc91c90b6

    def __init__(self, user_id, access_hash):
        """
        :param user_id: Telegram type: "int".
        :param access_hash: Telegram type: "long".

        Constructor for InputPeer: Instance of either InputPeerEmpty, InputPeerSelf, InputPeerChat, InputPeerUser, InputPeerChannel.
        """
        super().__init__()

        self.user_id = user_id
        self.access_hash = access_hash

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'access_hash': self.access_hash,
        }

    def on_send(self, writer):
        writer.write_int(InputPeerUser.constructor_id, signed=False)
        writer.write_int(self.user_id)
        writer.write_long(self.access_hash)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputPeerUser(None, None)

    def on_response(self, reader):
        self.user_id = reader.read_int()
        self.access_hash = reader.read_long()

    def __repr__(self):
        return 'inputPeerUser#7b8e7de6 user_id:int access_hash:long = InputPeer'

    def __str__(self):
        return '(inputPeerUser (ID: 0x7b8e7de6) = (user_id={}, access_hash={}))'.format(str(self.user_id), str(self.access_hash))
