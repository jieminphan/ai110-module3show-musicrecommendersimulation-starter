from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv
import math

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read a songs CSV and return a list of dicts with numeric fields cast to int/float."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    float(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return a (total_score, reasons) tuple."""
    score = 0.0
    reasons = []

    # Genre match — highest weight (+3.0)
    if song["genre"] == user_prefs["genre"]:
        score += 3.0
        reasons.append(f"Genre match: {song['genre']} (+3.0)")

    # Mood match — second highest weight (+2.5)
    if song["mood"] == user_prefs["mood"]:
        score += 2.5
        reasons.append(f"Mood match: {song['mood']} (+2.5)")

    # Energy — Gaussian distance, max +2.0
    # Formula: 2.0 * exp(-(diff²) / (2 * 0.25²))
    # Rewards songs close to the user's target; drops sharply as distance grows
    energy_diff = abs(user_prefs["target_energy"] - song["energy"])
    energy_score = 2.0 * math.exp(-(energy_diff ** 2) / (2 * 0.25 ** 2))
    score += energy_score
    reasons.append(
        f"Energy: target {user_prefs['target_energy']} vs song {song['energy']} "
        f"→ diff {energy_diff:.2f} → (+{energy_score:.2f})"
    )

    # Acousticness — preference bonus (+1.5)
    if user_prefs["likes_acoustic"] and song["acousticness"] > 0.6:
        score += 1.5
        reasons.append(f"Acoustic texture match: {song['acousticness']} (+1.5)")
    elif not user_prefs["likes_acoustic"] and song["acousticness"] < 0.3:
        score += 1.5
        reasons.append(f"Electronic texture match: {song['acousticness']} (+1.5)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song, sort by score descending, and return the top k as (song, score, explanation) tuples."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = " | ".join(reasons)
        scored.append((song, score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
