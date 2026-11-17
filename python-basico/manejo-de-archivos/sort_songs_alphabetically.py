
with open('canciones.txt', 'r', encoding='utf-8') as file:
    songs = []

    for line in file:
        song = line.strip()

        if song != '':
            songs.append(song)

songs.sort()

with open('canciones_ordenadas.txt', 'w', encoding='utf-8') as file:
    for song in songs:
        file.write(song + '\n')

print('Las canciones se guardaron en canciones_ordenadas.txt')
