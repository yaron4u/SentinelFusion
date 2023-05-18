# soar_integration.py
import requests


def get_threat_intelligence(ip_address):
    # Example API call
    response = requests.get(f"https://api.splunksoar.com/v1/intelligence/{ip_address}")
    data = response.json()
    return data
