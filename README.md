# scraping-reed-data-analyst-jobs
This repository contains a Scrapy project aimed at scraping data analyst job listings from the Reed job portal (https://www.reed.co.uk). The project is designed to extract various details from job listings, including the job title, salary, contract type, job type, and location.

To run this project:
1. Clone the repository to your local machine
2. Set Up a Virtual Environment (Optional but recommended)

    command: `python3 -m venv env`
4. Activate the Virtual Environment

   On Windows: venv\Scripts\activate

   on  MacOS/Linux : source env/bin/activate
6. Install Required Dependencies

   Command: pip install scrapy
8. Run the Web Scraper

   command: scrapy crawl dataanalystspider -o output.json


