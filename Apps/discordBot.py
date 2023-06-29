"""
Step 1: Set up a Discord Bot Application

Go to the Discord Developer Portal (https://discord.com/developers/applications) and create a new application.
Navigate to the "Bot" tab on the left-hand side and click on "Add Bot" to create a bot user for your application.
Note down the "Token" for your bot; you'll need it later to authenticate the bot with the Discord server.
Step 2: Install the Required Libraries

Open your terminal or command prompt.
Install the discord.py library by running the following command:
Copy code
pip install discord.py
Step 3: Write the Bot Code

Create a new Python file (e.g., discord_bot.py) and open it in a code editor.

Import the necessary modules:

"""

import discord
from discord.ext import commands


#Create an instance of the bot:


bot = commands.Bot(command_prefix="!")


#Define an event handler for the bot's on_ready event:

@bot.event
async def on_ready():
    print(f"Bot is connected as {bot.user}")


#Define a command for the bot:

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I'm your Discord bot!")


#Add the bot token at the end of the file:

bot.run("YOUR_BOT_TOKEN")

#Step 4: Run the Bot

#Replace "YOUR_BOT_TOKEN" with the token you obtained in Step 1.
#Save the file and run it in your terminal using the command:

python discord_bot.py

#Step 5: Add the Bot to a Discord Server
"""
Go back to the Discord Developer Portal.
Navigate to the "OAuth2" tab on the left-hand side.
Under "Scopes," select "bot" and under "Bot Permissions," choose the required permissions for your bot.
Copy the generated OAuth2 URL and open it in a web browser.
Select a Discord server where you have the necessary permissions and authorize the bot to join the server.
Your Discord bot should now be up and running. It will respond to the "!hello" command with a greeting message. You can extend the bot's functionality by adding more commands and event handlers to suit your needs."""
