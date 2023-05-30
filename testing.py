import openai
import json

with open('api_keys.json') as api_keys:
    key_dict = json.load(api_keys)
openai.api_key = key_dict["openai"]


i=0
while True:
    print("ask a question.")
    q = input()

    messages=[{"role": "system", "content": "Ime ti je Klemen Bajec. Si profesor informatike na gimnaziji Vič (Slovenija, Ljubljana) Velikokrat se šališ o svoji pleši. Si v svojih petdesetih letih"}]
    messages.append({"role": "user", "content": q})

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= messages
    )

    print(completion["choices"][0]["message"]["content"])

    answer = completion.choices[0].message
    messages.append(answer)
