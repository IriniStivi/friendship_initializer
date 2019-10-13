# cooperian_friendship_initializer.py
import re

print("Hello, human. What's your name?")
x = input()
print()
print("Well, hello,", x,"! Now, imagine the following:\n"
      "Your phone rings. You pick up: it's me.\n"
      "\n"
      "Talk to me.\n"
      "\n"
      "*RING! RING!*\n"
      "\n"
      "Hi,", x,"! Would you like to share a meal?")

z = input()
if re.findall(".es", z):            # for Y/yes
    print("Great!")

elif re.findall(".o", z):           # for N/no
    print("Do you then enjoy a hot beverage?")

    z1 = input()
    if re.findall(".es", z1):
        print("What would you like: tea, coffee or cocoa?")
        z2 = input()
        print("Great! Let's have", z2, "together!")
    elif re.findall(".o", z1):
        print("Nevermind. Let's share a recreational activity.")
        print("Tell me one of your interests, like riding, hiking or whatever.")
        
        for i in 1, 2, 3, 4:
            
            # asking seven times max
            
            z3 = input()
            if re.findall("[Rr]unning", z3):
                print("Great! I like", z3,", too. Why don't we do that?")
                break
            else:
                print("Sorry, but I don't like", z3,"very much. Anything else?")
        else:
            print("Alright then. Let's stick to", z3,".")
    
print()
print("BEGIN FRIENDSHIP.")


