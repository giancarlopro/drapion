from drapion import Drapion, GenericObject


class TelegramBotAPI(Drapion):
    """Creates an Drapion instance from a telegram bot api token"""

    def __init__(self, token: str, parser = GenericObject):
        url = "https://api.telegram.org/bot{token}/".format(
            token=token
        )
        super().__init__(url, parser)
