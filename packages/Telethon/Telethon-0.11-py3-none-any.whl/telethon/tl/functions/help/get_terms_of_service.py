from ....tl.mtproto_request import MTProtoRequest


class GetTermsOfServiceRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    help.getTermsOfService#350170f3  = help.TermsOfService"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x350170f3
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x20ee8312

    def __init__(self):
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(GetTermsOfServiceRequest.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return GetTermsOfServiceRequest()

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'help.getTermsOfService#350170f3  = help.TermsOfService'

    def __str__(self):
        return '(help.getTermsOfService (ID: 0x350170f3) = ())'.format()
