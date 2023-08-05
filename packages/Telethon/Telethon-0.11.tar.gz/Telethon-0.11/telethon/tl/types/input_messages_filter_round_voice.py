from ...tl.mtproto_request import MTProtoRequest


class InputMessagesFilterRoundVoice(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputMessagesFilterRoundVoice#7a7c17a4  = MessagesFilter"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x7a7c17a4
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8a36ec14

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(InputMessagesFilterRoundVoice.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputMessagesFilterRoundVoice()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'inputMessagesFilterRoundVoice#7a7c17a4  = MessagesFilter'

    def __str__(self):
        return '(inputMessagesFilterRoundVoice (ID: 0x7a7c17a4) = ())'.format()
