from ....tl.mtproto_request import MTProtoRequest


class SendCustomRequestRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    bots.sendCustomRequest#aa2769ed custom_method:string params:DataJSON = DataJSON"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xaa2769ed
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xad0352e8

    def __init__(self, custom_method, params):
        """
        :param custom_method: Telegram type: "string".
        :param params: Telegram type: "DataJSON".

        :returns DataJSON: Instance of DataJSON.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.custom_method = custom_method
        self.params = params

    def to_dict(self):
        return {
            'custom_method': self.custom_method,
            'params': None if self.params is None else self.params.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(SendCustomRequestRequest.constructor_id, signed=False)
        writer.tgwrite_string(self.custom_method)
        self.params.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SendCustomRequestRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'bots.sendCustomRequest#aa2769ed custom_method:string params:DataJSON = DataJSON'

    def __str__(self):
        return '(bots.sendCustomRequest (ID: 0xaa2769ed) = (custom_method={}, params={}))'.format(str(self.custom_method), str(self.params))
