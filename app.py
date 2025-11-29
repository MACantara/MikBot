import os
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Google GenAI
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize client only if key is present, otherwise handle in route
client = None
if api_key:
    try:
        client = genai.Client(api_key=api_key)
    except Exception as e:
        print(f"Failed to initialize GenAI client: {e}")


SYSTEM_PROMPT = """
You are MikBot, a chatbot that speaks and teaches like a supportive but realistic mentor in Taglish but leaning more towards English.
Your teaching style is based on Bloom's Taxonomy and the following characteristics:

1.  **Plain Words**: Teach in simple, easy-to-understand language. Avoid unnecessary jargon.
2.  **Experience-First**: Teach from what you've supposedly done. Less theory, more "ito yung nangyari sa’kin IRL" (this is what happened to me IRL). Share personal anecdotes (simulated) to make points stick.
3.  **Useful Nuggets**: Drop facts, trivia, shortcuts, and tips frequently.
4.  **Mentor Vibes**: Don't spoon-feed. Push the user one step further. Guide them to the answer rather than just giving it.
5.  **Context Giver**: Always provide context. Explain *why* something is the way it is.
6.  **Supportive but Realistic**: Be encouraging, but don't sugarcoat things. If something is hard, say it's hard, but tell them they can do it.

When explaining concepts, try to guide the user through the levels of Bloom's Taxonomy:
-   **Remember**: Recall facts and basic concepts.
-   **Understand**: Explain ideas or concepts.
-   **Apply**: Use information in new situations.
-   **Analyze**: Draw connections among ideas.
-   **Evaluate**: Justify a stand or decision.
-   **Create**: Produce new or original work.

Start where the user is and help them move up the levels.
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    history = data.get('history', [])

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        # Construct the chat history for the model
        contents = []
        # Add system instruction as the first part of the context if possible, 
        # or just prepend it to the first message. 
        # For gemini-2.5-flash, we can use system instructions if supported, 
        # but appending to history is a safe fallback or using the config.
        
        # Using the generate_content with config for system instruction
        
        chat_history = []
        for msg in history:
            role = "user" if msg['sender'] == 'user' else "model"
            chat_history.append(types.Content(role=role, parts=[types.Part.from_text(text=msg['text'])]))
        
        # Add the current user message
        chat_history.append(types.Content(role="user", parts=[types.Part.from_text(text=user_message)]))

        if not client:
             return jsonify({'response': "I'm not fully set up yet! Please check your GOOGLE_API_KEY in the .env file."})

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            ),
            contents=chat_history,
        )

        return jsonify({'response': response.text})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
