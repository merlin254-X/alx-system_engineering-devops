#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given subreddit.
    If the subreddit is invalid or returns a redirect, return 0.
    """
    # URL for the subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid 'Too Many Requests' issues
    headers = {
        "User-Agent": "python:0x16.api.advanced:v1.0.0 (by /u/yourusername)"
    }

    try:
        # Send a GET request to the Reddit API with no redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code indicates success
        if response.status_code == 200:
            # Get the data from the response and return the number of subscribers
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        
        # If status code indicates not found or invalid, return 0
        elif response.status_code in (404, 302):
            return 0
        
        # For other unexpected status codes, return 0
        else:
            return 0
    
    except requests.RequestException:
        # Handle request-related errors
        return 0
    
    except ValueError:
        # Handle cases where JSON decoding fails
        return 0
