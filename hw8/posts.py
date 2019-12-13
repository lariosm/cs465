from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
POSTS = {
    "0": {
        "user_id": 5,
        "username": "john",
        "category": "CS360: Programming Languages",
        "title": "Haskell on Windows",
        "url": "http://www.example.com",
        "body": "What tools do I need to start programming on Windows?",
        "timestamp": get_timestamp(),
    },
    "1": {
        "user_id": 7,
        "username": "amy",
        "category": "For sale",
        "title": "iPhone X - EXCELLENT CONDITION!",
        "url": "http://www.example.net",
        "body": "Looking to upgrade to iPhone 11 and need this gone ASAP.",
        "timestamp": get_timestamp(),
    },
    "2": {
        "user_id": 12,
        "username": "joe",
        "category": "Off topic",
        "title": "Ford v Ferrari",
        "url": "http://www.example.org",
        "body": "What do y\"all think? Should I go watch it?",
        "timestamp": get_timestamp(),
    }
}


# Create a handler for our read (GET) posts
def read():
    """
    This function responds to a request for /api/posts
    with a list of posts

    :return:        sorted list of posts
    """
    # Create the list of posts from our data
    return [POSTS[key] for key in sorted(POSTS.keys())]
