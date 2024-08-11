from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Parse the incoming JSON data
    print("Received data:", data)  # Log the entire payload for debugging

    # Check if 'messages' are in the incoming data
    if 'messages' in data:
        for message in data['messages']:
            message_type = message['type']
            sender_id = message['from']
            print(f"Message type: {message_type} from {sender_id}")

            # Handle text messages
            if message_type == 'text':
                text = message['text']['body']
                print(f"Text message: {text}")

            # Handle media messages
            elif message_type in ['image', 'video', 'audio', 'document']:
                media_url = message[message_type]['url']
                print(f"Media message: {message_type} at {media_url}")

            # Handle interactive messages (e.g., button clicks)
            elif message_type == 'interactive':
                interaction = message['interactive']
                if interaction['type'] == 'button_reply':
                    button_id = interaction['button_reply']['id']
                    print(f"Button clicked: {button_id}")

    return jsonify({"status": "received"}), 200  # Acknowledge receipt of the event

if __name__ == '__main__':
    app.run(port=2341, debug=True)
