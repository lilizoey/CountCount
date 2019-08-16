from bot import bot

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {bot.latency}")
