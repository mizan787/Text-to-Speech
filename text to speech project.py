import pyttsx3
import speech_recognition as sr

# ---------- Text to Speech ----------
engine = pyttsx3.init()
engine.setProperty("rate", 90)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------- Speech to Text ----------
listener = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening... Speak now")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)

        text = listener.recognize_google(audio)
        print("You said:", text)
        return text

    except:
        print("Sorry, couldn't hear you")
        return ""

# ---------- Main Menu ----------
while True:

    print("\nChoose an option:")
    print("1. Text to Speech")
    print("2. Speech to Text")
    print("3. Exit")

    choice = input("Enter 1, 2 or 3: ")

    if choice == "1":
        text = input("Enter text to convert into speech: ")
        speak(text)

    elif choice == "2":
        result = listen()
        if result != "":
            speak("You said " + result)

    elif choice == "3":
        print("Goodbye 👋")
        speak("Goodbye")
        break

    else:
        print("Invalid choice, try again")
        break