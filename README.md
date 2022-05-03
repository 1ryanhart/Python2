# Meme Generator

## Overview

This is a project submission in the Udacity Intermediate Python nanodegree. The program is a meme generator which can be run from the command line or on a browser via a Flask server.

## Installing Dependencies and Running

1. **Python 3.10** - Pthon 3.10 was used. Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Environment** - It is recommend to work within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by and running:
```bash
$ pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

4. **Running local Flask server** - Set up the local Flask server by running:
```bash
$ python app.py run
```

or

```bash
$ export FLASK_APP=hello
$ flask run
```

Open http://127.0.0.1:5000/ in a web browser to access the app. 

5. **Generating memes from the command line** - The app can be run from the command line, without the need to set up a Flask server. Navigate to the root directory (src) and run:

```bash
$ python meme.py --path {path} --body {body} --author {author}
```

Path, body and author are all optional arguements. If none are passed, then defaults are randomly selected.
- Path is the file path to the image for the meme. 
- Body is the body of the quote.
- Author is the author of the quote.


## Modules

### MemeEngine
The MemeEngine module contains only the MemeEngine class with is instantiated when the app is ran (either in the command line or via Flask server). This class has the *makememe* method which takes 3 parameters (image path, body, author) and returns to path to a generated meme 

### QuoteEngine
The QuoteEngine module contains the following:
- **IngestorInterface** -  An abstract base class for other specific child Ingestors to inherit from. Defines the *can_ingest* and *parse* methods 
- **Ingestors** - Childer IngestorInterface classes to parse .txt, .pdf, .docx or .csv files and to generate Quote objects from the parsed text
- **Ingestor** - Realises the IngestorInterface abstract base class. Used as a 
    selector to parse a given file to the correct Ingestor (pdf, txt, docx, csv).
