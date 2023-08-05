from ...tl.mtproto_request import MTProtoRequest


class UpdateChatAdmins(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    updateChatAdmins#6e947941 chat_id:int enabled:Bool version:int = Update"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x6e947941
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x9f89304e

    def __init__(self, chat_id, enabled, version):
        """
        :param chat_id: Telegram type: "int".
        :param enabled: Telegram type: "Bool".
        :param version: Telegram type: "int".

        Constructor for Update: Instance of either UpdateNewMessage, UpdateMessageID, UpdateDeleteMessages, UpdateUserTyping, UpdateChatUserTyping, UpdateChatParticipants, UpdateUserStatus, UpdateUserName, UpdateUserPhoto, UpdateContactRegistered, UpdateContactLink, UpdateNewEncryptedMessage, UpdateEncryptedChatTyping, UpdateEncryption, UpdateEncryptedMessagesRead, UpdateChatParticipantAdd, UpdateChatParticipantDelete, UpdateDcOptions, UpdateUserBlocked, UpdateNotifySettings, UpdateServiceNotification, UpdatePrivacy, UpdateUserPhone, UpdateReadHistoryInbox, UpdateReadHistoryOutbox, UpdateWebPage, UpdateReadMessagesContents, UpdateChannelTooLong, UpdateChannel, UpdateNewChannelMessage, UpdateReadChannelInbox, UpdateDeleteChannelMessages, UpdateChannelMessageViews, UpdateChatAdmins, UpdateChatParticipantAdmin, UpdateNewStickerSet, UpdateStickerSetsOrder, UpdateStickerSets, UpdateSavedGifs, UpdateBotInlineQuery, UpdateBotInlineSend, UpdateEditChannelMessage, UpdateChannelPinnedMessage, UpdateBotCallbackQuery, UpdateEditMessage, UpdateInlineBotCallbackQuery, UpdateReadChannelOutbox, UpdateDraftMessage, UpdateReadFeaturedStickers, UpdateRecentStickers, UpdateConfig, UpdatePtsChanged, UpdateChannelWebPage, UpdateDialogPinned, UpdatePinnedDialogs, UpdateBotWebhookJSON, UpdateBotWebhookJSONQuery, UpdateBotShippingQuery, UpdateBotPrecheckoutQuery, UpdatePhoneCall.
        """
        super().__init__()

        self.chat_id = chat_id
        self.enabled = enabled
        self.version = version

    def to_dict(self):
        return {
            'chat_id': self.chat_id,
            'enabled': self.enabled,
            'version': self.version,
        }

    def on_send(self, writer):
        writer.write_int(UpdateChatAdmins.constructor_id, signed=False)
        writer.write_int(self.chat_id)
        writer.tgwrite_bool(self.enabled)
        writer.write_int(self.version)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UpdateChatAdmins(None, None, None)

    def on_response(self, reader):
        self.chat_id = reader.read_int()
        self.enabled = reader.tgread_bool()
        self.version = reader.read_int()

    def __repr__(self):
        return 'updateChatAdmins#6e947941 chat_id:int enabled:Bool version:int = Update'

    def __str__(self):
        return '(updateChatAdmins (ID: 0x6e947941) = (chat_id={}, enabled={}, version={}))'.format(str(self.chat_id), str(self.enabled), str(self.version))
