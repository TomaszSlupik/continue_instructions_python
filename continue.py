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
    