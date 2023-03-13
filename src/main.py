import discord
import settings
from discord import app_commands
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents )


    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        print(f'We have logged in as {bot.user}')
        # try:
        #     synced = await bot.tree.sync()
        #     print(f"Synced {len(synced)} command(s)")
        # except Exception as e:
        #     print(f"Error syncing commands: {e}")

    @bot.command(help="This is Help",
    description="This is description",
    brief = "This is brief")

    async def ping(ctx):
        await ctx.send("Pong")

    # @bot.tree.command(name="hello")
    # async def hello(interaction: discord.Interaction): 
    #     await interaction.response.send_message(f"Hey {interaction.user.mention}! You used a slash command.", ephemeral=True)

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)


if __name__=="__main__":
    run()