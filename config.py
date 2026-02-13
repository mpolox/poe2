"""
Configuration for PoE2 Data Scraper
"""

import os
from datetime import datetime

# Project Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
GUIDES_DIR = os.path.join(BASE_DIR, 'guides')
LEAGUE_DATA_DIR = os.path.join(BASE_DIR, 'league-data')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

# Create logs directory if it doesn't exist
os.makedirs(LOGS_DIR, exist_ok=True)

# PoE2 Trade API Configuration
POE_TRADE_API_BASE = "https://www.pathofexile.com/api/trade2"
POE_TRADE_FETCH = "https://www.pathofexile.com/api/trade2/fetch"
POE_TRADE_SEARCH = "https://www.pathofexile.com/api/trade2/search"

# Wiki Configuration
POE2_WIKI_BASE = "https://poe2.wiki.gg"
POE2_WIKI_OMEN_PAGE = f"{POE2_WIKI_BASE}/wiki/Omens"
POE2_WIKI_ITEM_BASE_PAGE = f"{POE2_WIKI_BASE}/wiki/Item_bases"

# Community Price Sources
POENINJA_BASE = "https://poe.ninja/api/data"  # If available for PoE2
POEDB_BASE = "https://poedb.tw"

# Update Schedule
UPDATE_SCHEDULE = {
    'prices': 'weekly',  # Update base prices weekly (Sunday)
    'omens': 'monthly',   # Update omen database monthly
    'currency': 'monthly', # Update currency rates monthly
    'league_info': 'weekly' # Update league info weekly
}

# Trade Query Configuration
ITEM_TYPES = {
    'boots': {
        'search_term': 'Boots',
        'category': 'armour',
        'subcategory': 'boots'
    },
    'gloves': {
        'search_term': 'Gloves',
        'category': 'armour',
        'subcategory': 'gloves'
    },
    'helmet': {
        'search_term': 'Helmet',
        'category': 'armour',
        'subcategory': 'helmet'
    },
    'chest': {
        'search_term': 'Chest',
        'category': 'armour',
        'subcategory': 'body_armour'
    },
    'shield': {
        'search_term': 'Shield',
        'category': 'armour',
        'subcategory': 'shield'
    },
    'weapon': {
        'search_term': 'Weapon',
        'category': 'weapon'
    },
    'ring': {
        'search_term': 'Ring',
        'category': 'jewellery',
        'subcategory': 'ring'
    },
    'amulet': {
        'search_term': 'Amulet',
        'category': 'jewellery',
        'subcategory': 'amulet'
    },
    'flask': {
        'search_term': 'Flask',
        'category': 'flask'
    }
}

# Price query limits (how many bases to track per type)
BASES_PER_TYPE = 5

# API Request Configuration
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

# Logging
LOG_FILE = os.path.join(LOGS_DIR, f'poe2_scraper_{datetime.now().strftime("%Y%m%d")}.log')
LOG_LEVEL = 'INFO'

# File Output
PRICE_PRECISION = 2  # Decimal places for prices
UPDATE_TIMESTAMP = True  # Add update timestamp to files

# League Configuration
CURRENT_LEAGUE = None  # Set to specific league name, None = current league
TRACK_HISTORICAL_DATA = True  # Keep price history for trend analysis
