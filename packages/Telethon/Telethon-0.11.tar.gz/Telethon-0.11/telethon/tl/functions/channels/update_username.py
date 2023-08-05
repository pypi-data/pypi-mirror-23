from ....tl.mtproto_request import MTProtoRequest


class UpdateUsernameRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channels.updateUsername#3514b3de channel:InputChannel username:string = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x3514b3de
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, channel, username):
        """
        :param channel: Telegram type: "InputChannel".
        :param username: Telegram type: "string".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.channel = channel
        self.username = username

    def to_dict(self):
        return {
            'channel': None if self.channel is None else self.channel.to_dict(),
            'username': self.username,
        }

    def on_send(self, writer):
        writer.write_int(UpdateUsernameRequest.constructor_id, signed=False)
        self.channel.on_send(writer)
        writer.tgwrite_string(self.username)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UpdateUsernameRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'channels.updateUsername#3514b3de channel:InputChannel username:string = Bool'

    def __str__(self):
        return '(channels.updateUsername (ID: 0x3514b3de) = (channel={}, username={}))'.format(str(self.channel), str(self.username))
