from ...tl.mtproto_request import MTProtoRequest


class PageBlockEmbed(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    pageBlockEmbed#cde200d1 flags:# full_width:flags.0?true allow_scrolling:flags.3?true url:flags.1?string html:flags.2?string poster_photo_id:flags.4?long w:int h:int caption:RichText = PageBlock"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xcde200d1
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x1aca5644

    def __init__(self, w, h, caption, full_width=None, allow_scrolling=None, url=None, html=None, poster_photo_id=None):
        """
        :param full_width: Telegram type: "true".
        :param allow_scrolling: Telegram type: "true".
        :param url: Telegram type: "string".
        :param html: Telegram type: "string".
        :param poster_photo_id: Telegram type: "long".
        :param w: Telegram type: "int".
        :param h: Telegram type: "int".
        :param caption: Telegram type: "RichText".

        Constructor for PageBlock: Instance of either PageBlockUnsupported, PageBlockTitle, PageBlockSubtitle, PageBlockAuthorDate, PageBlockHeader, PageBlockSubheader, PageBlockParagraph, PageBlockPreformatted, PageBlockFooter, PageBlockDivider, PageBlockAnchor, PageBlockList, PageBlockBlockquote, PageBlockPullquote, PageBlockPhoto, PageBlockVideo, PageBlockCover, PageBlockEmbed, PageBlockEmbedPost, PageBlockCollage, PageBlockSlideshow, PageBlockChannel.
        """
        super().__init__()

        self.full_width = full_width
        self.allow_scrolling = allow_scrolling
        self.url = url
        self.html = html
        self.poster_photo_id = poster_photo_id
        self.w = w
        self.h = h
        self.caption = caption

    def to_dict(self):
        return {
            'full_width': self.full_width,
            'allow_scrolling': self.allow_scrolling,
            'url': self.url,
            'html': self.html,
            'poster_photo_id': self.poster_photo_id,
            'w': self.w,
            'h': self.h,
            'caption': None if self.caption is None else self.caption.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(PageBlockEmbed.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.full_width else 0
        flags |= (1 << 3) if self.allow_scrolling else 0
        flags |= (1 << 1) if self.url else 0
        flags |= (1 << 2) if self.html else 0
        flags |= (1 << 4) if self.poster_photo_id else 0
        writer.write_int(flags)

        if self.url:
            writer.tgwrite_string(self.url)

        if self.html:
            writer.tgwrite_string(self.html)

        if self.poster_photo_id:
            writer.write_long(self.poster_photo_id)

        writer.write_int(self.w)
        writer.write_int(self.h)
        self.caption.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return PageBlockEmbed(None, None, None, None, None, None, None, None)

    def on_response(self, reader):
        flags = reader.read_int()

        if (flags & (1 << 0)) != 0:
            self.full_width = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 3)) != 0:
            self.allow_scrolling = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 1)) != 0:
            self.url = reader.tgread_string()

        if (flags & (1 << 2)) != 0:
            self.html = reader.tgread_string()

        if (flags & (1 << 4)) != 0:
            self.poster_photo_id = reader.read_long()

        self.w = reader.read_int()
        self.h = reader.read_int()
        self.caption = reader.tgread_object()

    def __repr__(self):
        return 'pageBlockEmbed#cde200d1 flags:# full_width:flags.0?true allow_scrolling:flags.3?true url:flags.1?string html:flags.2?string poster_photo_id:flags.4?long w:int h:int caption:RichText = PageBlock'

    def __str__(self):
        return '(pageBlockEmbed (ID: 0xcde200d1) = (full_width={}, allow_scrolling={}, url={}, html={}, poster_photo_id={}, w={}, h={}, caption={}))'.format(str(self.full_width), str(self.allow_scrolling), str(self.url), str(self.html), str(self.poster_photo_id), str(self.w), str(self.h), str(self.caption))
