from sys import exit

def soursops():
    print "Right on. It's night time and you want some Thai goodness."
    print "You know you love the Waterburger, but you also see that there are new items on the menu."
    print "Will  you order a waterburger or try something new?"

    choice = raw_input("Choose: waterburger or new.  ")

    if choice == "waterburger":
        print "Yeah, baby! This is why we have tastebuds."
        exit(0)
    elif choice == "new":
        print "Fantastic! You're expanding your horizons, but you are a little sorry that you've missout on the waterburger."
        exit(0)
    else:
        useless("Why are you even here if you're not going to eat something?")
    
def spokesman():
    print "Ooh. You're at Spokesman for a cappuccini and something sweet."
    print "They have cookies and muffins from Crema Bakery."
    print "You have your eyes on the poppyseed muffin and a snickerdoodle cookie."
    print "Which one will you choose?"

    choice = raw_input("Choose: muffin or cookie.")

    if choice == "muffin":
        print "Fine. It's from Crema, and you love their goods, but muffins are wannabes."
        print "But you got two breve caps and are good to go."
        exit(0)
    elif choice == "cookie":
        print "Right? No cookie beats a snickerdoodle, and no one out doodles a snicker like Crema!"
        exit(0)
    else:
        useless("Can you not read and follow simple instructions?")

def am_pm():
    print "What time of day is it? I mean, this does matter."
    print "Is it early (before 2p) or late?"
    
    choice = raw_input("Choose: early or late.  ")

    if choice == "early":
        spokesman()
    elif choice == "late":
        soursops()
    else:
        useless("Honestly, mate. Make a decision.")
        
    

def home_food():
    print "Ok. You want to save money."
    print "You've opened the fridge and see two options:"
    print "Making a salad or reheating leftovers. What do you choose?"

    choice = raw_input("Choose: salad or leftovers.  ")

    if choice == "salad":
        print """You're sad but will pretend that you've made the right decision.
You may take a photo to show everyone how good you were.
You wish you had a cookie.
        """
        exit(0)
    elif choice == "leftovers":
        print """You'll go to bed regretting this. Not enough salsa and
hot sauce to make this good.
        """
        exit(0)
    else:
        useless("If these are the choices you're going to make, we can't hang out.")

def useless(reason):
    print reason, "You're useless."
    exit(0)
    
def start():
    print "You are feeling peckish."
    print "You have two options: going out or staying in."
    print "What will you do?"

    choice = raw_input("Choose: out or in.  ")

    if choice == "out":
        am_pm()
    elif choice == "in":
        home_food()
    else:
        useless("If you can't even decide what to do, I can't help you.")

start()
