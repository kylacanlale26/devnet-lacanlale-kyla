"""
Module 2 — Lesson 2: Control Flow (if / elif
/ else)
Student: Lacanlale, Kyla G.
Date: 09/29/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================

'if', 'elif', and 'else' are conditional 
statements that evaluates which block of 
code to execute based on whether the first 
condition is true, 'if' is used for the 
first condition that the program checks. 
The code under the 'if' condition will be 
executed if the conditions are met, and will
proceed to the next condition, 'elif', if 
not. Meanwhile, 'else' is for when none of 
the previous conditions are met.

============================================
KEY VOCABULARY
============================================
- condition:
- if / elif / else: conditional statements
that controls the flow of the program.
    - if: first condition the program checks
    - elif: following condition if the 'if'
    statement is false
    - else: executed if none of the previous
    conditions are met
- comparison operator: compares two values
that will tell whether the condition is true
or false.
- boolean expression: evaluates two compared
values, whether it is true or false.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below 
that you came up with yourself — not copied 
from class.
"""

animal = "cat"

if animal == "dog":
  print("Woof!")
elif animal == "cat":
  print("Meow~")
else:
  print("Not an animal.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get
wrong about this topic?]

One mistake I think I did wrong is using the 
"else" for the next condition, instead of
using it to display value mistakes. Maybe if
the value is hardcoded, that is okay, but if
the value has to be entered by the person,
the 'else' will execute regardless of
the entered value entered as long as the
'if' condition is flase. There is really no
controlled that way.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
