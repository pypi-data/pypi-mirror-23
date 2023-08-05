from ...tl.mtproto_request import MTProtoRequest


class MessageEntityTextUrl(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messageEntityTextUrl#76a6d327 offset:int length:int url:string = MessageEntity"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x76a6d327
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xcf6419dc

    def __init__(self, offset, length, url):
        """
        :param offset: Telegram type: "int".
        :param length: Telegram type: "int".
        :param url: Telegram type: "string".

        Constructor for MessageEntity: Instance of either MessageEntityUnknown, MessageEntityMention, MessageEntityHashtag, MessageEntityBotCommand, MessageEntityUrl, MessageEntityEmail, MessageEntityBold, MessageEntityItalic, MessageEntityCode, MessageEntityPre, MessageEntityTextUrl, MessageEntityMentionName, InputMessageEntityMentionName.
        """
        super().__init__()

        self.offset = offset
        self.length = length
        self.url = url

    def to_dict(self):
        return {
            'offset': self.offset,
            'length': self.length,
            'url': self.url,
        }

    def on_send(self, writer):
        writer.write_int(MessageEntityTextUrl.constructor_id, signed=False)
        writer.write_int(self.offset)
        writer.write_int(self.length)
        writer.tgwrite_string(self.url)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return MessageEntityTextUrl(None, None, None)

    def on_response(self, reader):
        self.offset = reader.read_int()
        self.length = reader.read_int()
        self.url = reader.tgread_string()

    def __repr__(self):
        return 'messageEntityTextUrl#76a6d327 offset:int length:int url:string = MessageEntity'

    def __str__(self):
        return '(messageEntityTextUrl (ID: 0x76a6d327) = (offset={}, length={}, url={}))'.format(str(self.offset), str(self.length), str(self.url))
