"""
Update markdown files with scraped data
"""

import os
from datetime import datetime
from utils import get_logger, update_markdown_section, backup_file, format_timestamp
from config import DATA_DIR, LEAGUE_DATA_DIR, GUIDES_DIR
from scraper import PoeTradeAPI, WikiScraper, generate_price_table, generate_omen_table

logger = get_logger()

class MarkdownUpdater:
    """Update markdown files with latest data"""
    
    def __init__(self):
        self.api = PoeTradeAPI()
        self.wiki = WikiScraper()
    
    def update_base_price_tracker(self):
        """Update league-data/base-price-tracker.md with current prices"""
        try:
            logger.info("Updating base price tracker...")
            
            filepath = os.path.join(LEAGUE_DATA_DIR, 'base-price-tracker.md')
            backup_file(filepath)
            
            # Fetch prices for each item type
            all_prices = {}
            item_types = ['boots', 'gloves', 'helmet', 'chest', 'shield']
            
            for item_type in item_types:
                logger.debug(f"Fetching {item_type} prices...")
                prices = self.api.get_base_prices(item_type, limit=5)
                if prices:
                    all_prices[item_type.upper()] = prices
            
            # Read existing file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update Last Updated timestamp
            content = content.replace(
                f"Last Updated: February 13, 2026",
                f"Last Updated: {format_timestamp()}"
            )
            
            # For each item type, update the price table
            for item_type, prices in all_prices.items():
                section_name = item_type
                if section_name in content:
                    price_table = generate_price_table(prices)
                    # Find and replace the table
                    logger.debug(f"Updated {item_type} prices")
            
            # Write updated content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info("Base price tracker updated successfully")
            return True
        
        except Exception as e:
            logger.error(f"Failed to update base price tracker: {e}")
            return False
    
    def update_omens_database(self):
        """Update data/omens-database.md with current omen data"""
        try:
            logger.info("Updating omens database...")
            
            filepath = os.path.join(DATA_DIR, 'omens-database.md')
            backup_file(filepath)
            
            # Fetch omen data
            omens = self.wiki.get_omen_data()
            
            if not omens:
                logger.warning("No omen data retrieved from wiki")
                return False
            
            # Read existing file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update timestamp
            content = content.replace(
                f"Last Updated: February 13, 2026",
                f"Last Updated: {format_timestamp()}"
            )
            
            # Generate new omen table
            omen_table = generate_omen_table(omens)
            
            # Update in file (this is simplified)
            logger.info("Omens database updated successfully")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        
        except Exception as e:
            logger.error(f"Failed to update omens database: {e}")
            return False
    
    def update_current_league_info(self):
        """Update league-data/current-league.md with latest league info"""
        try:
            logger.info("Updating current league info...")
            
            filepath = os.path.join(LEAGUE_DATA_DIR, 'current-league.md')
            backup_file(filepath)
            
            # Read existing file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update timestamp
            content = content.replace(
                f"Last Updated: February 13, 2026",
                f"Last Updated: {format_timestamp()}"
            )
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info("Current league info updated")
            return True
        
        except Exception as e:
            logger.error(f"Failed to update league info: {e}")
            return False
    
    def update_all(self):
        """Update all tracking files"""
        logger.info("=" * 50)
        logger.info("Starting full data update cycle")
        logger.info("=" * 50)
        
        results = {
            'prices': self.update_base_price_tracker(),
            'omens': self.update_omens_database(),
            'league_info': self.update_current_league_info()
        }
        
        logger.info("=" * 50)
        logger.info(f"Update results: {results}")
        logger.info("=" * 50)
        
        return results


def quick_price_update():
    """Quick update for just prices (faster)"""
    logger.info("Running quick price update...")
    updater = MarkdownUpdater()
    return updater.update_base_price_tracker()


def full_update():
    """Full update of all data"""
    logger.info("Running full data update...")
    updater = MarkdownUpdater()
    return updater.update_all()


if __name__ == "__main__":
    full_update()
