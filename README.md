# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

## Demo Walkthrough
1. User enters a guess of 1
2. Game returns "Too Low"
3. User enters a guess of 100, and the game shows "Too High"
4. User enters a guess of 50, and the game ends because it was the secret value
5. Score updates correctly after each guess
6. The player's stats are shown from the current game, and the player has an option to play again

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# This is my pytest output:
# python -m pytest .\tests\test_game_logic.py
# ========================= 10 passed in 0.04s =========================
```

## 🚀 Stretch Features

### Enhanced UI (Challenge 4)

Three output improvements were added without changing the core game logic. `check_guess`, `parse_guess` and `update_score` behave exactly as before, and all 10 tests still pass.

#### 1. Hot/Cold emojis: `get_temperature()` in [logic_utils.py](logic_utils.py)

New function `get_temperature(guess, secret, low, high)` returns a `(label, emoji, color)` tuple. It measures the distance from the secret as a fraction of the difficulty's range (`high - low`), so the thresholds scale with Easy/Normal/Hard:

| Distance from secret | Label | Emoji | Color |
|---|---|---|---|
| exact match | Correct | 🎯 | green |
| within 5% of range | Hot | 🔥 | red |
| within 15% | Warm | 🌡️ | orange |
| within 30% | Cool | 🧊 | blue |
| further away | Cold | 🥶 | violet |

Example: on Normal (1–100) with a secret of 60, a guess of 50 is 10% away, so it returns `("Warm", "🌡️", "orange")`.

#### 2. Color-coded hints: the `if submit:` block in [app.py](app.py)

After `check_guess()` returns its `(outcome, message)` tuple, `app.py` calls `get_temperature()` and renders the hint with Streamlit's colored-text markdown (`:color[...]`). The hint now shows the temperature and the direction together, in the temperature's color, for example:

> :red[**🔥 Hot** — 📉 Go LOWER!]

This replaces the old plain `st.warning(message)`. It still respects the "Show hint" checkbox. `check_guess()` itself is unchanged, so the direction text and its tests are unaffected.

#### 3. Session summary table: `render_summary()` in [app.py](app.py)

- Every submitted guess is appended to a new `st.session_state.log` list as a dict with `Attempt`, `Guess`, `Result` (Win / Too High / Too Low / Invalid), `Temperature` (e.g. `🔥 Hot`) and `Score change` (the score before and after `update_score()`). Invalid input is logged too, as `Invalid` with `—` for temperature and `0` score change.
- `render_summary()` draws a "📊 Session summary" section with three metrics (**Guesses**, **Score**, **Status**) and a table (`st.table`) of the log.
- It is called at the end of each run and also in the won/lost branch before `st.stop()`, so the table stays visible after the game ends.
- `log` is cleared in the **New Game** reset. It is separate from the existing `history` list, so the Developer Debug Info panel is unchanged.

Sample table:

| Attempt | Guess | Result | Temperature | Score change |
|---|---|---|---|---|
| 1 | 10 | Too Low | 🥶 Cold | -5 |
| 2 | 55 | Too Low | 🌡️ Warm | -5 |
| 3 | 62 | Win | 🎯 Correct | 50 |