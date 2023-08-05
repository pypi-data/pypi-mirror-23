from ...tl.mtproto_request import MTProtoRequest


class ChatPhoto(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    chatPhoto#6153276a photo_small:FileLocation photo_big:FileLocation = ChatPhoto"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x6153276a
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xac3ec4e5

    def __init__(self, photo_small, photo_big):
        """
        :param photo_small: Telegram type: "FileLocation".
        :param photo_big: Telegram type: "FileLocation".

        Constructor for ChatPhoto: Instance of either ChatPhotoEmpty, ChatPhoto.
        """
        super().__init__()

        self.photo_small = photo_small
        self.photo_big = photo_big

    def to_dict(self):
        return {
            'photo_small': None if self.photo_small is None else self.photo_small.to_dict(),
            'photo_big': None if self.photo_big is None else self.photo_big.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(ChatPhoto.constructor_id, signed=False)
        self.photo_small.on_send(writer)
        self.photo_big.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ChatPhoto(None, None)

    def on_response(self, reader):
        self.photo_small = reader.tgread_object()
        self.photo_big = reader.tgread_object()

    def __repr__(self):
        return 'chatPhoto#6153276a photo_small:FileLocation photo_big:FileLocation = ChatPhoto'

    def __str__(self):
        return '(chatPhoto (ID: 0x6153276a) = (photo_small={}, photo_big={}))'.format(str(self.photo_small), str(self.photo_big))
