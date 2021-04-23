[![PyPI version](https://badge.fury.io/py/randdate.svg)](https://badge.fury.io/py/randdate)
[![randdate](https://snyk.io/advisor/python/randdate/badge.svg)](https://snyk.io/advisor/python/randdate)


# randdate
Generate a list of random dates (datetime objects).


## Installation
The `randdate` [git repo](http://github.com/kmedian/randdate) is available as [PyPi package](https://pypi.org/project/randdate)

```
pip install randdate
```


## Usage
Check the [examples](examples) folder for notebooks.


## Commands
* Check syntax: `flake8 --ignore=F401`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`
* Create README.rst: `pandoc README.md --from markdown --to rst -s -o README.rst`
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`


## Support
Please [open an issue](https://github.com/kmedian/randdate/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/kmedian/randdate/compare/).
