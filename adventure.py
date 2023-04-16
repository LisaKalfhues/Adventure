# Welcoming message
print("""
Find the Dragon Egg
===================

Your quest starts.
""")

descriptions = {
    "hometown": """You are in your hometown!""",
    "beekeepers house": """You are at the beekeepers house!""",
    "forest": """You are at the forest!""",
    "deep forest": """You go deeper into the forest and reach a clearing!""",
    "clearing": """You have reached a clearing"""
}
path = {
    "hometown": ["beekeepers house", "forest"],
    "beekeepers house": ["forest", "hometown"],
    "forest": ["deep forest", "hometown"],
    "deep forest": ["forest", "clearing"]
}

room = "hometown"
honey = False

while room != "clearing":
    print(descriptions[room])
    print("Where would you like to go next?\n" + ", ".join(path[room]) + "?")
    target = input()
    target = target.lower()
    if target in path[room]:
        if target == "beekeepers house" and not honey:
            print("\n")
            print("The beekeeper tells you horrifying stories about a BEAR in the forest. He offers you a pot of honey and you buy it!")
            honey = True
            room = target
        elif target == "beekeepers house" and honey is True:
            print("\n")
            room = target
        elif target == "hometown":
            print("\n")
            room = target
        elif target.lower() == "forest":
            if not honey:
                print("\n")
                print("The darkness that sourrounds you is cold and frightening.\nSuddenly you see a BEAR! You run back to your", room)
            else:
                print("\n")
                print("Luckily you went to the beekeeper! You leave the honeypot for the bear and carefully sneak by!")
                honey = False
                room = target
                print("Where would you like to go next?\n" + ", ".join(path[room]), "?")
                target = input()
                target = target.lower()
                if target == "deep forest":
                    print("\n")
                    room = target
                    print(descriptions[room])
                    room = "clearing"
                elif target == "hometown":
                    print("\n")
                    print("Don't give up!")
                    room = target
    else:
        print("\n")
        print("Wait! That is not a given option.")

# Congrats to the player
print("""
In the middle of the clearing you discover the dragon egg.

Your request has been successful!
""")
