# Homework 3: Writing a simple RESTful web service

The purpose of this homework is to:

1. Learn how to build a simple REST endpoint based on a defined message structure.
2. Prepare a foundation of code and knowledge for building a fully database-backed microservice.

## Motivation for writing a new service

The organization that built Wolfit (where you are a developer) is growing and adding new apps to their inventory. The plan is to have these new apps share the same authentication platform (aka "single sign-on", or SSO). That will happen later, but for now as a first step we want to extract out the activity logging functionality from within the app and write a microservice to fulfill this function. By encapsulating activity logging as a separate microservice, the organization will be able to:

* Allow multiple applications to log activities to a central service
* Decouple the individual apps from the database backend that is used to store activity logging. This will allow, for example, a migration away from SQLite to a database platform that is better suited for user activity logging.
* If needed, because activity logging is not essential for the user experience of Wolfit, the process of logging events can be done asynchronously to reduce blocking wait times for the end user.

## Building your first microservice

You will be building a microservice, which is simply a web app that knows how to respond to a subset of the RESTful commands along a few end points. For this week you will not be completing the microservice by making it fully database-backed. We just want a working endpoint that responds correctly to the calls and can process and validate the right sorts of JSON messages.

It is helpful to think about the microservice as having some verbs and nouns corresponding to the functions it needs to provide. Because we aren't inventing this service out of the blue and it is being extracted out of the Wolfit app, we can learn from how it is invoked there and what data is required. The nouns involved are **JSON messages**, while the verbs will come from REST itself, limiting us to GET, PUT/POST, PATCH, and DELETE. Because the function we are building is activity logging, we intentionally do not want to support the PATCH or DELETE verbs because we want our log to be write-once and immutable via the service API.

### Message structure

There are many ways you can think about defining and describing the message structure. A good starting point is to look at the object schema specification in Python where we originally defined an ActivityLog entry in ```models.py```:

```
class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    details = db.Column(db.Text)
```

The ```db.*``` portions are specific to the SQLAlchemy object-relational database layer, and only serve to confuse things when we think about message structure. Also, for reasons that will become more clear later, let's also include the user_name. So let's simplify the above and use our own ad-hoc schema definition:

```
ActivityLog:
    id: string
    timestamp: timestamp
    username: string
    user_id: int
    details: string
```

Note that we are changing the identifier of the log entry itself type from an integer to a string. This is because we will want to leverage some of the internal unique identifier capabilities in our future database environment, and moving to a string type will keep things more flexible.

This is probably good enough to move forward, but it is worth mentioning that there are many options to add more rigor to both schema definition and validation. One example is Cerberus, a Python-based JSON schema validation tool. A Cerberus schema is just a Python dictionary that describes what a JSON message should look like (and also allows you to validate if a given message instance adheres to the schema). For example, this would be a schema we might use for our ActivityLog:

```
activity_log_schema = {
    'id': {'type': 'string'},
    'timestamp': {'type': 'datetime'},
    'user_id': {'type': 'integer'},
    'username': {'type': 'string'},
    'details': {'type': 'string'},
}
```

So a JSON message for a single log entry that adheres to this schema would look something like:

```
{
    "id": "12345",
    "timestamp": "Sat, 06 Oct 2018 16:00:32 GMT",
    "user_id": 1,
    "username": "john",
    "details": "Important stuff here",
}
```

### The service API

Here's a detailed description of the endpoints (with REST verbs) that you will be building for this assignment:

* ```GET: /api/activities``` -- returns the most recent "n" activity entries, where "n" is a service-defined variable. Because you will be using dummy data without a database for this assignment, you can return all activities in the list. This method should return a JSON document with a single key value named ```activities``` which in turn contains an array of "n" activity entries.

* ```GET: /api/activities/<id>``` -- return a single activity entry corresponding to the specified id.

* ```POST: /api/activities``` -- create a new activity entry. The inbound message should not contain an ID as that is system generated. This endpoint will return the created activity (as JSON) with the id field populated.

### How to build your microservice

* Use the Flask framework to build your app.
* For this assignment you are not required to write automated ```pytest``` tests.
* This will be a "single file application", with all application code in a file called ```app.py```. You will likely have 4 files checked in for the homework in the repository I create for you:
    * ```app.py``` -- the application code
    * ```Pipfile``` -- generated by pipenv. Use Python 3.7.
    * ```Pipfile.lock``` -- generated by pipenv.
    * ```rundev.sh``` -- Helper script to run your server. Makes it easier to ensure environment variables like ```FLASK_APP``` and ```FLASK_ENV``` are set properly.

Because you will not be interacting with a "real" database for this assignment, at the top of your ```app.py``` file you can create a list of 2 or more activity log entries that you will use for the to GET end points. Use this as a starting point:

```
activity_log = [
    {
        'id': '0',
        'user_id': 1,
        'username': 'john',
        'timestamp': datetime.utcnow(),
        'details': "Important stuff here",
    },
    {
        'id': '1',
        'user_id': 2,
        'username': 'yoko',
        'timestamp': datetime.utcnow(),
        'details': "Even more important",
    },
]
```

So if you used this exact list, you would have two valid IDs to lookup (0 and 1) and can return the proper one by simply indexing into the list (```activity_log[id]```).

The POST method does not need to modify this list and can simply generate a random ID and return a valid JSON activity message with the ID populated.

## Turning in your work

* Use the repository that is generated for you (will look something like ```hw3-<username>```).
* Use the ```curl``` tool to interact with your API. Capture a shell session (text only) where you interact with your API using ```curl``` and hit all three of the methods required. Save this in an ```evidence``` folder within this repository.
* Submit the URL for the repository (no need to point to a specific commit).