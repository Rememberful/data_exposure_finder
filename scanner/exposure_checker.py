import re

def scan_page_for_exposures(html, base_url):
    results = []

    email_pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
    api_key_pattern = r"(?i)(api[_-]?key|secret)[\s=:\"']+[a-z0-9\-_]{16,40}"

    emails = re.findall(email_pattern, html)
    api_keys = re.findall(api_key_pattern, html)

    for email in set(emails):
        results.append({
            "type": "Email Leak",
            "url": base_url,
            "data": email
        })

    for key in set(api_keys):
        results.append({
            "type": "API Key Leak",
            "url": base_url,
            "data": key
        })

    return results
