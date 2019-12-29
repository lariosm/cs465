# Mid-term Programming Assignments
## Part 1 -- Writing a REST/JSON Python Flask Service (20 pts)
Create a Python Flask app, using ```pipenv``` to create your package manifest and virtual environment. You may copy over code from other projects you own to help you get started.

Write a single API method in your microservice that takes a single positive integer parameter and returns a dictionary with several attributes about the provided integer. The URL that will be invoked should look something like this (use this to decide on how to name your route):

http://localhost:5000/api/intdata/256

This will return a JSON dictionary containing a few interesting attributes about the provided integer:

* "Even"ness - a boolean that is true if the integer is even.
* The inverted (negative) value of the integer.

Calling the API with the integer "256" would return JSON like this:

```
{
  "even":true, 
  "inverted":-256
}
```

Calling the API with the integer "1" would return JSON like this:

```
{
  "even":false, 
  "inverted":-1
}
```

## How to submit your work
1. I've automatically created a repository for you named ```midterm-server-<user>```. You should see this repository in your list.
2. Push your work to this repository (after committing) for credit.