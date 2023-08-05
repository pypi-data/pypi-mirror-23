from ...tl.mtproto_request import MTProtoRequest


class InputChatPhotoEmpty(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputChatPhotoEmpty#1ca48f57  = InputChatPhoto"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x1ca48f57
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xd4eb2d74

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(InputChatPhotoEmpty.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputChatPhotoEmpty()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'inputChatPhotoEmpty#1ca48f57  = InputChatPhoto'

    def __str__(self):
        return '(inputChatPhotoEmpty (ID: 0x1ca48f57) = ())'.format()
