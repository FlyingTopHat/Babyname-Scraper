from setuptools import setup, find_packages

setup(
    name='babynamebot',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = babynamebot.settings']},
)
