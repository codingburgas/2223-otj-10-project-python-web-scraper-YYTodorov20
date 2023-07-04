# Website Word Counter and Sorter

This is a Python script that scrapes a website, counts the occurrence of each word, and sorts them by usage. It uses the BeautifulSoup and requests libraries to retrieve the HTML content of a website and process the text data.

## How it Works

The script follows these steps to count and sort the words:

1. Sends a GET request to the provided website URL.
2. Retrieves the HTML content of the webpage.
3. Parses the HTML using BeautifulSoup to extract the text data.
4. Cleans the text by removing non-alphanumeric characters and converting it to lowercase.
5. Splits the text into individual words.
6. Counts the occurrence of each word using the Counter class from the collections module.
7. Sorts the words by their count in descending order.

## Prerequisites

Make sure you have the following prerequisites installed before running the script:

- Python 3 (https://www.python.org/downloads/)
- requests library (can be installed via `pip install requests`)
- BeautifulSoup library (can be installed via `pip install beautifulsoup4`)

## Usage

1. Clone this repository or download the script (`web_scraper.py`) to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:

   ```shell
   python web_scraper.py
