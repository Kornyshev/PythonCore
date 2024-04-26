from openai import OpenAI

from global_keys import OPEN_AI_KEY

client = OpenAI(api_key=OPEN_AI_KEY)

prompt = "Suggest a good architecture of Test Automation Framework in Java stack for UI and API testing."
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "assistant", "content": prompt}
    ]
)

print(completion.choices[0].message.content)
