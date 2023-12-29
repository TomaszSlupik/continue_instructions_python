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
    if gam [1] == 'USD':
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

# 
maze = [
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'W'],
    ['W', 'E', 'W', 'E', 'W', 'E', 'W', 'W', 'E', 'W'],
    ['W', 'E', 'W', 'E', 'E', 'E', 'W', 'E', 'E', 'W'],
    ['W', 'E', 'W', 'E', 'W', 'E', 'W', 'E', 'W', 'W'],
    ['W', 'E', 'E', 'E', 'W', 'E', 'W', 'E', 'E', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
]