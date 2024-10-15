import requests

def test_open_redirect(url, payload):
    target_url = url + payload
    response = requests.get(target_url)
    if response.status_code == 200:
        print("Open redirect vulnerability found!")
        print(f"Redirected to: {response.url}")
    else:
        print("No open redirect vulnerability found.")

# Example usage
test_open_redirect("URL_WITH_VULNERABLE_ENDPOINT", "WEBSITE_TO_REDIRECT_TO")
