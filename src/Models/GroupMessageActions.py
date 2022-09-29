import random

from src.Models.Message import Message

class GroupMessageActions:

    def sendMessage(self, userID, text):
        message = Message()
        message.messageText = text
        message.messageSentBy = userID
        message.messageId = 1234 #random UUID
        return message;
    def reactToMessage(self, message: Message, userId, reaction):
        message.messageReactions[(message.messageId,userId)] = reaction
        print("Message liked")