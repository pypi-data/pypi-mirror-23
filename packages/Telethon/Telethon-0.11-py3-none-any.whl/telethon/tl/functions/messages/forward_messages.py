from ....tl.mtproto_request import MTProtoRequest
from ....utils import get_input_peer
import os


class ForwardMessagesRequest(MTProtoRequest):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.forwardMessages#708e0195 flags:# silent:flags.5?true background:flags.6?true with_my_score:flags.8?true from_peer:InputPeer id:Vector<int> random_id:Vector<long> to_peer:InputPeer = Updates"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x708e0195
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8af52aac

    def __init__(self, from_peer, id, to_peer, silent=None, background=None, with_my_score=None, random_id=None):
        """
        :param silent: Telegram type: "true".
        :param background: Telegram type: "true".
        :param with_my_score: Telegram type: "true".
        :param from_peer: Telegram type: "InputPeer".
        :param id: Telegram type: "int". Must be a list.
        :param random_id: Telegram type: "long". Must be a list.
        :param to_peer: Telegram type: "InputPeer".

        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, UpdatesTg, UpdateShortSentMessage.
        """
        super().__init__()
        self.result = None
        self.confirmed = True  # Confirmed by default

        self.silent = silent
        self.background = background
        self.with_my_score = with_my_score
        self.from_peer = get_input_peer(from_peer)
        self.id = id
        self.random_id = random_id if random_id is not None else int.from_bytes(os.urandom(8), signed=True, byteorder='little')
        self.to_peer = get_input_peer(to_peer)

    def to_dict(self):
        return {
            'silent': self.silent,
            'background': self.background,
            'with_my_score': self.with_my_score,
            'from_peer': None if self.from_peer is None else self.from_peer.to_dict(),
            'id': [] if self.id is None else self.id[:],
            'random_id': [] if self.random_id is None else self.random_id[:],
            'to_peer': None if self.to_peer is None else self.to_peer.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(ForwardMessagesRequest.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 6) if self.background else 0
        flags |= (1 << 8) if self.with_my_score else 0
        writer.write_int(flags)

        self.from_peer.on_send(writer)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.id))
        for id_item in self.id:
            writer.write_int(id_item)

        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.random_id))
        for random_id_item in self.random_id:
            writer.write_long(random_id_item)

        self.to_peer.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ForwardMessagesRequest(None, None, None, None, None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'messages.forwardMessages#708e0195 flags:# silent:flags.5?true background:flags.6?true with_my_score:flags.8?true from_peer:InputPeer id:Vector<int> random_id:Vector<long> to_peer:InputPeer = Updates'

    def __str__(self):
        return '(messages.forwardMessages (ID: 0x708e0195) = (silent={}, background={}, with_my_score={}, from_peer={}, id={}, random_id={}, to_peer={}))'.format(str(self.silent), str(self.background), str(self.with_my_score), str(self.from_peer), None if not self.id else [str(_) for _ in self.id], None if not self.random_id else [str(_) for _ in self.random_id], str(self.to_peer))
