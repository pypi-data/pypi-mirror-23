from ....tl.mtproto_request import MTProtoRequest


class DiscardEncryptionRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.discardEncryption#edd923c5 chat_id:int = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xedd923c5
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, chat_id):
        """
        :param chat_id: Telegram type: "int".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.chat_id = chat_id

    def to_dict(self):
        return {
            'chat_id': self.chat_id,
        }

    def on_send(self, writer):
        writer.write_int(DiscardEncryptionRequest.constructor_id, signed=False)
        writer.write_int(self.chat_id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return DiscardEncryptionRequest(None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'messages.discardEncryption#edd923c5 chat_id:int = Bool'

    def __str__(self):
        return '(messages.discardEncryption (ID: 0xedd923c5) = (chat_id={}))'.format(str(self.chat_id))
