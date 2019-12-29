# Homework 5: Load Balancing the Activity Logger

The purpose of this homework is to:

1. Gain hands-on experience with HTTP load balancing
2. Lay the ground-work for improved fault-tolerance and resiliency of the activity logger microservice

## What you need first

You must have Wolfit and the Activity Log microservice working and integrated together in order to complete this assignment.

## Install and enable ```nginx```

Using the instructions provided, install and configure the ```nginx``` web server. This is the tool you will be using to load balance your microservice. Make sure you preserve the default configuration for the server as you will be modifying this to turn on the load balancing capabilities.

## Configure ```nginx``` for load balancing
For this assignment you will run ```nginx``` on your designated machine (the same one where you run Wolfit and the activity logging microservice). Using the guidance already shared, you should modify your configuration to support simple round-robin load balancing between two instances of your microservices. Here's an example of what a portion of your ```nginx.conf``` file might look like:

```
http {
    upstream backend {
      server localhost:5001;
      server localhost:5002;
    }

    server {
        listen 8080;
        location / {
            proxy_pass http://backend;
        }
    }
```

Note that this is just a portion as there are other elements that must still be present in order for ```nginx``` to run properly. The sections you see above are essentially additions to the existing configuration.

## Run two instances of your activity logging microservice

By inspecting the configuration example above, you see two ```backend references```; these are the services that need to be running behind the load balancer:

```
server localhost:5001;
server localhost:5002;
```

This means you will run two separate instances of your microservice: one running on port 5001, the other on 5002.

## Verify the load balancing is working
By inspecting the configuration above, you see that the ```nginx``` server is listening on port 8080. Once you start the ```nginx``` server you can verify that it is running and that that requests are alternating between your two services. If you are calling into a VM you will need to change ```localhost``` to the IP or hostname that your VM will respond to.

http://localhost:8080/api/activities/

## Experiment with a failed server

Once you have the load balancing working, kill one of your microservice instances (Ctrl-C will work for this). Keep refreshing the browser and observe: you should see valid responses coming back to your browser, but now all traffic should be going to the single remaining instance of your microservice.

## Tying it back to Wolfit

Wolfit is likely configured to talk to a single instance of the activity logging microservice, such as ```localhost:5001```. Change this configuration to point to the load balancing ```nginx``` proxy, likely ```localhost:8080```. Go through a few interactions on the Wolfit web site (login, up vote, write a new post, etc.) and observe the ```POST``` actions alternating between your two microservices.

Turning in your work
* A repository was created for you as a holding place for evidence ```hw5-<username>)```. This is URL you will turn into Moodle.
* Copy the ```nginx.conf``` file that you created to the root of this repository and commit it.
* Create an ```evidence/``` folder and include evidence that your load balancing is working into this folder. Examples:
    * Screen shots showing POSTs or similar operations alternating between your two microservices.
    * Record a video / screencast and include the video file.
    * Text logs of your terminal sessions showing your two services alternating traffic.
    * Alternatively, with instructor approval, demonstrate these function in class or during office hours.