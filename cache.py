import json
import os
from datetime import datetime, timedelta
from config import CACHE_FILE

class CacheManager:
    def __init__(self, cache_duration_hours=1):
        self.cache_file = CACHE_FILE
        self.cache_duration = timedelta(hours=cache_duration_hours)
    
    def save_to_cache(self, data):
        """Save data to cache file"""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Cache save error: {e}")
            return False
    
    def load_from_cache(self):
        """Load data from cache if not expired"""
        if not os.path.exists(self.cache_file):
            return None
        
        try:
            with open(self.cache_file, 'r') as f:
                cache_data = json.load(f)
            
            # Check if cache is expired
            cache_time = datetime.fromisoformat(cache_data.get('posts', {}).get('timestamp', '2000-01-01'))
            if datetime.now() - cache_time > self.cache_duration:
                return None  # Cache expired
                
            return cache_data
        except Exception as e:
            print(f"Cache load error: {e}")
            return None
    
    def clear_cache(self):
        """Clear cache file"""
        if os.path.exists(self.cache_file):
            os.remove(self.cache_file)
            return True
        return False