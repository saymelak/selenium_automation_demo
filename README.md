## Selenium automation framework - demo

This project was created just for demo proposes.

### Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

* Pip
* Python
* Chromedriver
* Some Python libraries following

#### Install the following Python libraries:

 * **nose 1.3.7**
 * **selenium 3.141.0**
 * **urllib3 1.25.10**


With:
```
pip install -r requirements.txt
```

#### Chromedriver

[Download chromedriver from the official repository.](https://chromedriver.chromium.org/downloads)
Then put the file in the lib folder

#### Running the code
You can use any of the following commands
```
nosetests -v
nosetests -a priority=high -v
nosetests -a priority=medium -v
nosetests -a priority=low -v
nosetests -a category=sanity -v
nosetests -a category=smoke -v
nosetests -a category=regression -v
```

