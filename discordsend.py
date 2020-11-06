# from discord.ext.commands import Bot
# from discord import Embed
# from cogs.reply import Reply
# import os
# from dotenv import load_dotenv

# load_dotenv()

# TOKEN = os.getenv('DISCORD_TOKEN')
# client = Bot(command_prefix="!")

# client.remove_command('help')
# client.add_cog(Reply(client))

from discord_webhook import DiscordWebhook
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/oop", methods=["POST"])
def index():
    hi = request.form["data"]
    webhook = DiscordWebhook(
        url="https://discord.com/api/webhooks/774106283355013162/T2d0pI6yGyrjABVRPLTlcO2guhnBv9mfqqjbxsHDSf3Jd5eDnQMiLES8jprHvMMOYDwP",
        content=hi,
    )
    response = webhook.execute()
    return "Server Works!"


app.run("localhost", 9005)

# @client.command()
# async def help(ctx):
# 	await ctx.message.channel.send('!change :emoji: to change react emoji \n!r reaction_name to send reaction e.g. !r shrug \n!set reaction_name and attach a .jpeg/.jpg/.png/.gif to set reaction \n!all_reactions to list all reactions \n+poll {question} [option1] [option2] [etc] for poll \n:x: react to message to delete with notif \n:pushpin: react to message to pin it, unreact to unpin \n:closed_book: status to set description')


#     # embed = Embed(color=0x45884)
#     # embed.add_field(name="The Reply Bot", value="\u200b")
#     # embed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/email-2-2/32/Reply-all-Email-512.png")
#     # embed.add_field(name="Description:", value="A bot that adds reply functionality to Discord")
#     # embed.add_field(name="Usage:", value="To reply to a message simply react to a message with ✉ and write your response")
#     # await ctx.message.channel.send(embed=embed)

# client.run(TOKEN)
