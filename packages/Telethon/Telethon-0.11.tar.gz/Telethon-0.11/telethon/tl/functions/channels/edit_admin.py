from ....tl.mtproto_request import MTProtoRequest


class EditAdminRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channels.editAdmin#eb7611d0 channel:InputChannel user_id:InputUser role:ChannelParticipantRole = Updates"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xeb7611d0
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8af52aac

    def __init__(self, channel, user_id, role):
        """
        :param channel: Telegram type: "InputChannel".
        :param user_id: Telegram type: "InputUser".
        :param role: Telegram type: "ChannelParticipantRole".

        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, UpdatesTg, UpdateShortSentMessage.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.channel = channel
        self.user_id = user_id
        self.role = role

    def to_dict(self):
        return {
            'channel': None if self.channel is None else self.channel.to_dict(),
            'user_id': None if self.user_id is None else self.user_id.to_dict(),
            'role': None if self.role is None else self.role.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(EditAdminRequest.constructor_id, signed=False)
        self.channel.on_send(writer)
        self.user_id.on_send(writer)
        self.role.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return EditAdminRequest(None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'channels.editAdmin#eb7611d0 channel:InputChannel user_id:InputUser role:ChannelParticipantRole = Updates'

    def __str__(self):
        return '(channels.editAdmin (ID: 0xeb7611d0) = (channel={}, user_id={}, role={}))'.format(str(self.channel), str(self.user_id), str(self.role))
