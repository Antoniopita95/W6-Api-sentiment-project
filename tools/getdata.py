from config.configuration import db, collection

def dialog(char):
    """
    Function that returns all the quotes of a certain character
    """
    proj = {"_id": 0, "index": 0}
    query = {"char": f"{char}"}
    quotes = list(collection.find(query,proj))
    return quotes

def quotes_movie(movie):
    """
    Function that returns all the quotes of one of the three movies
    """
    proj = {"_id": 0, "index": 0}
    query = {"movie": f"{movie}"}
    quotes = list(collection.find(query,proj))
    return quotes
