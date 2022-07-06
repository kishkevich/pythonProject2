
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
#reg_season = data[data['season']=='regular season']
#reg_wins_home = pd.DataFrame(reg_season[reg_season['home_team_win'] >0].value_counts(), columns=["total_runs", "date", "away_team", "home_team" ])
#reg_wins_home.set_axis(['wins'],axis='columns',inplace=True)
#reg_wins.index.name = 'team'
#print ("15. Какая команда выиграла наибольшее количество домашних матчей в сезоне?", end='\n')
#print (reg_wins_home.sort_values(by='wins',ascending=False).head(1))

#16. Какая команда выиграла наибольшее количество гостевых матчей в сезоне?
season_games = games.drop(games[games.season == 'post season'].index).reset_index().drop(columns=['index'])
home_team_wins = pd.pivot_table( season_games, index='home_team', values='home_team_win', aggfunc=np.sum)
win_loss_games = season_games.drop(season_games[(season_games['home_team_loss'] == 0)
                                                & (season_games['home_team_win'] == 0)].index)
away_team_wins = pd.pivot_table( win_loss_games, index='away_team', values='home_team_loss', aggfunc=np.sum)
team_wins = home_team_wins['home_team_win'] + away_team_wins['home_team_loss']
team_wins.idxmax()
print ("16. Какая команда выиграла наибольшее количество гостевых матчей в сезоне?", end='\n')
print (away_team_wins['home_team_loss'].idxmax())

#17. Какая команда проиграла наибольшее количество матчей в сезоне?
home_team_loss = pd.pivot_table( win_loss_games, index='home_team', values='home_team_loss', aggfunc=np.sum)
away_team_loss = pd.pivot_table( season_games, index='away_team', values='home_team_win', aggfunc=np.sum)
team_loss = home_team_loss['home_team_loss'] + away_team_loss['home_team_win']
print ("#17. Какая команда проиграла наибольшее количество матчей в сезоне?", end='\n')
print (team_loss.idxmax())

#18. Зависит ли выигрыш от количества посетителей матча?
print ("18. Зависит ли выигрыш от количества посетителей матча?", end='\n')
if abs(season_games.corr()['attendance']['home_team_win']) > 0.1: #abs возвращает абсолютное значение
    print("Есть некоторая зависимость!")
else:
    print("нет")

#19. Правда ли что большинство проигрышных домашних матчей приходятся на Субботу и Воскресенье?
print ("19. Правда ли что большинство проигрышных домашних матчей приходятся на Субботу и Воскресенье?", end='\n')
day_home_loss = pd.pivot_table( win_loss_games, index='day_of_week', values='home_team_loss', aggfunc=np.sum)
weekend_loss_number = day_home_loss['home_team_loss']['Sunday'] + day_home_loss['home_team_loss']['Saturday']
if weekend_loss_number > (day_home_loss.sum()['home_team_loss'] - weekend_loss_number):
    print("Большинство домашних проигрышей происходят по выходным!")
else:
    print("Большинство домашних проигрышей происходят по будням!")

#20. Правда ли что наибольшее количество ранов происходит в холодную погоду?
print ("20. Правда ли что наибольшее количество ранов происходит в холодную погоду?", end='\n')
season_games['cold_weather'] = season_games.apply(lambda row: (1,0)[(row['temperature'] - 32) * 5 / 9 < 0], axis=1)
temperature_runs = pd.pivot_table(season_games, index='cold_weather', values='total_runs', aggfunc=np.sum)
if temperature_runs['total_runs'][0] > temperature_runs['total_runs'][1]:
    print("Большинство ранов произошло в холодную погоду!")
else:
    print("Большинство ранов произошло в теплую погоду!")