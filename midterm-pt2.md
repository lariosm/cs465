# Mid-term Programming Assignments

## Part 2 -- Call a REST/JSON service from Python (20 pts)

Create a Python command-line app (you can write a ```__main__``` conditional, but not required) that invokes this REST JSON service (use this exact URL):

https://reqres.in/api/unknown

Your program should print out the color "name" of the 0th and 1st items in the returned array of resources. The array is contained in the "data" element of the top level dictionary.

Name your Python file ```colors.py```, and it should be invoked as following and display the data shown:

```
$ python colors.py
cerulean
fuchsia rose
```

Use the following Python libraries in your solution:

* ```requests```: for querying the HTTP service. You'll need to install this with ```pipenv```
* ```json```: for processing the JSON response from the service

## How to submit your work

* I've automatically created a repository for you named ```midterm-client-<user>```. You should see this repository in your list.
* Push your work to this repository (after committing) for credit.