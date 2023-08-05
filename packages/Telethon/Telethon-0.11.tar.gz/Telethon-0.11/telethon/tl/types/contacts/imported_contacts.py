from ....tl.mtproto_request import MTProtoRequest


class ImportedContacts(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    contacts.importedContacts#ad524315 imported:Vector<ImportedContact> retry_contacts:Vector<long> users:Vector<User> = contacts.ImportedContacts"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xad524315
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8172ad93

    def __init__(self, imported, retry_contacts, users):
        """
        :param imported: Telegram type: "ImportedContact". Must be a list.
        :param retry_contacts: Telegram type: "long". Must be a list.
        :param users: Telegram type: "User". Must be a list.

        Constructor for contacts.ImportedContacts: Instance of ImportedContacts.
        """
        super().__init__()

        self.imported = imported
        self.retry_contacts = retry_contacts
        self.users = users

    def to_dict(self):
        return {
            'imported': [] if self.imported is None else [None if x is None else x.to_dict() for x in self.imported],
            'retry_contacts': [] if self.retry_contacts is None else self.retry_contacts[:],
            'users': [] if self.users is None else [None if x is None else x.to_dict() for x in self.users],
        }

    def on_send(self, writer):
        writer.write_int(ImportedContacts.constructor_id, signed=False)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.imported))
        for imported_item in self.imported:
            imported_item.on_send(writer)

        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.retry_contacts))
        for retry_contacts_item in self.retry_contacts:
            writer.write_long(retry_contacts_item)

        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.users))
        for users_item in self.users:
            users_item.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ImportedContacts(None, None, None)

    def on_response(self, reader):
        reader.read_int()  # Vector's constructor ID
        self.imported = []  # Initialize an empty list
        imported_len = reader.read_int()
        for _ in range(imported_len):
            imported_item = reader.tgread_object()
            self.imported.append(imported_item)

        reader.read_int()  # Vector's constructor ID
        self.retry_contacts = []  # Initialize an empty list
        retry_contacts_len = reader.read_int()
        for _ in range(retry_contacts_len):
            retry_contacts_item = reader.read_long()
            self.retry_contacts.append(retry_contacts_item)

        reader.read_int()  # Vector's constructor ID
        self.users = []  # Initialize an empty list
        users_len = reader.read_int()
        for _ in range(users_len):
            users_item = reader.tgread_object()
            self.users.append(users_item)

    def __repr__(self):
        return 'contacts.importedContacts#ad524315 imported:Vector<ImportedContact> retry_contacts:Vector<long> users:Vector<User> = contacts.ImportedContacts'

    def __str__(self):
        return '(contacts.importedContacts (ID: 0xad524315) = (imported={}, retry_contacts={}, users={}))'.format(None if not self.imported else [str(_) for _ in self.imported], None if not self.retry_contacts else [str(_) for _ in self.retry_contacts], None if not self.users else [str(_) for _ in self.users])
