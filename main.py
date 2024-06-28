import discord

from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")
    try:
        synced = await bot.tree.sync()  # Synchronisiere die globalen Slash-Commands
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.tree.command(name="getbadge", description="Get developer badge")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Please wait to get your badge it can be take 24 hours")

# Bot mit Token starten
if __name__ == "__main__":
    token = input("Please enter your bot token: ")
    bot.run(token)