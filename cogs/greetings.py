from discord.ext import commands
import discord

class GreetingsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('GreetingCog on ready')

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

async def setup(bot):
    await bot.add_cog(GreetingsCog(bot))