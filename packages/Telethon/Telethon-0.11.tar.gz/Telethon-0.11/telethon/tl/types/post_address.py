from ...tl.mtproto_request import MTProtoRequest


class PostAddress(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    postAddress#1e8caaeb street_line1:string street_line2:string city:string state:string country_iso2:string post_code:string = PostAddress"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x1e8caaeb
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8d7eda2c

    def __init__(self, street_line1, street_line2, city, state, country_iso2, post_code):
        """
        :param street_line1: Telegram type: "string".
        :param street_line2: Telegram type: "string".
        :param city: Telegram type: "string".
        :param state: Telegram type: "string".
        :param country_iso2: Telegram type: "string".
        :param post_code: Telegram type: "string".

        Constructor for PostAddress: Instance of PostAddress.
        """
        super().__init__()

        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.city = city
        self.state = state
        self.country_iso2 = country_iso2
        self.post_code = post_code

    def to_dict(self):
        return {
            'street_line1': self.street_line1,
            'street_line2': self.street_line2,
            'city': self.city,
            'state': self.state,
            'country_iso2': self.country_iso2,
            'post_code': self.post_code,
        }

    def on_send(self, writer):
        writer.write_int(PostAddress.constructor_id, signed=False)
        writer.tgwrite_string(self.street_line1)
        writer.tgwrite_string(self.street_line2)
        writer.tgwrite_string(self.city)
        writer.tgwrite_string(self.state)
        writer.tgwrite_string(self.country_iso2)
        writer.tgwrite_string(self.post_code)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return PostAddress(None, None, None, None, None, None)

    def on_response(self, reader):
        self.street_line1 = reader.tgread_string()
        self.street_line2 = reader.tgread_string()
        self.city = reader.tgread_string()
        self.state = reader.tgread_string()
        self.country_iso2 = reader.tgread_string()
        self.post_code = reader.tgread_string()

    def __repr__(self):
        return 'postAddress#1e8caaeb street_line1:string street_line2:string city:string state:string country_iso2:string post_code:string = PostAddress'

    def __str__(self):
        return '(postAddress (ID: 0x1e8caaeb) = (street_line1={}, street_line2={}, city={}, state={}, country_iso2={}, post_code={}))'.format(str(self.street_line1), str(self.street_line2), str(self.city), str(self.state), str(self.country_iso2), str(self.post_code))
