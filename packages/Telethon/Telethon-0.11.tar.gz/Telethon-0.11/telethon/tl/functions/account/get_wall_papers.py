from ....tl.mtproto_request import MTProtoRequest


class GetWallPapersRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    account.getWallPapers#c04cfac2  = Vector<WallPaper>"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xc04cfac2
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8ec35283

    def __init__(self):
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(GetWallPapersRequest.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return GetWallPapersRequest()

    def on_response(self, reader):
        self.result = reader.tgread_vector()

    def __repr__(self):
        return 'account.getWallPapers#c04cfac2  = Vector<WallPaper>'

    def __str__(self):
        return '(account.getWallPapers (ID: 0xc04cfac2) = ())'.format()
