from ...tl.mtproto_request import MTProtoRequest


class ChannelFull(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channelFull#c3d5512f flags:# can_view_participants:flags.3?true can_set_username:flags.6?true id:int about:string participants_count:flags.0?int admins_count:flags.1?int kicked_count:flags.2?int read_inbox_max_id:int read_outbox_max_id:int unread_count:int chat_photo:Photo notify_settings:PeerNotifySettings exported_invite:ExportedChatInvite bot_info:Vector<BotInfo> migrated_from_chat_id:flags.4?int migrated_from_max_id:flags.4?int pinned_msg_id:flags.5?int = ChatFull"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xc3d5512f
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xd49a2697

    def __init__(self, id, about, read_inbox_max_id, read_outbox_max_id, unread_count, chat_photo, notify_settings, exported_invite, bot_info, can_view_participants=None, can_set_username=None, participants_count=None, admins_count=None, kicked_count=None, migrated_from_chat_id=None, migrated_from_max_id=None, pinned_msg_id=None):
        """
        :param can_view_participants: Telegram type: "true".
        :param can_set_username: Telegram type: "true".
        :param id: Telegram type: "int".
        :param about: Telegram type: "string".
        :param participants_count: Telegram type: "int".
        :param admins_count: Telegram type: "int".
        :param kicked_count: Telegram type: "int".
        :param read_inbox_max_id: Telegram type: "int".
        :param read_outbox_max_id: Telegram type: "int".
        :param unread_count: Telegram type: "int".
        :param chat_photo: Telegram type: "Photo".
        :param notify_settings: Telegram type: "PeerNotifySettings".
        :param exported_invite: Telegram type: "ExportedChatInvite".
        :param bot_info: Telegram type: "BotInfo". Must be a list.
        :param migrated_from_chat_id: Telegram type: "int".
        :param migrated_from_max_id: Telegram type: "int".
        :param pinned_msg_id: Telegram type: "int".

        Constructor for ChatFull: Instance of either ChatFull, ChannelFull.
        """
        super().__init__()

        self.can_view_participants = can_view_participants
        self.can_set_username = can_set_username
        self.id = id
        self.about = about
        self.participants_count = participants_count
        self.admins_count = admins_count
        self.kicked_count = kicked_count
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.chat_photo = chat_photo
        self.notify_settings = notify_settings
        self.exported_invite = exported_invite
        self.bot_info = bot_info
        self.migrated_from_chat_id = migrated_from_chat_id
        self.migrated_from_max_id = migrated_from_max_id
        self.pinned_msg_id = pinned_msg_id

    def to_dict(self):
        return {
            'can_view_participants': self.can_view_participants,
            'can_set_username': self.can_set_username,
            'id': self.id,
            'about': self.about,
            'participants_count': self.participants_count,
            'admins_count': self.admins_count,
            'kicked_count': self.kicked_count,
            'read_inbox_max_id': self.read_inbox_max_id,
            'read_outbox_max_id': self.read_outbox_max_id,
            'unread_count': self.unread_count,
            'chat_photo': None if self.chat_photo is None else self.chat_photo.to_dict(),
            'notify_settings': None if self.notify_settings is None else self.notify_settings.to_dict(),
            'exported_invite': None if self.exported_invite is None else self.exported_invite.to_dict(),
            'bot_info': [] if self.bot_info is None else [None if x is None else x.to_dict() for x in self.bot_info],
            'migrated_from_chat_id': self.migrated_from_chat_id,
            'migrated_from_max_id': self.migrated_from_max_id,
            'pinned_msg_id': self.pinned_msg_id,
        }

    def on_send(self, writer):
        writer.write_int(ChannelFull.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 3) if self.can_view_participants else 0
        flags |= (1 << 6) if self.can_set_username else 0
        flags |= (1 << 0) if self.participants_count else 0
        flags |= (1 << 1) if self.admins_count else 0
        flags |= (1 << 2) if self.kicked_count else 0
        flags |= (1 << 4) if self.migrated_from_chat_id else 0
        flags |= (1 << 4) if self.migrated_from_max_id else 0
        flags |= (1 << 5) if self.pinned_msg_id else 0
        writer.write_int(flags)

        writer.write_int(self.id)
        writer.tgwrite_string(self.about)
        if self.participants_count:
            writer.write_int(self.participants_count)

        if self.admins_count:
            writer.write_int(self.admins_count)

        if self.kicked_count:
            writer.write_int(self.kicked_count)

        writer.write_int(self.read_inbox_max_id)
        writer.write_int(self.read_outbox_max_id)
        writer.write_int(self.unread_count)
        self.chat_photo.on_send(writer)
        self.notify_settings.on_send(writer)
        self.exported_invite.on_send(writer)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.bot_info))
        for bot_info_item in self.bot_info:
            bot_info_item.on_send(writer)

        if self.migrated_from_chat_id:
            writer.write_int(self.migrated_from_chat_id)

        if self.migrated_from_max_id:
            writer.write_int(self.migrated_from_max_id)

        if self.pinned_msg_id:
            writer.write_int(self.pinned_msg_id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ChannelFull(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

    def on_response(self, reader):
        flags = reader.read_int()

        if (flags & (1 << 3)) != 0:
            self.can_view_participants = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 6)) != 0:
            self.can_set_username = True  # Arbitrary not-None value, no need to read since it is a flag

        self.id = reader.read_int()
        self.about = reader.tgread_string()
        if (flags & (1 << 0)) != 0:
            self.participants_count = reader.read_int()

        if (flags & (1 << 1)) != 0:
            self.admins_count = reader.read_int()

        if (flags & (1 << 2)) != 0:
            self.kicked_count = reader.read_int()

        self.read_inbox_max_id = reader.read_int()
        self.read_outbox_max_id = reader.read_int()
        self.unread_count = reader.read_int()
        self.chat_photo = reader.tgread_object()
        self.notify_settings = reader.tgread_object()
        self.exported_invite = reader.tgread_object()
        reader.read_int()  # Vector's constructor ID
        self.bot_info = []  # Initialize an empty list
        bot_info_len = reader.read_int()
        for _ in range(bot_info_len):
            bot_info_item = reader.tgread_object()
            self.bot_info.append(bot_info_item)

        if (flags & (1 << 4)) != 0:
            self.migrated_from_chat_id = reader.read_int()

        if (flags & (1 << 4)) != 0:
            self.migrated_from_max_id = reader.read_int()

        if (flags & (1 << 5)) != 0:
            self.pinned_msg_id = reader.read_int()

    def __repr__(self):
        return 'channelFull#c3d5512f flags:# can_view_participants:flags.3?true can_set_username:flags.6?true id:int about:string participants_count:flags.0?int admins_count:flags.1?int kicked_count:flags.2?int read_inbox_max_id:int read_outbox_max_id:int unread_count:int chat_photo:Photo notify_settings:PeerNotifySettings exported_invite:ExportedChatInvite bot_info:Vector<BotInfo> migrated_from_chat_id:flags.4?int migrated_from_max_id:flags.4?int pinned_msg_id:flags.5?int = ChatFull'

    def __str__(self):
        return '(channelFull (ID: 0xc3d5512f) = (can_view_participants={}, can_set_username={}, id={}, about={}, participants_count={}, admins_count={}, kicked_count={}, read_inbox_max_id={}, read_outbox_max_id={}, unread_count={}, chat_photo={}, notify_settings={}, exported_invite={}, bot_info={}, migrated_from_chat_id={}, migrated_from_max_id={}, pinned_msg_id={}))'.format(str(self.can_view_participants), str(self.can_set_username), str(self.id), str(self.about), str(self.participants_count), str(self.admins_count), str(self.kicked_count), str(self.read_inbox_max_id), str(self.read_outbox_max_id), str(self.unread_count), str(self.chat_photo), str(self.notify_settings), str(self.exported_invite), None if not self.bot_info else [str(_) for _ in self.bot_info], str(self.migrated_from_chat_id), str(self.migrated_from_max_id), str(self.pinned_msg_id))
