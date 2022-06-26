
import pandas as pd
import numpy as np

data = pd.read_csv('baseball_games.csv')


#1. На какую игру пришло максимальное количество зрителей за весь сезон игр?
max__attendance = pd.DataFrame(data[data['attendance']==data['attendance'].max()],  columns=["attendance", "date", "away_team", "home_team" ])
print ("1. На какую игру пришло максимальное количество зрителей за весь сезон игр?", end='\n')
print (max__attendance)

#2. Какая игра была самая холодная (temperature) за весь сезон?
min_temperature = pd.DataFrame(data[data['temperature']==data['temperature'].min()],  columns=["temperature", "date", "away_team", "home_team" ])
print ("2. Какая игра была самая холодная (temperature) за весь сезон?", end='\n')
print (min_temperature)

#3. Какая игра была самая теплая за весь сезон?
max_temperature = pd.DataFrame(data[data['temperature']==data['temperature'].max()],  columns=["temperature", "date", "away_team", "home_team" ])
print ("3. Какая игра была самая теплая за весь сезон?", end='\n')
print (max_temperature)

#4. Какая игра в сезоне была самая долгая по продолжительности матча?
max_game_hours_dec = pd.DataFrame(data[data['game_hours_dec']==data['game_hours_dec'].max()],  columns=["game_hours_dec", "date", "away_team", "home_team" ])
print ("4. Какая игра в сезоне была самая долгая по продолжительности матча?", end='\n')
print (max_game_hours_dec)

#5. Какая игра в сезоне была самая короткая по продолжительности матча?
min_game_hours_dec = pd.DataFrame(data[data['game_hours_dec']==data['game_hours_dec'].min()],  columns=["game_hours_dec", "date", "away_team", "home_team" ])
print ("5. Какая игра в сезоне была самая короткая по продолжительности матча?", end='\n')
print (min_game_hours_dec)

#6. Сколько матчей в сезоне закончилось ничьей?
data['compare']= pd.DataFrame (data['home_team_loss'] == data['home_team_win'])
print ("6. Сколько матчей в сезоне закончилось ничьей?", end='\n')
print (data['compare'].value_counts())
#tie_game = pd.DataFrame (data['home_team_loss'], data['home_team_win'])

#7. Какая игра была последней в сезоне?
games = pd.read_csv('baseball_games.csv')
games['date'] = pd.to_datetime(data['date'])
print ("#7. Какая игра была последней в сезоне?", end='\n')
print (games[games['date']==games['date'].dt.date.max()])

#8. У какой игры было минимальное количество зрителей?
min__attendance = pd.DataFrame(data[data['attendance']==data['attendance'].min()],  columns=["attendance", "date", "away_team", "home_team" ])
print ("8. У какой игры было минимальное количество зрителей?", end='\n')
print (min__attendance)

#9. Какая игра в сезоне была самая ветренная?
max_wind_speed = pd.DataFrame(data[data['wind_speed']==data['wind_speed'].max()],  columns=["wind_speed", "date", "away_team", "home_team" ])
print ("9. Какая игра в сезоне была самая ветренная?", end='\n')
print (max_wind_speed)

#10. В какой игре получили максимальное количество очков?
#max_value = pd.DataFrame((data['away_team_hits'] + data['home_team_runs']).value_counts())
#print ("10. В какой игре получили максимальное количество очков?", end='\n')
#print (max_value.max())

#11. Какая игра содержала максимальное количество ошибок домашней команды?
max_errors = pd.DataFrame(data[data['home_team_errors']==data['home_team_errors'].max()],  columns=["home_team_errors", "date", "away_team", "home_team" ])
print ("11. Какая игра содержала максимальное количество ошибок домашней команды?", end='\n')
print (max_errors)

#12. В какой игре было максимальное количество ранов?
max_total_runs = pd.DataFrame(data[data['total_runs']==data['total_runs'].max()],  columns=["total_runs", "date", "away_team", "home_team" ])
print ("#12. В какой игре было максимальное количество ранов?", end='\n')
print (max_total_runs)

#13. Выведите количество игр которая сыграла каждая команда в данном сезоне?
count_game_teams = data['away_team'].value_counts() + data['home_team'].value_counts()
print ("#13. Выведите количество игр которая сыграла каждая команда в данном сезоне?", end='\n')
print (count_game_teams)

#14. Какая команда выиграла наибольшое количество матчей в сезоне?
reg_season = data[data['season']=='regular season']
reg_wins = pd.DataFrame(reg_season[reg_season['home_team_runs'] > reg_season['away_team_runs']]['home_team'].value_counts() + reg_season[reg_season['home_team_runs'] < reg_season['away_team_runs']]['away_team'].value_counts())
reg_wins.set_axis(['wins'],axis='columns',inplace=True)
reg_wins.index.name = 'team'
print ("14. Какая команда выиграла наибольшое количество матчей в сезоне?", end='\n')
print (reg_wins.sort_values(by='wins',ascending=False).head(1))

#15. Какая команда выиграла наибольшее количество домашних матчей в сезоне?
reg_season = data[data['season']=='regular season']
reg_wins_home = pd.DataFrame(reg_season[reg_season['home_team_win'] >0].value_counts())
reg_wins_home.set_axis(['wins'],axis='columns',inplace=True)
reg_wins.index.name = 'team'
print ("15. Какая команда выиграла наибольшее количество домашних матчей в сезоне?", end='\n')
print (reg_wins_home.sort_values(by='wins',ascending=False).head(1))




