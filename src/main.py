import discord
import settings
from discord import app_commands
from discord.ext import commands

logger = settings.logging.getLogger("bot")


def run():
    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        print(f"We have logged in as {bot.user}")
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(f"Error syncing commands: {e}")

    @bot.tree.command(name="hello")
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(
            f"Hey {interaction.user.mention}! You used a slash command.", ephemeral=True
        )

    @bot.tree.command(name="say2")
    @app_commands.describe(thing_to_say="What should i say?")
    async def say2(interaction: discord.Interaction, thing_to_say: str):
        await interaction.response.send_message(
            f"{interaction.user.name} said: `{thing_to_say}`", ephemeral=True
        )

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)


if __name__ == "__main__":
    run()
