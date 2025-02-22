import json
import os
from typing import List, Set, Tuple

from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CacheMode,
    CrawlerRunConfig,
    LLMExtractionStrategy,
)

from models.property import Property

def get_browser_config() -> BrowserConfig:
    return BrowserConfig(
        browser_type="chromium",
        headless=False,
        verbose=True,
    )

def get_llm_strategy() -> LLMExtractionStrategy:
    return LLMExtractionStrategy(
        provider="openai/gpt-4o",
        api_token=os.getenv("OPENAI_API_KEY"),
        model="gpt-4o",
        schema=Property.model_json_schema(),
        extraction_type="schema",
        instruction="""
        Extract the following information from the real estate listing:
        1. Basic Information:
           - Title
           - Property Type
           - Price (in EUR)
           - Location
        2. Property Details:
           - Total Area (m²)
           - Number of Floors
           - Number of Bedrooms
           - Number of Bathrooms
           - Garage/Parking details
        3. Features:
           - All listed amenities
           - Energy Rating
           - Construction details
        4. Additional Information:
           - Description
           - Construction Status
           - Special features
        
        Format as JSON with Portuguese text preserved.
        If information is not found, use null.
        """,
        input_format="html",
        verbose=True,
    )

async def fetch_and_process_listing(
    crawler: AsyncWebCrawler,
    url: str,
    css_selector: str,
    llm_strategy: LLMExtractionStrategy,
    session_id: str,
) -> Tuple[dict, bool]:
    """
    Fetches and processes a single property listing.
    """
    print(f"Processing listing: {url}")

    result = await crawler.arun(
        url=url,
        config=CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            extraction_strategy=llm_strategy,
            css_selector=css_selector,
            session_id=session_id,
        ),
    )

    if not (result.success and result.extracted_content):
        print(f"Error fetching listing: {result.error_message}")
        return None, False

    # Parse extracted content
    try:
        property_data = json.loads(result.extracted_content)
        print("Extracted property data:", property_data)
        return property_data, True
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None, False 