import logging
import sys

def get_logger(name: str) -> logging.Logger:

    logger = logging.getLogger(name)
    # Avoid adding multiple handlers if the logger is requested multiple times
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Create console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        
        # Create formatter and add it to the handler
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(formatter)
        
        # Add the handler to the logger
        logger.addHandler(console_handler)
        
    return logger

logger = get_logger("quicklook")
