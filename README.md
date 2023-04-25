# ArXiv Metadata Scraper
  This is a simple dashboard for scraping the metadata of research papers from the ArXiv API. The dashboard is built using the Streamlit library, and it allows users to select various parameters such as category, sorting order, and keyword to search for papers on ArXiv.
  Please read ArXiv API usage guideline before using.
https://info.arxiv.org/about/index.html

 The app sends requests to the ArXiv API to fetch the metadata of the papers that match the search criteria specified by the user. The metadata is then parsed and stored in a CSV file, which can be downloaded from the dashboard.

## How to Use
To use a deployed version https://metadatarxiv.streamlit.app/.
To use the ArXiv Metadata Scraper locally, follow these steps:

- Clone the repository to your local machine.
- Install the required packages listed in the requirements.txt file by running pip install -r requirements.txt in your terminal.
- Run the app using the following command: streamlit run app.py.
- In the dashboard, select the parameters such as category, sorting order, and keyword to search for papers on ArXiv.
Click on the "Download CSV" button to download the metadata of the papers that match the search criteria as a CSV file.
# Parameters
 The dashboard allows users to select the following parameters:

- **Category:** The category of papers to search for. Users can choose from a list of categories such as AI, Computation and Language, Computer Vision, ML, etc.
- **Sort Order:** The sorting order of the search results. Users can choose to sort the results in ascending or descending order of relevance.
- **Sort By:** The attribute to sort the search results by. Users can choose to sort the results by relevance, last updated, or submitted date.
- **Max Results:** The maximum number of search results to fetch. Users can specify a value between 1 and 1000.
- **Start:** The index of the first search result to fetch. Users can specify a value between 1 and 50000.
- **Keyword:** An optional keyword to search for in the title, abstract, or author fields of the papers.
# Output
The metadata of the papers that match the search criteria is stored in a CSV file. The file contains the following columns:

- Title: The title of the paper.
- Authors: The authors of the paper.
- Abstract: The abstract of the paper.
- Categories: The categories of the paper.
- Published: The date on which the paper was published.
- Updated: The date on which the paper was last updated.
- Link: The URL of the paper on the ArXiv website.
