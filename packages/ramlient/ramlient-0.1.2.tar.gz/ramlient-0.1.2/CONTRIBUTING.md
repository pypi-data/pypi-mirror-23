# Contributing

Thank you for helping ramlient to get a better piece of software.

## Support

If you have any questions regarding the usage of ramlient please use [StackOverflow](https://stackoverflow.com).

## Reporting Issues / Proposing Features

Before you submit an Issue or proposing a Feature check the existing Issues in order to avoid duplicates. <br>
Please make sure you provide enough information to work on your submitted Issue or proposed Feature:

* Which version of ramlient are you using?
* Which version of python are you using?
* On which platform are you running ramlient?

## Pull Requests

We are very happy to receive Pull Requests considering:

* Style Guide. Follow the rules of [PEP8](http://legacy.python.org/dev/peps/pep-0008/), but you may ignore *too-long-lines* and similar warnings. There is a *pylintrc* file for more information.
* Tests. If our change affects python code inside the source code directory, please make sure your code is covered by an automated test case.

### Testing

To test the ramlient source code against all supported python versions you should use *tox*:

```bash
cd ~/work/ramlient
pip install tox
tox
```

However, if you want to test your code on certain circumstances you can create a *virtualenv*:

```
cd ~/work/ramlient
virtualenv env
source env/bin/activate
pip install -r development.txt
pip install .
nosetests --rednose -v tests/ --with-cover --cover-package=ramlient/
```
