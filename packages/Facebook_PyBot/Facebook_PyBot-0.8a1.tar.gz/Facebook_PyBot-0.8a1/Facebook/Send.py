import os

from .exception import raise_error

try:
    import ujson as json
except:
    import json

import requests
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


headers = {"Content-Type": "application/json"}


class Send:
    def __init__(self, page_access_token):
        self.URL = 'https://graph.facebook.com/v2.9/{}'
        self.Access_Token = page_access_token

    def send_text(self, user_id, message, notification_type='REGULAR', quick_replies=None):
        """
        @optional
        
        sender_action
        
        @required
        
        :param user_id: user_id of the recipient
        :type user_id: string
        :param message: Message text
        :type message: string
        :param notification_type: Push notification type: REGULAR, SILENT_PUSH, or NO_PUSH
        :type notification_type: string
        :param quick_replies: a list containing number of quick replies.(Up to 11)
        :return: return response from facebook or type of error if encountered
        
        """
        url = self.URL.format("me/messages")
        payload = {}
        params = {"access_token": self.Access_Token}
        header = {"Content-Type": "application/json"}
        payload['recipient'] = {"id": user_id}
        payload['message'] = {"text": message}
        if quick_replies is not None:
            payload["message"]["quick_replies"] = quick_replies
        payload["notification_type"] = notification_type
        response = requests.post(url, headers=header, params=params, data=json.dumps(payload))
        result = response.json()
        if 'recipient_id' not in result:
            error = raise_error(result)
            raise error
        else:
            return result

    def send_attachment(self, user_id, type, url=None, file=None, notification_type='REGULAR', quick_replies=None):
        """
        @required
        
        :param user_id: user_id of the recipient
        :param type: Type of attachment, may be image, audio, video, file or template
        :type type: str
        :param url: URL of data
        :param notification_type: Push notification type: REGULAR, SILENT_PUSH, or NO_PUSH
        :type notification_type: string
        :param quick_replies: a list containing number of quick replies.(Up to 11)
        :return: response from facebook or type of error if encountered
        
        """

        payload = {
            "recipient": {
                "id": user_id
            },
            "message": {
                "attachment": {
                    "type": type,
                    "payload": {}
                }
            },
        }
        if url is not None:
            payload["message"]["attachment"]["payload"]["url"] = url
        else:
            payload["filedata"] = (os.path.basename(file), open(file, 'rb'))
        if quick_replies is not None:
            payload["message"]["quick_replies"] = quick_replies
        payload["notification_type"] = notification_type
        params = {"access_token": self.Access_Token}
        URL = self.URL.format("me/messages")
        response = requests.post(URL, headers=headers, params=params, data=json.dumps(payload))
        result = response.json()
        if "recipient_id" not in result:
            error = raise_error(result)
            raise error
        else:
            return result

    def sender_action(self, user_id, action="mark_seen"):
        """
        Sender Action of Facebook bot API.
        For more info https://developers.facebook.com/docs/messenger-platform/send-api-reference/sender-actions
        
        :param user_id: User id of the person who is going to receive the action
        :type user_id: str
        :param action: type of sender action
        :type action: str
        
        """
        if not isinstance(action, str):
            raise ValueError
        payload = {
            "recipient": {
                "id": user_id
            },
            "sender_action": action
        }
        url = self.URL.format("me/messages")
        param = {"access_token": self.Access_Token}
        response = requests.post(url, headers=headers, params=param, data=json.dumps(payload))
        data = response.json()
        return data

    def get_user_info(self, user_id):
        """
        
        The User Profile API lets your bot get more information about the user
        for more info go to https://developers.facebook.com/docs/messenger-platform/user-profile
        
        :param user_id: User id of the person of whom user info is to be retrieved.
        :type user_id: str
        :return: first name,last name,profile pic,locale,timezone,gender.
        
        """
        url = self.URL.format(user_id)
        key = {"fields": "first_name,last_name,profile_pic,locale,timezone,gender",
               "access_token": self.Access_Token
               }
        response = requests.get(url, params=key)
        data = response.json()
        try:
            data = json.decode(data)
        except:
            pass
        try:
            return data["first_name"], data["last_name"], data["profile_pic"], data["locale"], data["timezone"], data[
                "gender"]
        except:
            return None

    def send_button_template(self, user_id, text, button_1, button_2=None, button_3=None, quick_replies=None):
        """
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/button-template
        
        :param user_id: User Id of the recipient to whom the message is being sent.
        :param text: UTF-8 encoded text of up to 640 characters that appears the in main body.
        :param button_1,button_2,button_3: Set of, one to three, buttons that appear as call-to-actions.
        :param quick_replies: a list containing number of quick replies.(Up to 11)
        :return:
        
        """
        try:
            button_1 = json.loads(button_1)
            button_2 = json.loads(button_2)
            button_3 = json.loads(button_3)
        except:
            pass
        buttons = [button_1]
        if button_2 is not None:
            buttons.append(button_2)
        if button_3 is not None:
            buttons.append(button_3)
        payload = {
            "recipient": {
                "id": user_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": text,
                        "buttons": buttons
                    }
                }
            }
        }
        if quick_replies is not None:
            payload["message"]["quick_replies"] = quick_replies
        url = self.URL.format("me/messages")
        params = {"access_token": self.Access_Token}
        response = requests.post(url, headers=headers, params=params, data=json.dumps(payload))
        data = response.json()
        if not data.get("recipient_id"):
            error = raise_error(data)
            raise error
        else:
            return data

    def send_generic_template(self, user_id, elements, quick_replies=None):
        """
        For more info go to https://developers.facebook.com/docs/messenger-platform/send-api-reference/generic-template
        
        :param user_id: User Id of the recipient to whom the message is being sent.
        :type user_id: str
        :param elements: a list of elements(up to 10).
        :param quick_replies: a list containing number of quick replies.(Up to 11)
        Element: Data for each bubble in message
        :return:
        
        """
        logger.info(elements)
        payload = {
            "recipient": {
                "id": user_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "image_aspect_ratio": "horizontal",
                        "elements": elements
                    }
                }
            }
        }
        logger.info(payload)
        if quick_replies is not None:
            payload["message"]["quick_replies"] = quick_replies
        url = self.URL.format("me/messages")
        params = {"access_token": self.Access_Token}
        response = requests.post(url, headers=headers, params=params, data=json.dumps(payload))
        data = response.json()
        logger.info(data)
        if not data.get("recipient_id"):
            error = raise_error(data)
            raise error
        else:
            return data

    def send_list_template(self, user_id, elements, top_element_style="large", quick_replies=None):
        """
        For more info go to https://developers.facebook.com/docs/messenger-platform/send-api-reference/list-template
        
        :param user_id: User Id of the recipient to whom the message is being sent.
        :type user_id: str
        :param top_element_style: Value must be large or compact. Default to large if not specified.
        :type top_element_style: enum
        :param elements: List of view elements (maximum of 4 elements and minimum of 2 elements).
        :param quick_replies: a list containing number of quick replies.(Up to 11)
        :return:
        
        """
        payload = {
            "recipient": {
                "id": user_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "list",
                        "top_element_style": top_element_style,
                        "elements": elements
                    }
                }
            }
        }
        logger.info(payload)
        if quick_replies is not None:
            payload["message"]["quick_replies"] = quick_replies
        url = self.URL.format("me/messages")
        params = {"access_token": self.Access_Token}
        response = requests.post(url, headers=headers, params=params, data=json.dumps(payload))
        data = response.json()
        if not data.get("recipient_id"):
            error = raise_error(data)
            raise error
        else:
            return data
