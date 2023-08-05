from ....tl.mtproto_request import MTProtoRequest


class SavedGifs(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.savedGifs#2e0709a5 hash:int gifs:Vector<Document> = messages.SavedGifs"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x2e0709a5
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xa68b61f5

    def __init__(self, hash, gifs):
        """
        :param hash: Telegram type: "int".
        :param gifs: Telegram type: "Document". Must be a list.

        Constructor for messages.SavedGifs: Instance of either SavedGifsNotModified, SavedGifs.
        """
        super().__init__()

        self.hash = hash
        self.gifs = gifs

    def to_dict(self):
        return {
            'hash': self.hash,
            'gifs': [] if self.gifs is None else [None if x is None else x.to_dict() for x in self.gifs],
        }

    def on_send(self, writer):
        writer.write_int(SavedGifs.constructor_id, signed=False)
        writer.write_int(self.hash)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.gifs))
        for gifs_item in self.gifs:
            gifs_item.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SavedGifs(None, None)

    def on_response(self, reader):
        self.hash = reader.read_int()
        reader.read_int()  # Vector's constructor ID
        self.gifs = []  # Initialize an empty list
        gifs_len = reader.read_int()
        for _ in range(gifs_len):
            gifs_item = reader.tgread_object()
            self.gifs.append(gifs_item)

    def __repr__(self):
        return 'messages.savedGifs#2e0709a5 hash:int gifs:Vector<Document> = messages.SavedGifs'

    def __str__(self):
        return '(messages.savedGifs (ID: 0x2e0709a5) = (hash={}, gifs={}))'.format(str(self.hash), None if not self.gifs else [str(_) for _ in self.gifs])
