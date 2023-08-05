from ...tl.mtproto_request import MTProtoRequest


class PrivacyKeyPhoneCall(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    privacyKeyPhoneCall#3d662b7b  = PrivacyKey"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x3d662b7b
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x824651c3

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(PrivacyKeyPhoneCall.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return PrivacyKeyPhoneCall()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'privacyKeyPhoneCall#3d662b7b  = PrivacyKey'

    def __str__(self):
        return '(privacyKeyPhoneCall (ID: 0x3d662b7b) = ())'.format()
