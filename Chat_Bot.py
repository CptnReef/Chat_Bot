from random import choice

user_response = ""

def get_mood_bot_response(user_response):

    happy = ["Oh yeah?! Then I implore you to finish my sentence? (yes/no/maybe?)","Great to hear! Knock, Knock?! (ask me 'who's there')"]
    orelse =  ["Everything will get easier!","You take care, okay.","Bye for now"]

    if user_response == "happy":
        if user_response == "happy":
            print(choice(happy))
            user_response = input("")

            if happy[0] and user_response == "yes":
                print("Roses are ___")
                user_response = input("")

                if user_response == "red":
                    print("violets are ____")
                    user_response = input("")
                
                    if user_response == "blue":
                        print("I heart you!")
                        return
                    else:
                        print("that's not a violet, baby")
                else:
                    print("that's not a rose, honey")
            elif happy[0] and user_response == "no":
                return print("That's ok. It's been a pleasure!")
            elif happy[0] and user_response == "maybe":
                return print("hm... it's okay if you don't. Take it easy!")
            elif happy[1] and user_response == "who's there" or user_response == "who's there?":
                print("what would you do")
                user_response = input("")
                if user_response == "what would you do, who" or user_response == "what would you do, who?" or user_response == "what would you do who?":
                    return print("What would you do-woo-woo- for a kondak bar")
            elif happy[1] and user_response != "who's there" or happy[1] and user_response != "who's there?":
                return print("Ugh-....")
            elif user_response == "done":
                return print("Good-Bye!")
            else:
                return print("...?")
        return choice(happy)
    else:
        return print(choice(orelse))

print("Welcome! Don't be a stranger, I'm Chat Bot")
print("Tell me how you're feeling?")

user_response = ""

while True:
    doneChat = ["Bye!","Later!","Sayonara","Peace"]
    okay = ["oki-dokey! Please enjoy the rest of your day.","good to hear. See you later!","ofcourse, take care!"]
    sad = ["sorry to hear that...", "hope everything gets better.","take care."]
    user_response = input("How are you feeling today?: ")

    if user_response == "done":
        print(choice(doneChat))
        break
    elif user_response == "okay":
        if user_response == "okay":
            print(choice(okay))
            break
    elif user_response == "sad":
        if user_response == "sad":
            print(choice(sad))
            break
    elif user_response != "okay" or user_response != "sad" or user_response != "done":
        print("\n")
    bot_response = get_mood_bot_response(user_response)
    print(bot_response)
  
