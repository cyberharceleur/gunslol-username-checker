import requests
from requests.structures import CaseInsensitiveDict

def check_username(username):
    url = f"https://guns.lol/api/view/{username}"

    headers = CaseInsensitiveDict()
    headers["authority"] = "guns.lol"
    headers["accept"] = "*/*"
    headers["accept-language"] = "?0; Mobile"
    headers["cookie"] = "cf_clearance=PxQ43WBVlE73LEN3qiKC2gTauYIEhoSBh7cq.1lRoR8-1706625953-1-AfDAoZUap6+aQbhw/oJI0UGtVeGxnYfLaa3+jQMQM/Ll6nvJW4EViEuS/NXOogatEiFnNNY4Op+V5HgJwWJYBts=; _ga=GA1.1.787883208.1706625953; _ga_HVFV509737=GS1.1.1706625953.1.0.1706625953.0.0.0; _1__bProxy_v=defdb2f2cb4c2bacfea711befc12e794a5cea5742837e8fcc3369539c1da96ee"
    headers["referer"] = f"https://guns.lol/{username}"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    headers["verify_user"] = f"oQ0xoT_{username}"

    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        result = f"{username} not valid"
    elif resp.status_code == 400:
        result = f"{username} valid | saved in input.txt"
        with open("all.txt", "a") as file:
            file.write(f"{username}\n")
    else:
        result = f"Unknown status code: {resp.status_code}"

    print(result)

with open("input.txt", "r") as file:
    usernames = file.read().splitlines()

for username in usernames:
    check_username(username)
