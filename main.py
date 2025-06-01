from scanner.crawler import fetch_page_source, extract_internal_links
from scanner.exposure_checker import scan_page_for_exposures
from scanner.sensitive_file_checker import check_sensitive_paths
from utils.logger import save_report
import sys
from urllib.parse import urlparse
from collections import deque

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python main.py <target_url> [max_depth]")
        return

    target_url = sys.argv[1]
    max_depth = int(sys.argv[2]) if len(sys.argv) == 3 else 2

    domain = urlparse(target_url).netloc
    visited = set()
    queue = deque([(target_url, 0)])
    findings = []

    print(f"[+] Starting recursive scan on {target_url} up to depth {max_depth}...")

    while queue:
        current_url, depth = queue.popleft()
        if current_url in visited or depth > max_depth:
            continue

        visited.add(current_url)
        print(f"[~] Scanning: {current_url} (depth {depth})")
        try:
            html = fetch_page_source(current_url)
        except Exception as e:
            print(f"[!] Failed to fetch {current_url}: {e}")
            continue

        exposures = scan_page_for_exposures(html, current_url)
        sensitive = check_sensitive_paths(current_url)
        findings.extend(exposures + sensitive)

        if depth < max_depth:
            new_links = extract_internal_links(html, current_url, domain)
            for link in new_links:
                if link not in visited:
                    queue.append((link, depth + 1))

    if findings:
        save_report(findings)
        print("[+] Scan complete. Findings saved to output/exposure_report.csv")
    else:
        print("[-] No sensitive data exposures found.")

if __name__ == "__main__":
    main()
