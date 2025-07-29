DB = "ovl.db"

def get_info_for_nummerplaat(nummerplaat):
    
    import util
    import sqlite3
    
    nummerplaat_stripped = util.strip_spaces_and_hyphens(nummerplaat)
    connection = sqlite3.connect(DB)
    cursor = connection.cursor()
    sql_query = """
    SELECT info FROM nummerplaten
    WHERE lower(replace(replace(nummerplaat, ' ', ''), '-', '')) = lower(?)
    """

    cursor.execute(sql_query, 
                   (nummerplaat_stripped,))
    result = cursor.fetchone()

    connection.close()

    if result:
        return str(result[0])
    else:
        return "De nummerplaat is niet beschikbaar"
