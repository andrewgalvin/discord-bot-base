import interactions
from interactions import slash_command


class HelloWorldCommand(interactions.Extension):
    def __init__(self, client):
        """
        Initializes the command with the given Discord client.

        Args:
            client (discord.Client): The Discord client instance.

        Attributes:
            authorized_users (list): A list of authorized user IDs.
        """
        self.authorized_users = ["YOUR_DISCORD_USER_ID_INT"]

    @slash_command(
        name="hello_world",
        description="Says hello to the world.",
    )
    async def hello_world(self, ctx):
        """
        Sends a "Hello, World!" message if the user is authorized.
        Args:
            ctx (commands.Context): The context in which the command was invoked.
        Returns:
            None
        """
        if ctx.author.id not in self.authorized_users:
            return await ctx.send("You are not authorized to use this command.")

        await ctx.send("Hello, World!")


def setup(client):
    HelloWorldCommand(client)
