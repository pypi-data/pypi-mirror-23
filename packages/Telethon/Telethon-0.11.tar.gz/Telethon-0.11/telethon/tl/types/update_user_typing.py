from ...tl.mtproto_request import MTProtoRequest


class UpdateUserTyping(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    updateUserTyping#5c486927 user_id:int action:SendMessageAction = Update"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x5c486927
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x9f89304e

    def __init__(self, user_id, action):
        """
        :param user_id: Telegram type: "int".
        :param action: Telegram type: "SendMessageAction".

        Constructor for Update: Instance of either UpdateNewMessage, UpdateMessageID, UpdateDeleteMessages, UpdateUserTyping, UpdateChatUserTyping, UpdateChatParticipants, UpdateUserStatus, UpdateUserName, UpdateUserPhoto, UpdateContactRegistered, UpdateContactLink, UpdateNewEncryptedMessage, UpdateEncryptedChatTyping, UpdateEncryption, UpdateEncryptedMessagesRead, UpdateChatParticipantAdd, UpdateChatParticipantDelete, UpdateDcOptions, UpdateUserBlocked, UpdateNotifySettings, UpdateServiceNotification, UpdatePrivacy, UpdateUserPhone, UpdateReadHistoryInbox, UpdateReadHistoryOutbox, UpdateWebPage, UpdateReadMessagesContents, UpdateChannelTooLong, UpdateChannel, UpdateNewChannelMessage, UpdateReadChannelInbox, UpdateDeleteChannelMessages, UpdateChannelMessageViews, UpdateChatAdmins, UpdateChatParticipantAdmin, UpdateNewStickerSet, UpdateStickerSetsOrder, UpdateStickerSets, UpdateSavedGifs, UpdateBotInlineQuery, UpdateBotInlineSend, UpdateEditChannelMessage, UpdateChannelPinnedMessage, UpdateBotCallbackQuery, UpdateEditMessage, UpdateInlineBotCallbackQuery, UpdateReadChannelOutbox, UpdateDraftMessage, UpdateReadFeaturedStickers, UpdateRecentStickers, UpdateConfig, UpdatePtsChanged, UpdateChannelWebPage, UpdateDialogPinned, UpdatePinnedDialogs, UpdateBotWebhookJSON, UpdateBotWebhookJSONQuery, UpdateBotShippingQuery, UpdateBotPrecheckoutQuery, UpdatePhoneCall.
        """
        super().__init__()

        self.user_id = user_id
        self.action = action

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'action': None if self.action is None else self.action.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(UpdateUserTyping.constructor_id, signed=False)
        writer.write_int(self.user_id)
        self.action.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UpdateUserTyping(None, None)

    def on_response(self, reader):
        self.user_id = reader.read_int()
        self.action = reader.tgread_object()

    def __repr__(self):
        return 'updateUserTyping#5c486927 user_id:int action:SendMessageAction = Update'

    def __str__(self):
        return '(updateUserTyping (ID: 0x5c486927) = (user_id={}, action={}))'.format(str(self.user_id), str(self.action))
