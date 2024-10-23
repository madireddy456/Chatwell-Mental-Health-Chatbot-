from flask import Flask, render_template, request, jsonify
import requests
RASA_API_URL = 'http://127.0.0.1:5005/webhooks/rest/webhook'
#RASA_API_URL = 'http://127.0.0.1:5000/webhooks/rest/webhook'
app = Flask(__name__)

@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message:", user_message)

    # send user message to rasa and get bot's response
    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa response:", rasa_response_json)

    bot_response = rasa_response_json[0]['text'] if rasa_response_json else "Sorry, I am not trained for this! :("

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
