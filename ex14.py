#prompting and passing
# this is an example of argv and input prompts being used together

from sys import argv
script, user_name = argv
prompt = "> " #this is literally just adding an aesthetic > to each prompt

print(f"hi {user_name}, i'm the {script} script.")
print("I would like to ask you a few questions")
print(f"do you like me {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
alright, so you said {likes} about liking me.
you live in {lives}. Not sure where that is.
and you have a {computer} computer. nice.
""")
