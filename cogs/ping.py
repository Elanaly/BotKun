import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('pingが読み込まれました')

    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency
        latency_ms: int = round(latency * 1000)
        await ctx.send(f'🏓Pong! ({latency_ms}ms)')

async def setup(bot):
    await bot.add_cog(Ping(bot))