import random
import time
import sys

nameList = ["Bartholomew", "Jonathan", "Jamal", "Jamar", "Shamar", "Eugene", "Matthew", "Joe", "Bob", "Michael",
            "Jimmy", "Dicky", "Daequan"]
statusList = ["middle"]
parentsList = ["Both Alive", "1 Alive", "1 Gone"]
parents2List = ["Overcaring", "Caring", "Neglectful", "Abusive"]
mm = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

name = random.choice(nameList)
status = random.choice(statusList)
parents = random.choice(parentsList)
parents2 = random.choice(parents2List)
middlemoney = random.choice(mm)

customperson = input("Hello, what is your name?")

money = 0
happiness = 100
fitness = 50
popularity = 50


def stats():
    print("Money: " + "$" + str(money))
    print("Happiness: " + str(happiness))
    print("Fitness: " + str(fitness))
    print("Popularity: " + str(popularity))


print("Hello " + customperson + "!" + " Welcome to your life as a high school student," +
      " your name is now " + name + " and you live in an " + status + " family."
                                                                      " Your parent(s) status: " + parents + " and your parent(s) are " + parents2 + ".")
time.sleep(5)
# ///
if status == ("Upper-Middle Class"):
    print("")
    print("Since you are Upper-Middle Class, you get an allowance of"
          " $25 per day!")
    time.sleep(5)
elif status == ("Affluent"):
    print("")
    print("Since you are affluent, you get an allowance of"
          " $50 per day!")
    time.sleep(5)
if parents2 == ("Abusive"):
    print("")
    print("Due to abusive parent(s), you get -5 happiness a day, sorry.")
elif parents2 == ("Overcaring"):
    print("")
    print("Due to over caring parent(s), you get -2 happiness a day." +
          " While it is good to have parents who care for you, there is a limit.")

# ///
if status == ("Middle Class"):
    print("")
    print("Since you are Middle Class, you can get an allowance of"
          " $15 to $25 per day!")
    time.sleep(5)
if parents2 == ("Abusive"):
    print("")
    print("Due to abusive parent(s), you get -5 happiness a day, sorry.")
elif parents2 == ("Overcaring"):
    print("")
    print("Due to over caring parent(s), you get -2 happiness a day." +
          " While it is good to have parents who care for you, there is a limit.")

print("Now the game begins.")
print("")
print("It is September 2016, your first day of high school, what would you like to do?")
print("1. Wake up and get ready.")
print("2. View stats.")

if status == ("Upper-Middle Class"):
    money += 25
if status == ("Affluent"):
    money += 50
if status == ("Middle"):
    money += middlemoney

answer = input("What would you like to do? ")
if answer == "1":
    print(
        "As you start rushing out of your house in the lovely suburbs you call home, you yell out goodbye to whoever is listening. Once you get outside you hop on your skateboard and start skating down the road to school.")
    print("")
    time.sleep(2)
    print(
        "You reach school before the first bell rings and all the students are waiting outside. Some talking some doing that awkward greeting to make new friends and some just sitting around doing 'nothing'.")
    print("You have 2 choices.")
    print("1. Go Try to talk to some people")
    print("2. Just stand there looking at people until the bell rings")
    dayone = input("What will you choose ")
    print("")
    time.sleep(2)
    if dayone == "1":
        print(
            "Before you can go to one of the groups of people talking someone behind you says 'Ok I see you.' and laughs. You turn around and a cute asian girl with a skateboard is standing there. She's wearing Off-White 1's, bell bottoms, a crop top and a shirt over it.")
        time.sleep(2)
        jakie = input("Do you want to be friends with her? 1. Yes or 2. No ")
        time.sleep(1)
        if jakie == "1":
            print((
                              "You just try to play it off cool and say 'Like you're one to speak.' she rolls her eyes and says 'My name is Jakie, what about you?' say 'Oh my name is " + name + ".' She laughs again and then you continue talking until the bell for first period rings."))
            print("")
            print("Popularity: " + str(popularity + 5))
            print("")
            print("You both have English and history for two periods so you spend that time joking around and talking.")
            time.sleep(2)
            print(
                "It's last period, art, the room is set up with a lot of easels and canvases in a circle and the teacher is standing in the middle. Class starts and everyone is told to paint something, you paint Reptar and think it's pretty nice until a short, very skinny kid comes and scribbles black paint all over it and says 'It was $h!# anyway.'")
            time.sleep(2)
            art = input("What will you do? 1. Confront them. 2. Turn their sabotage into something beautiful.")
            if art == "1":
                print(
                    "You stand up and Hisoka uppercut the small kid, he goes flying and everyone just stares at you. You then look around and grab your stuff and the painting and run out of school and rush home.")
                print("")
                print("Popularity: " + str(popularity + 15))
                print("Fitness: " + str(fitness + 5))
                print("")
                time.sleep(3)
                print("See I appreciate you doing that but you got suspended.")
                print("G A M E O V E R")
                exit()
            if art == "2":
                print(
                    "You look at the kid that sabotaged your beautiful piece, think about Hiskoa punching him, then look back at your art and let your mind go free with no limits. Once the bell rings you finnaly wake up from your artistic trance and look at your beautiful masterpiece. 'Damn I kinda snapped' You mumble as you are walking out of the building.")
                time.sleep(2)
                print(
                    "As you are walking home a hipster looking guy stops you and asks to see your art. He looks amazed and offers you $100 for it.")
                sell = input("Will you sell it? 1. Yes 2.No")
                if sell == "1":
                    print(
                        "The man hands you a crisp $100 bill and you hand him the painting and then stand there amazed. After a while you start skating home.")
                    print("")
                    print("Money: $" + str(money + 100))
                    print("")
                    time.sleep(4)
                    print("Money: $" + str(money + middlemoney))
                    welp = input(
                        "You wake uap and its your second day of school, what do you wand to do? 1. Go to School. 2. View Stats")
                    if welp == "1":
                        print("")
                    if welp == "2":
                        stats()
                        statscho = input("Do yoy want to go to school now? 1. Yes 2. No")
                        if statscho == "1":
                            print(
                                "You gather your things by the door, skipping breakfast because you took so long trying to figure out what to wear. You head out for the day and as you are walking Jakie comes running around the corner at you and hugs you and asks if you are ok after yesterday.")
                            time.sleep(2)
                            print(
                                "You say you're fine and laugh it off then she says 'You know you would be the best FRIEND if you did that if i was even in a situation like that.' and laughs. You give a depressed laugh and stay mostly quiet for the rest of the walk to school and through your first 3 periods as she talks about herslef and clothes and girls she hates.")
                            time.sleep(2)
                            print("")
                            print("Happiness: " + str(happiness - 5))
                            print("")
                            print(
                                "During 4'th period lunch you are sitting with Jakie and her friends when two guys aproach you and one of them says 'Yo my guy that painting you did yesterday was fire by the way.' You give a suprised thanks and look at them quizzically. You realize its the two guys that were sitting next to you when you were painting. You remember the guy on the left name is Ryan and the one that was speaking to you is Leaym.")
                            time.sleep(2)
                            randl = input(
                                "I see you paint too.' you say when you see Leaym is wearing painted pants, shoes and jacket. 'Ehh i guess' he says, 'You wanna come over to our table and talk for a little?' 1.Yes 2.No")
                            if randl == "1":
                                print(
                                    "You say bye to Jakie and walk with them to their table corner of the cafeteria and talk tith them until the bell rings and then you say bye to them, just to walk to the same music class.")
                                time.sleep(2)
                                print(
                                    "You sit next to them and you guys talk throughout the class even though Mr. Antaky tells you guys to be quiet multiple times")
                                time.sleep(2)
                            if randl == "2":
                                print(
                                    "You say 'Nah im good bruh' then Ryan says 'Oh ok well well see you later' and they walk away")
                                time.sleep(2)
                                print(
                                    "Jakie says you shoulda gone with them but you shrug and go back on Instagram waiting for the bell to ring. Once you get into music class you sit in a random seat and look around. Right next to you is Leaym and Ryan looking at you laughing. You start laughing too, dap them up then you guys start talking getting to know each other better.")
                                time.sleep(2)
                                print("")
                                print("Popularity: " + str(popularity + 10))
                                print("")
                                print(
                                    "The day flies by as you and your new found friends go through the day together. Once school is done there is an anouncement telling everyone that clubs are now open to join in the gym. You, Leaym and Ryan go find Jakie then you all go to the gyl to look for a good club to join. You guys look around fo a while until you spot something in the back corner and it calls to you. You walk over and find out its the schools quidditch team, The Potters.")
                                time.sleep(2)
                                quid = input("Do you want to join 1.Yes 2.no")
                                if quid == "1":
                                    print(
                                        "You immediately fill out the application form then call over Jakie and the boys. Leaym and Ryan took one quisicall look the said 'Screw it and signed up too. Jakie was hesitant about it but you manages to convince her by saying 'I bet you ther's a Malfoy on the team too' since she said the had a fat crush on Drako Malfoy for some odd reason.")
                                    time.sleep(2)
                                if quid == "2":
                                    print("")
                if sell == "2":
                    print(
                        "You decline the weird dudes offer and continue skating home. When you get there you just flop on your bed and fall asleep shoes on and everything because you're so exausted ")
                    time.sleep(2)
                    print("Money: $" + str(money + middlemoney))
                    welp = input(
                        "You wake uap and its your second day of school, what do you wand to do? 1. Go to School. 2. View Stats")
                    if welp == "1":
                        print("")
                    if welp == "2":
                        stats()
                        statscho = input("Do yoy want to go to school now? 1. Yes 2. No")
                        if statscho == "1":
                            print(
                                "You gather your things by the door, skipping breakfast because you took so long trying to figure out what to wear. You head out for the day and as you are walking Jakie comes running around the corner at you and hugs you and asks if you are ok after yesterday.")
                            time.sleep(2)
                            print(
                                "You say you're fine and laugh it off then she says 'You know you would be the best FRIEND if you did that if i was even in a situation like that.' and laughs. You give a depressed laugh and stay mostly quiet for the rest of the walk to school and through your first 3 periods as she talks about herslef and clothes and girls she hates.")
                            time.sleep(2)
                            print("")
                            print("Happiness: " + str(happiness - 5))
                            print("")
                            print(
                                "During 4'th period lunch you are sitting with Jakie and her friends when two guys aproach you and one of them says 'Yo my guy that painting you did yesterday was fire by the way.' You give a suprised thanks and look at them quizzically. You realize its the two guys that were sitting next to you when you were painting. You remember the guy on the left name is Ryan and the one that was speaking to you is Leaym.")
                            time.sleep(2)
                            randl = input(
                                "I see you paint too.' you say when you see Leaym is wearing painted pants, shoes and jacket. 'Ehh i guess' he says, 'You wanna come over to our table and talk for a little?' 1.Yes 2.No")
                            if randl == "1":
                                print(
                                    "You say bye to Jakie and walk with them to their table corner of the cafeteria and talk tith them until the bell rings and then you say bye to them, just to walk to the same music class.")
                                time.sleep(2)
                                print(
                                    "You sit next to them and you guys talk throughout the class even though Mr. Antaky tells you guys to be quiet multiple times")
                                time.sleep(2)
                            if randl == "2":
                                print(
                                    "You say 'Nah im good bruh' then Ryan says 'Oh ok well well see you later' and they walk away")
                                time.sleep(2)
                                print(
                                    "Jakie says you shoulda gone with them but you shrug and go back on Instagram waiting for the bell to ring. Once you get into music class you sit in a random seat and look around. Right next to you is Leaym and Ryan looking at you laughing. You start laughing too, dap them up then you guys start talking getting to know each other better.")
                                time.sleep(2)
                                print("")
                                print("Popularity: " + str(popularity + 10))
                                print("")
                                print(
                                    "The day flies by as you and your new found friends go through the day together. Once school is done there is an anouncement telling everyone that clubs are now open to join in the gym. You, Leaym and Ryan go find Jakie then you all go to the gyl to look for a good club to join. You guys look around fo a while until you spot something in the back corner and it calls to you. You walk over and find out its the schools quidditch team, The Potters.")
                                time.sleep(2)
                                quid = input("Do you want to join 1.Yes 2.no")
                                if quid == "1":
                                    print(
                                        "You immediately fill out the application form then call over Jakie and the boys. Leaym and Ryan took one quisicall look the said 'Screw it and signed up too. Jakie was hesitant about it but you manages to convince her by saying 'I bet you ther's a Malfoy on the team too' since she said the had a fat crush on Drako Malfoy for some odd reason.")
                                    time.sleep(2)
                                if quid == "2":
                                    print("")
        if jakie == "2":
            print(
                "You give a annoyed scoff then turn around and walk away to find someone to talk to. Before you fully leave you hear a girl say 'What happend there Jakie?' to the asian girl. ")
            time.sleep(2)
            print(
                "You approach two guys talking not far from where you were standing and say 'Yo what up boys.' They look at you and laugh and one of them says 'Why the hell did you just blow off Jakie like that?.'")
            time.sleep(2)
            print("")
            print("1. I don't know man I was getting bad vibes.")
            print("2. She looked too good for me")
            nojakie = input("Option 1 or 2? ")
            if nojakie == "1":
                print(
                    "You say 'I don't know man I was getting bad vibes.' They look at you in disbelief then the guy on the right says 'Bro you looks like the male version of her but whatever.' The guy on the left yells 'TRUUUE.' and starts laughing.")
                time.sleep(2)
                print(
                    "The guy on the right then says 'Im Ryan and this is Leaym by the way' you say 'Cool im " + name + ".' they laugh and you guys continue talking until first period starts.")
                time.sleep(2)
                print("")
                print("Popularity: " + str(popularity + 10))
                time.sleep(3)
                print(
                    "You three have English and history for two periods so you spend that time joking around and talking too.")
                time.sleep(3)
                print(
                    "It's last period, art, the room is set up with a lot of easels and canvases in a circle and the teacher is standing in the middle. Class starts and everyone is told to paint something, you paint Reptar and think it's pretty nice until a short, very skinny kid comes and scribbles black paint all over it and says 'It was $h!# anyway.'")
                time.sleep(2)
                art = input("What will you do? 1. Confront them. 2. Turn their sabotage into something beautiful.")
                if art == "1":
                    print(
                        "You stand up and Hisoka uppercut the small kid, he goes flying and everyone just stares at you. You then look around and grab your stuff and the painting and run out of school and rush home.")
                    print("")
                    print("Popularity: " + str(popularity + 15))
                    print("Fitness: " + str(fitness + 5))
                    print("")
                    time.sleep(3)
                    print("See I appreciate you doing that but you got suspended.")
                    print("G A M E O V E R")
                    exit()
                if art == "2":
                    print(
                        "You look at the kid that sabotaged your beautiful piece, think about Hiskoa punching him, then look back at your art and let your mind go free with no limits. Once the bell rings you finnaly wake up from your artistic trance and look at your beautiful masterpiece. 'Damn I kinda snapped' You mumble as you are walking out of the building.")
                    time.sleep(2)
                    print(
                        "As you are walking home a hipster looking guy stops you and asks to see your art. He looks amazed and offers you $100 for it.")
                    sell = input("Will you sell it? 1. Yes 2.No")
                    if sell == "1":
                        print(
                            "The man hands you a crisp $100 bill and you hand him the painting and then stand there amazed. After a while you start skating home.")
                        print("")
                        print("Money: $" + str(money + 100))
                        print("")
                        time.sleep(4)
                        print("Money: $" + str(money + middlemoney))
                        welp = input(
                            "You wake uap and its your second day of school, what do you wand to do? 1. Go to School. 2. View Stats")
                        if welp == "1":
                            print("")
                        if welp == "2":
                            stats()
                            statscho = input("Do yoy want to go to school now? 1. Yes 2. No")
                            if statscho == "1":
                                print(
                                    "You gather your things by the door, skipping breakfast because you took so long trying to figure out what to wear. You head out for the day and as you are walking Leaym and ryan comes running around the corner at you, dap you up and start asking you questions about yesterday.")
                                time.sleep(2)
                                print(
                                    "You say you're fine and laugh it off then Leaym says 'If thats what it takes to get you go to go Picasso then i happily do it all damn day.' and laughs. You give a depressed laugh and stay mostly quiet for the rest of the walk to school, because you donte even like painting, thinking about it makes you depressed. So you just listen to them talk through your first 3 periods as they talk about games and clothes and girls.")
                                time.sleep(2)
                                print("")
                                print("Happiness: " + str(happiness - 5))
                                print("")
                                print(
                                    "During 4'th period lunch you are sitting with Leaym and his friends when Jakie aproaches you and says 'Yo that painting you did yesterday was fire by the way.' You give a suprised thanks and look at her quizzically. You realize she was sitting from you when you were painting.")
                                time.sleep(2)
                                randl = input(
                                    "Those pants are better to be honest.' you say when you see she is wearing painted pants, shoes and jacket. 'Ehh i guess' she says, 'So umm, you wanna come over to our table and talk for a little?' 1.Yes 2.No")
                            if randl == "1":
                                print(
                                    "You say bye to Leaym and Ryan and walk with her to where she sits, at table in the corner of the cafeteria and talk with her until the bell rings. You realize shes actually pretty cool and could be a pretty good friend. You say bye to her, just to walk to the same music class.")
                                time.sleep(2)
                                print(
                                    "You sit next to her and you guys talk throughout the class even though Mr. Antaky tells you guys to be quiet multiple times")
                                time.sleep(2)
                                print(
                                    "The rest of the day flies by as you and your new found friends go through the day together. Once school is done there is an anouncement telling everyone that clubs are now open to join in the gym. You, Leaym and Ryan go find Jakie then you all go to the gym to look for a good club to join. You guys look around fo a while until you spot something in the back corner and it calls to you. You walk over and find out its the schools quidditch team, The Potters.")
                                time.sleep(2)
                                quid = input("Do you want to join 1.Yes 2.no")
                                if quid == "1":
                                    print(
                                        "You immediately fill out the application form then call over Jakie and the boys. Leaym and Ryan took one quisicall look the said 'Screw it and signed up too. Jakie was hesitant about it but you manages to convince her by saying 'I bet you ther's a Malfoy on the team too' since she said the had a fat crush on Drako Malfoy for some odd reason.")
                                    time.sleep(2)
                                if quid == "2":
                                    print("")
                            if randl == "2":
                                print(
                                    "You say 'Nah im good bruh' then Jakie says 'Oh ok well well see you later' and they walk away")
                                time.sleep(2)
                                print(
                                    "Ryan says you shoulda gone with them but you shrug and go back on Instagram waiting for the bell to ring. Once you get into music class you sit in a random seat and look around. Right next to you is Jakie looking at you laughing. You start laughing too, say whats up then you guys start talking getting to know each other better and you You realize shes actually pretty cool and could be a pretty good friend.")
                                time.sleep(2)
                                print("")
                                print("Popularity: " + str(popularity + 10))
                                print("")
                                print(
                                    "The rest of the day flies by as you and your new found friends go through the day together. Once school is done there is an anouncement telling everyone that clubs are now open to join in the gym. You, Leaym and Ryan go find Jakie then you all go to the gym to look for a good club to join. You guys look around fo a while until you spot something in the back corner and it calls to you. You walk over and find out its the schools quidditch team, The Potters.")
                                time.sleep(2)
                                quid = input("Do you want to join 1.Yes 2.no")
                                if quid == "1":
                                    print(
                                        "You immediately fill out the application form then call over Jakie and the boys. Leaym and Ryan took one quisicall look the said 'Screw it and signed up too. Jakie was hesitant about it but you manages to convince her by saying 'I bet you ther's a Malfoy on the team too' since she said the had a fat crush on Drako Malfoy for some odd reason.")
                                    time.sleep(2)
                                if quid == "2":
                                    print("")
                    if sell == "2":
                        print(
                            "You decline the weird dudes offer and continue skating home. When you get there you just flop on your bed and fall asleep shoes on and everything because you're so exausted ")
                        time.sleep(2)
                        print("Money: $" + str(money + middlemoney))
                        welp = input(
                            "You wake uap and its your second day of school, what do you wand to do? 1. Go to School. 2. View Stats")
                    if welp == "1":
                        print("")
                    if welp == "2":
                        stats()
                        statscho = input("Do yoy want to go to school now? 1. Yes 2. No")
                        if statscho == "1":
                            print(
                                "You gather your things by the door, skipping breakfast because you took so long trying to figure out what to wear. You head out for the day and as you are walking Jakie comes running around the corner at you and hugs you and asks if you are ok after yesterday.")
                            time.sleep(2)
                            print(
                                "You say you're fine and laugh it off then she says 'You know you would be the best FRIEND if you did that if i was even in a situation like that.' and laughs. You give a depressed laugh and stay mostly quiet for the rest of the walk to school and through your first 3 periods as she talks about herslef and clothes and girls she hates.")
                            time.sleep(2)
                            print("")
                            print("Happiness: " + str(happiness - 5))
                            print("")
                            print(
                                "During 4'th period lunch you are sitting with Jakie and her friends when two guys aproach you and one of them says 'Yo my guy that painting you did yesterday was fire by the way.' You give a suprised thanks and look at them quizzically. You realize its the two guys that were sitting next to you when you were painting. You remember the guy on the left name is Ryan and the one that was speaking to you is Leaym.")
                            time.sleep(2)
                            randl = input(
                                "I see you paint too.' you say when you see Leaym is wearing painted pants, shoes and jacket. 'Ehh i guess' he says, 'You wanna come over to our table and talk for a little?' 1.Yes 2.No")
                            if randl == "1":
                                print(
                                    "You say bye to Jakie and walk with them to their table corner of the cafeteria and talk tith them until the bell rings and then you say bye to them, just to walk to the same music class.")
                                time.sleep(2)
                                print(
                                    "You sit next to them and you guys talk throughout the class even though Mr. Antaky tells you guys to be quiet multiple times")
                                time.sleep(2)
                            if randl == "2":
                                print(
                                    "You say 'Nah im good bruh' then Ryan says 'Oh ok well well see you later' and they walk away")
                                time.sleep(2)
                                print(
                                    "Jakie says you shoulda gone with them but you shrug and go back on Instagram waiting for the bell to ring. Once you get into music class you sit in a random seat and look around. Right next to you is Leaym and Ryan looking at you laughing. You start laughing too, dap them up then you guys start talking getting to know each other better.")
                                time.sleep(2)
                                print("")
                                print("Popularity: " + str(popularity + 10))
                                print("")
                                print(
                                    "The day flies by as you and your new found friends go through the day together. Once school is done there is an anouncement telling everyone that clubs are now open to join in the gym. You, Leaym and Ryan go find Jakie then you all go to the gyl to look for a good club to join. You guys look around fo a while until you spot something in the back corner and it calls to you. You walk over and find out its the schools quidditch team, The Potters.")
                                time.sleep(2)
                                quid = input("Do you want to join 1.Yes 2.no")
                                if quid == "1":
                                    print(
                                        "You immediately fill out the application form then call over Jakie and the boys. Leaym and Ryan took one quisicall look the said 'Screw it and signed up too. Jakie was hesitant about it but you manages to convince her by saying 'I bet you ther's a Malfoy on the team too' since she said the had a fat crush on Drako Malfoy for some odd reason.")
                                    time.sleep(2)
                                if quid == "2":
                                    print("")
            if nojakie == "2":
                print(
                    "You say 'She looked too good for me' then chuckle They look at you in disbelief then the guy on the right says 'Bro you looks like the male version of her but whatever.' The guy on the left yells 'TRUUUE.' and starts laughing.")
                time.sleep(2)
                print(
                    "The guy on the right then says 'Im Ryan and this is Leaym by the way' you say 'Cool im " + name + ".' they laugh and you guys continue talking until first period starts.")
                time.sleep(2)
                print("")
                print("Popularity: " + str(popularity + 10))
                time.sleep(3)
                print(
                    "You three have English and history for two periods so you spend that time joking around and talking too.")
                time.sleep(3)
                print(
                    "It's last period, art, the room is set up with a lot of easels and canvases in a circle and the teacher is standing in the middle. Class starts and everyone is told to paint something, you paint Reptar and think it's pretty nice until a short, very skinny kid comes and scribbles black paint all over it and says 'It was $h!# anyway.'")
                time.sleep(2)
                art = input("What will you do? 1. Confront them. 2. Turn their sabotage into something beautiful.")
                if art == "1":
                    print(
                        "You stand up and Hisoka uppercut the small kid, he goes flying and everyone just stares at you. You then look around and grab your stuff and the painting and run out of school and rush home.")
                    print("")
                    print("Popularity: " + str(popularity + 15))
                    print("Fitness: " + str(fitness + 5))
                    print("")
                    time.sleep(3)
                    print("See I appreciate you doing that but you got suspended.")
                    print("G A M E O V E R")
                    exit()
                if art == "2":
                    print(
                        "You look at the kid that sabotaged your beautiful piece, think about Hiskoa punching him, then look back at your art and let your mind go free with no limits. Once the bell rings you finnaly wake up from your artistic trance and look at your beautiful masterpiece. 'Damn I kinda snapped' You mumble as you are walking out of the building.")
                    time.sleep(2)
                    print(
                        "As you are walking home a hipster looking guy stops you and asks to see your art. He looks amazed and offers you $100 for it.")
                    sell = input("Will you sell it? 1. Yes 2.No")
                    if sell == "1":
                        print(
                            "The man hands you a crisp $100 bill and you hand him the painting and then stand there amazed. After a while you start skating home.")
                        print("")
                        print("Money: $" + str(money + 100))
                        print("")
                        time.sleep(4)
                        print("Money: $" + str(money + middlemoney))
                        welp = input(
                            "You wake uap and its your second day of school, what do you wand to do? 1. Go to School. 2. View Stats")
                        if welp == "1":
                            print("")
                        if welp == "2":
                            stats()
                            statscho = input("Do yoy want to go to school now? 1. Yes 2. No")
                            if statscho == "1":
                                print(
                                    "You gather your things by the door, skipping breakfast because you took so long trying to figure out what to wear. You head out for the day and as you are walking Leaym and ryan comes running around the corner at you, dap you up and start asking you questions about yesterday.")
                                time.sleep(2)
                                print(
                                    "You say you're fine and laugh it off then Leaym says 'If thats what it takes to get you go to go Picasso then i happily do it all damn day.' and laughs. You give a depressed laugh and stay mostly quiet for the rest of the walk to school, because you donte even like painting, thinking about it makes you depressed. So you just listen to them talk through your first 3 periods as they talk about games and clothes and girls.")
                                time.sleep(2)
                                print("")
                                print("Happiness: " + str(happiness - 5))
                                print("")
                                print(
                                    "During 4'th period lunch you are sitting with Leaym and his friends when Jakie aproaches you and says 'Yo that painting you did yesterday was fire by the way.' You give a suprised thanks and look at her quizzically. You realize she was sitting from you when you were painting.")
                                time.sleep(2)
                                randl = input(
                                    "Those pants are better to be honest.' you say when you see she is wearing painted pants, shoes and jacket. 'Ehh i guess' she says, 'So umm, you wanna come over to our table and talk for a little?' 1.Yes 2.No")
                            if randl == "1":
                                print(
                                    "You say bye to Leaym and Ryan and walk with her to where she sits, at table in the corner of the cafeteria and talk with her until the bell rings. You realize shes actually pretty cool and could be a pretty good friend. You say bye to her, just to walk to the same music class.")
                                time.sleep(2)
                                print(
                                    "You sit next to her and you guys talk throughout the class even though Mr. Antaky tells you guys to be quiet multiple times")
                                time.sleep(2)
                                print(
                                    "The rest of the day flies by as you and your new found friends go through the day together. Once school is done there is an anouncement telling everyone that clubs are now open to join in the gym. You, Leaym and Ryan go find Jakie then you all go to the gym to look for a good club to join. You guys look around fo a while until you spot something in the back corner and it calls to you. You walk over and find out its the schools quidditch team, The Potters.")
                                time.sleep(2)
                                quid = input("Do you want to join 1.Yes 2.no")
                                if quid == "1":
                                    print(
                                        "You immediately fill out the application form then call over Jakie and the boys. Leaym and Ryan took one quisicall look the said 'Screw it and signed up too. Jakie was hesitant about it but you manages to convince her by saying 'I bet you ther's a Malfoy on the team too' since she said the had a fat crush on Drako Malfoy for some odd reason.")
                                    time.sleep(2)
                                if quid == "2":
                                    print("")
                            if randl == "2":
                                print(
                                    "You say 'Nah im good bruh' then Jakie says 'Oh ok well well see you later' and they walk away")
                                time.sleep(2)
                                print(
                                    "Ryan says you shoulda gone with them but you shrug and go back on Instagram waiting for the bell to ring. Once you get into music class you sit in a random seat and look around. Right next to you is Jakie looking at you laughing. You start laughing too, say whats up then you guys start talking getting to know each other better and you You realize shes actually pretty cool and could be a pretty good friend.")
                                time.sleep(2)
                                print("")
                                print("Popularity: " + str(popularity + 10))
                                print("")
                                print(
                                    "The rest of the day flies by as you and your new found friends go through the day together. Once school is done there is an anouncement telling everyone that clubs are now open to join in the gym. You, Leaym and Ryan go find Jakie then you all go to the gym to look for a good club to join. You guys look around fo a while until you spot something in the back corner and it calls to you. You walk over and find out its the schools quidditch team, The Potters.")
                                time.sleep(2)
                                quid = input("Do you want to join 1.Yes 2.no")
                                if quid == "1":
                                    print(
                                        "You immediately fill out the application form then call over Jakie and the boys. Leaym and Ryan took one quisicall look the said 'Screw it and signed up too. Jakie was hesitant about it but you manages to convince her by saying 'I bet you ther's a Malfoy on the team too' since she said the had a fat crush on Drako Malfoy for some odd reason.")
                                    time.sleep(2)
                                if quid == "2":
                                    print("")
                    if sell == "2":
                        print(
                            "You decline the weird dudes offer and continue skating home. When you get there you just flop on your bed and fall asleep shoes on and everything because you're so exausted ")
                        time.sleep(2)
                        print("Money: $" + str(money + middlemoney))
                        welp = input(
                            "You wake uap and its your second day of school, what do you wand to do? 1. Go to School. 2. View Stats")
                        if welp == "1":
                            print("")
                        if welp == "2":
                            stats()
                            statscho = input("Do yoy want to go to school now? 1. Yes 2. No")
                        if statscho == "1":
                            print(
                                "You gather your things by the door, skipping breakfast because you took so long trying to figure out what to wear. You head out for the day and as you are walking Jakie comes running around the corner at you and hugs you and asks if you are ok after yesterday.")
                            time.sleep(2)
                            print(
                                "You say you're fine and laugh it off then she says 'You know you would be the best FRIEND if you did that if i was even in a situation like that.' and laughs. You give a depressed laugh and stay mostly quiet for the rest of the walk to school and through your first 3 periods as she talks about herslef and clothes and girls she hates.")
                            time.sleep(2)
                            print("")
                            print("Happiness: " + str(happiness - 5))
                            print("")
                            print(
                                "During 4'th period lunch you are sitting with Jakie and her friends when two guys aproach you and one of them says 'Yo my guy that painting you did yesterday was fire by the way.' You give a suprised thanks and look at them quizzically. You realize its the two guys that were sitting next to you when you were painting. You remember the guy on the left name is Ryan and the one that was speaking to you is Leaym.")
                            time.sleep(2)
                            randl = input(
                                "I see you paint too.' you say when you see Leaym is wearing painted pants, shoes and jacket. 'Ehh i guess' he says, 'You wanna come over to our table and talk for a little?' 1.Yes 2.No")
                            if randl == "1":
                                print(
                                    "You say bye to Jakie and walk with them to their table corner of the cafeteria and talk tith them until the bell rings and then you say bye to them, just to walk to the same music class.")
                                time.sleep(2)
                                print(
                                    "You sit next to them and you guys talk throughout the class even though Mr. Antaky tells you guys to be quiet multiple times")
                                time.sleep(2)
                            if randl == "2":
                                print(
                                    "You say 'Nah im good bruh' then Ryan says 'Oh ok well well see you later' and they walk away")
                                time.sleep(2)
                                print(
                                    "Jakie says you shoulda gone with them but you shrug and go back on Instagram waiting for the bell to ring. Once you get into music class you sit in a random seat and look around. Right next to you is Leaym and Ryan looking at you laughing. You start laughing too, dap them up then you guys start talking getting to know each other better.")
                                time.sleep(2)
                                print("")
                                print("Popularity: " + str(popularity + 10))
                                print("")
                                print(
                                    "The day flies by as you and your new found friends go through the day together. Once school is done there is an anouncement telling everyone that clubs are now open to join in the gym. You, Leaym and Ryan go find Jakie then you all go to the gyl to look for a good club to join. You guys look around fo a while until you spot something in the back corner and it calls to you. You walk over and find out its the schools quidditch team, The Potters.")
                                time.sleep(2)
                                quid = input("Do you want to join 1.Yes 2.no")
                                if quid == "1":
                                    print(
                                        "You immediately fill out the application form then call over Jakie and the boys. Leaym and Ryan took one quisicall look the said 'Screw it and signed up too. Jakie was hesitant about it but you manages to convince her by saying 'I bet you ther's a Malfoy on the team too' since she said the had a fat crush on Drako Malfoy for some odd reason.")
                                    time.sleep(2)
                                if quid == "2":
                                    print("")
    if dayone == "2":
        print(
            "You just stand there looking awkward until the bell ring. No one aproaces you but you get a lot of weird and intrested looks")
        time.sleep(2)
        print("")
        print("Happiness: " + str(happiness - 5))
        print("")
        time.sleep(3)
        enddone = input("The day is done and you made no friends, but you can: 1. Go join a sports club or 2. Go home ")
        if enddone == "1":
            print(
                "You go to the gym where all the clubs are shown off and look around to see if there anything you like. You see one that really peaks you intrest, its Quidditch. You grab a flyer and run to the field outside where the team is meeting and have a great time with your new teamates.")
            print("")
            print("Popularity: " + str(popularity + 5))
            print("Happiness: " + str(happiness + 5))
            print("")
            time.sleep(2)
            print(
                "It is now March 2017, the new semester has started and you are taking you're nice walk to school, listening to 'Lil Uzi Vert Vs The World' when two of your teamate come running up to you, its Dillon and Francis.")
        if enddone == "2":
            print("You go home and sulk in bed waiting to see what awaits you tomorrow.")

    else:
        print("Invalid choice, try again.")
elif answer == "2":
    print("")
    stats()
    print("")
    print("1. Wake up and get ready.")
    answer2 = input("What would you like to do?")
    print("")
    if answer2 == "1":
        print(
            "As you start rushing out of your house in the lovely suburbs you call home, you yell out goodbye to whoever is listening. Once you get outside you hop on your skateboard and start skating down the road to school.")
        print("")
        time.sleep(2)
        print(
            "You reach school before the first bell rings and all the students are waiting outside. Some talking some doing that awkward greeting to make new friends and some just sitting around doing 'nothing'.")
        time.sleep(2)
        print("You have 3 choices.")
        print("1. Go Try to talk to some people")
        print("2. Just stand there looking at people until the bell rings")
        dayone = input("what will you choose")
        print("")
        time.sleep(2)
        if dayone == "1":
            print(
                "Before you can go to one of the groups of people talking someone behind you says 'Ok I see you.' and laughs. You turn around and a cute asian girl with a skateboard is standing there. She's wearing Off-White 1's, bell bottoms, a crop top and a shirt over it.")
            time.sleep(2)
            jakie = input(" Do you want to be friends with her? 1. Yes or 2. No")
            if jakie == "1":
                print((
                                  "You just try to play it off cool and say 'Like you're one to speak.' she rolls her eyes and says 'My name is Jakie, what about you?' say 'Oh my name is " + name + ".' She laughs again and then you continue talking until the bell for first period rings."))
                time.sleep(2)
                print("")
                time.sleep(2)
                enddone = input(
                    "The day is done and you made no friends, but you can: 1. Go join a sports club or 2. Go home ")
                if enddone == "1":
                    print(
                        "You go to the gym where all the clubs are shown off and look around to see if there anything you like. You see one that really peaks you intrest, its Quidditch. You grab a flyer and run to the field outside where the team is meeting and have a great time with your new teamates.")
                    time.sleep(2)
                    print("")
                    print("Popularity: " + str(popularity + 5))
                    print("Happiness: " + str(happiness + 5))
                    print("")
                    time.sleep(2)
                    print(
                        "It is now March 2017, the new semester has started and you are taking you're nice walk to school, listening to 'Lil Uzi Vert Vs The World' when two of your teamate come running up to you, its Dillon and Francis.")
                if enddone == "2":
                    print("You go home and sulk in bed waiting to see what awaits you tomorrow.")
            if jakie == "2":
                print(
                    "You give a annoyed scoff then turn around and walk away to find someone to talk to. Before you fully leave you hear a girl say 'What happend there Jakie?' to the asian girl. ")
                time.sleep(2)
                print(
                    "You approach two guys talking not far from where you were standing and say 'Yo what up boys.' They look at you and laugh and one of them says 'Why the hell did you just blow off Jakie like that?.'")
                time.sleep(2)
                print("")
                print("1. I don't know man I was getting bad vibes.")
                print("2. She looked too good for me")
                nojakie = input("Option 1 or 2?")
                if nojakie == "1":
                    print(
                        "You say 'I don't know man I was getting bad vibes.' They look at you in disbelief then the guy on the right says 'Bro you looks like the male version of her but whatever.' The guy on the lefy yells 'TRUUUE.' and starts laughing.")
                    time.sleep(2)
                    print(
                        "The guy on the right then says 'Im Ryan and this is Leaym by the way' you say 'Cool im " + name + ".' they laugh and you guys continue talking until first period starts.")
                    time.sleep(2)
                if nojakie == "2":
                    print(
                        "You say 'She looked too good for me' then chuckle They look at you in disbelief then the guy on the right says 'Bro you looks like the male version of her but whatever.' The guy on the left yells 'TRUUUE.' and starts laughing.")
                    time.sleep(2)
                    print(
                        "The guy on the right then says 'Im Ryan and this is Leaym by the way' you say 'Cool im " + name + ".' they laugh and you guys continue talking until first period starts.")
                    time.sleep(2)
                    print("")
                    print("Popularity: " + str(popularity + 10))
                    time.sleep(3)
                    print(
                        "You three have English and history for two periods so you spend that time joking around and talking too.")
                    time.sleep(3)
                    print(
                        "It's last period, art, the room is set up with a lot of easels and canvases in a circle and the teacher is standing in the middle. Class starts and everyone is told to paint something, you paint Reptar and think it's pretty nice until a short, very skinny kid comes and scribbles black paint all over it and says 'It was $h!# anyway.'")
                    time.sleep(2)
                    art = input("What will you do? 1. Confront them. 2. Turn their sabotage into something beautiful.")
                    if art == "1":
                        print(
                            "You stand up and Hisoka uppercut the small kid, he goes flying and everyone just stares at you. You then look around and grab your stuff and the painting and run out of school and rush home.")
                        print("")
                        print("Popularity: " + str(popularity + 15))
                        print("Fitness: " + str(fitness + 5))
                        print("")
                        time.sleep(3)
                        print("See I appreciate you doing that but you got suspended.")
                        print("G A M E O V E R")
                        exit()
                    if art == "2":
                        print(
                            "You look at the kid that sabotaged your beautiful piece, think about Hiskoa punching him, then look back at your art and let your mind go free with no limits. Once the bell rings you finnaly wake up from your artistic trance and look at your beautiful masterpiece. 'Damn I kinda snapped' You mumble as you are walking out of the building.")
                        time.sleep(2)
                        print(
                            "As you are walking home a hipster looking guy stops you and asks to see your art. He looks amazed and offers you $100 for it.")
                        sell = input("Will you sell it? 1. Yes 2.No")
                    if sell == "1":
                        print(
                            "The man hands you a crisp $100 bill and you hand him the painting and then stand there amazed. After a while you start skating home.")
                        print("")
                        print("Money: $" + str(money + 100))
                        print("")
                        time.sleep(4)
                        print("Money: $" + str(money + middlemoney))
                        welp = input(
                            "You wake uap and its your second day of school, what do you wand to do? 1. Go to School. 2. View Stats")
                        if welp == "1":
                            print("")
                        if welp == "2":
                            stats()
                            statscho = input("Do yoy want to go to school now? 1. Yes 2. No")
                            if statscho == "1":
                                print(
                                    "You gather your things by the door, skipping breakfast because you took so long trying to figure out what to wear. You head out for the day and as you are walking Leaym and ryan comes running around the corner at you, dap you up and start asking you questions about yesterday.")
                                time.sleep(2)
                                print(
                                    "You say you're fine and laugh it off then Leaym says 'If thats what it takes to get you go to go Picasso then i happily do it all damn day.' and laughs. You give a depressed laugh and stay mostly quiet for the rest of the walk to school, because you donte even like painting, thinking about it makes you depressed. So you just listen to them talk through your first 3 periods as they talk about games and clothes and girls.")
                                time.sleep(2)
                                print("")
                                print("Happiness: " + str(happiness - 5))
                                print("")
                                print(
                                    "During 4'th period lunch you are sitting with Leaym and his friends when Jakie aproaches you and says 'Yo that painting you did yesterday was fire by the way.' You give a suprised thanks and look at her quizzically. You realize she was sitting from you when you were painting.")
                                time.sleep(2)
                                randl = input(
                                    "Those pants are better to be honest.' you say when you see she is wearing painted pants, shoes and jacket. 'Ehh i guess' she says, 'So umm, you wanna come over to our table and talk for a little?' 1.Yes 2.No")
                            if randl == "1":
                                print(
                                    "You say bye to Leaym and Ryan and walk with her to where she sits, at table in the corner of the cafeteria and talk with her until the bell rings. You realize shes actually pretty cool and could be a pretty good friend. You say bye to her, just to walk to the same music class.")
                                time.sleep(2)
                                print(
                                    "You sit next to her and you guys talk throughout the class even though Mr. Antaky tells you guys to be quiet multiple times")
                                time.sleep(2)
                                print(
                                    "The rest of the day flies by as you and your new found friends go through the day together. Once school is done there is an anouncement telling everyone that clubs are now open to join in the gym. You, Leaym and Ryan go find Jakie then you all go to the gym to look for a good club to join. You guys look around fo a while until you spot something in the back corner and it calls to you. You walk over and find out its the schools quidditch team, The Potters.")
                                time.sleep(2)
                                quid = input("Do you want to join 1.Yes 2.no")
                                if quid == "1":
                                    print(
                                        "You immediately fill out the application form then call over Jakie and the boys. Leaym and Ryan took one quisicall look the said 'Screw it and signed up too. Jakie was hesitant about it but you manages to convince her by saying 'I bet you ther's a Malfoy on the team too' since she said the had a fat crush on Drako Malfoy for some odd reason.")
                                    time.sleep(2)
                                if quid == "2":
                                    print("")
                            if randl == "2":
                                print(
                                    "You say 'Nah im good bruh' then Jakie says 'Oh ok well well see you later' and they walk away")
                                time.sleep(2)
                                print(
                                    "Ryan says you shoulda gone with them but you shrug and go back on Instagram waiting for the bell to ring. Once you get into music class you sit in a random seat and look around. Right next to you is Jakie looking at you laughing. You start laughing too, say whats up then you guys start talking getting to know each other better and you You realize shes actually pretty cool and could be a pretty good friend.")
                                time.sleep(2)
                                print("")
                                print("Popularity: " + str(popularity + 10))
                                print("")
                                print(
                                    "The rest of the day flies by as you and your new found friends go through the day together. Once school is done there is an anouncement telling everyone that clubs are now open to join in the gym. You, Leaym and Ryan go find Jakie then you all go to the gym to look for a good club to join. You guys look around fo a while until you spot something in the back corner and it calls to you. You walk over and find out its the schools quidditch team, The Potters.")
                                time.sleep(2)
                                quid = input("Do you want to join 1.Yes 2.no")
                                if quid == "1":
                                    print(
                                        "You immediately fill out the application form then call over Jakie and the boys. Leaym and Ryan took one quisicall look the said 'Screw it and signed up too. Jakie was hesitant about it but you manages to convince her by saying 'I bet you ther's a Malfoy on the team too' since she said the had a fat crush on Drako Malfoy for some odd reason.")
                                    time.sleep(2)
                                if quid == "2":
                                    print("")
                    if sell == "2":
                        print(
                            "You decline the weird dudes offer and continue skating home. When you get there you just flop on your bed and fall asleep shoes on and everything because you're so exausted ")
                        time.sleep(2)
                        print("Money: $" + str(money + middlemoney))
                        welp = input(
                            "You wake uap and its your second day of school, what do you wand to do? 1. Go to School. 2. View Stats")
                        if welp == "1":
                            print("")
                        if welp == "2":
                            stats()
                            statscho = input("Do yoy want to go to school now? 1. Yes 2. No")
                        if statscho == "1":
                            print(
                                "You gather your things by the door, skipping breakfast because you took so long trying to figure out what to wear. You head out for the day and as you are walking Jakie comes running around the corner at you and hugs you and asks if you are ok after yesterday.")
                            time.sleep(2)
                            print(
                                "You say you're fine and laugh it off then she says 'You know you would be the best FRIEND if you did that if i was even in a situation like that.' and laughs. You give a depressed laugh and stay mostly quiet for the rest of the walk to school and through your first 3 periods as she talks about herslef and clothes and girls she hates.")
                            time.sleep(2)
                            print("")
                            print("Happiness: " + str(happiness - 5))
                            print("")
                            print(
                                "During 4'th period lunch you are sitting with Jakie and her friends when two guys aproach you and one of them says 'Yo my guy that painting you did yesterday was fire by the way.' You give a suprised thanks and look at them quizzically. You realize its the two guys that were sitting next to you when you were painting. You remember the guy on the left name is Ryan and the one that was speaking to you is Leaym.")
                            time.sleep(2)
                            randl = input(
                                "I see you paint too.' you say when you see Leaym is wearing painted pants, shoes and jacket. 'Ehh i guess' he says, 'You wanna come over to our table and talk for a little?' 1.Yes 2.No")
                            if randl == "1":
                                print(
                                    "You say bye to Jakie and walk with them to their table corner of the cafeteria and talk tith them until the bell rings and then you say bye to them, just to walk to the same music class.")
                                time.sleep(2)
                                print(
                                    "You sit next to them and you guys talk throughout the class even though Mr. Antaky tells you guys to be quiet multiple times")
                                time.sleep(2)
                            if randl == "2":
                                print(
                                    "You say 'Nah im good bruh' then Ryan says 'Oh ok well well see you later' and they walk away")
                                time.sleep(2)
                                print(
                                    "Jakie says you shoulda gone with them but you shrug and go back on Instagram waiting for the bell to ring. Once you get into music class you sit in a random seat and look around. Right next to you is Leaym and Ryan looking at you laughing. You start laughing too, dap them up then you guys start talking getting to know each other better.")
                                time.sleep(2)
                                print("")
                                print("Popularity: " + str(popularity + 10))
                                print("")
                                print(
                                    "The day flies by as you and your new found friends go through the day together. Once school is done there is an anouncement telling everyone that clubs are now open to join in the gym. You, Leaym and Ryan go find Jakie then you all go to the gyl to look for a good club to join. You guys look around fo a while until you spot something in the back corner and it calls to you. You walk over and find out its the schools quidditch team, The Potters.")
                                time.sleep(2)
                                quid = input("Do you want to join 1.Yes 2.no")
                                if quid == "1":
                                    print(
                                        "You immediately fill out the application form then call over Jakie and the boys. Leaym and Ryan took one quisicall look the said 'Screw it and signed up too. Jakie was hesitant about it but you manages to convince her by saying 'I bet you ther's a Malfoy on the team too' since she said the had a fat crush on Drako Malfoy for some odd reason.")
                                    time.sleep(2)
                                if quid == "2":
                                    print("")
        if dayone == "2":
            print(
                "You just stand there looking awkward until the bell ring. No one aproaces you but you get a lot of weird and intrested looks")
            time.sleep(2)
            print("")
            print("Happiness: " + str(happiness - 5))
            print("")
            time.sleep(3)
            enddone = input(
                "The day is done and you made no friends, but you can: 1. Go join a sports club or 2. Go home ")
            if enddone == "1":
                print(
                    "You go to the gym where all the clubs are shown off and look around to see if there anything you like. You see one that really peaks you intrest, its Quidditch. You grab a flyer and run to the field outside where the team is meeting and have a great time with your new teamates.")
                time.sleep(2)
                print("")
                print("Popularity: " + str(popularity + 5))
                print("Happiness: " + str(happiness + 5))
                print("")
                time.sleep(2)
                print(
                    "It is now March 2017, the new semester has started and you are taking you're nice walk to school, listening to 'Lil Uzi Vert Vs The World' when two of your teamate come running up to you, its Dillon and Francis.")
                time.sleep(2)
            if enddone == "2":
                print("You go home and sulk in bed waiting to see what awaits you tomorrow.")
        else:
            print("Invalid choice, try again.")
    else:
        print("Invalid choice, try again.")
else:
    print("Invalid choice, try again.")
