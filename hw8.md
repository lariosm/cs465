# Homework 8: REST API Design

The purpose of this homework is to

1. Get hands-on experience designing your own REST API for a new microservice.
2. Use a higher-level framework to build your microservice and witness the benefits of API inspection.

## Building your second microservice

Having completed the activity logging microservice, it is time to factor out the next key component from the monolith: posts. Before we fully complete the transition, we want to built a static instance of the microservice while we refine the REST API we will use. To do this, we will use the [Connexion](https://connexion.readthedocs.io/en/latest/index.html) framework which runs on top of Flask.

### Message design

Using the experience you've gained from building the activity logger, design message structure for a post using the Swagger approach to designing an API. Pay attention to the [data types and formats](https://swagger.io/docs/specification/data-models/data-types/) available for Swagger specs.

### The service API

You only need to implement a single REST method:

```GET: /api/posts``` -- returns a static list of posts using the message format you have designed.

## How to build your microservice

* Use the Connexion framework to build your app.
* For this assignment you are not required to write automated ```pytest``` tests.
* Use this tutorial to build out the API described (```/api/people```) and get that working first.
* Modify the ```swagger.yml``` specification to use your ```posts``` message design.
* Rename ```people.py``` to ```posts.py```, substituting sample data that allows you to execute the API and inspect the results.

## Turning in your work

* Use the repository that is generated for you (will look something like ```hw8-<username>```).
* Include all source code and ```Pipfile.*``` for your project in this repo.
Create an ```evidence``` folder and show the following:
    * A screenshot of the UI for your API, likely at localhost:5000/api/ui/
    * A screenshot showing the execution of your ```posts``` API with returned static data.
* Submit the URL for the repository (no need to point to a specific commit).