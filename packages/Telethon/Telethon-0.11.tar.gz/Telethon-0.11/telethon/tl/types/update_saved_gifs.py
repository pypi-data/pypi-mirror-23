from ...tl.mtproto_request import MTProtoRequest


class UpdateSavedGifs(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    updateSavedGifs#9375341e  = Update"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x9375341e
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x9f89304e

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(UpdateSavedGifs.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UpdateSavedGifs()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'updateSavedGifs#9375341e  = Update'

    def __str__(self):
        return '(updateSavedGifs (ID: 0x9375341e) = ())'.format()
