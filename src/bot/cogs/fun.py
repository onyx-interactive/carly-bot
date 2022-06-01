import discord
from discord.ext import commands
from discord.ext import tasks

from ..log_setup import logger
from ..utils import utils as ut

import random

### @package misc
#
# Collection of miscellaneous helpers.
#

class Fun(commands.Cog):
    """
    Various useful Commands for everyone
    """

    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(name='dado', help="Sorteia um número de 1 à 6")
    async def dado(self, ctx):
        """!
        @param ctx Context of the message
        """
        numr = random.randint(1,6)
        logger.info(f"dado - lado : {round(numr)}")

        await ctx.send(
            embed=ut.make_embed(
                name='Dado: ',
                value=f'`{round(numr)}`')
        )

    # Example for an event listener
    # This one will be called on each message the bot recieves
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        pass

def setup(bot):
    bot.add_cog(Fun(bot))
