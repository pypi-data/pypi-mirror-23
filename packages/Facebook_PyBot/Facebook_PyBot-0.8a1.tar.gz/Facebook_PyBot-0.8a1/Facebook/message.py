try:
    import ujson as json
except:
    import json


def updates(callback):
    """
    This function takes the callback as an input and creates an instance for each message received and stores it(instance) into
    an array. Which is then returned
    
    :param callback: contains the callback from facebook.
    :return: array of Message instances.
    
    """
    entries = []
    try:
        callback = json.decode(callback)
    except:
        pass
    for entry in callback["entry"]:
        messaging = entry["messaging"]
        messages = [Message(data) for data in messaging]
        entries.extend(messages)
    return entries


class Message:
    custom_data = []

    def __init__(self, data):
        """
         
        :param data: Message containing callback from facebook i.e. sender_id,recipient_id,message etc.
        :type data: Dict
        
        """
        self.USER_ID = str(data['sender']['id'])
        self.PAGE_ID = data['recipient']['id']
        # Thing may fuck up a little below, cause I dunno if "is_echo" is always there or just in echo callbacks
        # TODO: Check echo callbacks

        self.Message_Received = Received(data)
        try:
            self.Message_Echo = Echo(data)
            # if self.Message_Echo.echo is not None:
            # self.Message_Received.message = None
        except:
            pass
        self.Message_Delivered = Delivered(data)
        self.Message_Read = Read(data)


class Received:
    """
    Message Received callback
    
    This class stores the text or attachment sent by facebook in the callback.
    
    Attributes:
        :param mid:     Message id of the message received. Be it either text or attachment
        :param text:    stores the text of the message if received(otherwise none)
        :param attachment: instance of the attachment class
    
    For more info go to https://developers.facebook.com/docs/messenger-platform/webhook-reference/message
    """

    def __init__(self, messaging):
        self.mid = self.text = self.quick_reply = None
        self.attachments = None
        self.message = None
        self.postback = None
        self.referral = None
        if messaging.get('message'):
            self.message = messaging['message']
            self.mid = self.message['mid']
            if self.message.get('text'):  # If a text message is received then the message will be stored
                self.text = self.message['text']
            elif self.message.get('attachments'):  # an array of attachments is stored here
                # TODO: Attachments object looks like consisting of an array, Take a look at it later
                for eachAttachment in self.message['attachments']:
                    """
                    If a attachment is received then it will be stored
                    This creates an instance of attachments class and stores it.
                    the instance will consist of either contain coordinates or either URL of the attachment
                    """
                    self.attachments = Attachments(eachAttachment)
            if self.message.get('quick_reply'):
                self.quick_reply = self.message['quick_reply']
                self.payload = self.quick_reply['payload']
        elif messaging.get("postback"):
            self.postback = messaging["postback"]
            self.payload = self.postback.get("payload")
            self.referral = self.postback.get("referral")


class Delivered:
    """
    Message Delivered callback
        
    For more info go to https://developers.facebook.com/docs/messenger-platform/webhook-reference/message-delivered
    If a delivery callback is received then it will be stored otherwise delivery will be none
    """

    def __init__(self, messaging):
        self.mids = []
        if 'delivery' in messaging:
            self.delivery = messaging['delivery']
            if self.delivery.get('mids'):
                for ids in self.delivery['mids']:
                    self.mids = self.mids.append(ids)
            self.watermark = self.delivery['watermark']
            self.seq = self.delivery['seq']
        else:
            self.delivery = None


class Read:
    """
    Message Read Callback
    For more info go to https://developers.facebook.com/docs/messenger-platform/webhook-reference/message-read
    If a read callback is received then it will be stored otherwise read will be none
    """

    def __init__(self, messaging):
        if 'read' in messaging:
            self.read = messaging['read']
            self.Watermark = self.read['watermark']
            self.Seq = self.read['seq']
        else:
            self.Watermark = None
            self.read = None
            self.Seq = None


class Echo:
    """
    Message Echo callback
    For more info go to https://developers.facebook.com/docs/messenger-platform/webhook-reference/message-echo
    """

    def __init__(self, messaging):
        self.message = messaging['message']
        if self.message.get('is_echo'):
            self.message = messaging['message']
            self.app_id = self.message['app_id']
            if self.message.get('metadata'):
                self.metadata = self.message['metadata']
            else:
                self.metadata = None
            self.mid = self.message['mid']
            self.seq = self.message['seq']
        else:
            self.echo = None


class Attachments:
    """
    This class contains the type of the attachments and their payload
    :param type: The type of attachment. Will be one of many type : location, image,video,audio or file
    :param url: URL of the image,video,audio or file
    :param coordinates_lat: latitude of the coordinate of the location received
    :param self.coordinates_long: longitude of the coordinate of the location
    """

    def __init__(self, attachment):
        self.type = attachment['type']
        self.url = None
        if self.type == 'location':
            print(attachment)
            self.title = attachment["title"]
            self.coordinates_lat = attachment['payload']['coordinates']['lat']
            self.coordinates_long = attachment['payload']['coordinates']['long']
        else:
            self.url = attachment['payload']['url']
