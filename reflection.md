# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|-------|-------------------|-----------------|------------------------|----------------------|
| Guess of 1 | Hint should be "Go HIGHER!" | Hint was "Go LOWER!"| none | app.py,check_guess |
| Switched to hard difficulty level | Range should increase | Range decreased | none | app.py, get_range_for_difficulty |
| clicked new game button | Resets game stats and allows user to enter more guesses | Does not reset score and history, does not allow the player to enter guesses, banner still displays win | none | app.py, lines 134-145 |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One example of a correct AI suggestion was removing occurences of a TypeError by ensuring that the secret variable was an integer instead of a string, as the code did for even values. I verified the result by running the test cases to ensure they still passed from before and after making the change. I also played the game again to check for any type errors, which did not happen.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
One example of an AI suggestion that I did not accept as written occurred when I was fixing the bugs in the check_guess function. The suggestion was more wordy and harder to read with repetitive conditional statements, so I edited some parts to make the code easier to read. I verified my version by ensuring that the game still performed the same way after and before I made the changes.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided if a bug was fixed if the test cases passed and I was able to play the game with the same performance as before the fix. I tested numbers that were higher or lower than the secret value as well as edge cases. I also made sure the code was readable and not unnecessarily long.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One manual test I ran was using the normal game mode to test player guesses and their corresponding hints. For example, I tested a number that was higher than the secret value, a number that was lower than the secret value, and extreme numbers on either side of the range to make sure that the hints displayed were accurate. This test showed me whether the bugs in the check_guess function were fixed for both higher and lower guessess.
- Did AI help you design or understand any tests? How?
Yes, AI designed tests in the test_game_logic.py folder to test the accuracy of hints displayed based on player guesses as well as the correct type of input from guesses. For example, a higher guess should encourage the player to guess a lower number, while a lower guess should encourage them to guess a higher number. Additionally, guesses should be an integer data type, which means the game will show an error to the player if they enter a string, for example.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit "reruns" the entire Python file every time something is clicked, which wipes normal variables. Session state is a small memory box that survives those "reruns", so you put anything the app must remember there, like the secret number or the number of attempts.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to reuse frequent Git commits in future labs and projects. I feel like I was able to make multiple meaningful commits about what I changed in the code, which helped me figure out where to go next based on the versions I had created. Having this project broken up into various parts also helped me understand the incremental changes I was making so I could write about them in my commit messages.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would spend more time crafting more detailed prompts rather than going for speed in finding a solution. I think that the extra time spent explaining the context to the AI agent will be more useful in generating clean, effective code, rather than lengthy, complicated code that may not be the most efficient.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project helped me realize that AI generated code is more powerful at finding bug fixes and refactoring than I previously thought. However, I also noticed that AI still makes some errors that require human oversight, such as producing code that runs but is not easy to read.
