# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

SparklingRecommender v1.0  

---

## 2. Intended Use  

This recommender generates music based on what the user listens to. It assumes the genre/s that the user likes to listen to, based on the frequency of listening of songs from a particular genre. This is for classroom exploration however if this recommender can be improved and worked on in the future, it could possibily be for real users.

---

## 3. How the Model Works  

The model looks at five things about each song: its genre (like pop, lofi, or jazz), its mood (like happy, chill, or intense), its energy level (a number from 0 to 1 representing how calm or intense it feels), its acousticness (how organic and acoustic vs. electronic it sounds), and its tempo (how fast or slow the beat is). The model asks the user four things: their favorite genre, their preferred mood, their ideal energy level, and whether they prefer acoustic or electronic sounds. These four inputs become the lens through which every song in the catalog is evaluated. Each song gets points based on how well it matches the user's preferences. Genre and mood are the most important — if a song matches both, it gets a big boost. Energy is scored by distance: songs closer to the user's target energy score higher, and songs far away score much lower. Acousticness works as a supporting check — if the user likes acoustic music and the song sounds acoustic, it earns extra points. All the points are added together into a final score, and the top-scoring songs become the recommendations. Each contributing factor also produces a plain-language reason, like "Matches your preferred mood" or "Energy level is a close match."

---

## 4. Data  

This model uses a dataset of 10 songs. The genres included are pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip-hop, classical, r&b, country, edm, folk, metal, reggae. I added about 8 more songs.

Prompts:  
 
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
