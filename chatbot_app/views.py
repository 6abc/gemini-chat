from dotenv import load_dotenv
import os 
from django.shortcuts import render, redirect
from .models import Message
import google.generativeai as genai
load_dotenv()

# Configure the Google Generative AI client
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def chat_view(request):
    if request.method == "POST":
        if 'delete_chat' in request.POST:  # Check if the delete button is clicked
            Message.objects.all().delete()  # Delete all chat messages
            return redirect('chat_view')  # Redirect to clear the form

        user_message = request.POST.get('message')
        bot_message = get_genai_response(user_message)
        Message.objects.create(user_message=user_message, bot_message=bot_message)

    messages = Message.objects.all()
    return render(request, 'chatbot_app/chat.html', {'messages': messages})


def get_genai_response(user_input: str) -> str:
    """
    Get a response from Google Generative AI using the gemini model.
    """
    try:
        # Create the generative model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generate the AI response
        response = model.generate_content(user_input)
        
        # Extract and return the text response
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"Sorry, I couldn't process that. Please try again. \n\n {e.message}"


def get_existing_messages() -> list:
    """
    Get all messages from the database and format them for further use.
    """
    formatted_messages = []

    for message in Message.objects.values('user_message', 'bot_message'):
        formatted_messages.append({"role": "user", "content": message['user_message']})
        formatted_messages.append({"role": "assistant", "content": message['bot_message']})

    return formatted_messages
