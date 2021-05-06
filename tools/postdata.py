from configuration import collection

def insert_quote(scene, characters_name, dialog):
    """
    Function that inserts a quote, a character name and a dialog
    """
    dic = {
        "scene": scene,
        "character_name": character_name,
        "dialogue": dialog,
    }
    insert = collection.insert_one(dic)

