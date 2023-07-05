# Website Word Sorter

The provided code is a web scraper that extracts the text content from a given URL and gives the user the option to order the words either by frequency or alphabetically. The program uses libraries such as requests and BeautifulSoup to fetch and parse the HTML content.

## How it Works

The script follows these steps to count and sort the words:

1. The count_and_order_words function retrieves the text content from a given URL, cleans it, and splits it into individual words.
2. If the sort_by_frequency parameter is True, the function counts the occurrences of each word and returns a list of words sorted by their frequency.
3. If sort_by_frequency is False, the function returns a list of words sorted alphabetically.
4. The print_ordered_words function takes a list of words and prints them, along with their counts if available.
5. The user can choose to order the words by frequency (option 1), order them alphabetically (option 2), or quit the program (option 3).
6. Depending on the user's choice, the count_and_order_words function is called with the appropriate arguments, and the print_ordered_words function is used to display the ordered words.
7. If an invalid choice is entered, an error message is displayed.
8. The program continues running until the user chooses to quit.

## Prerequisites

Make sure you have the following prerequisites installed before running the script:

- Python 3 (https://www.python.org/downloads/)
- requests library (can be installed via `pip install requests`)
- BeautifulSoup library (can be installed via `pip install beautifulsoup4`)
- bs4 library (can be installed via `pip install bs4`)

## Usage

1. Clone this repository or download the script (`main.py`) to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:

   ```shell
   python main.py
