import discord
from discord.ext import commands
import os.path
import json

class Profile(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Profile extension loaded')
        print('------')

    @commands.command()
    async def profile(self, ctx):
        await ctx.send("test profile")

    @commands.command()
    async def newCharacter(self, message, *args):
        dataDir = "Data/"
        author = str(message.author.id)
        server = str(message.guild.id)
        charName = ""
        serverDir = dataDir+server+"/"
        authorDir = serverDir+author+".json"

        #for arg in args:
            #charName = charName + " " + arg
        #print(charName)
        charName = args[0]

        if os.path.isfile(authorDir):
            print("User exists, proceeding to open JSON file of user "+author)
            
            #with open(authorDir, 'r') as f:
            #    dataList = [json.loads(line[7:]) for line in f]

            #for row in table:
            #    print(row)
            with open(authorDir) as json_file:

                data = json.load(json_file)
            print(data)

        else:
            print("User does not exist, proceeding to create JSON file for user "+author)
            
            charData = {
            charName: {
                "Level": 1
                }
            }
            #print(charData)

            if not os.path.exists(os.path.dirname(serverDir)):
                try:
                    print("Server does not exist, proceeding to create folder for server "+server)
                    
                    os.makedirs(os.path.dirname(serverDir))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            f = open(authorDir, "w")
            f.write(json.dumps(charData))
            f.close()
            
            print("------")


def setup(bot):
    bot.add_cog(Profile(bot))