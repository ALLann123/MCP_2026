import requests

def get_public_ip():
    # You can also use https://api.ipify.org or http://icanhazip.com
    response = requests.get('https://api.ipify.org')
    return response.text

print(f"My public IP address is: {get_public_ip()}")


"""
python public_ip.py
My public IP address is: 102.205.238.244
"""
