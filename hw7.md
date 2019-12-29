# Homework 7: Asynchronous Microservice Calls

The purpose of this homework is to:

1. Observe how an interconnected system with microservices behaves (and degrades) as we introduce latency.
2. Implement an asynchronous queuing strategy within Wolfit to deal with activity logging latency.

## What you need first

You must have Wolfit and the Activity Log microservice working and integrated together in order to complete this assignment. You do not need to use load balancing for this assignment, though running the microservice on Heroku is ok (but not required).

## Introduce simulated latency to the microservice

We will simulate increased [latency](http://www.plugthingsin.com/internet/speed/latency/) in the activity logging microservice in a very simple way: by introduce a ```sleep``` function call into the new activity post function. To do this, you will import the ```time``` module at the top of your microservice app:

```
import time
```

You'll want to make the duration of the sleep an environment variable so that you can easily turn it on or off. In the same place you configure your MongoDB connection, you can add a variable ```sleep_time``` that you load from the environment variable ```SLEEP_TIME```:

```
sleep_time = os.getenv('SLEEP_TIME', default=0)
```

Finally, you will simply make a call to the ```sleep()``` function after you save the object to the database. This will allow you to simulate latency in the response:

```
a.save()
time.sleep(int(sleep_time))
```

Once you've added this latency, test your microservice and prove to yourself that the POST method is indeed taking longer (by the ```SLEEP_TIME``` configuration amount). Then test Wolfit and see how it dramatically degrades performance of the app whenever the user performs an action that requires activity logging (login, logout, new post, up vote, down vote).

## Adapt Wolfit to call the log_event REST call asynchronously

Use the instructions provided elsewhere on the course site to add Redis to your environment. Then add the Celery library and run-time do your Wolfit project.

You will move the call to the ```requests.post``` from your ```log_event``` method, instead doing that work in a Celery task that will look something like this:

```
@celery.task
def post_activity(activity):
    url = app.config['LOGGER_URL']
    post_url = url + "/api/activities"
    try:
        r = requests.post(post_url, json=activity)
        ...
```

With this Celery task in place, your code in ```log_event()``` would look something like this:

```
def log_event(cls, user, details):
    new_activity = {
        "user_id": user.id,
        "username": user.username,
        "timestamp": str(datetime.utcnow()),
        "details": details,
    }
    post_activity.delay(new_activity)
```

## Turning in your work

* Continue working in your ```hw3-username``` and ```wolfit-username``` repositories.
* Create an ```evidence/hw7``` folder under ```hw3-username``` and include evidence that your simulated latency and asynchronous event logging are working. Examples:
    * Screen shots or trace logs showing the Celery and/or Redis queue monitoring.
    * Alternatively, with instructor approval, demonstrate these function in class or during office hours.
* Submit URLs to both of your repositories.