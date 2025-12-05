import requests
import json
from config import API_BASE_URL, ENDPOINTS, TIMEOUT
from datetime import datetime

class APIHandler:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "GlobalTrend-API-Integration/1.0"
        })
    
    def fetch_data(self, endpoint_name):
        """Fetch data from API with error handling"""
        if endpoint_name not in ENDPOINTS:
            return {"error": f"Invalid endpoint: {endpoint_name}"}
        
        url = API_BASE_URL + ENDPOINTS[endpoint_name]
        
        try:
            response = self.session.get(url, timeout=TIMEOUT)
            response.raise_for_status()
            
            # Check if response is valid JSON
            data = response.json()
            
            # Validate response structure
            if not isinstance(data, list):
                return {"error": "Invalid response format: expected list"}
                
            return {"success": True, "data": data, "timestamp": datetime.now().isoformat()}
            
        except requests.exceptions.Timeout:
            return {"error": f"Request timeout after {TIMEOUT} seconds"}
        except requests.exceptions.ConnectionError:
            return {"error": "Network connection failed"}
        except requests.exceptions.HTTPError as e:
            return {"error": f"HTTP Error: {e.response.status_code}"}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response from server"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    def fetch_all_data(self):
        """Fetch data from both endpoints"""
        posts_data = self.fetch_data("posts")
        users_data = self.fetch_data("users")
        
        return {
            "posts": posts_data,
            "users": users_data
        }