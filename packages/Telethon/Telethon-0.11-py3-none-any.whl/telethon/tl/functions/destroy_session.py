from ...tl.mtproto_request import MTProtoRequest


class DestroySessionRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    destroy_session#e7512126 session_id:long = DestroySessionRes"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xe7512126
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xaf0ce7bd

    def __init__(self, session_id):
        """
        :param session_id: Telegram type: "long".

        :returns DestroySessionRes: Instance of either DestroySessionOk, DestroySessionNone.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.session_id = session_id

    def to_dict(self):
        return {
            'session_id': self.session_id,
        }

    def on_send(self, writer):
        writer.write_int(DestroySessionRequest.constructor_id, signed=False)
        writer.write_long(self.session_id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return DestroySessionRequest(None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'destroy_session#e7512126 session_id:long = DestroySessionRes'

    def __str__(self):
        return '(destroy_session (ID: 0xe7512126) = (session_id={}))'.format(str(self.session_id))
