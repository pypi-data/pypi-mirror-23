from ...tl.mtproto_request import MTProtoRequest


class SendMessageUploadPhotoAction(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    sendMessageUploadPhotoAction#d1d34a26 progress:int = SendMessageAction"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xd1d34a26
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x20b2cc21

    def __init__(self, progress):
        """
        :param progress: Telegram type: "int".

        Constructor for SendMessageAction: Instance of either SendMessageTypingAction, SendMessageCancelAction, SendMessageRecordVideoAction, SendMessageUploadVideoAction, SendMessageRecordAudioAction, SendMessageUploadAudioAction, SendMessageUploadPhotoAction, SendMessageUploadDocumentAction, SendMessageGeoLocationAction, SendMessageChooseContactAction, SendMessageGamePlayAction, SendMessageRecordRoundAction, SendMessageUploadRoundAction.
        """
        super().__init__()

        self.progress = progress

    def to_dict(self):
        return {
            'progress': self.progress,
        }

    def on_send(self, writer):
        writer.write_int(SendMessageUploadPhotoAction.constructor_id, signed=False)
        writer.write_int(self.progress)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SendMessageUploadPhotoAction(None)

    def on_response(self, reader):
        self.progress = reader.read_int()

    def __repr__(self):
        return 'sendMessageUploadPhotoAction#d1d34a26 progress:int = SendMessageAction'

    def __str__(self):
        return '(sendMessageUploadPhotoAction (ID: 0xd1d34a26) = (progress={}))'.format(str(self.progress))
