

def structure (names, goals, goals_avoided, assists):

   return list(zip(names,goals,goals_avoided,assists)) #me arma la lista con las estructuras que ya tenia 



def max_player (players):

   max_p = max(players, key=lambda x: x[1])

   return max_p[0], max_p[1] #retorna nombre y cantidad de goles