import openai
#openai.api_key = open("key.txt", "r").read().strip("\n")
openai.api_key = "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"

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
