# Import
import discord
from discord.ext import commands
from Authentication.AccountCreator import AccountCreator

# Main
class Main(commands.Cog, discord.Client) :

    # Constructor
    def __init__(self, bot):
        self.bot = bot

    # Create Account
    @commands.command(pass_context=True)
    async def create_account(self, ctx) :
        createAccount = AccountCreator(ctx)
        await createAccount.create()

# Prefix
bot = commands.Bot(command_prefix=("?"))

# Initializing Display
@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

# Add Comment to Bot
bot.add_cog(Main(bot))

# Reading token and Run
with open('token.txt') as f:
    lines = f.readlines()
    bot.run(lines[0], bot=True)