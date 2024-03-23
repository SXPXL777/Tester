import os
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == 'hi':
        await message.channel.send('Hello!')

# Get your Discord bot token from Render's environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Keep the bot alive with the web server
keep_alive()

# Run the bot
bot.run(TOKEN)
