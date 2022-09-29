from datetime import time

class Message:
    messageId : int
    messageText : str
    messageSentBy : str
    messageReceivedBy : str # received in a group or individual
    messageReactions = {} #: dict # {"user":"reaction"}
    messageTime : time
    isMessageDeleted : bool
    messageReadBy : list # [user1, user2 .... ]

