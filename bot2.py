import requests

# API Endpoint
api_url = "https://aaa.com/buy"

# Replace with your actual private key
private_key = "your_private_key_here"

# Token mint address for HXTh56cHH97ibiNMEtMyMs6ZPAeqy5E9kqe4do3spump
mint_address = "HXTh56cHH97ibiNMEtMyMs6ZPAeqy5E9kqe4do3spump"

# Amount in SOL you wish to spend
amount_in_sol = 0.01  # Example: 0.01 SOL

# Transaction parameters
microlamports = 433000  # Default value
units = 300000          # Default value
slippage = 10           # Example: 10 for 10% slippage

# Payload for the POST request
payload = {
    "private_key": private_key,
    "mint": mint_address,
    "amount": amount_in_sol,
    "microlamports": microlamports,
    "units": units,
    "slippage": slippage
}

try:
    # Send POST request to the API
    response = requests.post(api_url, json=payload)
    response_data = response.json()

    if response.status_code == 200 and response_data.get("status") == "success":
        print(f"Transaction successful! TXID: {response_data.get('txid')}")
    else:
        print(f"Transaction failed: {response_data.get('message', 'Unknown error')}")

except Exception as e:
    print(f"An error occurred: {e}")
