import random   

print("==Welcome to The CHAT BABA==")

while True:
    message = input("USER: ").strip().lower()
    greetings = ["hello", "hi", "hey", "hlo"]

    if any(word in message.split() for word in greetings):
        respones = ["Hey, how can i help you" , "Hello, my friend ,how can i help you",
                    "Namaste, how can i help you"]
        print("BOT: ",random.choice(respones))
    elif message in ["how are you?", "how have you been?" , "baba how are you?" ]:
        respones = ["I'm doing great , how can i help you" , "Great, how can i help you "]
        print("BOT: ",random.choice(respones))
    elif message in ["what is your name?" , "your name?" , "name?"]:
        respones = ["My name is BABA , how can I help you" , "Name's BABA ,how can I help you" ]
        print("BOT: ",random.choice(respones))
    elif message in ["thank you", "thanks" , "thanks baba" , "thank you baba"]:
        responses = ["You're welcome!", "Welcome, my friend!", "Happy to help!"]
        print("BOT:", random.choice(responses))
    elif  message in ["baba" , "baba is it?" , "baba, nice name" , "nice name"]:
        respones = ["Yes, how can i help you" , "That's right , how can i help you" , "Hmmm , how can I help you"]
        print("BOT: ",random.choice(respones))
    elif message == "help":
        commands =["Hello" , "How are you?" , "What is your name" , "Thanks" , "bye"] 
        print ("BOT: You can ask me :-")
        for command in commands:
            print(command)
    elif message == "bye" or message == "nothing bye" :
        print("BOT: bye")
        break
    else:
        print("BOT: sorry, I dont understand.")
