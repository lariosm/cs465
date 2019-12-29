# Homework 9: Rolling microservice updates

The purpose of this homework is to

1. Learn the motivations behind the benefits of an architecture that supports live, rolling updates
2. Gain hands-on experience executing a live, rolling update with a microservice that you designed.

## Pick a microservice to start with
You've developed several microservices in this course. For this homework, choose one to work on for the purpose of this assignment. You might find it easiest to use the microservice developed for homework 8 using the Connexion library. You will only need to invoke a single ```GET``` method of this microservice (again, which method you invoke is up to you).

To help verify that the rolling upgrade works, you must add a new element to the dictionary returned by your ```GET``` method: ```"version"```. Your initial microservice should return ```"version": "1.0"``` to signify that this is the first version of the microservice.

### Create two separate working directories

From the starting point of having a working microservice (it isn't important to have this microservice talking to a database), clone it into two separate working directories on your computer. You'll need this in order to keep an "old" version running while you run a newer, enhanced version.

### Load balance the two microservices

Using the experience you had with ```nginx``` and load balancing, configure your load balancer to alternate traffic between two separate instances of this microservice. As a starting point, make sure you can run the microservice from each of the two directories (on separate ports of course) and load balance traffic between the two of them in a round-robin fashion.

## Develop a simple console client for your microservice
Write a small Python program to act as a client of your single ```GET``` method of your microservice. To demonstrate the benefit of a rolling upgrade, this program should repeatedly call the ```GET``` method with a ```sleep()``` between each invocation. Have the client print out an important element of the returned JSON object **along with the version of the API you are accessing**.

## Kill the old microservice, then run a second instance of the new one

To demonstrate the value of a rolling upgrade, kill the "old" microservice then run a second instance of the new one. You should see the load balancer automatically pick up the new instance (as long as you run it on the same port as the original) and begin the load balancing between two instances of the new version.

## Example output

Here's an example of what you might see in your output while load balancing between the two different versions microservices. In this case, I extended the "posts" microservice to include a new schema item: number of votes.

```
$ python main.py
Accessing posts on: http://localhost:8080/api/posts/1
Version: 1.0
Version: 2.0
  votes: 3
Version: 1.0
Version: 2.0
  votes: 3
Version: 1.0
Version: 2.0
  votes: 3
```

## Turning in your work

* Use the repository that is generated for you (will look something like ```hw9-<username>```).
* Include all source code and ```Pipfile.*``` for your test client in this repo. You do not need to share the source of your microservice for this homework.
* Create an ```evidence``` folder and show the following:
    * Screenshots or video showing the client running against the load balancer with both versions of the microservice (1.0 and 2.0).
    * Screenshots or video showing how the client is only accessing the 2.0 version (without any interruption) after you kill the 1.0 version. Again, the client should be accessing the microservice _through_ the load balancer.
* Submit the URL for the repository (no need to point to a specific commit).