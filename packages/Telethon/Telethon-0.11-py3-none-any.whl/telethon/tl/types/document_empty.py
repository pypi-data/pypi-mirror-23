from ...tl.mtproto_request import MTProtoRequest


class DocumentEmpty(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    documentEmpty#36f8c871 id:long = Document"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x36f8c871
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x211fe820

    def __init__(self, id):
        """
        :param id: Telegram type: "long".

        Constructor for Document: Instance of either DocumentEmpty, Document.
        """
        super().__init__()

        self.id = id

    def to_dict(self):
        return {
            'id': self.id,
        }

    def on_send(self, writer):
        writer.write_int(DocumentEmpty.constructor_id, signed=False)
        writer.write_long(self.id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return DocumentEmpty(None)

    def on_response(self, reader):
        self.id = reader.read_long()

    def __repr__(self):
        return 'documentEmpty#36f8c871 id:long = Document'

    def __str__(self):
        return '(documentEmpty (ID: 0x36f8c871) = (id={}))'.format(str(self.id))
