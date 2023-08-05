from ...tl.mtproto_request import MTProtoRequest


class InputFileLocation(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputFileLocation#14637196 volume_id:long local_id:int secret:long = InputFileLocation"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x14637196
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x1523d462

    def __init__(self, volume_id, local_id, secret):
        """
        :param volume_id: Telegram type: "long".
        :param local_id: Telegram type: "int".
        :param secret: Telegram type: "long".

        Constructor for InputFileLocation: Instance of either InputFileLocation, InputEncryptedFileLocation, InputDocumentFileLocation.
        """
        super().__init__()

        self.volume_id = volume_id
        self.local_id = local_id
        self.secret = secret

    def to_dict(self):
        return {
            'volume_id': self.volume_id,
            'local_id': self.local_id,
            'secret': self.secret,
        }

    def on_send(self, writer):
        writer.write_int(InputFileLocation.constructor_id, signed=False)
        writer.write_long(self.volume_id)
        writer.write_int(self.local_id)
        writer.write_long(self.secret)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputFileLocation(None, None, None)

    def on_response(self, reader):
        self.volume_id = reader.read_long()
        self.local_id = reader.read_int()
        self.secret = reader.read_long()

    def __repr__(self):
        return 'inputFileLocation#14637196 volume_id:long local_id:int secret:long = InputFileLocation'

    def __str__(self):
        return '(inputFileLocation (ID: 0x14637196) = (volume_id={}, local_id={}, secret={}))'.format(str(self.volume_id), str(self.local_id), str(self.secret))
