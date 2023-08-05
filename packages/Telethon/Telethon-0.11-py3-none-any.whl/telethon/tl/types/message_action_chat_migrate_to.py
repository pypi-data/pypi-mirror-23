from ...tl.mtproto_request import MTProtoRequest


class MessageActionChatMigrateTo(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messageActionChatMigrateTo#51bdb021 channel_id:int = MessageAction"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x51bdb021
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8680d126

    def __init__(self, channel_id):
        """
        :param channel_id: Telegram type: "int".

        Constructor for MessageAction: Instance of either MessageActionEmpty, MessageActionChatCreate, MessageActionChatEditTitle, MessageActionChatEditPhoto, MessageActionChatDeletePhoto, MessageActionChatAddUser, MessageActionChatDeleteUser, MessageActionChatJoinedByLink, MessageActionChannelCreate, MessageActionChatMigrateTo, MessageActionChannelMigrateFrom, MessageActionPinMessage, MessageActionHistoryClear, MessageActionGameScore, MessageActionPaymentSentMe, MessageActionPaymentSent, MessageActionPhoneCall.
        """
        super().__init__()

        self.channel_id = channel_id

    def to_dict(self):
        return {
            'channel_id': self.channel_id,
        }

    def on_send(self, writer):
        writer.write_int(MessageActionChatMigrateTo.constructor_id, signed=False)
        writer.write_int(self.channel_id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return MessageActionChatMigrateTo(None)

    def on_response(self, reader):
        self.channel_id = reader.read_int()

    def __repr__(self):
        return 'messageActionChatMigrateTo#51bdb021 channel_id:int = MessageAction'

    def __str__(self):
        return '(messageActionChatMigrateTo (ID: 0x51bdb021) = (channel_id={}))'.format(str(self.channel_id))
