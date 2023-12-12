# User Guide

Pre-requisites: the app has been tested on Cubbli Linux (Ubuntu-based distro of University of Helsinki), using Python 3.10 and Git 2.34.1.

1. Download and unzip the source code of the [latest release](https://github.com/yogajones/ot-harjoitustyo/releases).

2. Navigate to the newly created unzipped folder. Install dependencies with Poetry:

```bash
poetry install
```

3. Initialize the database:
```bash
poetry run invoke build
```

4. Start the application:

```bash
poetry run invoke start
```

## Starting your first Learning Journey

Type the name of your first Learning Journey, such as "WSET Level 3 Award in Wines". Then, click on - *you guessed it!* - "Add".

## Managing Learning Objectives

To start structuring your learning, find out at least the first Learning Objective of the Journey you just begun. Often, Learning Objectives can be found in a course syllabus, in the beginning of a textbook chapter. Valuable Learning Objectives might also be defined in the beginning of an internship. Click on "Manage Objectives" to proceed.

## The Manage View

This is where you get an overview of the Learning Objectives for the Journey you just chose. To add your first, such as "Participate in a Wine Flight", type it in and click "Add". If, for some reason, you typed "Participate in a Wine Fight", there is a "Rename" button. Clicking it will take you to another view. Clicking "Delete" will make the new objective disappear for good.

## The Rename View

This view is as simple and intuitive as it gets. Enter a new name, click on "Save" and you will be redirected back to the view where you can manage Learning Objectives.

## The Evaluate View

Under construction. 