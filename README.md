# Crawler

## Table of contents
* [Activation](#Activation)
* [Requirements](#Requirements)
* [Author](#Author)

This crawler is designed to search provided web page for urls, count internal and external links and references found in the web page and stores extracted data in a `.csv` file. Not only it search provided url but also every url that is referenced in that page.

## Activation

To activate crawler user must type in a command-line interface the  following code:
```
python main.py
```
After activation user must provide **url** for crawling, by writing/pasting it in the terminal. Operation may take a while to execute, depending on the complexity of the web page and quantity of the links. 

## Requirements

User must have installed following packages for the script to run:
```
requests
beautifulsoup
```

## Author

Andrzej Adahs
