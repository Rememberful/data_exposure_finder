import csv
import os

def save_report(findings):
    os.makedirs("output", exist_ok=True)
    with open("output/exposure_report.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["type", "url", "data"])
        writer.writeheader()
        for row in findings:
            writer.writerow(row)
