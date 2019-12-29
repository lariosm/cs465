# Homework 6: Deploying Activity Logger to the Cloud

The purpose of this homework is to:

1. Gain hands-on experience deploying a microservice to a cloud platform.
2. Learn how to apply several of the Twelve-Factor App principles as related to cloud-based deployment.

## What you need first

You must have Wolfit and the Activity Log microservice working and integrated together in order to complete this assignment.

## Create a free Heroku account.

[Sign up for a free account on the Heroku](https://signup.heroku.com/) cloud platform.

## Create an app for your microservice

Using the instructions and content provided for this week, create an app on the Heroku platform. Make sure you stick to the free tier. This app will give you all of the information you need to access it on the web, as well as instructions on how to push to it from your git repository.

## Configure and run your activity logger microservice on Heroku

Using the instructions and content provided for the week, configure your app to be deployable to Heroku. This will likely require (at a minimum):

* Moving your MongoDB hosting to a free cloud provider like mLab
* Creating a ```Procfile``` to tell Heroku how to run your microservice
* Ensuring you have a **durable production** configuration for your app that will allow it to safely run both locally (**dev** and **test** configurations) and in the live production environment _without modifying the application_. This will require that you adhere properly to [III. Config](https://12factor.net/config).
* Set environment variables on Heroku using either the browser-based interface or the Heroku command-line tools.
## Connect Wolfit to this new activity logger instance

Adjust your Wolfit configuration so that it now finds the activity logging microservice on Heroku. Again, this should be a configuration option for Wolfit.

## Turning in your work
* Continue working in your ```hw3-username``` repository. Your microservice will evolve to include additional configuration and production deployment parameters such as the ```Procfile```
* Create an ```evidence/hw6``` folder and include evidence that your Heroku deployment is working. Examples:
    * Screen shots showing you accessing the GET methods of your service running on Heroku.
    * Screen shots showing Wolfit activity logging landing in a hosted MongoDB.
    * Alternatively, with instructor approval, demonstrate these function in class or during office hours.