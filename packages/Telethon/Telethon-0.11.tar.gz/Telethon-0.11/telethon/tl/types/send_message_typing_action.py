from ...tl.mtproto_request import MTProtoRequest


class SendMessageTypingAction(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    sendMessageTypingAction#16bf744e  = SendMessageAction"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x16bf744e
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x20b2cc21

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(SendMessageTypingAction.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SendMessageTypingAction()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'sendMessageTypingAction#16bf744e  = SendMessageAction'

    def __str__(self):
        return '(sendMessageTypingAction (ID: 0x16bf744e) = ())'.format()
