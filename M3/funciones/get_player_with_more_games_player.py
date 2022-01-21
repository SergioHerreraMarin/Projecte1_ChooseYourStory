from createCon import createConn
from getFormatedReports import getFormatedReports

def get_player_with_more_games_played():

    conexion = createConn()
    cursor = conexion.cursor()
    cursor.execute("select u.username, count(e.ID_USER) as 'num_partidas' from USER u inner join GAME e on u.ID_USER = e.ID_USER group by e.ID_USER order by num_partidas desc limit 1;")

    resultado = cursor.fetchall()

    return getFormatedReports(resultado, 120, ("NOMBRE USUARIO", "PERTIDAS JUGADAS"), (30))

print(get_player_with_more_games_played())