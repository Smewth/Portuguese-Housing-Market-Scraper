import asyncio
from crawl4ai import AsyncWebCrawler
from dotenv import load_dotenv

from config import BASE_URL, CSS_SELECTOR
from utils.data_utils import save_properties_to_json, save_properties_to_csv
from utils.scraper_utils import (
    fetch_and_process_listing,
    get_browser_config,
    get_llm_strategy,
)

load_dotenv()

async def crawl_property():
    """
    Main function to crawl property data from a single listing.
    """
    # Initialize configurations
    browser_config = get_browser_config()
    llm_strategy = get_llm_strategy()
    session_id = "property_crawl_session"

    # Start the web crawler context
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Fetch and process the single property listing
        property_data, success = await fetch_and_process_listing(
            crawler,
            BASE_URL,
            CSS_SELECTOR,
            llm_strategy,
            session_id,
        )

        if success and property_data:
            # Remove the 'error' field from each property if it exists
            if isinstance(property_data, list):
                for prop in property_data:
                    prop.pop('error', None)
            
            # Save the property data to both CSV and JSON
            save_properties_to_csv([property_data], "property_data.csv")
            save_properties_to_json([property_data], "property_data.json")
        else:
            print("Failed to extract property data.")

        # Display usage statistics for the LLM strategy
        llm_strategy.show_usage()

async def main():
    """
    Entry point of the script.
    """
    await crawl_property()

if __name__ == "__main__":
    asyncio.run(main()) 