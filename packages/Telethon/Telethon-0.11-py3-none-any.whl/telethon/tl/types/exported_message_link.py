from ...tl.mtproto_request import MTProtoRequest


class ExportedMessageLink(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    exportedMessageLink#1f486803 link:string = ExportedMessageLink"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x1f486803
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xdee644cc

    def __init__(self, link):
        """
        :param link: Telegram type: "string".

        Constructor for ExportedMessageLink: Instance of ExportedMessageLink.
        """
        super().__init__()

        self.link = link

    def to_dict(self):
        return {
            'link': self.link,
        }

    def on_send(self, writer):
        writer.write_int(ExportedMessageLink.constructor_id, signed=False)
        writer.tgwrite_string(self.link)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ExportedMessageLink(None)

    def on_response(self, reader):
        self.link = reader.tgread_string()

    def __repr__(self):
        return 'exportedMessageLink#1f486803 link:string = ExportedMessageLink'

    def __str__(self):
        return '(exportedMessageLink (ID: 0x1f486803) = (link={}))'.format(str(self.link))
