import typing as typ

from chaban.actions import Action

from . import text


class StartCommandAction(Action):
    def act(self, message: typ.Dict[str, typ.Any]) -> None:
        self.tbot.send_message(message["chat"]["id"], text.START_COMMAND)
