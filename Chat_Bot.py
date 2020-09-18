happy_chat = 0
okay_chat = 0
sad_chat = 0

def get_bot_response(user_response):
    print("Hi! How are you feeling, pal?")
    choice = input()
    
    if choice == "happy":
        print("Beautiful! Then would you like to help me finish poem?")
        choice1 = input()

        if choice1 == "yes":
            happy_chat = get_bot_response_happy("")

        elif choice1 == "no":
            print("No sweat. Please continue to have a blessed day, -Goodbye!")
        
        else: range(print("hmm-? I'll take that as no. That's fine!"))

    elif choice == "okay":
        print("Buddy are you okay? Are you okay, buddy? Because you've been hit by- You've been shot by- a ____")
        okay_chat = get_bot_response_okay("")

    elif choice == "sad":
        choices = ["I'm sorry to hear that...", "...", "Breathe easy, please."]
        saychoices = choices.len
        let i in range(saychoices):
            print (choices)

    return choice

def get_bot_response_happy(user_response_happy):
    print("Please help me finish this sen___ ")
    chat = input()

    if chat == "tence":
        print("You smart! Ok, let's move on!\n")
        print("Roses are ____ ")
        chat = input()

        if chat == "red":
            print("violets are ____ ")
            newchat = input()

            if newchat == "blue":
                print("I heart you")
            
            else: print("that's not a violet, baby...")


        elif chat != "red":
            print("that's not a rose, honey...")


        else: print("\n rip for roses")

    else: print("sayonara")

    return chat

chat_bot = get_bot_response("")
