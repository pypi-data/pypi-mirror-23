from ....tl.mtproto_request import MTProtoRequest


class SendChangePhoneCodeRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    account.sendChangePhoneCode#08e57deb flags:# allow_flashcall:flags.0?true phone_number:string current_number:flags.0?Bool = auth.SentCode"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x8e57deb
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x6ce87081

    def __init__(self, phone_number, allow_flashcall=None, current_number=None):
        """
        :param allow_flashcall: Telegram type: "true".
        :param phone_number: Telegram type: "string".
        :param current_number: Telegram type: "Bool".

        :returns auth.SentCode: Instance of SentCode.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.allow_flashcall = allow_flashcall
        self.phone_number = phone_number
        self.current_number = current_number

    def to_dict(self):
        return {
            'allow_flashcall': self.allow_flashcall,
            'phone_number': self.phone_number,
            'current_number': self.current_number,
        }

    def on_send(self, writer):
        writer.write_int(SendChangePhoneCodeRequest.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.allow_flashcall else 0
        flags |= (1 << 0) if self.current_number else 0
        writer.write_int(flags)

        writer.tgwrite_string(self.phone_number)
        if self.current_number:
            writer.tgwrite_bool(self.current_number)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SendChangePhoneCodeRequest(None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'account.sendChangePhoneCode#08e57deb flags:# allow_flashcall:flags.0?true phone_number:string current_number:flags.0?Bool = auth.SentCode'

    def __str__(self):
        return '(account.sendChangePhoneCode (ID: 0x8e57deb) = (allow_flashcall={}, phone_number={}, current_number={}))'.format(str(self.allow_flashcall), str(self.phone_number), str(self.current_number))
