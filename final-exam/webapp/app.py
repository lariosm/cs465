from flask import Flask, abort, render_template
import requests
import json


app = Flask(__name__)

POSTS = [
    {
        'id': 0,
        'title': "Interesting post",
        'content': 'Lorem ipsum etc.',
        'author': 'Poe',
    },
    {
        'id': 1,
        'title': "Storing data from csv file",
        'content': 'So I wanted a project that included a gui so I decided to write a script that would help me calculate wind adjustments (and maybe other stuff down the line) for playing Golf Clash. Basically every club has an "accuracy" and is affected differently depending on wind strength. I created a spreadsheet containing all the attributes for each club and saved it as a csv file. Here is a small sample...',  # noqa: E501
        'author': 'Joe',
    },
    {
        'id': 2,
        'title': "Django Rest Framework serialisation",
        'content': "I'm new to Python/Django and having trouble trying to serialize a N-N relation using Django Rest Framework.",  # noqa: E501
        'author': 'Moe',
    },
]


@app.route('/')
def index():
    get_url = "http://localhost:5001/api/votes"
    try:
        r = requests.get(get_url)
        if r.status_code == 200:
            data = json.loads(r.text)
            return render_template(
                "index.html",
                title="Microblog for Microservices",
                posts=POSTS,
                votes=data,
            )
    except requests.exceptions.RequestException:
        print(f"Could not connect to the service at {get_url}")


@app.route('/post/<int:post_id>')
def post(post_id):
    if post_id < 0 or post_id >= len(POSTS):
        abort(404)
    get_url = "http://localhost:5001/api/votes"
    try:
        r = requests.get(get_url)
        if r.status_code == 200:
            data = json.loads(r.text)
            post = POSTS[post_id]
            return render_template(
                "post.html",
                title=POSTS[post_id]['title'],
                post=post,
                vote_count=data[post_id]['vote_count'],
            )
    except requests.exceptions.RequestException:
        print(f"Could not connect to the service at {get_url}")
