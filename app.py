import json

def get_scheme_reply(user_text):
    with open("schemes.json") as f:
        schemes = json.load(f)

    user_text = user_text.lower()

    for scheme in schemes:
        if scheme in user_text:
            s = schemes[scheme]
            return f"{s['description']} Eligibility: {s['eligibility']} Benefits: {s['benefits']}"

    return "Sorry, scheme not found. Please try another scheme."