from ....tl.mtproto_request import MTProtoRequest


class SetInlineBotResultsRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.setInlineBotResults#eb5ea206 flags:# gallery:flags.0?true private:flags.1?true query_id:long results:Vector<InputBotInlineResult> cache_time:int next_offset:flags.2?string switch_pm:flags.3?InlineBotSwitchPM = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xeb5ea206
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, query_id, results, cache_time, gallery=None, private=None, next_offset=None, switch_pm=None):
        """
        :param gallery: Telegram type: "true".
        :param private: Telegram type: "true".
        :param query_id: Telegram type: "long".
        :param results: Telegram type: "InputBotInlineResult". Must be a list.
        :param cache_time: Telegram type: "int".
        :param next_offset: Telegram type: "string".
        :param switch_pm: Telegram type: "InlineBotSwitchPM".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.gallery = gallery
        self.private = private
        self.query_id = query_id
        self.results = results
        self.cache_time = cache_time
        self.next_offset = next_offset
        self.switch_pm = switch_pm

    def to_dict(self):
        return {
            'gallery': self.gallery,
            'private': self.private,
            'query_id': self.query_id,
            'results': [] if self.results is None else [None if x is None else x.to_dict() for x in self.results],
            'cache_time': self.cache_time,
            'next_offset': self.next_offset,
            'switch_pm': None if self.switch_pm is None else self.switch_pm.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(SetInlineBotResultsRequest.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.gallery else 0
        flags |= (1 << 1) if self.private else 0
        flags |= (1 << 2) if self.next_offset else 0
        flags |= (1 << 3) if self.switch_pm else 0
        writer.write_int(flags)

        writer.write_long(self.query_id)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.results))
        for results_item in self.results:
            results_item.on_send(writer)

        writer.write_int(self.cache_time)
        if self.next_offset:
            writer.tgwrite_string(self.next_offset)

        if self.switch_pm:
            self.switch_pm.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SetInlineBotResultsRequest(None, None, None, None, None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'messages.setInlineBotResults#eb5ea206 flags:# gallery:flags.0?true private:flags.1?true query_id:long results:Vector<InputBotInlineResult> cache_time:int next_offset:flags.2?string switch_pm:flags.3?InlineBotSwitchPM = Bool'

    def __str__(self):
        return '(messages.setInlineBotResults (ID: 0xeb5ea206) = (gallery={}, private={}, query_id={}, results={}, cache_time={}, next_offset={}, switch_pm={}))'.format(str(self.gallery), str(self.private), str(self.query_id), None if not self.results else [str(_) for _ in self.results], str(self.cache_time), str(self.next_offset), str(self.switch_pm))
