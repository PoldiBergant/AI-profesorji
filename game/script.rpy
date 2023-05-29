
define b = Character("Bajec")

init python:
    import requests
    import json

    #odpre json in shrani ključ (ne dela ker file z ključem ni vključen v kodi)
    with open('api_keys.json') as api_keys:
        key_dict = json.load(api_keys)
    api_key = key_dict["openai"]

    def completion(messages, api_key):
        # URL endpointa API-ja za ChatGPT generiranje odgovorov
        url = "https://api.openai.com/v1/chat/completions"

        # nastavi headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer [api_key]"
        }

        # nastavi data
        data = {
            "model": "gpt-3.5-turbo",
            "messages": messages ,
        }

        # pošlje request
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Preveri, če je odgovor uspešen (statusna koda 200)
        if response.status_code == 200:
            completion = response.json()["choices"][0]["message"]
            messages.append(completion)
            return messages
        else:
            # če statusna koda ni 200, sproži izjemo
            # (najverjetneje je server preobremenjen ali pa se je odgovor predolgo generireal)
            raise Exception("Nekaj je šlo narobe")

label start:
    "bajec appears before you"
    show bajec
    b "živjo"

    python:
        messages = [
                   {"role": "system", "content": "Ime ti je Klemen Bajec. Si profesor informatike na gimnaziji Vič (Slovenija, Ljubljana). Občasno se šališ o svoji pleši. Si v svojih petdesetih letih."},
                   {"role": "system", "content": "Tvoji odgovori naj bodo kratki, največ 5 povedi."},
                   {"role": "system", "content": "Uporabnika tikaš"},
                   {"role": "assistant", "content": "Jaz grem samo na čik pavzo bomo kasneje začeli pouk."},
                   {"role": "user", "content": "Živjo profesor."},
                   {"role": "assistant", "content": "Pozdravljen, dijak, kako gre kaj projekt? Boš imel danes predstavitev?"}
                ]

        while True:
            user_input = q = renpy.input("Kaj rečeš:", length=600)
            messages.append(
                        {"role": "user", "content": user_input}
                    )

            messages = completion(messages,api_key)
            response = messages[-1]["content"]
            b("[response]")


    return
