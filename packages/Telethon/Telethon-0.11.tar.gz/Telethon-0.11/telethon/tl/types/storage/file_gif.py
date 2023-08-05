from ....tl.mtproto_request import MTProtoRequest


class FileGif(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    storage.fileGif#cae1aadf  = storage.FileType"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xcae1aadf
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf3a1e6f3

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(FileGif.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return FileGif()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'storage.fileGif#cae1aadf  = storage.FileType'

    def __str__(self):
        return '(storage.fileGif (ID: 0xcae1aadf) = ())'.format()
