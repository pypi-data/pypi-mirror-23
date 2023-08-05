from ....tl.mtproto_request import MTProtoRequest


class SendInvitesRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    auth.sendInvites#771c1d97 phone_numbers:Vector<string> message:string = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x771c1d97
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, phone_numbers, message):
        """
        :param phone_numbers: Telegram type: "string". Must be a list.
        :param message: Telegram type: "string".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.phone_numbers = phone_numbers
        self.message = message

    def to_dict(self):
        return {
            'phone_numbers': [] if self.phone_numbers is None else self.phone_numbers[:],
            'message': self.message,
        }

    def on_send(self, writer):
        writer.write_int(SendInvitesRequest.constructor_id, signed=False)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.phone_numbers))
        for phone_numbers_item in self.phone_numbers:
            writer.tgwrite_string(phone_numbers_item)

        writer.tgwrite_string(self.message)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SendInvitesRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'auth.sendInvites#771c1d97 phone_numbers:Vector<string> message:string = Bool'

    def __str__(self):
        return '(auth.sendInvites (ID: 0x771c1d97) = (phone_numbers={}, message={}))'.format(None if not self.phone_numbers else [str(_) for _ in self.phone_numbers], str(self.message))
