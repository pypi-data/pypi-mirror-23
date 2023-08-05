from ....tl.mtproto_request import MTProtoRequest


class SaveCallDebugRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    phone.saveCallDebug#277add7e peer:InputPhoneCall debug:DataJSON = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x277add7e
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, peer, debug):
        """
        :param peer: Telegram type: "InputPhoneCall".
        :param debug: Telegram type: "DataJSON".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.peer = peer
        self.debug = debug

    def to_dict(self):
        return {
            'peer': None if self.peer is None else self.peer.to_dict(),
            'debug': None if self.debug is None else self.debug.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(SaveCallDebugRequest.constructor_id, signed=False)
        self.peer.on_send(writer)
        self.debug.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SaveCallDebugRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'phone.saveCallDebug#277add7e peer:InputPhoneCall debug:DataJSON = Bool'

    def __str__(self):
        return '(phone.saveCallDebug (ID: 0x277add7e) = (peer={}, debug={}))'.format(str(self.peer), str(self.debug))
