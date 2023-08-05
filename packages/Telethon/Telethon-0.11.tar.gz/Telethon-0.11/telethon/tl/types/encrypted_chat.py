from ...tl.mtproto_request import MTProtoRequest


class EncryptedChat(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    encryptedChat#fa56ce36 id:int access_hash:long date:date admin_id:int participant_id:int g_a_or_b:bytes key_fingerprint:long = EncryptedChat"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xfa56ce36
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x6d28a37a

    def __init__(self, id, access_hash, date, admin_id, participant_id, g_a_or_b, key_fingerprint):
        """
        :param id: Telegram type: "int".
        :param access_hash: Telegram type: "long".
        :param date: Telegram type: "date".
        :param admin_id: Telegram type: "int".
        :param participant_id: Telegram type: "int".
        :param g_a_or_b: Telegram type: "bytes".
        :param key_fingerprint: Telegram type: "long".

        Constructor for EncryptedChat: Instance of either EncryptedChatEmpty, EncryptedChatWaiting, EncryptedChatRequested, EncryptedChat, EncryptedChatDiscarded.
        """
        super().__init__()

        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id
        self.g_a_or_b = g_a_or_b
        self.key_fingerprint = key_fingerprint

    def to_dict(self):
        return {
            'id': self.id,
            'access_hash': self.access_hash,
            'date': self.date,
            'admin_id': self.admin_id,
            'participant_id': self.participant_id,
            'g_a_or_b': self.g_a_or_b,
            'key_fingerprint': self.key_fingerprint,
        }

    def on_send(self, writer):
        writer.write_int(EncryptedChat.constructor_id, signed=False)
        writer.write_int(self.id)
        writer.write_long(self.access_hash)
        writer.tgwrite_date(self.date)
        writer.write_int(self.admin_id)
        writer.write_int(self.participant_id)
        writer.tgwrite_bytes(self.g_a_or_b)
        writer.write_long(self.key_fingerprint)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return EncryptedChat(None, None, None, None, None, None, None)

    def on_response(self, reader):
        self.id = reader.read_int()
        self.access_hash = reader.read_long()
        self.date = reader.tgread_date()
        self.admin_id = reader.read_int()
        self.participant_id = reader.read_int()
        self.g_a_or_b = reader.tgread_bytes()
        self.key_fingerprint = reader.read_long()

    def __repr__(self):
        return 'encryptedChat#fa56ce36 id:int access_hash:long date:date admin_id:int participant_id:int g_a_or_b:bytes key_fingerprint:long = EncryptedChat'

    def __str__(self):
        return '(encryptedChat (ID: 0xfa56ce36) = (id={}, access_hash={}, date={}, admin_id={}, participant_id={}, g_a_or_b={}, key_fingerprint={}))'.format(str(self.id), str(self.access_hash), str(self.date), str(self.admin_id), str(self.participant_id), str(self.g_a_or_b), str(self.key_fingerprint))
