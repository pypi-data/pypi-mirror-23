from ....tl.mtproto_request import MTProtoRequest


class ChatsSlice(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.chatsSlice#9cd81144 count:int chats:Vector<Chat> = messages.Chats"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x9cd81144
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x99d5cb14

    def __init__(self, count, chats):
        """
        :param count: Telegram type: "int".
        :param chats: Telegram type: "Chat". Must be a list.

        Constructor for messages.Chats: Instance of either Chats, ChatsSlice.
        """
        super().__init__()

        self.count = count
        self.chats = chats

    def to_dict(self):
        return {
            'count': self.count,
            'chats': [] if self.chats is None else [None if x is None else x.to_dict() for x in self.chats],
        }

    def on_send(self, writer):
        writer.write_int(ChatsSlice.constructor_id, signed=False)
        writer.write_int(self.count)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.chats))
        for chats_item in self.chats:
            chats_item.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ChatsSlice(None, None)

    def on_response(self, reader):
        self.count = reader.read_int()
        reader.read_int()  # Vector's constructor ID
        self.chats = []  # Initialize an empty list
        chats_len = reader.read_int()
        for _ in range(chats_len):
            chats_item = reader.tgread_object()
            self.chats.append(chats_item)

    def __repr__(self):
        return 'messages.chatsSlice#9cd81144 count:int chats:Vector<Chat> = messages.Chats'

    def __str__(self):
        return '(messages.chatsSlice (ID: 0x9cd81144) = (count={}, chats={}))'.format(str(self.count), None if not self.chats else [str(_) for _ in self.chats])
