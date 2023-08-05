from ...tl.mtproto_request import MTProtoRequest


class PageBlockAnchor(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    pageBlockAnchor#ce0d37b0 name:string = PageBlock"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xce0d37b0
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x1aca5644

    def __init__(self, name):
        """
        :param name: Telegram type: "string".

        Constructor for PageBlock: Instance of either PageBlockUnsupported, PageBlockTitle, PageBlockSubtitle, PageBlockAuthorDate, PageBlockHeader, PageBlockSubheader, PageBlockParagraph, PageBlockPreformatted, PageBlockFooter, PageBlockDivider, PageBlockAnchor, PageBlockList, PageBlockBlockquote, PageBlockPullquote, PageBlockPhoto, PageBlockVideo, PageBlockCover, PageBlockEmbed, PageBlockEmbedPost, PageBlockCollage, PageBlockSlideshow, PageBlockChannel.
        """
        super().__init__()

        self.name = name

    def to_dict(self):
        return {
            'name': self.name,
        }

    def on_send(self, writer):
        writer.write_int(PageBlockAnchor.constructor_id, signed=False)
        writer.tgwrite_string(self.name)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return PageBlockAnchor(None)

    def on_response(self, reader):
        self.name = reader.tgread_string()

    def __repr__(self):
        return 'pageBlockAnchor#ce0d37b0 name:string = PageBlock'

    def __str__(self):
        return '(pageBlockAnchor (ID: 0xce0d37b0) = (name={}))'.format(str(self.name))
