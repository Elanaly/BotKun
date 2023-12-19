import discord
from os import environ
from discord.ext.commands import errors
from discord.ext.commands.context import Context
from dotenv import load_dotenv
from discord.ext import commands

extensions = [
    'cogs.ping',
    'cogs.greetings',
    'cogs.searchpic'
]

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=environ['PREFIX'],
            intents=discord.Intents.all()
        )

    async def setup_hook(self):
        for extension in extensions:
            await bot.load_extension(extension)

    async def on_ready(self):
        print("起動しました")
        await bot.change_presence(activity=discord.Game(name="*で反応するよ", type=1))
        return
    
    async def on_command_error(self, context: Context, exception: Exception) -> None:
        return await super().on_command_error(context, exception)



bot = MyBot()

load_dotenv()
bot.run(environ['TOKEN'])
