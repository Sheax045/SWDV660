# Please add write your fight_song program in this file.
def goTeamGo ():
    print ('Go, team, go!')
    print ('Defeat your foe.')
    
def SimTheBest ():
    print ('Simply the best,')
    print ('Better than the rest.')
    
def goTeamTheBest ():
    goTeamGo ()
    SimTheBest ()
    goTeamGo ()
    print ('')

goTeamGo ()
print ('')

for index in range (2):
    goTeamTheBest ()
    
goTeamGo ()