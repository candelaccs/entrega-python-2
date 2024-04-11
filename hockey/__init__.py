

def structure (names, goals, goals_avoided, assists):

   return list(zip(names,goals,goals_avoided,assists)) #me arma la lista con las estructuras que ya tenia 



def max_player (players):

   max_p = max(players, key=lambda x: x[1])

   return max_p[0], max_p[1] #retorna nombre y cantidad de goles

def most_inf (players):
   
   inf_player =  max(list, key= lambda x: x[1]*1.5+ x[2]*1.25+ x[3])

   return (inf_player)