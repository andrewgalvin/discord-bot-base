import asyncio
import unittest
from unittest.mock import AsyncMock, MagicMock

from commands.hello_world_command import HelloWorldCommand


class TestHelloWorldCommand(unittest.TestCase):
    def setUp(self):
        self.client = MagicMock()
        self.command = HelloWorldCommand(self.client)
        self.ctx = MagicMock()
        self.ctx.send = AsyncMock()
        self.ctx.author.id = "YOUR_DISCORD_USER_ID_INT"
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def test_hello_world_authorized_user(self):
        self.ctx.author.id = "YOUR_DISCORD_USER_ID_INT"
        self.command.authorized_users = ["YOUR_DISCORD_USER_ID_INT"]

        async def test():
            await self.command.hello_world(self.ctx)
            self.ctx.send.assert_called_with("Hello, World!")

        self.loop.run_until_complete(test())

    def test_hello_world_unauthorized_user(self):
        self.ctx.author.id = "UNAUTHORIZED_USER_ID"
        self.command.authorized_users = ["YOUR_DISCORD_USER_ID_INT"]

        async def test():
            await self.command.hello_world(self.ctx)
            self.ctx.send.assert_called_with(
                "You are not authorized to use this command."
            )

        self.loop.run_until_complete(test())


if __name__ == "__main__":
    unittest.main()
