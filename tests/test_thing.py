from __future__ import annotations

from discord.ext import something, commands

class TestThing:
    def test_init(self) -> None:
        bot = something.Thing(command_prefix='$')
        assert isinstance(bot, commands.Bot)
