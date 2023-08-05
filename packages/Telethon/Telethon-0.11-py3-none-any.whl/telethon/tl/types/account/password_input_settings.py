from ....tl.mtproto_request import MTProtoRequest


class PasswordInputSettings(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    account.passwordInputSettings#86916deb flags:# new_salt:flags.0?bytes new_password_hash:flags.0?bytes hint:flags.0?string email:flags.1?string = account.PasswordInputSettings"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x86916deb
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xc426ca6

    def __init__(self, new_salt=None, new_password_hash=None, hint=None, email=None):
        """
        :param new_salt: Telegram type: "bytes".
        :param new_password_hash: Telegram type: "bytes".
        :param hint: Telegram type: "string".
        :param email: Telegram type: "string".

        Constructor for account.PasswordInputSettings: Instance of PasswordInputSettings.
        """
        super().__init__()

        self.new_salt = new_salt
        self.new_password_hash = new_password_hash
        self.hint = hint
        self.email = email

    def to_dict(self):
        return {
            'new_salt': self.new_salt,
            'new_password_hash': self.new_password_hash,
            'hint': self.hint,
            'email': self.email,
        }

    def on_send(self, writer):
        writer.write_int(PasswordInputSettings.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.new_salt else 0
        flags |= (1 << 0) if self.new_password_hash else 0
        flags |= (1 << 0) if self.hint else 0
        flags |= (1 << 1) if self.email else 0
        writer.write_int(flags)

        if self.new_salt:
            writer.tgwrite_bytes(self.new_salt)

        if self.new_password_hash:
            writer.tgwrite_bytes(self.new_password_hash)

        if self.hint:
            writer.tgwrite_string(self.hint)

        if self.email:
            writer.tgwrite_string(self.email)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return PasswordInputSettings(None, None, None, None)

    def on_response(self, reader):
        flags = reader.read_int()

        if (flags & (1 << 0)) != 0:
            self.new_salt = reader.tgread_bytes()

        if (flags & (1 << 0)) != 0:
            self.new_password_hash = reader.tgread_bytes()

        if (flags & (1 << 0)) != 0:
            self.hint = reader.tgread_string()

        if (flags & (1 << 1)) != 0:
            self.email = reader.tgread_string()

    def __repr__(self):
        return 'account.passwordInputSettings#86916deb flags:# new_salt:flags.0?bytes new_password_hash:flags.0?bytes hint:flags.0?string email:flags.1?string = account.PasswordInputSettings'

    def __str__(self):
        return '(account.passwordInputSettings (ID: 0x86916deb) = (new_salt={}, new_password_hash={}, hint={}, email={}))'.format(str(self.new_salt), str(self.new_password_hash), str(self.hint), str(self.email))
