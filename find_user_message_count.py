from read_data import read_data
from find_all_users_id import find_all_users_id


def find_user_message_count(data: dict, users_id: str) -> dict:
    """
    This function will find the user's message count.

    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    mp = {}
    for i in users_id:
        for k in data["messages"]:
            if k.get("from_id") and k.get("from_id") == i:
                if mp.get(i):
                    mp[i] = mp[i]+1
                else:
                    mp[i] = 1
            if k.get("actor_id") and k.get("actor_id") == i:
                if mp.get(i):
                    mp[i] = mp[i]+1
                else:
                    mp[i] = 1

    return mp
