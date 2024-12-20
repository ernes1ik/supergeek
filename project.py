## project_5

# Представим, что некое приложение хранит плейлист песен в двух видах:
#   * многострочная строка
#   * кортеж из двух словарей
# Каждая песня содержит: название и время звучания.

# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

# В результате решением задачи является функция, которая:
#   * может принимать как первый плейлист, так и второй в качестве аргумента
#   * принимает параметр n, число. Это количество песен
#   * возвращает время звучания, как объект времени timedelta, либо строку, либо вещественное число
# При этом функций в задаче может быть несколько. То есть решение можно разбить на несколько функций.
# Но результат задачи можно получить вызвав одну функцию!
# get_duration(playlist: Iterable, n: int) -> Any

playlist_e = """
Sunday 5.09
Why Does My Heart Feel so Bad? 4.23
Everlong 3.25
To Let Myself Go 4.09
Golden 2.56
Daisuke 2.41
Miami 3.31
Chill Bill Lofi 2.05
The Perfect Girl 1.48
Resonance 3.32
"""


playlist_f = (
    {"Free Bird": 9.08, "Enter Sandman": 5.31, "One" : 7.45, "Sliver" : 2.10, "Come as You Are": 3.45},
    {"Thunderstruck": 4.53, "You Shook Me All Night Long": 3.29, "Everlong" : 4.51, "My Hero" : 4.02},
)

import random
from datetime import timedelta
from typing import Any, Iterable

def parse_playlist_string(playlist: str) -> dict:
    songs = {}
    for line in playlist.strip().split('\n'):
        parts = line.rsplit(' ', 1)
        if len(parts) == 2:
            title, duration = parts
            try:
                if '.' in duration:
                    total_minutes = float(duration)
                else:
                    minutes, seconds = map(int, duration.split(':'))
                    total_minutes = minutes + seconds / 60.0
                songs[title] = total_minutes
            except ValueError:
                print(f"Ошибка в формате длительности для '{title}': '{duration}'")
                continue
    return songs
    
def parse_playlist_tuple(playlist: tuple) -> dict:
    songs = {}
    for song_dict in playlist:
        songs.update(song_dict)
    return songs

def get_duration(playlist: Iterable, n: int) -> Any:
    if isinstance(playlist, str):
        songs_dict = parse_playlist_string(playlist)
    elif isinstance(playlist, tuple):
        songs_dict = parse_playlist_tuple(playlist)
    else:
        raise ValueError("Unsupported playlist format")
def get_duration(playlist: Iterable, n: int) -> Any:
    if isinstance(playlist, str):
        songs_dict = parse_playlist_string(playlist)
    elif isinstance(playlist, tuple):
        songs_dict = parse_playlist_tuple(playlist)
    else:
        raise ValueError("Unsupported playlist format")

    song_titles = list(songs_dict.keys())
    selected_songs = random.sample(song_titles, min(n, len(song_titles)))

    total_duration = sum(songs_dict[title] for title in selected_songs)

    total_seconds = total_duration * 60
    return timedelta(seconds=total_seconds)

print(get_duration(playlist_e, 3))
print(get_duration(playlist_f, 3))
