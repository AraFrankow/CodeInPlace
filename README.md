# 🎓 Code in Place 2026 - Stanford University

My journey through Stanford's **Code in Place** program — a competitive, 6-week intensive Python course focused on programming fundamentals and problem-solving.

## 📊 About the Program

- **Institution:** Stanford University
- **Duration:** 6 weeks (April - June 2026)
- **Acceptance Rate:** ~12% (selected from 15,000+ global applicants)
- **Format:** Weekly interactive sections, coding assignments, and final project
- **Focus:** Python fundamentals, algorithmic thinking, real-world problem-solving

## 📚 Course Progress

### Week 1: Introduction to Programming with Karel ✅
**April 2026**

Started with Karel the Robot — a visual programming environment designed by Stanford to teach core concepts.

**Concepts learned:**
- Control flow: `while` loops and `if/else` statements
- Defining and calling functions with `def`
- Problem decomposition
- Basic algorithmic thinking

**What is Karel?**  
A robot that lives in a grid world and can:
- `move()` - Move forward one space
- `turn_left()` - Rotate 90° left
- `put_beeper()` - Place a marker
- `pick_beeper()` - Pick up a marker

Simple environment, powerful concepts. Great way to visualize logic before diving into syntax.

---

### Week 2: Control Flow & Conditionals with Karel ✅
**April - May 2026**

Built on Week 1 foundations with more complex Karel problems using conditional logic.

**New concepts:**
- Boolean functions for decision-making:
  - `front_is_clear()` - Check if robot can move forward
  - `beepers_present()` - Check if there's a beeper at current location
  - `beepers_in_bag()` - Check if robot has beepers to place
  - `left_is_clear()`, `right_is_clear()` - Check adjacent spaces
  - `facing_north()`, `facing_south()`, `facing_east()`, `facing_west()` - Check orientation

**Key takeaway:**  
Learning to combine conditions to solve increasingly complex problems. Karel teaches you to *think* like a programmer before worrying about syntax.

---

### Week 3: Real Python — Beyond Karel 🐍 ✅
**May 2026**

Transitioned from Karel's visual world to writing "real" Python code.

**Topics covered:**
- `print()` and `input()` - User interaction
- Arithmetic operations (`+`, `-`, `*`, `/`)
- Integer division (`//`) and remainders (`%`)
- Exponentiation (`**`)
- Type conversion: `int()`, `float()`, `str()`
- Rounding with `round()`
- String formatting with f-strings
- Random number generation with `random` module
- Constants and multi-branch conditionals (`if/elif/else`)

**Programs created:**
- `hello_name.py` - Greet the user by name using input and string formatting
- `multiply.py` - Multiply two numbers entered by the user
- `mad_libs.py` - Insert user-provided color, adjective and object into a pre-built sentence
- `dice_roller.py` - Simulate a dice roll using random numbers
- `mars_weight.py` - Convert Earth weight to Mars equivalent (37.8% of Earth weight)
- `planetary_weight.py` - Convert Earth weight to any planet using gravity constants
- `dog_years.py` - Convert a person's age into dog years
- `haiku_generator.py` - Generate a haiku (5-7-5 syllables) from user input

**What clicked:**  
Karel taught the logic; Python gives it real-world application. Every concept from Karel — loops, conditionals, functions — now works on actual data and produces meaningful output. The jump from "move a robot" to "calculate something useful" makes the purpose of programming click.

---

### Week 4: Functions, Parameters & Game Development 🎮 ✅
**May 2026**

Dove deeper into functions with parameters, return values, and building complete programs.

**Topics covered:**
- Functions with multiple parameters and return values
- Game state management across function calls
- Random number generation with `random` module
- Control flow with `while` loops and conditionals
- Boolean logic and comparisons
- Input validation and error handling
- Mathematical sequences and algorithms

**Programs created:**
- `liftoff.py` - Countdown loop from 10 to 1
- `random_numbers.py` - Generate and print 10 random numbers (1-100)
- `doubler.py` - Double numbers until reaching 100
- `joke_bot.py` - Simple interactive chatbot
- `hailstone.py` - Collatz conjecture: divide evens by 2, multiply odds by 3+1 until reaching 1
- `high_low_game.py` - Guessing game comparing your number vs computer's
- `the_game_of_nimm.py` - Two-player strategy game: alternate taking 1-2 stones, last to take loses
**Main project:**
`math_game.py` -  Progressive difficulty math challenge game

**What clicked:**  
Functions transform code from linear scripts into modular, reusable components. Return values allow functions to communicate state changes, enabling complex multi-level game mechanics. The strategy games (High-Low, Nimm) showed how the same Boolean logic used in simple conditionals can power complete turn-based game systems.

---

### Week 5: Graphics & Visual Programming 🎨 ✅
**May 2026**

Transitioned from text-based programs to visual programming using Stanford's Graphics library.

**Topics covered:**
- Canvas creation and coordinate systems
- Drawing shapes: circles, ovals, rectangles, lines
- Color systems and `random.choice()` for random colors
- Function composition: functions calling other functions
- Positioning elements with x/y coordinates
- Nested loops for grid-based patterns
- Breaking visual programs into parameterized functions

**Programs created:**
- `box_row.py` - Draw a row of 5 equally-sized boxes filling the bottom of the canvas
- `draw_flag.py` - Recreate the flag of Indonesia using rectangles
- `my_flag.py` - Recreate my own country's flag (Argentina 🇦🇷)
- `pyramid.py` - Draw a brick pyramid where each row decreases by one brick
- `quilt.py` - Generate a repeating patch pattern to simulate a quilt blanket
- `random_circles.py` - Draws 20 circles at random positions with random colors on the canvas
- `scene_with_functions.py` - Draw a natural scene broken into parameterized functions

**Key insight:**  
The same programming concepts (loops, functions, randomness) now create visual output. Each project built on the last: from a single row of boxes → a pyramid → a full quilt pattern. The final scene project tied everything together — using functions with parameters to draw reusable visual components.

---

### Week 6: Lists, Dictionaries & Data Structures 📚 ✅
**May 2026**

Final week of live sessions. Moved from visual programming into working with 
data structures to store, organize, and analyze information.

**Topics covered:**
- Lists: ordered collections, iteration, and file loading
- Dictionaries: key-value pairs for structured data
- Looping over lists and dictionaries
- File reading: loading data from `.txt` files into lists
- Counting occurrences with dictionaries
- String formatting for aligned output (`f"{word : <8}"`)
- Dictionary methods: `.get()`, `.pop()`, `del`, `.keys()`

**Programs created:**
- `compute_average.py` - Load numbers from a file and calculate their average
- `quizzlet.py` - Spanish vocabulary quiz that loops over a dictionary and tracks score
- `baby_vocab.py` - Count word frequency from a file and display a text-based histogram
- `[one more coming soon]`

**Key insight:**  
Lists and dictionaries are the backbone of real-world programming. 
A list loads raw data from a file; a dictionary gives that data structure and meaning. 
The Baby Vocab project tied both together: load words into a list, 
count them into a dictionary, display results as a histogram — a complete data pipeline in pure Python.

---

## 🎯 What I'm Learning

Beyond just Python syntax, Code in Place emphasizes:
- **Problem decomposition** - Breaking complex problems into smaller functions
- **Algorithmic thinking** - Planning solutions before coding
- **Clean code** - Writing readable, maintainable programs
- **Debugging** - Systematic problem-solving when code doesn't work
- **Visual thinking** - Translating logic into graphics and coordinate systems
- **Data structures** - Organizing and manipulating information with lists and dictionaries

The Karel-to-Python progression is brilliant: you learn the **concepts** first (loops, conditionals, functions) in a forgiving visual environment, then apply them to real code — and eventually to graphics, games, and data structures.

---

## 📂 Repository Structure

```
code-in-place-2026/
├── week1-karel/          # Karel programs (control flow basics)
├── week2-karel/          # Karel programs (conditionals)
├── week3-python/         # First Python programs (arithmetic, I/O, constants)
├── week4-functions/      # Functions, parameters, games (Nimm, High-Low, Math Game)
├── week5-graphics/       # Graphics library (flags, pyramid, quilt, scene)
├── week6-data/           # Lists and dictionaries
└── final-project/        # Final project (coming soon)
```

---

## 🏆 Certificate

Will be added upon successful completion of the program (June 2026).

---

## 🔗 More About Code in Place

Code in Place is Stanford's free community offering of the first half of CS106A (Introduction to Computer Science). It's taught by Stanford students and faculty using the same materials as the on-campus course.

**Learn more:** [codeinplace.stanford.edu](https://codeinplace.stanford.edu)

---

## 📫 Connect

This repo documents my learning journey. Feel free to reach out if you're also participating or interested in the program!

- **LinkedIn:** [linkedin.com/in/arabelafrankow](https://www.linkedin.com/in/arabelafrankow/)
- **GitHub:** [@AraFrankow](https://github.com/AraFrankow)

---

<div align="center">
  <i>Learning in public, one week at a time 🚀</i>
</div>
