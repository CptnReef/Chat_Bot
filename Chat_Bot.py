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
  
#   print(bot_response)
# from random import choice


# def get_mood_bot_response(user_response):

#     happy = ["Super-D-Duper! How about helping me finishing this poem? (yes/no/maybe)","Oh yeah?! Then I implore you to finish my sentence? (yes/no/maybe?)","Great to hear! Knock, Knock?! (ask me 'who's there')"]
#     okay = ["oki-dokey! Please enjoy the rest of your day.","good to hear. See you later!","ofcourse, take care!"]
#     sad = ["sorry to hear that...", "hope everything gets better.","take care."]
#     or_else =  ["Everything will get easier!","You take care, okay.","Bye for now"]

#     if user_response == "happy":
#         return choice(happy)
#     elif user_response == "okay":
#         return choice(okay)
#     elif user_response == "sad":
#         return choice(sad)
#     else:
#         return choice(or_else)

# print("\nTell me how you feeling?: ")
  
# print("Welcome! Don't be a stranger, I'm Chat Bot")

# while True:
#     doneChat = ["Bye!","Later!","Sayonara","Peace"]
#     user_response = input()
#     bot_response = get_mood_bot_response(user_response)

#     if user_response == "done":
#         print(choice(doneChat))
#         break

#     elif user_response == "okay":
#         break
#     elif user_response == "sad":
#         break

#     elif user_response == "yes":
#         print("Roses are ___")
#         user_response = input("")
#         if user_response == "red":
#             print("violets are ____")
#             user_response = input("")
#             if user_response == "blue":
#                 print("I heart you!")
#                 break
#             else:
#                 print("that's not a violet, baby")
#                 continue                      
#         else:
#             print("that's not a rose, honey")
#             continue

#     elif user_response == "who's there" or user_response == "who's there?":
#         print("what would you do")
#         user_response = input("")
#         if user_response == "what would you do, who" or user_response == "what would you do, who?" or user_response == "what would you do who?":
#             print("What would you do-woo-woo- for a kondak bar")
#             if user_response != "who's there?" or user_response != "who's there":
#                 print("Ugh-....")
#             elif user_response == "done":
#                 print("Good-Bye!")                

#     elif user_response != "happy" or user_response != "okay" or user_response != "sad":
#         print("\nI don't understand. Are you done?")
#         user_response = input("")
#         if user_response == "yes" or user_response == "done" or user_response == "I'm done" or user_response == "I am done":
#             print("Have a good day!!!")
#             continue
#         elif user_response == "no":
#             print("Let's try again \n")
#             continue
#         else:
#             print("Type in 'done' to ESC!!!\n")
#             continue

#     print(bot_response)
