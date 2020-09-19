import random

# these are the bot responses to the mood user inputs.
happy = ["Super-D-Duper! How about helping me finishing this poem? (yes/no/maybe)","Oh yeah?! Then I implore you to finish my sentence? (yes/no/maybe?)","Great to hear! Knock, Knock?! (ask me 'who's there')"]
okay = ["oki-dokey! Please enjoy the rest of your day.","good to hear. See you later!","ofcourse, take care!"]
sad = ["sorry to hear that...", "hope everything gets better.","take care."]
i = 0

def get_bot_response(user_response):
    bot_response = input("")
    return  bot_response

# Just made a countdown until it calls for the 'get_bot_response' function

while i <= 3:
    i = int(i) + 1

    if i <= 3:
        print("..." + str(i))
    
    elif i == 3 or i > 3:
        print("\nHello human, How are you feeling? (happy/okay/sad?)")
        response = get_bot_response("")

        if response == "happy":
            print(random.choice(happy))
            response = input("")
                
            if happy[0] and response == "yes":
                print("Roses are ___")
                response == input("")
                if response == "red":
                    print("violets are ____")
                    response == input("")
                    if response == "blue":
                        print("I heart you!")
                    else:
                        print("that's not a violet, baby")                        
                else:
                    print("that's not a rose, honey")
                    
            elif happy[0] and response == "no":
                print("That's ok. It's been a pleasure!")
            elif happy[0] and response == "maybe":
                print("hm... it's okay if you don't. Take it easy!")
            elif happy[1] and response == "yes":
                print("tsting")
            elif happy[1] and response == "no":
                print("ts22")
            elif happy[2] and response == "who's there" or response == "who's there?":
                print("what would you do")
                response = input("")
                if response == "what would you do, who" or response == "what would you do, who?" or response == "what would you do who?":
                    print("What would you do-woo-woo- for a kondak bar")
            elif happy[2] and response != "who's there" or response != "who's there":
                print("Ugh-....")
            elif response == "done":
                print("Good-Bye!")
                
            else:
                print("...?")
                

        elif response == "okay":
            print(random.choice(okay))
        elif response == "sad":
            print(random.choice(sad))
        elif response != "happy" or response != "okay" or response != "sad":
            print("\nI don't understand. Are you done?")
            response = input("")

            if response == "yes" or response == "done" or response == "I'm done" or response == "I am done":
                print("Have a good day!!!")
            elif response == "no":
                print("Let's try again \n")
            else:
                print("Type in 'done' to ESC!!!\n")
                
                
