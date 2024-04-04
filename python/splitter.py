import requests

# Fetch the content of the URL
url = "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/config-tg.txt"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the URL: {e}")
else:
    content = response.text

    # Separate the subscriptions based on the v2ray type
    subscriptions = content.splitlines()
    vmess = [s for s in subscriptions if s.startswith('vmess://')]
    vless = [s for s in subscriptions if s.startswith('vless://')]
    trojan = [s for s in subscriptions if s.startswith('trojan://')]
    ss = [s for s in subscriptions if s.startswith('ss://')]
    socks = [s for s in subscriptions if s.startswith('socks://')]

    # Write the results to separate files
    with open('vmess.txt', 'w') as f:
        f.write('\n'.join(vmess))
    with open('vless.txt', 'w') as f:
        f.write('\n'.join(vless))
    with open('trojan.txt', 'w') as f:
        f.write('\n'.join(trojan))
    with open('ss.txt', 'w') as f:
        f.write('\n'.join(ss))
    with open('socks.txt', 'w') as f:
        f.write('\n'.join(socks))