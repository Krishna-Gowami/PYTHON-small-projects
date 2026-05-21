import random

subjects = ["Shah Rukh Khan", "Deepika Padukone", "Aamir Khan", "Priyanka Chopra", "Ranveer Singh", "Alia Bhatt", "Krishna Goswami"]
verbs = ["announced", "revealed", "shared", "confidential", "disclosed", "confirmed", "leaked", "reported"]
objects = ["a new movie", "a secret project", "a collaboration", "a personal milestone", "an upcoming event", "a charity initiative"]

while True:
    subject= random.choice(subjects)
    verb= random.choice(verbs)
    object= random.choice(objects)

    fake_news= f"{subject} {verb} {object}."
    print("\n" + fake_news)

    ch = input("Generate Another News? [y/n]: ")
    if(ch.lower() == 'n'):
        break
    else:
        continue