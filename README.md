# 🔥 Higher or Lower: Follower Guessing Game (Python)

A fun Python terminal game where you guess who has more Instagram followers between two public figures!

---

## 🎮 How to Play

1. Run the game.
2. Enter how many times you want to play (number of rounds).
3. In each round:
   - Two random people will be shown.
   - You’ll see their **name**, **profession**, and **country**.
   - Guess who has **more followers** by typing `A` or `B`.
4. Get a point for each correct answer.
5. At the end, your **final score** will be shown.

---

## 📁 Project Files

- `main.py` — Contains all game logic.
- `game_data.py` — A list of dictionaries with people and follower counts.
- `art.py` *(optional)* — ASCII logo for better terminal appearance.

---

## 🧠 Sample Entry Format (game_data.py)

```python
data = [
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 650,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 400,
        'description': 'Singer and actress',
        'country': 'USA'
    }
    # Add more entries...
]
