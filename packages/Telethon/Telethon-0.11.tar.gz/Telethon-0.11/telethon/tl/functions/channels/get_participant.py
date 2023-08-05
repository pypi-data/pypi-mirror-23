from ....tl.mtproto_request import MTProtoRequest


class GetParticipantRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channels.getParticipant#546dd7a6 channel:InputChannel user_id:InputUser = channels.ChannelParticipant"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x546dd7a6
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x6658151a

    def __init__(self, channel, user_id):
        """
        :param channel: Telegram type: "InputChannel".
        :param user_id: Telegram type: "InputUser".

        :returns channels.ChannelParticipant: Instance of ChannelParticipant.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.channel = channel
        self.user_id = user_id

    def to_dict(self):
        return {
            'channel': None if self.channel is None else self.channel.to_dict(),
            'user_id': None if self.user_id is None else self.user_id.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(GetParticipantRequest.constructor_id, signed=False)
        self.channel.on_send(writer)
        self.user_id.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return GetParticipantRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'channels.getParticipant#546dd7a6 channel:InputChannel user_id:InputUser = channels.ChannelParticipant'

    def __str__(self):
        return '(channels.getParticipant (ID: 0x546dd7a6) = (channel={}, user_id={}))'.format(str(self.channel), str(self.user_id))
