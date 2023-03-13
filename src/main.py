import discord
import settings
from discord import app_commands
from discord.ext import commands





def run():
    bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())
    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(f"Error syncing commands: {e}")


    @bot.tree.command(name="hello")
    async def hello(interaction: discord.Interaction): 
        await interaction.response.send_message(f"Hey {interaction.user.mention}! You used a slash command.", ephemeral=True)


    bot.run(settings.DISCORD_API_SECRET)


if __name__=="__main__":
    run()