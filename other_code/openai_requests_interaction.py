import requests

from global_keys import OPEN_AI_KEY


def send_openai_request(api_key, messages):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    payload = {"model": "gpt-3.5-turbo", "messages": messages}
    url = 'https://api.openai.com/v1/chat/completions'
    response = requests.post(url, headers=headers, json=payload)
    return response.json() if response.ok else response.raise_for_status()


prompt = "Suggest a good architecture of Test Automation Framework in Java stack for UI and API testing."
try:
    response_data = send_openai_request(OPEN_AI_KEY, [{"role": "assistant", "content": prompt}])
    print(f"Spent tokens: {response_data.get('usage', {}).get('total_tokens', 'Unknown')}")
    for choice in response_data.get('choices', []):
        print(f"Response message:\n{choice.get('message', {}).get('content', 'No content')}")
except requests.HTTPError as e:
    print(f"Request failed: {e}")
