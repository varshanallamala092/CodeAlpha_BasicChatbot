def chatbot():

    print(" Namaste Welcome to Chatbot!")

    while True:

        user = input("MOON: ").lower()

        if user == "hello":
            print("STAR: Hi!")

        elif user == "how are you":
            print("STAR: I'm fine, thanks!")

        elif user == "bye":
            print("STAR: Goodbye!")
            break

        else:
            print("STAR: Sorry, I don't understand.")

chatbot()