from drapion import Drapion


class TelegramBotAPI(Drapion):
    """Creates an Drapion instance from a telegram bot api token
    
    See documentation for api reference:
    https://core.telegram.org/bots/api
    """

    def __init__(self, token: str):
        url = "https://api.telegram.org/bot{token}/".format(
            token=token
        )
        super().__init__(url)