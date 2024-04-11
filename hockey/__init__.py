

def structure (names, goals, goals_avoided, assists):

   """ 
   genero mi nueva estructura, con los datos de las 4 estructuras que dispongo hago un zip para crear una lista de tuplas.

   """

   return list(zip(names,goals,goals_avoided,assists)) #me arma la lista con las estructuras que ya tenia 



def max_player (players):

   """ 
   utilizo la función max que me ayudará a buscar un máximo entre todos los goles, le indico con [1] a donde se tiene que dirigir para calcular el max
   o sea, a los goles.

   """

   max_p = max(players, key=lambda x: x[1])

   return max_p[0], max_p[1] #retorna nombre y cantidad de goles


def most_inf (players):

   """
   busco al jugador mas influyente utilizando max+lambda para buscar el maximo puntaje que lo obtendre calculando goles + goles evitados + asistencias
   y multiplicandolo por sus respectivos valores/puntajes. 

   """

   return max(players, key= lambda x: x[1]*1.5+ x[2]*1.25+ x[3])


def prom_games (players, plays):

   """"
   utilizo sum + map + lambda para que sume todos los elementos (goles) iterando sobre cada jugador indicandole con lambda que dato tiene que utilizar [1]

   """

   total = sum(map(lambda x: x[1], players))

   return total/plays


def prom_player (goals, plays):

   """ 
   calculo de promedio = total/cantidad 

   """
      
   return goals/plays

