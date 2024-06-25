import openai
import speech_recognition as sr
import pyttsx3
import os

# Set the OpenAI API key and base URL for the local server
openai.api_key = "lm-studio"
openai.api_base = "URL_OF_LM_STUDIO_SERVER"

# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Initialize recognizer
r = sr.Recognizer()

# Function to record user's speech
def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("Listening...")
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                print(f"You said: {MyText}")
                return MyText
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            SpeakText("Sorry, I couldn't reach the speech recognition service.")
        except sr.UnknownValueError:
            print("Unknown error occurred")
            SpeakText("Sorry, I didn't catch that. Please try again.")

# Function to send user's message to OpenAI for a response
def send_to_openai(messages, model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error communicating with OpenAI: {e}")
        SpeakText("Sorry, I couldn't process your request.")

messages = []

# Main loop for conversation
while True:
    user_text = record_text()
    if user_text:
        messages.append({"role": "user", "content": user_text})
        assistant_response = send_to_openai(messages)
        if assistant_response:
            SpeakText(assistant_response)
            print(assistant_response)
            messages.append({"role": "assistant", "content": assistant_response})
