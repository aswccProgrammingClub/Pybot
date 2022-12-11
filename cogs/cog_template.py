from discord.ext import commands

class YourClassName(commands.Cog):
    #executes whenclass is initialized
    def __init__(self, bot):
        self.bot = bot

    #executes when cog has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
       await print("MyClassName Ready")

    #send $hello_world in a private message to bot to call method
    @commands.command()
    async def hello_world(self, ctx):
        await print("Hello, world!")

#called when this file is passed to load_extenction
async def setup(bot):
    await bot.add_cog(YourClassName(bot))        
          
     
