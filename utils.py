"""
Utility functions for PoE2 data scraper
"""

import logging
import os
from datetime import datetime
from config import LOG_FILE, LOG_LEVEL

# Setup logging
def setup_logging():
    """Configure logging for the scraper"""
    logger = logging.getLogger('poe2_scraper')
    logger.setLevel(getattr(logging, LOG_LEVEL))
    
    # File handler
    fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(getattr(logging, LOG_LEVEL))
    
    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(getattr(logging, LOG_LEVEL))
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    # Add handlers
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)
    
    return logger

logger = setup_logging()

def get_logger():
    """Get the configured logger"""
    return logger

def format_price(price, precision=2):
    """Format price with specified precision"""
    try:
        return round(float(price), precision)
    except (ValueError, TypeError):
        return 0

def format_timestamp():
    """Get current timestamp formatted"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_date():
    """Get current date formatted"""
    return datetime.now().strftime("%Y-%m-%d")

def safe_divide(numerator, denominator):
    """Safely divide two numbers"""
    try:
        if denominator == 0:
            return 0
        return numerator / denominator
    except (ValueError, TypeError):
        return 0

def extract_chaos_value(price_string):
    """
    Extract chaos equivalent value from price string
    Examples: "5c", "2.5 chaos", "1.5c" -> returns float
    """
    if not price_string:
        return 0
    
    price_string = str(price_string).lower().strip()
    
    # Remove common text
    price_string = price_string.replace('chaos', '').replace('c', '').replace(' ', '')
    
    try:
        return float(price_string) if price_string else 0
    except ValueError:
        return 0

def create_table_row(columns, column_widths=None):
    """Create a markdown table row"""
    return "| " + " | ".join(str(col).ljust(w-2) if column_widths else str(col) 
                              for col, w in zip(columns, column_widths or [len(str(c))+2]*len(columns))) + " |"

def create_table_header(headers):
    """Create markdown table header"""
    header = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    return f"{header}\n{separator}"

def backup_file(filepath):
    """Create a backup of file before updating"""
    if os.path.exists(filepath):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{filepath}.backup_{timestamp}"
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info(f"Backup created: {backup_path}")
            return backup_path
        except Exception as e:
            logger.error(f"Failed to backup {filepath}: {e}")
            return None
    return None

def update_markdown_section(filepath, section_name, new_content, create_if_missing=True):
    """
    Update a specific section in a markdown file
    Assumes section headers are marked with ## Section Name
    """
    try:
        # Read existing content
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            if not create_if_missing:
                logger.warning(f"File not found: {filepath}")
                return False
            content = f"# {os.path.basename(filepath).replace('.md', '')}\n\n"
        
        # Find section
        section_header = f"## {section_name}"
        next_section_header = "## "
        
        if section_header not in content:
            # Append new section
            content += f"\n{section_header}\n\n{new_content}\n"
        else:
            # Replace section content
            start_idx = content.find(section_header)
            end_idx = content.find(next_section_header, start_idx + len(section_header))
            
            if end_idx == -1:
                end_idx = len(content)
            
            before = content[:start_idx]
            after = content[end_idx:]
            
            content = f"{before}{section_header}\n\n{new_content}\n\n{after}"
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"Updated section '{section_name}' in {filepath}")
        return True
    
    except Exception as e:
        logger.error(f"Failed to update {filepath}: {e}")
        return False

def cleanup_old_backups(directory, days=7):
    """Remove backup files older than specified days"""
    from datetime import timedelta
    import glob
    
    cutoff_date = datetime.now() - timedelta(days=days)
    
    for backup_file in glob.glob(os.path.join(directory, '*.backup_*')):
        try:
            file_mtime = datetime.fromtimestamp(os.path.getmtime(backup_file))
            if file_mtime < cutoff_date:
                os.remove(backup_file)
                logger.info(f"Removed old backup: {backup_file}")
        except Exception as e:
            logger.error(f"Failed to remove backup {backup_file}: {e}")
