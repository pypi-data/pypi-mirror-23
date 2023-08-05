from ....tl.mtproto_request import MTProtoRequest


class ToggleChatAdminsRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.toggleChatAdmins#ec8bd9e1 chat_id:int enabled:Bool = Updates"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xec8bd9e1
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8af52aac

    def __init__(self, chat_id, enabled):
        """
        :param chat_id: Telegram type: "int".
        :param enabled: Telegram type: "Bool".

        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, UpdatesTg, UpdateShortSentMessage.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.chat_id = chat_id
        self.enabled = enabled

    def to_dict(self):
        return {
            'chat_id': self.chat_id,
            'enabled': self.enabled,
        }

    def on_send(self, writer):
        writer.write_int(ToggleChatAdminsRequest.constructor_id, signed=False)
        writer.write_int(self.chat_id)
        writer.tgwrite_bool(self.enabled)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ToggleChatAdminsRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'messages.toggleChatAdmins#ec8bd9e1 chat_id:int enabled:Bool = Updates'

    def __str__(self):
        return '(messages.toggleChatAdmins (ID: 0xec8bd9e1) = (chat_id={}, enabled={}))'.format(str(self.chat_id), str(self.enabled))
