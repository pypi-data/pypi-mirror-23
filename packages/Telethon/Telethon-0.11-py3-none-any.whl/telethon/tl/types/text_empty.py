from ...tl.mtproto_request import MTProtoRequest


class TextEmpty(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    textEmpty#dc3d824f  = RichText"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xdc3d824f
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf1d0b479

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(TextEmpty.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return TextEmpty()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'textEmpty#dc3d824f  = RichText'

    def __str__(self):
        return '(textEmpty (ID: 0xdc3d824f) = ())'.format()
