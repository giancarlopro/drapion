import json

from drapion import Drapion, parsers


class TelegramParser(parsers.BaseParser):
    @classmethod
    def parse(cls, data):
        """Validates and parse valid telegram api responses

        :param data: JSON-serialized str
        :return: Return from parsers.JSONParser.parse
        """
        obj = json.loads(data)

        if obj['ok'] is False:
            raise Exception(obj['description'])

        return parsers.JSONParser.parse(obj['result'])


class TelegramBotAPI(Drapion):
    """Creates an Drapion instance from a telegram bot api token

    See documentation for api reference:
    https://core.telegram.org/bots/api
    """

    def __init__(self, token: str):
        url = "https://api.telegram.org/bot{token}/".format(
            token=token
        )
        super().__init__(url, parser=TelegramParser)
