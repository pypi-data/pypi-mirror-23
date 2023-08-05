from ....tl.mtproto_request import MTProtoRequest


class EditPhotoRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channels.editPhoto#f12e57c9 channel:InputChannel photo:InputChatPhoto = Updates"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xf12e57c9
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8af52aac

    def __init__(self, channel, photo):
        """
        :param channel: Telegram type: "InputChannel".
        :param photo: Telegram type: "InputChatPhoto".

        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, UpdatesTg, UpdateShortSentMessage.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.channel = channel
        self.photo = photo

    def to_dict(self):
        return {
            'channel': None if self.channel is None else self.channel.to_dict(),
            'photo': None if self.photo is None else self.photo.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(EditPhotoRequest.constructor_id, signed=False)
        self.channel.on_send(writer)
        self.photo.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return EditPhotoRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'channels.editPhoto#f12e57c9 channel:InputChannel photo:InputChatPhoto = Updates'

    def __str__(self):
        return '(channels.editPhoto (ID: 0xf12e57c9) = (channel={}, photo={}))'.format(str(self.channel), str(self.photo))
