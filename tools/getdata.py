from configuration import db, collection

def dialogue(char):
    """
    Function that returns all the quotes from a certain character
    """
    proj = {"_id": 0}
    query = {"character_name": f"{char}"}
    quotes = list(collection.find(query,proj))
    return quotes

def quotes():
    """
    Function that returns all quotes 
    """
    query = {}
    quotes = list(collection.find(query,{"_id": 0}))
    return quotes

def scene_(scene):
    """
    Function that let you find the performance of certain scene
    """
    proj = {"_id": 0}
    query = {"scene": f"{scene}"}
    quotes = list(collection.find(query,proj))
    return quotes





