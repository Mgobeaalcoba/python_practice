def run():
    numbers = [1,2,3,4,5]
    # Me voy a quedar solo con los pares a traves de filter. 
    print(numbers)
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    print(even_numbers)
    print(numbers)

    matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

    print(matches)
    print(len(matches))

    new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

    print(new_list)
    print(len(new_list))

    print(matches)
    print(len(matches))

if __name__ == '__main__':
    run()
    # Filter: función python para filtrar sobre una lista y retornar otra
    # Con filter no tenemos el problema en memorio que teniamos con map
    # Por lo que no necesitamos hacer un copy() para resolverlo. 