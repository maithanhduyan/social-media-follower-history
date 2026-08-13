from datetime import datetime, UTC
import re
import requests
import csv


url = "https://x.com/Christinany6666"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}

def get_followers():
    r = requests.get(url, headers=headers)
    matches = re.findall(r'([\d,.]+)\s+Followers', r.text, re.IGNORECASE)
    if matches:
        return int(matches[0].replace(",", ""))
    return 0

followers = get_followers()

with open("followers.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        datetime.now(UTC).isoformat(),
        followers,
    ])

print("Done")


