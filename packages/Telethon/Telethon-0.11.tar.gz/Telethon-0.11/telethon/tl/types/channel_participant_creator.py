from ...tl.mtproto_request import MTProtoRequest


class ChannelParticipantCreator(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channelParticipantCreator#e3e2e1f9 user_id:int = ChannelParticipant"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xe3e2e1f9
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xd9c7fc18

    def __init__(self, user_id):
        """
        :param user_id: Telegram type: "int".

        Constructor for ChannelParticipant: Instance of either ChannelParticipant, ChannelParticipantSelf, ChannelParticipantModerator, ChannelParticipantEditor, ChannelParticipantKicked, ChannelParticipantCreator.
        """
        super().__init__()

        self.user_id = user_id

    def to_dict(self):
        return {
            'user_id': self.user_id,
        }

    def on_send(self, writer):
        writer.write_int(ChannelParticipantCreator.constructor_id, signed=False)
        writer.write_int(self.user_id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ChannelParticipantCreator(None)

    def on_response(self, reader):
        self.user_id = reader.read_int()

    def __repr__(self):
        return 'channelParticipantCreator#e3e2e1f9 user_id:int = ChannelParticipant'

    def __str__(self):
        return '(channelParticipantCreator (ID: 0xe3e2e1f9) = (user_id={}))'.format(str(self.user_id))
