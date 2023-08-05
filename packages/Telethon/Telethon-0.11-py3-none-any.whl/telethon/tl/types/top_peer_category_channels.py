from ...tl.mtproto_request import MTProtoRequest


class TopPeerCategoryChannels(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    topPeerCategoryChannels#161d9628  = TopPeerCategory"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x161d9628
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xddf02502

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(TopPeerCategoryChannels.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return TopPeerCategoryChannels()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'topPeerCategoryChannels#161d9628  = TopPeerCategory'

    def __str__(self):
        return '(topPeerCategoryChannels (ID: 0x161d9628) = ())'.format()
