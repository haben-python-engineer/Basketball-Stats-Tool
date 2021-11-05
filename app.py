import constants
import copy

DATA_BASE = [player for player in copy.deepcopy(constants.PLAYERS)]
bandits = []
panthers  = []
warriors  = []


#Converts player's height to True/False statements and
#Removes 'and' in player's guardians and replaces them with commas
def clean_data():
    for player in DATA_BASE.copy():
        player['height'] = int(player['height'][:2])
        player['guardians'] = player['guardians'].split('and')
        player['guardians'] = ', '.join(player['guardians'])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False


#Gathers an equal amount of experienced and inexperienced
#Players and stores them in any team desired
def balance(team, data):
    experienced = []
    inexperienced = []
    for player in data.copy():
        if len(team) < 6:
            if player['experience'] and len(experienced) < 3:
                experienced.append(player)
                data.remove(player)
            elif not player['experience'] and len(inexperienced) < 3:
                inexperienced.append(player)
                data.remove(player)
    team.extend(experienced)
    team.extend(inexperienced)



#Takes team name and data and displays key stats like total experienced players,
#Total inexperienced players, players average height, players and their guardians name
def roster_info_for(team_name, team_data):
    print(f'\nTeam: {team_name}')
    print('_'*14)
    experience = [value['experience'] for key, value in enumerate(team_data)]
    height_average = sum([value['height'] for key, value in enumerate(team_data)]) / len(team_data)
    print(f'Total experienced: {experience.count(True)}')
    print(f'Total inexperienced: {experience.count(False)}')
    print(f'Average height: {format(height_average, ".1f")}\n')
    players_names = [player['name'] for player in team_data]
    players_names = ', '.join(players_names)
    print(f'Players on Team: \n {players_names}\n')
    guardians_names = [player['guardians'] for player in team_data]
    guardians_names = ', '.join(guardians_names)
    print(f'Guardians: \n {guardians_names}')


if __name__ == "__main__":
    clean_data()
    balance(panthers, DATA_BASE)
    balance(bandits, DATA_BASE)
    balance(warriors, DATA_BASE)

    print(DATA_BASE)
    print(constants.PLAYERS)

    while True:
        print("""
        BASKETBALL TEAM STATS TOOL \n
            _____Menu_____ \n
        Here are your menu options:
        (A). Display Team Stats
        (B). Quit
        """)

        try:
            chosen_option = input('Select one of the two menu options above: ').upper()
            if chosen_option.isnumeric() or chosen_option not in ['A', 'B']:
                raise ValueError(f' ---> {chosen_option} <--- is not one of the valid values of either A or B')
            if chosen_option == 'A':
                print('(A). Panthers\n(B). Bandits\n(C). Warriors\n')
                chosen_team = input('Select one of the 3 teams available above: ').upper()
                if chosen_team.isnumeric() or chosen_team not in ['A', 'B', 'C']:
                    raise ValueError(f' ---> {chosen_team} <--- is not one of the valid values of either A, B, or C')
                if chosen_team == 'A':
                    roster_info_for('Panthers', panthers)
                elif chosen_team == 'B':
                    roster_info_for('Bandits', bandits)
                elif chosen_team == 'C':
                    roster_info_for('Warriors', warriors)
            elif chosen_option == 'B':
                break
            continue_using_stats_tool = input('\nPress ENTER to continue...' )
            if continue_using_stats_tool == '':
                continue
        except ValueError as e:
            print('_' * 88)
            print(f'Oh no ran into an error! ({e})')
            print('_' * 88)
