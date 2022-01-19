from createCon import createConn

def getReplayAdventures():
    conexion =createConn()
    cursor =conexion.cursor()
    cursor.execute("SELECT GAME.ID_USER, Us.username, GAME.ID_ADVENTURE, Ad.adventure_name, GAME.ID_CHARACTER, Ch.character_name FROM GAME "
                   "JOIN ADVENTURE Ad ON GAME.ID_ADVENTURE = Ad.ID_ADVENTURE "
                   "JOIN USER Us ON Us.ID_USER = GAME.ID_USER "
                   "JOIN CHARACTER Ch ON Ch.ID_CHARACTER = GAME.ID_CHARACTER;")
    resReplay = cursor.fetchall()
    # Proceso de desconexión, en el fallo de la query de debajo
    # se comprueba que la connexión no esta hecha
    if conexion.is_connected():
        conexion.disconnect()
    # cursor.execute("SELECT * FROM ADVENTURE")
    # res2 =cursor.fetchall()

    return res2

print(getReplayAdventures())