# Data Exposure Finder

Data Exposure Finder is a Python tool that uses Selenium WebDriver to perform recursive scans of websites.
It analyzes web pages up to a specified depth to find potential data exposures and saves detailed findings in a CSV report.

## Features

- Recursive crawling of webpages starting from a base URL.
- Customizable scan depth to control the crawl extent.
- Uses Selenium to handle dynamic content and JavaScript-heavy sites.
- Outputs detailed scan results in `output/exposure_report.csv`.
- Supports headless browser mode for efficient, GUI-free operation.
- Logs scan progress and findings for easy debugging.

## Requirements

- Python 3.7+
- Selenium
- Chrome WebDriver (compatible with your installed Chrome version)
- pandas

## Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Rememberful/data_exposure_finder.git](https://github.com/Rememberful/data_exposure_finder.git)
    cd data_exposure_finder
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Download and install ChromeDriver and add it to your system `PATH`.

## Usage

Run the main script with the target URL and scan depth as arguments:

```bash
python main.py [https://example.com](https://example.com) 2
