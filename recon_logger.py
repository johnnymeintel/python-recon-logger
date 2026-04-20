import requests

def get_headers(url):
    try:
        r = requests.get(url, timeout=5)
        return dict(r.headers)
    except requests.RequestException as e:
        print(f"[ERROR] {e}")
        return {}

required = ["X-Frame-Options", "X-Content-Type-Options", "Strict-Transport-Security"]
outdated = ["PHP/5", "Apache/2.2", "Apache/2.4.1", "nginx/1.0", "IIS/6", "IIS/7"]

url = input("Target URL: ")
headers = get_headers(url)

for header in required:
    if header not in headers:
        print(f"[MISSING] {header}")

for key, value in headers.items():
    for sig in outdated:
        if sig.lower() in value.lower():
            print(f"[OUTDATED] {key}: {value}")

acao = headers.get("Access-Control-Allow-Origin", "")
acac = headers.get("Access-Control-Allow-Credentials", "")

if acao == "*" and acac.lower() == "true":
    print(f"[CORS] Wildcard origin + credentials: potential misconfiguration")
elif acao == "*":
    print(f"[CORS] Wildcard origin - note for context")

print("\n[RAW HEADERS]")
for k, v in headers.items():
    print(f"  {k}: {v}")