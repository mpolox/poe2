"""
Main entry point for PoE2 Data Scraper
"""

import sys
import argparse
from utils import get_logger
from file_updater import quick_price_update, full_update
from scheduler import get_scheduler

logger = get_logger()

def main():
    """Main function with CLI arguments"""
    parser = argparse.ArgumentParser(
        description='PoE2 Crafting Data Scraper',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python main.py --update              # Run one-time full update
  python main.py --prices              # Run one-time price update
  python main.py --schedule            # Start scheduler (foreground)
  python main.py --schedule-background  # Start scheduler (background)
        '''
    )
    
    parser.add_argument(
        '--update', '-u',
        action='store_true',
        help='Run one-time full data update'
    )
    parser.add_argument(
        '--prices', '-p',
        action='store_true',
        help='Run one-time price update only'
    )
    parser.add_argument(
        '--schedule', '-s',
        action='store_true',
        help='Start scheduler (blocking/foreground)'
    )
    parser.add_argument(
        '--schedule-background', '-sb',
        action='store_true',
        help='Start scheduler in background'
    )
    parser.add_argument(
        '--log-level',
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Set logging level'
    )
    
    args = parser.parse_args()
    
    # If no arguments, show help
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    logger.info("Starting PoE2 Crafting Data Scraper")
    logger.info(f"Mode: {args}")
    
    try:
        if args.prices:
            logger.info("Executing: Quick price update")
            result = quick_price_update()
            if result:
                logger.info("✓ Price update completed successfully")
            else:
                logger.warning("⚠ Price update completed with warnings")
                sys.exit(1)
        
        elif args.update:
            logger.info("Executing: Full data update")
            result = full_update()
            if result:
                logger.info("✓ Full update completed successfully")
            else:
                logger.warning("⚠ Full update completed with warnings")
                sys.exit(1)
        
        elif args.schedule:
            logger.info("Executing: Start scheduler (foreground)")
            scheduler = get_scheduler()
            scheduler.start()
        
        elif args.schedule_background:
            logger.info("Executing: Start scheduler (background)")
            scheduler = get_scheduler()
            scheduler.start_background()
            logger.info("Scheduler is running in background")
            logger.info("Press Ctrl+C to stop")
            
            try:
                while True:
                    import time
                    time.sleep(1)
            except KeyboardInterrupt:
                logger.info("Background scheduler stopped by user")
    
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
