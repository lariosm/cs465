# Homework 1: String Compressor using Test Driven Development

The purpose of this homework is to give you some first-hand experience with Test Driven Development (TDD), as well as to familiarize you with the process of turning in assignments using commits to your personal Git repository. The problem you will be solving is not a difficult one, and you can probably find solutions in Python on the Internet with a search. Here's a statement of the problem to solve:

Implement a method to perform basic string compression using the counts of repeated characters, with the exception that a single non-repeating character will not include a count. For example, the string aabcccccaaa would become a2bc5a3. If the compressed string would not become smaller than the original string your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z, A-Z).

Additional examples:

```
encode("") == ""
encode("ab") == "ab"
encode("Aabb") == "Aab2"
encode("AAb") == "A2b"
```

This is an example of [run length encoding](https://en.wikipedia.org/wiki/Run-length_encoding), a simplistic approach to data compression.

## Solution requirements

* Develop your solution using Python 3.7 (or newer)

    * You will write a single function to implement the encoding:

        ```def encode(input_string):```

    * Your tests will be written and evaluated with the ```pytest``` library

    * There will be two files in your repository: ```encode.py``` and ```test_encode.py```.

* Make **incremental** commits to Git after each [red-green-refactor](https://www.jamesshore.com/Blog/Red-Green-Refactor.html) cycle (see below for an example of what a first commit might look like). "Incremental" means you perform Git commits as you successively make progress. A good benchmark for "make progress" is that you write and make pass a singular, granular test case.
    
    * Each commit should have a descriptive message describing what new case or situation was handled.

## Turning in your work

Your use of Git and your full commit history is an evaluated aspect of all your work in this course. As you work you should demonstrate good use of Git, our version control system. By "good" we mean that you should commit small, incremental changes and use meaningful commit messages.

Incremental changes mean that each commit should focus on a single issue, feature, or addition to your solution. For this assignment, a good guideline is to do a commit after you write a new test and subsequently implement code that allows the test to pass.

Commit messages should consist of a brief one-line summary and an optional, more detailed explanation separated by an empty line. For example, one commit message might be:

```
Handle the case of no repeating characters.

Because a string with no repeating characters will be incompressible, the returned string will match the provided string.
```

The first line of the commit message is similar to an email subject, and the optional explanation is like the body of an email message. [Consult this note for guidance on how to write good commit messages](https://chris.beams.io/posts/git-commit/).

You will turn in your work by submitting the commit URL to Moodle of the final commit within your repository. Spend some time understanding the different URLs that GitHub produces and provides. Do not submit a link to your repository when I ask for a commit URL -- know the difference. Understanding [URLs / URIs](https://danielmiessler.com/study/url-uri/) is an important element of understanding microservice architecture.

## Example first commit

```encode.py:```

```
def encode(input_string):
    return ""
```

```test_encode.py:```

```
from encode import encode


def test_empty_string():
    assert encode("") == ""
```