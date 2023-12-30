# Instrukcja continue jest używana w pętlach (takich jak for lub while)
# do przejścia do następnej iteracji pętli bez wykonania pozostałego kodu w bieżącej iteracji.
# Gdy interpreter Pythona napotka continue, przeskakuje on pozostały kod w bieżącej iteracji pętli
# i przechodzi do następnej iteracji.

# nalezy zmienić ceny zamknięcia wyrażone w USD na ceny wyrażone w PLN. Przyjmij kurs USDPLN = 4.0.
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

for gam in gaming.values():
    if gam[1] == 'USD':
        gam[0] *= 4.0
        gam[1] = 'PLN'
        continue
print(gaming)

print('---')

names = ['Jack', 'Leon', 'Alice', None, 'Bob']

for name in names:
    if isinstance(name, str):
        print(name)
        continue


print('---')

# Potrzebujesz wydrukować tekst każdego posta z pominięciem postów, które mają mniej niż 50 polubień.
posts = [
    {
        'text': 'Lorem ipsum dolor sit amet, consectetur elit.',
        'author': 'John',
        'likes': 32,
    },
    {
        'text': 'Nulla facilisi. Duis eu aliquam libero.',
        'author': 'Jane',
        'likes': 87,
    },
    {
        'text': 'Vestibulum at ipsum ac diam sollicitudin tempor.',
        'author': 'Bob',
        'likes': 113,
    },
    {
        'text': 'Curabitur lobortis luctus velit, et scelerisque eu.',
        'author': 'Alice',
        'likes': 24,
    },
    {
        'text': 'Suspendisse nec enim rutrum, vehicula lectus ut.',
        'author': 'Mike',
        'likes': 99,
    },
]

for post in posts:
    if post['likes'] > 50:
        print(post['text'])
        continue

print('---')

# Labirynt składa się ze ścian - oznaczonych literą 'W' i pustych przestrzeni - oznaczonych literą 'E'
# Wydrukuj indeksy pustych przestrzeni - litera E
maze = [
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'W'],
    ['W', 'E', 'W', 'E', 'W', 'E', 'W', 'W', 'E', 'W'],
    ['W', 'E', 'W', 'E', 'E', 'E', 'W', 'E', 'E', 'W'],
    ['W', 'E', 'W', 'E', 'W', 'E', 'W', 'E', 'W', 'W'],
    ['W', 'E', 'E', 'E', 'W', 'E', 'W', 'E', 'E', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
]

index_pairs = []

for i, row in enumerate(maze):
    for j, cell in enumerate(row):
        if cell == 'E':
            index_pairs.append([i, j])
            continue

print(index_pairs)

print('---')

# Potrzebujesz obliczyć całkowity czas trwania połączeń wykonanych przez określonego rozmówcę
# - użytkownika o imieniu 'John', pomijając połączenia trwające krócej niż 1 minutę (60 sekund).
call_records = [
    {
        'name': 'John',
        'phone': '123456789',
        'duration': 30,
        'cost': 5.0,
    },
    {
        'name': 'Jane',
        'phone': '234567890',
        'duration': 90,
        'cost': 10.0,
    },
    {
        'name': 'John',
        'phone': '345678901',
        'duration': 120,
        'cost': 15.0,
    },
    {
        'name': 'Alice',
        'phone': '456789012',
        'duration': 45,
        'cost': 7.5,
    },
    {
        'name': 'John',
        'phone': '567890123',
        'duration': 75,
        'cost': 9.0,
    },
]

john_call = []

for john in call_records:
    if john['name'] == 'John':
        if john['duration'] > 60:
            john_call.append(john['duration'])
            continue

print(f"Total call duration for John, {sum(john_call)} seconds")

print('---')

# Potrzebujesz wydrukować nazwy wszystkich nieukończonych zadań
# (pomijając zadania, które zostały już zakończone)

construction_tasks = [
    {
        'name': 'Foundation',
        'description': 'Excavate and pour concrete',
        'completed': True,
    },
    {
        'name': 'Framing',
        'description': 'Frame the walls, roof, and floors',
        'completed': False,
    },
    {
        'name': 'Plumbing',
        'description': 'Install the plumbing and fixtures',
        'completed': False,
    },
    {
        'name': 'Electrical',
        'description': 'Install the electrical wiring and outlets',
        'completed': True,
    },
    {
        'name': 'Drywall',
        'description': 'Install drywall on the walls and ceilings',
        'completed': False,
    },
]

no_completed = []

for task in construction_tasks:
    if task['completed'] == False:
        no_completed.append(task['name'])
        continue
for task in no_completed:
    print(f"{task} is incomplete")
