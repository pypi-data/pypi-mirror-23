from ...tl.mtproto_request import MTProtoRequest


class InputPrivacyKeyStatusTimestamp(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputPrivacyKeyStatusTimestamp#4f96cb18  = InputPrivacyKey"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x4f96cb18
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x53627f8

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(InputPrivacyKeyStatusTimestamp.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputPrivacyKeyStatusTimestamp()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'inputPrivacyKeyStatusTimestamp#4f96cb18  = InputPrivacyKey'

    def __str__(self):
        return '(inputPrivacyKeyStatusTimestamp (ID: 0x4f96cb18) = ())'.format()
