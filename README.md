# Portuguese Real Estate Web Scraper

A web scraping tool designed to extract detailed property listings from Portuguese real estate websites (currently supporting imovirtual.com).

## Current Status

This is the most barebones version it will ever be. I will continually update this in the following weeks for a project that I'm working on. The code right now works but still has some tweaks needed. I'm unsure whether gpt-4o-mini is the right fit for it, among many other things.

**Important Note:** This tool is for instructional use only. All implementations carefully respect GDPR compliance.

## Future Plans

- [ ] Adapt it to cycle between webpages and scrape all houses
- [ ] Add functionality for users to choose:
  - Property type
  - Rent vs ownership
  - District/location
  - Other filtering options
- [ ] Build in GUI
- [ ] Create an agent that automatically scrapes data at configurable intervals
- [ ] Perform analysis on the collected data
- [ ] Implement best deal detection as listings appear
- [ ] Add duplicate detection and handling for automated runs


## Intent

To gather data for my own Data Science projects, with the goals of:
- Creating reports on Kaggle
- Improving and updating my Portfolio
- Analyzing real estate market trends

## Features

- Extracts comprehensive property information including:
  - Basic property details (title, type, price, location)
  - Property specifications (area, bedrooms, bathrooms)
  - Features and amenities
  - Energy certificates
  - Construction details
- Preserves Portuguese text in the output
- Exports data to both CSV and JSON formats
- Uses OpenAI's GPT-4 for accurate data extraction

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. Clone the repository:

bash
git clone https://github.com/Smewth/Portuguese-Housing-Market-Scraper.git
cd portuguese-real-estate-scraper

2. Install required packages:

bash
pip install -r requirements.txt

3. Create a `.env` file in the root directory and add your OpenAI API key:

bash
OPENAI_API_KEY=your_api_key_here

## Usage

1. Update the URL in `config.py` with the property listing you want to scrape:

python
BASE_URL = "your_property_url_here"

2. Run the scraper:

bash
python main.py


The script will create two output files:
- `property_data.csv`: CSV format of the extracted data
- `property_data.json`: JSON format of the extracted data

## Configuration

You can modify the scraping behavior in `config.py`:
- CSS selectors for different elements
- Required fields
- Property type mappings
- Condition mappings
- Utility types
- Security features
- And more...

## Project Structure

portuguese-real-estate-scraper/
├── models/
│ └── property.py # Data models for property information
├── utils/
│ ├── data_utils.py # Data processing utilities
│ └── scraper_utils.py # Web scraping utilities
├── .env # Environment variables (not in repo)
├── .gitignore # Git ignore rules
├── config.py # Configuration settings
├── main.py # Main script
├── LICENSE # MIT License
├── README.md # This file
└── requirements.txt # Python dependencies

## Output Format

The scraper extracts data in a structured format including:
- Property basics (ID, type, title, description)
- Location details
- Property specifications
- Financial information
- Utilities and amenities
- Legal features
- Media information
- Market insights

## Error Handling

The scraper includes:
- Retry mechanisms for failed requests
- Proper error logging
- Data validation
- Fallback options for missing data

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

Please check and comply with the terms of service of any website you plan to scrape. This tool is for educational purposes only.

## Author

Smewth

## Support

For support, please open an issue in the GitHub repository.