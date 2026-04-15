# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> SparklingRecommender v1.0  

---

## 2. Intended Use

This recommender generates music based on what the user listens to. It assumes the genre/s that the user likes to listen to, based on the frequency of listening of songs from a particular genre. This is for classroom exploration however if this recommender can be improved and worked on in the future, it could possibily be for real users.
---

## 3. How It Works (Short Explanation)

In real-world recommendations, a combination of techniques are used. Some examples are Collaborative Filtering, Content-Based Filtering, Natural Language Processing and Deep Learning. In Collaborative Filtering, the system finds users with similar tastes profiles and recommend what they enjoy. It also finds songs similar to the one users liked, based on shared listeners. In Content-Based Filtering, songs are analyzed, using features such as tempo, key genre, artistes and listen time. In this recommendation system, Content-Based Filertering will be prioritized.

The model looks at five things about each song: its genre (like pop, lofi, or jazz), its mood (like happy, chill, or intense), its energy level (a number from 0 to 1 representing how calm or intense it feels), its acousticness (how organic and acoustic vs. electronic it sounds), and its tempo (how fast or slow the beat is). The model asks the user four things: their favorite genre, their preferred mood, their ideal energy level, and whether they prefer acoustic or electronic sounds. These four inputs become the lens through which every song in the catalog is evaluated. Each song gets points based on how well it matches the user's preferences. Genre and mood are the most important — if a song matches both, it gets a big boost. Energy is scored by distance: songs closer to the user's target energy score higher, and songs far away score much lower. Acousticness works as a supporting check — if the user likes acoustic music and the song sounds acoustic, it earns extra points. All the points are added together into a final score, and the top-scoring songs become the recommendations. Each contributing factor also produces a plain-language reason, like "Matches your preferred mood" or "Energy level is a close match."

This model might be biased to genre; scores given by genre are higher than those given by mood.

---

## 4. Data

This model uses a dataset of 10 songs. The genres included are pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip-hop, classical, r&b, country, edm, folk, metal, reggae. I added about 8 more songs.

---

## 5. Strengths

The system works best for users with consistent, well-aligned preferences — where genre, mood, and energy all point toward the same kind of music. For example, a user who wants pop/happy/energy=0.8 gets Sunrise City as the top result with a score of 9.49/9.5, which is nearly perfect. Similarly, a user who wants rock/intense/energy=0.95 gets Storm Runner as the clear #1 — the right song by any intuitive measure.

The Gaussian energy scoring creates a natural gradient rather than a binary match. Songs very close to the target energy score nearly the full +4.0, while songs far away drop off sharply — this mirrors how listeners actually perceive energy mismatch. The acoustic/electronic texture check also works well at the extremes: a user who dislikes acoustic music reliably gets low-acousticness songs, and vice versa, as long as those songs have acousticness below 0.3 or above 0.6.

- Starter profile (pop/happy/0.8): Sunrise City ranked #1 at near-perfect score. Intuitive.
- Rock/intense/0.95 profile: Storm Runner ranked #1, which is the heaviest, fastest rock song in the catalog. Exactly right.
- Reggae/dreamy/0.5 profile: Island Sunrise ranked #1. It is the only reggae and only dreamy song, and its energy is a near-exact match. The system found the correct song confidently despite the acousticness dead zone bug affecting its score.
- After the weight shift, the pop/dreamy profile correctly surfaced Island Sunrise (the only dreamy song) over pop songs that matched genre but not mood — showing the scoring can be tuned toward better behavior.

---

## 6. Limitations and Bias

Three fields are loaded from the CSV but never used in scoring: `tempo_bpm`, `valence`, and `danceability`. A user who wants to dance has no way to express that preference — the system scores a song with danceability=0.95 identically to one with danceability=0.35, as long as genre, mood, energy, and acousticness match. Valence (emotional positivity) is similarly invisible, even though it is one of the most meaningful attributes for mood-based listening.

Most genres appear only once in the 18-song catalog: classical, folk, country, metal, ambient, jazz, synthwave, r&b, hip-hop, indie pop, edm, and reggae each have exactly one song. Only pop and lofi have two. This means a user who prefers classical gets one possible genre match regardless of their other preferences, while a pop user has two candidates to compete for the top spot. Rare moods have the same problem — "sad," "dreamy," "melancholic," "angry," "romantic," "nostalgic," "moody," and "focused" each appear on only one song. If that one song doesn't match the user's energy or acousticness, it may lose to songs from completely different genres.

Before the weight adjustment, genre and mood together accounted for up to 5.5 out of 9.0 points. This caused the Sad Banger problem: a user who asked for folk/sad/energy=0.9 received Willow and Rain (energy=0.22) as #1, because its genre+mood bonus of 5.5 was mathematically unreachable by any other song. The stated energy preference had almost no effect on the result. Even after halving the genre weight, a song that matches both genre and mood still has a strong structural advantage over songs that match only energy.

Pop and lofi users get more candidate songs than users of any other genre. Niche genre listeners are more likely to receive a recommendation that conflicts with their other preferences. Songs with acousticness between 0.3 and 0.6 earn zero points from the acousticness check, regardless of the user's preference. Several songs fall in this range (Island Sunrise at 0.55, Slow Burn at 0.40, Rooftop Lights at 0.35). Users whose best-matching song happens to fall in this band are quietly disadvantaged. Many high-energy songs have low acousticness (below 0.3), so users who prefer electronic music tend to receive the +1.5 acousticness bonus on a wider range of songs. Acoustic-preferring users only receive it on low-energy songs, creating an implicit link between acoustic preference and slower music that the user never chose. If a user misspells a genre or uses an alternate format (e.g., "hip hop" instead of "hip-hop"), the genre bonus never fires and the system returns results without any warning. The output looks normal, but one of the four inputs is being completely ignored.

---

## 7. Evaluation

To evaluate the recommender, I designed seven adversarial user profiles — each one constructed to probe a specific weakness in the scoring logic rather than to get a good recommendation. The profiles included a "Sad Banger" (folk/sad with energy=0.9), a "Classical Trap" (classical/happy with energy=0.95), an acoustic user whose best-matching song had a mid-range acousticness value, a pop user who wanted a dreamy mood that no pop song in the catalog has, a user requesting a genre not present in the catalog at all, a user who wanted both high energy and acoustic texture simultaneously, and a normal pop/happy profile used to confirm that ignored features like danceability had no effect on the output.

For each profile I looked at whether the top-ranked song actually reflected what the user asked for, and whether the score breakdown explained why it won. In the well-behaved cases the reasons were clear and the winner felt intuitive. In the adversarial cases I traced the math by hand to understand exactly which weight was responsible for the unexpected result.

The most surprising finding was the Sad Banger profile. I expected the energy mismatch to hurt Willow and Rain's score significantly, but the genre and mood bonuses together totaled 5.5 points out of a 9.0 maximum — more than the combined ceiling of energy and acousticness (3.5 points). That meant no song could ever beat a genre+mood match on energy alone, no matter how perfectly it matched the requested energy level. The user asked for high-energy folk music and received the quietest song in the catalog.

I also ran a weight sensitivity test — halving the genre bonus from 3.0 to 1.5 and doubling the energy ceiling from 2.0 to 4.0 — and re-ran all seven profiles to compare the results. Two profiles improved meaningfully: the Sad Banger now correctly surfaces high-energy songs, and the Wrong Vibe Pop profile now surfaces the only dreamy song instead of defaulting to genre-matched songs with the wrong mood. The other five profiles produced different scores but the same underlying failure modes, which confirmed that those bugs are structural rather than a matter of tuning.

---

## 8. Future Work

The most impactful next step would be adding danceability and tempo as scored features, since they are already in the catalog but currently ignored. After that, replacing the hard acousticness thresholds (0.3 and 0.6) with a continuous Gaussian — similar to how energy is scored — would eliminate the dead zone where a user's acoustic preference has no effect. Finally, adding a diversity check to prevent the top results from being dominated by a single genre when the catalog has relevant songs from other genres would make the recommendations feel less repetitive.

---

## 9. Personal Reflection

The most surprising thing was how confidently the system gave wrong answers. When I asked for high-energy folk music, it returned the quietest song in the catalog — and the score breakdown made it look completely reasonable. That made me realize that a recommendation being explainable is not the same as it being correct.

Building this changed how I think about real music apps. Spotify or Apple Music aren't just running a scoring function — they're working around exactly these kinds of edge cases at massive scale, which is a much harder problem than it looks from the outside.

Human judgment still matters most when preferences conflict with each other, like wanting acoustic and high-energy at the same time. The model just picks a winner silently. A real system should probably surface that tension to the user instead of hiding it in the math.

