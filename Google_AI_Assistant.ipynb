# Import necessary libraries for Google Generative AI and text-to-speech conversion
!pip install -q -U google-generativeai gTTS
from gtts import gTTS  # Google Text-to-Speech library for converting text to audio
from IPython.display import Audio, display  # Libraries for displaying and playing audio in Colab
import google.generativeai as genai  # Google's generative AI library

# Configure the API key for Google Generative AI
GOOGLE_API_KEY = 'your-google-api-key'
genai.configure(api_key=GOOGLE_API_KEY)

# Function to prompt the user for their question
def ask_question(name):
    # Create a personalized prompt for the user
    prompt = f'Hey {name}, what do you want? '
    # Capture the user's input
    question = input(prompt)
    return question

# Example usage of ask_question function
ask_question("Nutan")

# Function to classify the type of question asked
def classify_questions(question):
    # List of device-related commands
    device_commands = ['Set an alarm', 'set a reminder', 'send a message', 'call']
    # Dictionary of personal questions and responses
    personal_responses = {'who are you?': 'I am Jarvis', 'who created you?': 'I am created by your username'}

    # Check if the question is a device-related command
    is_device_command = any(cmd in question for cmd in device_commands)
    if is_device_command:
        print("This question is related to device operations, which is not supported in this assistant.")

    # Check if the question is a personal query
    is_personal_question = any(pq in question for pq in personal_responses)
    if is_personal_question:
        print("Hey, I am a personal assistant created by your name.")

    # Determine if a web search is needed (i.e., it's not a device command or personal question)
    needs_web_search = not (is_device_command or is_personal_question)
    return needs_web_search

# Example usage of classify_questions function
ques = "Set an alarm"
result = classify_questions(ques)
print("Go ahead with web search:", result)
classify_questions("Who are you?")

# Function to generate an answer using Google's Gemini API
def ask_gemini(question):
    # Initialize the generative model
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Generate content based on the user's question
    response = model.generate_content(question)
    return response.text

# Function to convert text to speech and play it
def speak(answer):
    # Convert text to speech
    tts = gTTS(answer)
    # Save the speech to an audio file
    tts.save('audio.mp3')
    # Play the audio file
    display(Audio('audio.mp3', autoplay=True))

# Main script to handle user interaction
def main():
    have_any_other_ques = 'y'
    name = ''
    while have_any_other_ques.lower() == 'y':
        # Prompt for the user's name if not already provided
        if name == '':
            name = input("What is your name? ")

        # Get the user's question
        question = ask_question(name)
        # Classify the question to determine if a web search is needed
        go_ahead = classify_questions(question)
        
        # Initialize the answer variable
        answer = ''
        if go_ahead:
            # Generate an answer using Gemini API if needed
            answer = ask_gemini(question)
        
        # Print and speak the answer
        print(answer)
        speak(answer)

        # Ask if the user has more questions
        have_any_other_ques = input("Do you have any other questions? (y/n)")

# Run the main function
main()
