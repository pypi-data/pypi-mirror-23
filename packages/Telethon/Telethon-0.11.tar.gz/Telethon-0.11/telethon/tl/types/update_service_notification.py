from ...tl.mtproto_request import MTProtoRequest


class UpdateServiceNotification(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    updateServiceNotification#ebe46819 flags:# popup:flags.0?true inbox_date:flags.1?date type:string message:string media:MessageMedia entities:Vector<MessageEntity> = Update"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xebe46819
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x9f89304e

    def __init__(self, type, message, media, entities, popup=None, inbox_date=None):
        """
        :param popup: Telegram type: "true".
        :param inbox_date: Telegram type: "date".
        :param type: Telegram type: "string".
        :param message: Telegram type: "string".
        :param media: Telegram type: "MessageMedia".
        :param entities: Telegram type: "MessageEntity". Must be a list.

        Constructor for Update: Instance of either UpdateNewMessage, UpdateMessageID, UpdateDeleteMessages, UpdateUserTyping, UpdateChatUserTyping, UpdateChatParticipants, UpdateUserStatus, UpdateUserName, UpdateUserPhoto, UpdateContactRegistered, UpdateContactLink, UpdateNewEncryptedMessage, UpdateEncryptedChatTyping, UpdateEncryption, UpdateEncryptedMessagesRead, UpdateChatParticipantAdd, UpdateChatParticipantDelete, UpdateDcOptions, UpdateUserBlocked, UpdateNotifySettings, UpdateServiceNotification, UpdatePrivacy, UpdateUserPhone, UpdateReadHistoryInbox, UpdateReadHistoryOutbox, UpdateWebPage, UpdateReadMessagesContents, UpdateChannelTooLong, UpdateChannel, UpdateNewChannelMessage, UpdateReadChannelInbox, UpdateDeleteChannelMessages, UpdateChannelMessageViews, UpdateChatAdmins, UpdateChatParticipantAdmin, UpdateNewStickerSet, UpdateStickerSetsOrder, UpdateStickerSets, UpdateSavedGifs, UpdateBotInlineQuery, UpdateBotInlineSend, UpdateEditChannelMessage, UpdateChannelPinnedMessage, UpdateBotCallbackQuery, UpdateEditMessage, UpdateInlineBotCallbackQuery, UpdateReadChannelOutbox, UpdateDraftMessage, UpdateReadFeaturedStickers, UpdateRecentStickers, UpdateConfig, UpdatePtsChanged, UpdateChannelWebPage, UpdateDialogPinned, UpdatePinnedDialogs, UpdateBotWebhookJSON, UpdateBotWebhookJSONQuery, UpdateBotShippingQuery, UpdateBotPrecheckoutQuery, UpdatePhoneCall.
        """
        super().__init__()

        self.popup = popup
        self.inbox_date = inbox_date
        self.type = type
        self.message = message
        self.media = media
        self.entities = entities

    def to_dict(self):
        return {
            'popup': self.popup,
            'inbox_date': self.inbox_date,
            'type': self.type,
            'message': self.message,
            'media': None if self.media is None else self.media.to_dict(),
            'entities': [] if self.entities is None else [None if x is None else x.to_dict() for x in self.entities],
        }

    def on_send(self, writer):
        writer.write_int(UpdateServiceNotification.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.popup else 0
        flags |= (1 << 1) if self.inbox_date else 0
        writer.write_int(flags)

        if self.inbox_date:
            writer.tgwrite_date(self.inbox_date)

        writer.tgwrite_string(self.type)
        writer.tgwrite_string(self.message)
        self.media.on_send(writer)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.entities))
        for entities_item in self.entities:
            entities_item.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UpdateServiceNotification(None, None, None, None, None, None)

    def on_response(self, reader):
        flags = reader.read_int()

        if (flags & (1 << 0)) != 0:
            self.popup = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 1)) != 0:
            self.inbox_date = reader.tgread_date()

        self.type = reader.tgread_string()
        self.message = reader.tgread_string()
        self.media = reader.tgread_object()
        reader.read_int()  # Vector's constructor ID
        self.entities = []  # Initialize an empty list
        entities_len = reader.read_int()
        for _ in range(entities_len):
            entities_item = reader.tgread_object()
            self.entities.append(entities_item)

    def __repr__(self):
        return 'updateServiceNotification#ebe46819 flags:# popup:flags.0?true inbox_date:flags.1?date type:string message:string media:MessageMedia entities:Vector<MessageEntity> = Update'

    def __str__(self):
        return '(updateServiceNotification (ID: 0xebe46819) = (popup={}, inbox_date={}, type={}, message={}, media={}, entities={}))'.format(str(self.popup), str(self.inbox_date), str(self.type), str(self.message), str(self.media), None if not self.entities else [str(_) for _ in self.entities])
