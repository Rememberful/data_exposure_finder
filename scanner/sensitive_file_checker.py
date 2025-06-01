import requests

def check_sensitive_paths(base_url):
    paths = ["/.env", "/config.php", "/.git/HEAD", "/backup.zip", "/db.sql"]
    findings = []

    for path in paths:
        url = base_url.rstrip("/") + path
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200 and len(response.text) > 10:
                findings.append({
                    "type": "Exposed Sensitive File",
                    "url": url,
                    "data": f"{response.status_code} - {path}"
                })
        except requests.RequestException:
            continue

    return findings
