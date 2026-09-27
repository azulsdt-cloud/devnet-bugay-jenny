"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Bugay, Jenny L.
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================

This topic is to output other condition. If the first condition didn't meet the required
condition, it will go to the elif which have another condition to meet. If it matches, 
it will print the text written on that condition. 

============================================
KEY VOCABULARY
============================================
- condition:
- if / elif / else: It is used for printing a decision since there is other options
and keeps the code on going until you match the condition.
- comparison operator: It is the and/or operator, it is used to compare two things.
- boolean expression: To see if it is True or False. 
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- 
choice = input("Do you want to watch Haikyuu? (1 for Yes, 0 for No): ")
if choice == "1":
  print("Let's Go!")
else:
  print("Okay :<")
 ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

The mistake I just made recently is that for the if condition I forgot to use the ""
I only realized it late and know the reason why my choice is not catching my if. I only
did if choice == 1 

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
