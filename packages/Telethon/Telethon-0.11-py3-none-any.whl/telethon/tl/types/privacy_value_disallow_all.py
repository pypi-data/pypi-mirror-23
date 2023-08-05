from ...tl.mtproto_request import MTProtoRequest


class PrivacyValueDisallowAll(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    privacyValueDisallowAll#8b73e763  = PrivacyRule"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x8b73e763
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xebb7f270

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(PrivacyValueDisallowAll.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return PrivacyValueDisallowAll()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'privacyValueDisallowAll#8b73e763  = PrivacyRule'

    def __str__(self):
        return '(privacyValueDisallowAll (ID: 0x8b73e763) = ())'.format()
