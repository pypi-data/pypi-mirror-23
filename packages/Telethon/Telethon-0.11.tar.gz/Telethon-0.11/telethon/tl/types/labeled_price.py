from ...tl.mtproto_request import MTProtoRequest


class LabeledPrice(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    labeledPrice#cb296bf8 label:string amount:long = LabeledPrice"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xcb296bf8
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x1c84047a

    def __init__(self, label, amount):
        """
        :param label: Telegram type: "string".
        :param amount: Telegram type: "long".

        Constructor for LabeledPrice: Instance of LabeledPrice.
        """
        super().__init__()

        self.label = label
        self.amount = amount

    def to_dict(self):
        return {
            'label': self.label,
            'amount': self.amount,
        }

    def on_send(self, writer):
        writer.write_int(LabeledPrice.constructor_id, signed=False)
        writer.tgwrite_string(self.label)
        writer.write_long(self.amount)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return LabeledPrice(None, None)

    def on_response(self, reader):
        self.label = reader.tgread_string()
        self.amount = reader.read_long()

    def __repr__(self):
        return 'labeledPrice#cb296bf8 label:string amount:long = LabeledPrice'

    def __str__(self):
        return '(labeledPrice (ID: 0xcb296bf8) = (label={}, amount={}))'.format(str(self.label), str(self.amount))
