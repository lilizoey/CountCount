
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
    
    return sql.execute("SELECT Count_i from Count_Data where User_ID = ?", (user_id,)).fetchall()