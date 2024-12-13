playlist_e = (
    {"title": "Sunday", "duration": 5.09},
    {"title": "Why Does My Heart Feel so Bad?", "duration": 4.23},
    {"title": "Everlong", "duration": 3.25},
    {"title": "To Let Myself Go", "duration": 4.40},
    {"title": "Golden", "duration": 2.56},
    {"title": "Daisuke", "duration": 2.41},
    {"title": "Miami", "duration": 3.31},
    {"title": "Chill Bill Lofi", "duration": 2.05},
    {"title": "The Perfect Girl", "duration": 1.48},
    {"title": "Resonance", "duration": 3.32},
)
playlist_f = (
    {"title": "Free Bird", "duration": 9.08},
    {"title": "Enter Sandman", "duration": 5.31},
    {"title": "One", "duration": 7.45},
    {"title": "Sliver", "duration": 2.10},
    {"title": "Come as You Are", "duration": 3.45},
    {"title": "Thunderstruck", "duration": 4.53},
    {"title": "You Shook Me All Night Long", "duration": 3.29},
    {"title": "Everlong", "duration": 4.51},
    {"title": "My Hero", "duration": 4.02},
)
import random
from datetime import timedelta
from typing import Iterable, Any, Union

def parse_playlist(playlist: str) -> list:
    songs = []
    for line in playlist.strip().split("\n"):
        name, duration = line.rsplit(" ", 1)
        songs.append((name, float(duration)))
    return songs

def get_duration(playlist: Iterable, n: int) -> Union[timedelta, str, float]:
    if isinstance(playlist, str):
        playlist = parse_playlist(playlist)
    elif isinstance(playlist, tuple) and all(isinstance(i, dict) for i in playlist):
        playlist = [(song['title'], song['duration']) for song in playlist]
    if n > len(playlist):
        return
    chosen_songs = random.sample(playlist, n)
    total_duration = sum(song[1] for song in chosen_songs)
    return timedelta(hours=int(total_duration // 60), minutes=int(total_duration % 60))
