import pdb
game_dictionary = {
    'home': {
        'team_name': 'Brooklyn Nets',
        'colors': ['Black', 'White'],
        'players': {'Alan Anderson' : {'number': 0, 'shoe': 16, 'points': 22, 'rebounds': 12,
                                    'assists': 12, 'steals':3, 'blocks':1, 'slam_dunks':1},
                    'Reggie Evans' : {'number': 30, 'shoe': 14, 'points': 12, 'rebounds': 12,
                                    'assists': 12, 'steals':12, 'blocks':12, 'slam_dunks':7},
                    'Brook Lopez' : {'number': 11, 'shoe': 17, 'points': 17, 'rebounds': 19,
                                    'assists': 10, 'steals':3, 'blocks':1, 'slam_dunks':15},
                    'Mason Plumlee' : {'number': 1, 'shoe': 19, 'points': 26, 'rebounds': 12,
                                    'assists': 6, 'steals':3, 'blocks':8, 'slam_dunks':5},
                    'Jason Terry' : {'number': 31, 'shoe': 15, 'points': 19, 'rebounds': 2,
                                    'assists': 2, 'steals':4, 'blocks':11, 'slam_dunks':1}
                    }
                },
    'away': {
        'team_name': 'Charlotte Hornets',
        'colors': ['Turquoise', 'Purple'],
        'players': {
                   'Jeff Adrien': {'number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1,
                                   'assists': 1, 'steals': 2, 'blocks': 7, 'slam dunks': 2},
                   'Bismack Biyombo': {'number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4,
                                   'assists': 7, 'steals': 7, 'blocks': 15, 'slam dunks': 10},
                   'DeSagna Diop':{'number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12,
                                   'assists': 12, 'steals': 4, 'blocks': 5, 'slam dunks': 5},
                   'Ben Gordon':{'number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3,
                                   'assists': 2, 'steals': 1, 'blocks': 1, 'slam dunks': 0},
                   'Brendan Haywood':{'number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12,
                                   'assists': 12, 'steals': 22, 'blocks': 5, 'slam dunks': 12}
                       }
            }
}
def game_dict():
    return game_dictionary

def home_team_name():
  return game_dict()['home']['team_name']

def full_roster():
    all_players = {}
    for location, team_stat in game_dict().items():
        all_players.update(team_stat['players'])
        #pdb.set_trace()
    return all_players
#print(full_roster())

def player_stats(player):
    roster = full_roster()
    return roster[player]
#print(player_stats('Jeff Adrien'))

def num_points_scored(player):
    stats = player_stats(player)
    return stats['points']
#print (num_points_scored('Ben Gordon'))


def shoe_size(player):
    stats = player_stats(player)
    return stats['shoe']

def team_colors(team):
    for location, team_stat in game_dict().items():
        if team_stat['team_name'] == team:
            return team_stat['colors']
#print(team_colors('Brooklyn Nets'))
def team_names():
    teams= []
    for location, team_stat in game_dict().items():
        teams.append(team_stat['team_name'])
    return teams
#print(team_names())

def player_numbers(team):
#iterate through team and send player into player_stat function to get numbers
   team_num = []
   for location, team_stat in game_dict().items():
       if team_stat['team_name'] == team:
           for person in team_stat['players']:
               team_num.append(player_stats(person)['number'])
   return team_num
#print(player_numbers('Charlotte Hornets'))

def player_shoe():
    player_shoe = []
    biggest = (0, 0)
    for i in full_roster():
        data = {i: shoe_size(i)}
        player_shoe.append(data)
        if shoe_size(i) > biggest[0]:
            biggest = (shoe_size(i), full_roster()[i]['rebounds'])
    return biggest[1]
#print(player_shoe())

# def most_points_scored():
#     home_points = [player['points'] for player in game_dictionary().items()['home']['players']]
#     return home_points
# print(most_points_scored())

def team_points(team):
#iterate through team and send player into player_stat function to get numbers
   team_pts = []
   for location, team_stat in game_dict().items():
       if team_stat['team_name'] == team:
           for person in team_stat['players']:
               team_pts.append(player_stats(person)['points'])
print (team_points('Charlotte Hornets'))

# def winning_team():
#     home_points = []
#     pdb.set_trace()
#     for i in game_dict.items():
#         home_points.append(['home']['players']i)
#         return home_points
#winning_team()


# def all_players():
#     roster_names = [i for i in full_roster()]
#     roster_points = [i['points'] for i in full_roster()]



#print(all_players())
