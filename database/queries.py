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

import sqlite3
conn = sqlite3.connect("database.sqlite3")
c = conn.cursor()

def initialize_counts():
    c.execute("""
    CREATE TABLE IF NOT EXISTS Count_Data (
        count_i Integer PRIMARY KEY AUTOINCREMENT,
        user_id Integer NOT NULL
    )
    """)
    conn.commit()

def get_all_counts(user_id):
    """
    Gets all the counts that the given user has made using the bot.

    Parameters
    ----------
    user_id : int
        The id of the user

    Returns
    -------
    List[int]
        A list of all the counts that the user has made
    """

    return [t[0] for t in c.execute("SELECT Count_i from Count_Data where User_ID = ?", (user_id,)).fetchall()]

def count(user_id):
    c.execute("INSERT INTO Count_Data (user_id) VALUES (?)", (user_id,))
    conn.commit()