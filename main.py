from api_handler import APIHandler
from cache import CacheManager
import json

class GlobalTrendApp:
    def __init__(self):
        self.api = APIHandler()
        self.cache = CacheManager()
        self.data = None
    
    def load_data(self, force_fresh=False):
        """Load data from cache or fetch fresh"""
        if not force_fresh:
            cached_data = self.cache.load_from_cache()
            if cached_data:
                print("✓ Using cached data")
                self.data = cached_data
                return True
        
        print("Fetching fresh data from API...")
        fresh_data = self.api.fetch_all_data()
        
        # Check for errors
        errors = []
        for key, value in fresh_data.items():
            if "error" in value:
                errors.append(f"{key}: {value['error']}")
        
        if errors:
            print("❌ API Errors:")
            for error in errors:
                print(f"  - {error}")
            return False
        
        self.data = fresh_data
        self.cache.save_to_cache(fresh_data)
        print("✓ Data fetched and cached successfully")
        return True
    
    def list_posts(self, user_id=None, limit=None):
        """List posts with filtering"""
        if not self.data or "posts" not in self.data:
            print("No posts data available")
            return
        
        posts = self.data["posts"]["data"]
        
        # Filter by user_id if provided
        if user_id is not None:
            try:
                user_id = int(user_id)
                posts = [p for p in posts if p.get("userId") == user_id]
                if not posts:
                    print(f"No posts found for user ID: {user_id}")
                    return
            except ValueError:
                print("Invalid user ID")
                return
        
        # Apply limit if provided
        if limit is not None:
            try:
                limit = int(limit)
                posts = posts[:limit]
            except ValueError:
                print("Invalid limit value")
                return
        
        # Display posts
        print(f"\n📝 POSTS (Showing {len(posts)} items)")
        print("=" * 60)
        for post in posts:
            print(f"ID: {post['id']}")
            print(f"Title: {post['title'][:50]}...")
            print(f"User ID: {post['userId']}")
            print("-" * 40)
    
    def list_users(self, city_filter=None):
        """List users with optional filtering"""
        if not self.data or "users" not in self.data:
            print("No users data available")
            return
        
        users = self.data["users"]["data"]
        
        # Filter by city if provided
        if city_filter:
            users = [u for u in users if city_filter.lower() in u.get("address", {}).get("city", "").lower()]
            if not users:
                print(f"No users found in city containing: {city_filter}")
                return
        
        print(f"\n👥 USERS (Showing {len(users)} items)")
        print("=" * 60)
        for user in users:
            print(f"ID: {user['id']}")
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"City: {user['address']['city']}")
            print(f"Company: {user['company']['name']}")
            print("-" * 40)
    
    def show_post_detail(self, post_id):
        """Show detailed view of a single post"""
        if not self.data or "posts" not in self.data:
            print("No posts data available")
            return
        
        try:
            post_id = int(post_id)
            posts = self.data["posts"]["data"]
            post = next((p for p in posts if p["id"] == post_id), None)
            
            if not post:
                print(f"❌ Post with ID {post_id} not found")
                return
            
            # Find user info
            user = None
            if "users" in self.data:
                users = self.data["users"]["data"]
                user = next((u for u in users if u["id"] == post["userId"]), None)
            
            print(f"\n📄 POST DETAILS - ID: {post_id}")
            print("=" * 60)
            print(f"Title: {post['title']}")
            print(f"\nBody:\n{post['body']}")
            print(f"\nUser ID: {post['userId']}")
            
            if user:
                print(f"Author: {user['name']}")
                print(f"Email: {user['email']}")
            
            print(f"\n📊 Post Statistics:")
            print(f"  - Title length: {len(post['title'])} chars")
            print(f"  - Body length: {len(post['body'])} chars")
            
        except ValueError:
            print("Invalid post ID")
    
    def show_user_detail(self, user_id):
        """Show detailed view of a single user"""
        if not self.data or "users" not in self.data:
            print("No users data available")
            return
        
        try:
            user_id = int(user_id)
            users = self.data["users"]["data"]
            user = next((u for u in users if u["id"] == user_id), None)
            
            if not user:
                print(f"❌ User with ID {user_id} not found")
                return
            
            # Find user's posts
            user_posts = []
            if "posts" in self.data:
                posts = self.data["posts"]["data"]
                user_posts = [p for p in posts if p["userId"] == user_id]
            
            print(f"\n👤 USER DETAILS - ID: {user_id}")
            print("=" * 60)
            print(f"Name: {user['name']}")
            print(f"Username: {user['username']}")
            print(f"Email: {user['email']}")
            print(f"Phone: {user['phone']}")
            print(f"Website: {user['website']}")
            print(f"\n📍 Address:")
            print(f"  Street: {user['address']['street']}")
            print(f"  Suite: {user['address']['suite']}")
            print(f"  City: {user['address']['city']}")
            print(f"  Zipcode: {user['address']['zipcode']}")
            print(f"\n🏢 Company:")
            print(f"  Name: {user['company']['name']}")
            print(f"  Catchphrase: {user['company']['catchPhrase']}")
            print(f"  BS: {user['company']['bs']}")
            
            print(f"\n📝 User's Posts: {len(user_posts)} posts")
            if user_posts:
                for post in user_posts[:3]:  # Show first 3 posts
                    print(f"  - {post['title'][:50]}...")
                if len(user_posts) > 3:
                    print(f"  ... and {len(user_posts) - 3} more")
            
        except ValueError:
            print("Invalid user ID")
    
    def run_cli(self):
        """Run command-line interface"""
        print("\n" + "="*60)
        print("🌍 GLOBAL TREND - API Integration Internship Assignment")
        print("="*60)
        
        # Load data
        if not self.load_data():
            print("Failed to load data. Exiting...")
            return
        
        while True:
            print("\n" + "="*60)
            print("MAIN MENU")
            print("="*60)
            print("1. List Posts (with filters)")
            print("2. List Users (with filters)")
            print("3. View Post Details")
            print("4. View User Details")
            print("5. Refresh Data (force fresh fetch)")
            print("6. Clear Cache")
            print("7. Exit")
            print("-" * 40)
            
            choice = input("Enter choice (1-7): ").strip()
            
            if choice == "1":
                print("\n📝 POST FILTERS")
                print("-" * 40)
                user_id = input("Filter by User ID (press Enter to skip): ").strip()
                limit = input("Limit results (press Enter for all): ").strip()
                
                if user_id == "":
                    user_id = None
                if limit == "":
                    limit = None
                
                self.list_posts(user_id=user_id, limit=limit)
                
            elif choice == "2":
                print("\n👥 USER FILTERS")
                print("-" * 40)
                city = input("Filter by city (press Enter to skip): ").strip()
                if city == "":
                    city = None
                self.list_users(city_filter=city)
                
            elif choice == "3":
                post_id = input("Enter Post ID: ").strip()
                if post_id:
                    self.show_post_detail(post_id)
                else:
                    print("Please enter a Post ID")
                    
            elif choice == "4":
                user_id = input("Enter User ID: ").strip()
                if user_id:
                    self.show_user_detail(user_id)
                else:
                    print("Please enter a User ID")
                    
            elif choice == "5":
                print("Fetching fresh data...")
                if self.load_data(force_fresh=True):
                    print("✓ Data refreshed successfully")
                else:
                    print("❌ Failed to refresh data")
                    
            elif choice == "6":
                if self.cache.clear_cache():
                    print("✓ Cache cleared successfully")
                else:
                    print("✓ Cache already empty")
                    
            elif choice == "7":
                print("\nThank you for using Global Trend API App! 👋")
                break
                
            else:
                print("Invalid choice. Please enter 1-7")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    app = GlobalTrendApp()
    app.run_cli()