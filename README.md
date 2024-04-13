Install Required Libraries:

Ensure you have requests and beautifulsoup4 libraries installed. You can install them using pip if you haven't already:
pip install requests
pip install beautifulsoup4

Save the Code:

Copy the provided code into a Python (.py) file, for example, wikipedia_search.py.

Execute the Script:

Open a terminal or command prompt.
Navigate to the directory containing the Python file.

Run the Program:

Run the Python script using the command: python wikipedia_search.py.

Input Wikipedia Page URL:

After running the script, it will prompt you to enter the URL of the Wikipedia page to start from.
Paste the URL of the Wikipedia page you want to start the search from and press Enter.

Wait for Results:

The program will start searching for the Hitler Wikipedia page from the provided starting page.
If the path to the Hitler page is found within 6 hops, it will print "Path to Hitler page found."
If the Hitler page is not found within the specified depth, it will print "Hitler not found."

Optional Optimization:

You can optimize the search by adjusting the maximum depth or exploring different starting pages.

Error Handling:

The program handles basic errors such as invalid URLs or network connectivity issues.
