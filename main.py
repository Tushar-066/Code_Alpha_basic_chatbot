import nltk
import speech_recognition as sr
import pyttsx3
from nltk.chat.util import Chat, reflections

# Define chatbot response patterns
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help?"]),
    (r"how are you?", ["I'm good, thanks for asking!", "Doing well! How about you?"]),
    (r"what is your name?", ["I'm Chatbot, your virtual assistant.", "You can call me Jarvis Sir!"]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Bye! Have a great day!"]),
    (r"what can you do?", ["I can chat with you, answer simple questions, and more!"]),
    (r"who created you?", ["I was created by a Python Developer Tushar!", "A Python developer Tushar Created me."]),
    (r"(.*)", ["I'm not sure how to respond.", "Can you rephrase that?", "Interesting... Tell me more!"])
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for user input using speech recognition."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            print("Speech service unavailable.")
            return ""

# Start chatbot interaction
print("ChatBot: Hello! Speak or type your message. Say 'bye' to exit.")
speak("Hello! Speak or type your message. Say 'bye' to exit.")

while True:
    user_input = listen()  # Get spoken input
    if not user_input:
        user_input = input("You (type instead): ").lower()  # Fallback to text input

    if user_input == "bye":
        print("ChatBot: Goodbye!")
        speak("Goodbye!")
        break

    response = chatbot.respond(user_input)
    print(f"ChatBot: {response}")
    speak(response)