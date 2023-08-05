from ....tl.mtproto_request import MTProtoRequest


class CreateChannelRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channels.createChannel#f4893d7f flags:# broadcast:flags.0?true megagroup:flags.1?true title:string about:string = Updates"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xf4893d7f
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8af52aac

    def __init__(self, title, about, broadcast=None, megagroup=None):
        """
        :param broadcast: Telegram type: "true".
        :param megagroup: Telegram type: "true".
        :param title: Telegram type: "string".
        :param about: Telegram type: "string".

        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, UpdatesTg, UpdateShortSentMessage.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.broadcast = broadcast
        self.megagroup = megagroup
        self.title = title
        self.about = about

    def to_dict(self):
        return {
            'broadcast': self.broadcast,
            'megagroup': self.megagroup,
            'title': self.title,
            'about': self.about,
        }

    def on_send(self, writer):
        writer.write_int(CreateChannelRequest.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.broadcast else 0
        flags |= (1 << 1) if self.megagroup else 0
        writer.write_int(flags)

        writer.tgwrite_string(self.title)
        writer.tgwrite_string(self.about)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return CreateChannelRequest(None, None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'channels.createChannel#f4893d7f flags:# broadcast:flags.0?true megagroup:flags.1?true title:string about:string = Updates'

    def __str__(self):
        return '(channels.createChannel (ID: 0xf4893d7f) = (broadcast={}, megagroup={}, title={}, about={}))'.format(str(self.broadcast), str(self.megagroup), str(self.title), str(self.about))
