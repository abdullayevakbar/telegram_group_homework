from read_data import read_data


def find_all_users_id(data: dict) -> list:
    """ 
    This function will find all the users in the json file and return the list of users id

    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    all = []
    for i in data['messages']:
        x = i.get("from_id")
        if (x and (x not in all)):
            all.append(i["from_id"])

    return all
