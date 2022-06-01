import discord
from discord.ext import commands

from ..utils import utils as utl
from ..environment import OWNER_NAME, OWNER_ID, VERSION, PREFIX

### @package help
# 
# This custom help command is a replacement for the default one on any Discord Bot written in discord.py!
# However, you must put "bot.remove_command('help')" in your bot, and the command must be in a cog for it to work.
# 
# Original concept by [Jared Newsom (AKA Jared M.F.)](https://gist.github.com/StudioMFTechnologies/ad41bfd32b2379ccffe90b0e34128b8b)
# Rewritten and optimized by [nonchris](https://github.com/nonchris)
# 
# This version relies more on the structure around this module than the gist does, which is more 'stand alone'


class Help(commands.Cog):
    """
    Sends this help message
    """

    def __init__(self, bot):
        """! 
        Constructor

        @param bot The bot instance to be used.
        """
        self.bot = bot

    @commands.command(aliases=['h', 'hilfe'])
    # @commands.bot_has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx, *params):
        """!
        Shows all modules of that bot
        
        @param ctx Context of the message.
        @param params further arguments
        """

        # checks if cog parameter was given
        # if not: sending all modules and commands not associated with a cog
        if not params:
            # checks if owner is on this server - used to 'tag' owner
            try:
                owner = ctx.guild.get_member(OWNER_ID).mention

            except AttributeError:
                owner = OWNER_NAME

            # starting to build embed
            emb = discord.Embed(title='Comandos & módulos', color=utl.blue_light,
                                description=f'Use `{PREFIX}h <módulo>` para obter mais informações sobre esse modulo '
                                            f':smiley:\n')

            # iterating trough cogs, gathering descriptions
            cogs_desc = ''
            for cog in self.bot.cogs:
                # ignoring boring cogs
                if cog == "MessageListener" or cog == "Help":
                    continue
                cogs_desc += f'`{cog}` {self.bot.cogs[cog].__doc__}\n'

            # adding 'list' of cogs to embed
            emb.add_field(name='Módulos', value=cogs_desc, inline=False)

            # integrating trough uncategorized commands
            commands_desc = ''
            for command in self.bot.walk_commands():
                # if cog not in a cog
                # listing command if cog name is None and command isn't hidden
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'

            # adding those commands to embed
            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)

            # setting information about author
            emb.add_field(name="Sobre",
                          value=f"Este bot é mantido por {owner}.\n\
                                Por favor, visite ::  http://www.onyxinteractive.fun/carly-bot para enviar ideias ou bugs.\n\
                                \n")
            emb.set_footer(text=f" Versão atual do BOT: {VERSION}")

        # block called when one cog-name is given
        # trying to find matching cog and it's commands
        elif len(params) == 1:

            # iterating trough cogs
            for cog in self.bot.cogs:
                # check if cog is the matching one
                if cog.lower() == params[0].lower():

                    # making title - getting description from doc-string below class
                    emb = discord.Embed(title=f'{cog} - comandos', description=self.bot.cogs[cog].__doc__,
                                        color=utl.green)

                    # getting commands from cog
                    for command in self.bot.get_cog(cog).get_commands():
                        # if cog is not hidden
                        if not command.hidden:
                            emb.add_field(name=f"{PREFIX}{command.name}", value=command.help, inline=False)
                    # found cog - breaking loop
                    break

            # if input not found
            # yes, for-loops have an else statement, it's called when no 'break' was issued
            else:
                emb = discord.Embed(title="Oque é isso?!",
                                    description=f"Eu nunca ouvir sobre o modulo `{params[0]}` antes :scream:",
                                    color=utl.orange)

        # too many cogs requested - only one at a time allowed
        elif len(params) > 1:
            emb = discord.Embed(title="Isso é demais. ",
                                description="Por favor, solicite apenas um módulo por vez :sweat_smile:",
                                color=utl.orange)

        else:
            emb = discord.Embed(title="É um lugar mágico",
                                description="Eu não sei como você chegou aqui. Mas eu não vi isso vindo.\n"
                                            "Você poderia ser tão gentil para relatar esse problema para mim no site?\n"
                                            "http://www.onyxintective.fun/carly-bot/report\n"
                                            "Obrigado! ~Isaías",
                                color=utl.orange)

        # sending reply embed using our own function defined above
        await utl.send_embed(ctx, emb)


def setup(bot):
    """!
    Setup a bot.

    @param bot The bot to setup.
    """
    bot.add_cog(Help(bot))
