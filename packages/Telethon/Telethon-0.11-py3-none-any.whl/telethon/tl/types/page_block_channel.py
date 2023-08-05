from ...tl.mtproto_request import MTProtoRequest


class PageBlockChannel(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    pageBlockChannel#ef1751b5 channel:Chat = PageBlock"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xef1751b5
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x1aca5644

    def __init__(self, channel):
        """
        :param channel: Telegram type: "Chat".

        Constructor for PageBlock: Instance of either PageBlockUnsupported, PageBlockTitle, PageBlockSubtitle, PageBlockAuthorDate, PageBlockHeader, PageBlockSubheader, PageBlockParagraph, PageBlockPreformatted, PageBlockFooter, PageBlockDivider, PageBlockAnchor, PageBlockList, PageBlockBlockquote, PageBlockPullquote, PageBlockPhoto, PageBlockVideo, PageBlockCover, PageBlockEmbed, PageBlockEmbedPost, PageBlockCollage, PageBlockSlideshow, PageBlockChannel.
        """
        super().__init__()

        self.channel = channel

    def to_dict(self):
        return {
            'channel': None if self.channel is None else self.channel.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(PageBlockChannel.constructor_id, signed=False)
        self.channel.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return PageBlockChannel(None)

    def on_response(self, reader):
        self.channel = reader.tgread_object()

    def __repr__(self):
        return 'pageBlockChannel#ef1751b5 channel:Chat = PageBlock'

    def __str__(self):
        return '(pageBlockChannel (ID: 0xef1751b5) = (channel={}))'.format(str(self.channel))
