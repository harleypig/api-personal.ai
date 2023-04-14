import requests
import json

##############################################################################
class PersonalAI:
    #-------------------------------------------------------------------------
    def __init__(self, api_key):
        self.base_url = "https://api.personal.ai/v1"
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'x-api-key': self.api_key
        }

    #-------------------------------------------------------------------------
    def __repr__(self):
        masked_api_key = self.api_key[:5] + "..." + self.api_key[-5:]
        return f"<PersonalAI(api_key='{masked_api_key}', base_url='{self.base_url}')>"

    #-------------------------------------------------------------------------
    def _api(self, method, call, payload=None):
        """
        Make an API call to Personal.AI.

        :param str method: HTTP method to use. Required.
                           Example: "POST" or "GET"

        :param str call: API call to make. Required.
                         Example: "memory" or "message"

        :param dict payload: JSON payload to send with the API call. Optional.
                             Example: {"Text": "My first memory with PersonalAI!"}
        """

        url = f"{self.base_url}/{call}"

        try:
            if method == "POST":
                response = requests.post(url, headers=self.headers, json=payload)

            elif method == "GET":
                response = requests.get(url, headers=self.headers)

            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as e:
            print(f"An HTTP error occurred: {e}")
            return None

    #-------------------------------------------------------------------------
    def create_memory(self, text,
                      source_name,
                      created_time=None,
                      device_name=None,
                      raw_feed=None,
                      ):
        """
        Create a memory in Personal.ai.

        This function takes text, source_name, and optional parameters to
        create a memory in Personal.AI. If the memory is created successfully,
        it returns True. Otherwise, it returns False.

        :param str text: Plain text memories to upload to your stack. Required.
                         Example: "My first memory with PersonalAI!"

        :param str source_name: The source or application of memory to help you
                                recall where it is from. Required.
                                Example: "Notes" or "My Thoughts"

        :param str created_time: Time (including timezone) of the memory to help
                                 you recall when it is from. Default: "Now"
                                 Example: "Wed, 28 Jul 2021 13:30:00 PDT"

        :param str device_name: The device from where the memory is captured
                                or uploaded. Default: "API"
                                Example: "Apple Watch""

        :param str raw_feed: The formatted text that can be stored as it is.
                             Example: <p>My first memory with PersonalAI!</p>

        :return: True if the memory was created successfully, False otherwise.
        :rtype: bool
        """

        payload = {
            "Text": text,
            "SourceName": source_name,
        }

        if created_time is not None:
            payload["CreatedTime"] = created_time

        if device_name is not None:
            payload["DeviceName"] = device_name

        if raw_feed is not None:
            payload["RawFeed"] = raw_feed

        return self._api("POST", "memory", payload)

    #-------------------------------------------------------------------------
    def ai_message(self, text):
        """
        Send a message to the AI and receive a response.

        :param str text: Message to send to your AI for a response
                         Example: "what is k8s?"

        :return: Response JSON object.
        :rtype: dict
        """

        return self._api("POST", "message", {"Text": text})

    #-------------------------------------------------------------------------
    def upload_uri(self, uri):
        """
        Upload a URI to Personal.AI.

        :param str uri: The URI to upload.

        :return: Response JSON object.
        :rtype: dict
        """

        return self._api("POST", "upload", {"Url": uri})

    #-------------------------------------------------------------------------
    def validate_key(self):
        """
        Validate the API key.

        :return: Response JSON object.
        :rtype: dict
        """

        return self._api("GET", "api-key/validate")

