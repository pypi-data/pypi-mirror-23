from ...tl.mtproto_request import MTProtoRequest


class MsgResendReq(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    msg_resend_req#7d861a08 msg_ids:Vector<long> = MsgResendReq"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x7d861a08
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x2024514

    def __init__(self, msg_ids):
        """
        :param msg_ids: Telegram type: "long". Must be a list.

        Constructor for MsgResendReq: Instance of MsgResendReq.
        """
        super().__init__()

        self.msg_ids = msg_ids

    def to_dict(self):
        return {
            'msg_ids': [] if self.msg_ids is None else self.msg_ids[:],
        }

    def on_send(self, writer):
        writer.write_int(MsgResendReq.constructor_id, signed=False)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.msg_ids))
        for msg_ids_item in self.msg_ids:
            writer.write_long(msg_ids_item)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return MsgResendReq(None)

    def on_response(self, reader):
        reader.read_int()  # Vector's constructor ID
        self.msg_ids = []  # Initialize an empty list
        msg_ids_len = reader.read_int()
        for _ in range(msg_ids_len):
            msg_ids_item = reader.read_long()
            self.msg_ids.append(msg_ids_item)

    def __repr__(self):
        return 'msg_resend_req#7d861a08 msg_ids:Vector<long> = MsgResendReq'

    def __str__(self):
        return '(msg_resend_req (ID: 0x7d861a08) = (msg_ids={}))'.format(None if not self.msg_ids else [str(_) for _ in self.msg_ids])
