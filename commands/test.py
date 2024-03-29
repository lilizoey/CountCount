"""
    Count-Count is a discord bot that gathers and displays statistics for users.
    Copyright (C) 2019 sayaks
    Copyright (C) 2019 Zylon

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from bot import bot
from database import queries

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {bot.latency}")

@bot.command()
async def get(ctx):
    await ctx.send(queries.get_all_counts(ctx.message.author.id))

@bot.command()
async def count(ctx):
    queries.count(ctx.message.author.id)