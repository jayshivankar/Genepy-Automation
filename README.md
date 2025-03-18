# Genepy Automation with Selenium

This project automates the process of logging into the [Genepy](https://genepy.org/exercises/) platform, retrieving exercise content, and sending it to ChatGPT for assistance.

## Features
- Automatically logs into the Genepy platform.
- Scrolls through the exercise page to locate the "Exceptions" problem.
- Extracts exercise details and sends them to ChatGPT.
- Designed for seamless automation using Selenium with Python.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Google Chrome (latest version)
- ChromeDriver (compatible with your Chrome version)

## Setup
1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/genepy-automation.git
    cd genepy-automation
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install required packages:

    ```bash
    pip install selenium
    ```

4. Ensure `chromedriver` is in your PATH or specify its location.

## Usage
1. Update your Genepy credentials in the script:

    ```python
    ACCOUNT_EMAIL = "your_username"
    ACCOUNT_PASSWORD = "your_password"
    ```

2. Run the script:

    ```bash
    python genepy_automation.py
    ```

## Explanation
- **Login Process**: Automates signing into the Genepy platform.
- **Content Extraction**: Scrapes the "Exceptions" problem.
- **ChatGPT Interaction**: Sends the extracted text to ChatGPT for problem-solving.

## Troubleshooting
- Ensure ChromeDriver is compatible with your Chrome version.
- Verify that your Genepy credentials are correct.
- If elements are not found, check the latest XPath using the browser's DevTools.

## Contributions
Feel free to fork this repository and open a pull request with improvements.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

