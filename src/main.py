"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


PROFILES = [
    {
        "name": "Starter Example",
        "prefs": {
            "genre":          "pop",
            "mood":           "happy",
            "target_energy":  0.8,
            "likes_acoustic": False,
        },
    },
    {
        "name": "1. Sad Banger — energy/mood conflict",
        "prefs": {
            "genre":          "folk",
            "mood":           "sad",
            "target_energy":  0.9,
            "likes_acoustic": False,
        },
    },
    {
        "name": "2. Classical Trap — niche genre + high energy",
        "prefs": {
            "genre":          "classical",
            "mood":           "happy",
            "target_energy":  0.95,
            "likes_acoustic": False,
        },
    },
    {
        "name": "3. Acousticness Dead Zone — acoustic=0.55 gets no bonus",
        "prefs": {
            "genre":          "reggae",
            "mood":           "dreamy",
            "target_energy":  0.5,
            "likes_acoustic": True,
        },
    },
    {
        "name": "4. Wrong Vibe Pop — genre weight beats mood match",
        "prefs": {
            "genre":          "pop",
            "mood":           "dreamy",
            "target_energy":  0.5,
            "likes_acoustic": False,
        },
    },
    {
        "name": "5. Ghost Genre — unsupported genre silently ignored",
        "prefs": {
            "genre":          "k-pop",
            "mood":           "happy",
            "target_energy":  0.8,
            "likes_acoustic": False,
        },
    },
    {
        "name": "6. Acoustic + High Energy — structurally contradictory",
        "prefs": {
            "genre":          "rock",
            "mood":           "intense",
            "target_energy":  0.95,
            "likes_acoustic": True,
        },
    },
    {
        "name": "7. Ignored Features — danceability/tempo have no effect",
        "prefs": {
            "genre":          "pop",
            "mood":           "happy",
            "target_energy":  0.8,
            "likes_acoustic": False,
        },
    },
]


def print_recommendations(profile_name: str, recommendations: list) -> None:
    print("\n" + "=" * 60)
    print(f"  {profile_name}")
    print("=" * 60)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        bar = "#" * int((score / 9.0) * 20)
        print(f"\n  #{rank}  {song['title']}  —  {song['artist']}")
        print(f"      Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}  |  Acoustic: {song['acousticness']}")
        print(f"      Score: {score:.2f} / 9.0  [{bar:<20}]")
        print(f"      Why:")
        for reason in explanation.split(" | "):
            print(f"        • {reason}")
        print("  " + "-" * 58)


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for profile in PROFILES:
        recommendations = recommend_songs(profile["prefs"], songs, k=3)
        print_recommendations(profile["name"], recommendations)

    print()


if __name__ == "__main__":
    main()
