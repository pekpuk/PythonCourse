players = ["Ваня", "Петя", "Андрей", "Семен", "Степа", "Ярик"]
count = len(players)
print("Игроков всего", count)
# Если игроков нечетное количество, в первой команде будет игроков больше
team_slicing = round(count/2)
print("Первая команда", players[0:team_slicing])
print("Вторая команда", players[team_slicing:count])
