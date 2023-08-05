from ...tl.mtproto_request import MTProtoRequest


class UpdateChannelWebPage(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    updateChannelWebPage#40771900 channel_id:int webpage:WebPage pts:int pts_count:int = Update"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x40771900
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x9f89304e

    def __init__(self, channel_id, webpage, pts, pts_count):
        """
        :param channel_id: Telegram type: "int".
        :param webpage: Telegram type: "WebPage".
        :param pts: Telegram type: "int".
        :param pts_count: Telegram type: "int".

        Constructor for Update: Instance of either UpdateNewMessage, UpdateMessageID, UpdateDeleteMessages, UpdateUserTyping, UpdateChatUserTyping, UpdateChatParticipants, UpdateUserStatus, UpdateUserName, UpdateUserPhoto, UpdateContactRegistered, UpdateContactLink, UpdateNewEncryptedMessage, UpdateEncryptedChatTyping, UpdateEncryption, UpdateEncryptedMessagesRead, UpdateChatParticipantAdd, UpdateChatParticipantDelete, UpdateDcOptions, UpdateUserBlocked, UpdateNotifySettings, UpdateServiceNotification, UpdatePrivacy, UpdateUserPhone, UpdateReadHistoryInbox, UpdateReadHistoryOutbox, UpdateWebPage, UpdateReadMessagesContents, UpdateChannelTooLong, UpdateChannel, UpdateNewChannelMessage, UpdateReadChannelInbox, UpdateDeleteChannelMessages, UpdateChannelMessageViews, UpdateChatAdmins, UpdateChatParticipantAdmin, UpdateNewStickerSet, UpdateStickerSetsOrder, UpdateStickerSets, UpdateSavedGifs, UpdateBotInlineQuery, UpdateBotInlineSend, UpdateEditChannelMessage, UpdateChannelPinnedMessage, UpdateBotCallbackQuery, UpdateEditMessage, UpdateInlineBotCallbackQuery, UpdateReadChannelOutbox, UpdateDraftMessage, UpdateReadFeaturedStickers, UpdateRecentStickers, UpdateConfig, UpdatePtsChanged, UpdateChannelWebPage, UpdateDialogPinned, UpdatePinnedDialogs, UpdateBotWebhookJSON, UpdateBotWebhookJSONQuery, UpdateBotShippingQuery, UpdateBotPrecheckoutQuery, UpdatePhoneCall.
        """
        super().__init__()

        self.channel_id = channel_id
        self.webpage = webpage
        self.pts = pts
        self.pts_count = pts_count

    def to_dict(self):
        return {
            'channel_id': self.channel_id,
            'webpage': None if self.webpage is None else self.webpage.to_dict(),
            'pts': self.pts,
            'pts_count': self.pts_count,
        }

    def on_send(self, writer):
        writer.write_int(UpdateChannelWebPage.constructor_id, signed=False)
        writer.write_int(self.channel_id)
        self.webpage.on_send(writer)
        writer.write_int(self.pts)
        writer.write_int(self.pts_count)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UpdateChannelWebPage(None, None, None, None)

    def on_response(self, reader):
        self.channel_id = reader.read_int()
        self.webpage = reader.tgread_object()
        self.pts = reader.read_int()
        self.pts_count = reader.read_int()

    def __repr__(self):
        return 'updateChannelWebPage#40771900 channel_id:int webpage:WebPage pts:int pts_count:int = Update'

    def __str__(self):
        return '(updateChannelWebPage (ID: 0x40771900) = (channel_id={}, webpage={}, pts={}, pts_count={}))'.format(str(self.channel_id), str(self.webpage), str(self.pts), str(self.pts_count))
