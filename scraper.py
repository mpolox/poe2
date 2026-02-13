"""
PoE2 Data Scraper - Main Module
Scrapes omen data, item prices, and market information
"""

import requests
import json
from typing import Dict, List, Optional
from datetime import datetime
from utils import get_logger, format_price, format_timestamp, extract_chaos_value
from config import (
    POE_TRADE_API_BASE, POE_TRADE_SEARCH, ITEM_TYPES,
    REQUEST_TIMEOUT, MAX_RETRIES, RETRY_DELAY, BASES_PER_TYPE
)
import time

logger = get_logger()

class PoeTradeAPI:
    """Interface with PoE Trade API v2"""
    
    def __init__(self):
        self.base_url = POE_TRADE_API_BASE
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'PoE2-Scraper/1.0'
        })
    
    def _make_request(self, url, method='GET', data=None, params=None, retries=0):
        """Make HTTP request with retry logic"""
        try:
            if method == 'GET':
                response = self.session.get(url, timeout=REQUEST_TIMEOUT, params=params)
            else:
                response = self.session.post(url, json=data, timeout=REQUEST_TIMEOUT, params=params)
            
            response.raise_for_status()
            return response
        
        except requests.exceptions.RequestException as e:
            if retries < MAX_RETRIES:
                logger.warning(f"Request failed ({retries+1}/{MAX_RETRIES}): {e}. Retrying...")
                time.sleep(RETRY_DELAY)
                return self._make_request(url, method, data, params, retries + 1)
            else:
                logger.error(f"Request failed after {MAX_RETRIES} retries: {e}")
                return None
    
    def search_bases(self, item_type: str) -> Optional[List[Dict]]:
        """
        Search for item bases by type
        Returns list of base names with prices
        """
        try:
            # Build query
            query = {
                "query": {
                    "filters": {
                        "type_filters": {
                            "filters": {
                                "category": item_type if isinstance(item_type, str) else {"option": item_type}
                            }
                        }
                    }
                },
                "sort": {
                    "price": "asc"
                }
            }
            
            # Search
            response = self._make_request(POE_TRADE_SEARCH, method='POST', data=query)
            if not response:
                return None
            
            data = response.json()
            logger.debug(f"Found {len(data.get('result', []))} results for {item_type}")
            
            return data.get('result', [])
        
        except Exception as e:
            logger.error(f"Error searching bases for {item_type}: {e}")
            return None
    
    def fetch_items(self, item_ids: List[str]) -> List[Dict]:
        """Fetch full item details from IDs"""
        try:
            # Fetch items (batch up to 10 at a time)
            items = []
            for i in range(0, len(item_ids), 10):
                batch = item_ids[i:i+10]
                fetch_url = f"{POE_TRADE_API_BASE}/fetch/{','.join(batch)}"
                
                response = self._make_request(fetch_url)
                if response:
                    data = response.json()
                    items.extend(data.get('result', []))
                    time.sleep(0.5)  # Rate limiting
            
            return items
        
        except Exception as e:
            logger.error(f"Error fetching items: {e}")
            return []
    
    def get_base_prices(self, item_type: str, limit: int = BASES_PER_TYPE) -> Dict:
        """Get current prices for item bases"""
        try:
            logger.info(f"Fetching prices for {item_type}...")
            
            # Search
            results = self.search_bases(item_type)
            if not results or len(results) == 0:
                logger.warning(f"No results found for {item_type}")
                return {}
            
            # Limit results
            item_ids = [r['id'] for r in results[:limit]]
            
            # Fetch details
            items = self.fetch_items(item_ids)
            
            # Extract price data
            prices = {}
            for item in items:
                try:
                    listing = item.get('listing', {})
                    price = listing.get('price', {})
                    
                    if price:
                        base_name = item.get('item', {}).get('name', 'Unknown')
                        chaos_price = extract_chaos_value(f"{price.get('amount', 0)}{price.get('currency', 'c')}")
                        
                        prices[base_name] = {
                            'price': chaos_price,
                            'currency': price.get('currency', 'c'),
                            'updated': format_timestamp()
                        }
                
                except Exception as e:
                    logger.debug(f"Error parsing item: {e}")
            
            logger.info(f"Retrieved prices for {len(prices)} bases")
            return prices
        
        except Exception as e:
            logger.error(f"Error getting base prices: {e}")
            return {}


class WikiScraper:
    """Scrape data from PoE2 Wiki"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'PoE2-Scraper/1.0'
        })
    
    def _make_request(self, url):
        """Make request to wiki"""
        try:
            response = self.session.get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            return response
        except Exception as e:
            logger.error(f"Failed to fetch {url}: {e}")
            return None
    
    def get_omen_data(self) -> List[Dict]:
        """
        Scrape omen data from wiki
        Returns list of omens with names, effects, and rarity
        """
        try:
            logger.info("Fetching omen data from wiki...")
            
            from bs4 import BeautifulSoup
            
            # This is a placeholder - actual implementation depends on wiki structure
            # You may need to adjust based on actual wiki HTML structure
            
            omens = [
                {
                    'name': 'Omens available',
                    'effect': 'Fetch from wiki - requires HTML parsing',
                    'rarity': 'Varies',
                    'note': 'Manual wiki scraping required - see wiki HTML structure'
                }
            ]
            
            logger.info(f"Retrieved {len(omens)} omens")
            return omens
        
        except Exception as e:
            logger.error(f"Error getting omen data: {e}")
            return []
    
    def get_item_bases(self) -> List[Dict]:
        """
        Scrape item base data from wiki
        Returns list of bases with types and stats
        """
        try:
            logger.info("Fetching item base data from wiki...")
            
            bases = [
                {
                    'name': 'Bases available',
                    'type': 'Fetch from wiki - requires HTML parsing',
                    'level': 'Varies',
                    'note': 'Manual wiki scraping required'
                }
            ]
            
            logger.info(f"Retrieved {len(bases)} bases")
            return bases
        
        except Exception as e:
            logger.error(f"Error getting item bases: {e}")
            return []


class MarketAnalyzer:
    """Analyze market data and trends"""
    
    @staticmethod
    def calculate_trend(previous_price: float, current_price: float) -> str:
        """Calculate price trend"""
        if current_price > previous_price:
            return '↑'
        elif current_price < previous_price:
            return '↓'
        else:
            return '→'
    
    @staticmethod
    def calculate_price_change_percent(previous_price: float, current_price: float) -> float:
        """Calculate percentage change"""
        if previous_price == 0:
            return 0
        return ((current_price - previous_price) / previous_price) * 100
    
    @staticmethod
    def estimate_profit_potential(base_cost: float, crafting_cost: float) -> str:
        """Estimate profit potential (simplified)"""
        total_investment = base_cost + crafting_cost
        
        if total_investment > 20:
            return 'Low'
        elif total_investment > 10:
            return 'Medium'
        else:
            return 'High'


def generate_price_table(prices: Dict) -> str:
    """Generate markdown table from price data"""
    if not prices:
        return "[No data available]"
    
    rows = ["| Base Name | Current Price | Currency | Last Updated |",
            "|-----------|---|---|---|"]
    
    for base_name, data in list(prices.items())[:BASES_PER_TYPE]:
        price = format_price(data.get('price', 0))
        currency = data.get('currency', 'c')
        updated = data.get('updated', 'N/A')
        rows.append(f"| {base_name} | {price} | {currency} | {updated} |")
    
    return "\n".join(rows)


def generate_omen_table(omens: List[Dict]) -> str:
    """Generate markdown table from omen data"""
    if not omens:
        return "[No omen data available]"
    
    rows = ["| Omen Name | Effect | Rarity | Notes |",
            "|-----------|--------|--------|-------|"]
    
    for omen in omens[:10]:  # Limit to 10
        name = omen.get('name', 'Unknown')
        effect = omen.get('effect', 'N/A')[:50]  # Truncate
        rarity = omen.get('rarity', 'Unknown')
        note = omen.get('note', '')[:30]
        rows.append(f"| {name} | {effect}... | {rarity} | {note} |")
    
    return "\n".join(rows)


if __name__ == "__main__":
    logger.info("Starting PoE2 data scraper...")
    
    # Example usage
    api = PoeTradeAPI()
    wiki = WikiScraper()
    
    # Fetch prices
    boots_prices = api.get_base_prices('boots')
    
    # Fetch omens
    omens = wiki.get_omen_data()
    
    logger.info("Data scraping completed")
