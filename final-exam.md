# Final Exam - Programming

## Final exam: refactoring a microservice out of a monolith

Before you start your work, you must:

Clone the starting code repository:

```$ git clone https://github.com/wou-cs/microservice-final-microblog```

Move into this directory, then attach it to your personal private repository for the final. This will look something like this:

```
$ cd microservice-final-microblog
$ git remote rm origin
$ git remote add origin https://github.com/wou-cs/final-<your username>.git
$ git push -u origin master
```

**Make sure you remove the existing remote as this will ensure that you connect this local repo to the proper remote for your personal final project**.

Finally, make sure you can run the microblogging app. From the root of the project directory, do the following:

```
$ cd webapp
$ pipenv install --three
$ pipenv shell
$ ./rundev
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```

Browse to the running app to verify that it is running. You should see a home page with 3 statically generated posts displayed, along with their vote counts.

## Part 1 -- Create a REST/JSON microservice for vote counts (20 pts)

Examine the functionality in the web application regarding vote counts. Your first assignment is to extract the voting functionality (read-only) into a separate microservice. This microservice will provide both the plural and singular ```GET``` operations for vote counts, with API endpoints that look like the following:

```
http://localhost:5001/api/votes             <-- the plural GET
http://localhost:5001/api/votes/<post_id>     <-- the singular GET
```

The plural GET will return a JSON representation of the votes for all posts. You will use the same sample static data that is provided in the web application. This means the plural GET would return a response like this:

```
GET http://127.0.0.1:5001/api/votes

[
  {
    "post_id": 0, 
    "vote_count": -1
  }, 
  {
    "post_id": 1, 
    "vote_count": 5
  }, 
  {
    "post_id": 2, 
    "vote_count": 42
  }
]
```

The singlular GET will take an ID as a parameter, so the call for votes on post 0 would look like:

```
GET http://127.0.0.1:5001/api/votes/0

{
  "post_id": 0, 
  "vote_count": -1
}
```

Create a subdirectory under the root of your repository called ```microservice```. In this directory, you will create a Python Flask app, using ```pipenv``` to create your package manifest and virtual environment. You may copy over code from other Git repositories you own to help you get started.

Thoroughly test your microservice using a browser before continuing on to part 2. You'll want to run this microservice on a port other than 5000 in order to avoid conflicting with the web app.

## Part 2 -- Modify the web app to call your microservice (20 pts)

Once you have the microservice running, return to the web app to replace the static data structure used for tracking votes with calls to your microservice. You will modify both the ```index()``` and ```post(post_id)``` methods to make calls to your service.

Use the following Python libraries in your solution:

* ```requests```: for querying the HTTP service. You'll need to install this with ```pipenv```
* ```json```: for processing the JSON response from the service
Don't forget to run the microservice and the web app on different ports.

## How to submit your work

* I've automatically created a repository for you named ```final-<user>```. You should see this repository in your list.
* Push your work to this repository (after committing) for credit for both parts 1 and 2.