from ...tl.mtproto_request import MTProtoRequest


class NotifyAll(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    notifyAll#74d07c60  = NotifyPeer"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x74d07c60
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xdfe8602e

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(NotifyAll.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return NotifyAll()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'notifyAll#74d07c60  = NotifyPeer'

    def __str__(self):
        return '(notifyAll (ID: 0x74d07c60) = ())'.format()
