

def structure (players, names, goals, goals_avoided, assists):

    for name, goal, gol_av, assi in zip(names,goals,goals_avoided,assists):

        player = {"name": name, "goals": goal, "goals avoided": gol_av, "assists": assi}
        players.append(player)

    return players
    

def recorrer (players):

    for player in players:

        print (player["name"], player["goals"], player["goals avoided"], player["assists"])
      