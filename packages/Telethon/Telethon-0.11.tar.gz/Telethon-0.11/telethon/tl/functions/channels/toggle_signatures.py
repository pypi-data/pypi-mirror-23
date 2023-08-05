from ....tl.mtproto_request import MTProtoRequest


class ToggleSignaturesRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channels.toggleSignatures#1f69b606 channel:InputChannel enabled:Bool = Updates"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x1f69b606
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8af52aac

    def __init__(self, channel, enabled):
        """
        :param channel: Telegram type: "InputChannel".
        :param enabled: Telegram type: "Bool".

        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, UpdatesTg, UpdateShortSentMessage.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.channel = channel
        self.enabled = enabled

    def to_dict(self):
        return {
            'channel': None if self.channel is None else self.channel.to_dict(),
            'enabled': self.enabled,
        }

    def on_send(self, writer):
        writer.write_int(ToggleSignaturesRequest.constructor_id, signed=False)
        self.channel.on_send(writer)
        writer.tgwrite_bool(self.enabled)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ToggleSignaturesRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'channels.toggleSignatures#1f69b606 channel:InputChannel enabled:Bool = Updates'

    def __str__(self):
        return '(channels.toggleSignatures (ID: 0x1f69b606) = (channel={}, enabled={}))'.format(str(self.channel), str(self.enabled))
