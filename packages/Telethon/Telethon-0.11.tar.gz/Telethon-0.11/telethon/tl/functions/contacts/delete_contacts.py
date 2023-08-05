from ....tl.mtproto_request import MTProtoRequest


class DeleteContactsRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    contacts.deleteContacts#59ab389e id:Vector<InputUser> = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x59ab389e
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, id):
        """
        :param id: Telegram type: "InputUser". Must be a list.

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.id = id

    def to_dict(self):
        return {
            'id': [] if self.id is None else [None if x is None else x.to_dict() for x in self.id],
        }

    def on_send(self, writer):
        writer.write_int(DeleteContactsRequest.constructor_id, signed=False)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.id))
        for id_item in self.id:
            id_item.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return DeleteContactsRequest(None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'contacts.deleteContacts#59ab389e id:Vector<InputUser> = Bool'

    def __str__(self):
        return '(contacts.deleteContacts (ID: 0x59ab389e) = (id={}))'.format(None if not self.id else [str(_) for _ in self.id])
