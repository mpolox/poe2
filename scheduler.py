"""
Scheduler for weekly data updates
Runs using schedule library
"""

import schedule
import time
from datetime import datetime
from utils import get_logger
from file_updater import quick_price_update, full_update
from config import UPDATE_SCHEDULE

logger = get_logger()

class DataUpdateScheduler:
    """Manages scheduled data updates"""
    
    def __init__(self):
        self.schedule_map = {
            'prices': self.schedule_price_update,
            'omens': self.schedule_omen_update,
            'currency': self.schedule_currency_update,
            'league_info': self.schedule_league_update
        }
    
    def schedule_price_update(self):
        """Schedule price updates weekly (Sundays at 10 AM)"""
        schedule.every().sunday.at("10:00").do(
            self.run_task,
            task_name="Price Update",
            func=quick_price_update
        )
        logger.info("Scheduled: Weekly price update every Sunday at 10:00 AM")
    
    def schedule_omen_update(self):
        """Schedule omen database update monthly"""
        schedule.every().sunday.at("11:00").do(
            self.run_task,
            task_name="Omen Update",
            func=full_update
        )
        logger.info("Scheduled: Monthly omen update (runs weekly, updates omens if needed)")
    
    def schedule_currency_update(self):
        """Schedule currency rate updates"""
        schedule.every().monday.at("10:00").do(
            self.run_task,
            task_name="Currency Update",
            func=full_update
        )
        logger.info("Scheduled: Weekly currency update every Monday at 10:00 AM")
    
    def schedule_league_update(self):
        """Schedule league info updates"""
        schedule.every().sunday.at("09:00").do(
            self.run_task,
            task_name="League Info Update",
            func=quick_price_update
        )
        logger.info("Scheduled: Weekly league info update every Sunday at 9:00 AM")
    
    def schedule_all(self):
        """Setup all scheduled tasks"""
        logger.info("Setting up data update schedule...")
        
        for task_type, schedule_func in self.schedule_map.items():
            try:
                schedule_func()
            except Exception as e:
                logger.error(f"Failed to schedule {task_type}: {e}")
        
        logger.info("Schedule setup complete")
    
    @staticmethod
    def run_task(task_name, func):
        """Run a scheduled task with logging"""
        logger.info(f"▶ Starting: {task_name}")
        start_time = datetime.now()
        
        try:
            result = func()
            elapsed = (datetime.now() - start_time).total_seconds()
            logger.info(f"✓ Completed: {task_name} ({elapsed:.2f}s)")
            return result
        except Exception as e:
            elapsed = (datetime.now() - start_time).total_seconds()
            logger.error(f"✗ Failed: {task_name} - {e} ({elapsed:.2f}s)")
            return False
    
    def start(self):
        """Start the scheduler (blocking)"""
        logger.info("Starting PoE2 data scheduler...")
        self.schedule_all()
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            logger.info("Scheduler stopped by user")
    
    def start_background(self):
        """Start scheduler in background thread"""
        import threading
        
        self.schedule_all()
        
        def run_scheduler():
            try:
                while True:
                    schedule.run_pending()
                    time.sleep(60)
            except Exception as e:
                logger.error(f"Scheduler error: {e}")
        
        thread = threading.Thread(target=run_scheduler, daemon=True)
        thread.start()
        logger.info("Scheduler started in background thread")
        return thread


def get_scheduler():
    """Get or create scheduler instance"""
    global _scheduler
    if '_scheduler' not in globals():
        _scheduler = DataUpdateScheduler()
    return _scheduler


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--background":
        logger.info("Starting scheduler in background mode")
        scheduler = get_scheduler()
        scheduler.start_background()
        
        # Keep main thread alive
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Background scheduler stopped")
    else:
        logger.info("Starting scheduler in foreground mode")
        scheduler = get_scheduler()
        scheduler.start()
