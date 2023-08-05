from ...tl.mtproto_request import MTProtoRequest


class InputPrivacyValueAllowUsers(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputPrivacyValueAllowUsers#131cc67f users:Vector<InputUser> = InputPrivacyRule"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x131cc67f
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x5a3b6b22

    def __init__(self, users):
        """
        :param users: Telegram type: "InputUser". Must be a list.

        Constructor for InputPrivacyRule: Instance of either InputPrivacyValueAllowContacts, InputPrivacyValueAllowAll, InputPrivacyValueAllowUsers, InputPrivacyValueDisallowContacts, InputPrivacyValueDisallowAll, InputPrivacyValueDisallowUsers.
        """
        super().__init__()

        self.users = users

    def to_dict(self):
        return {
            'users': [] if self.users is None else [None if x is None else x.to_dict() for x in self.users],
        }

    def on_send(self, writer):
        writer.write_int(InputPrivacyValueAllowUsers.constructor_id, signed=False)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.users))
        for users_item in self.users:
            users_item.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputPrivacyValueAllowUsers(None)

    def on_response(self, reader):
        reader.read_int()  # Vector's constructor ID
        self.users = []  # Initialize an empty list
        users_len = reader.read_int()
        for _ in range(users_len):
            users_item = reader.tgread_object()
            self.users.append(users_item)

    def __repr__(self):
        return 'inputPrivacyValueAllowUsers#131cc67f users:Vector<InputUser> = InputPrivacyRule'

    def __str__(self):
        return '(inputPrivacyValueAllowUsers (ID: 0x131cc67f) = (users={}))'.format(None if not self.users else [str(_) for _ in self.users])
