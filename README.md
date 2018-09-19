# [Task-Manager](https://ddeveloper72-taskmanager.herokuapp.com/)
# How Python Talks to Data in...
# The Mini-Walk Through Project
# A part of Data Centric Development


Welcome to my Python project on Cloud9 IDE!  Yes I've taken over the default Readme
to add in a few more bits about what this 
[Code Institute](https://courses.codeinstitute.net/) tutorial was all about.

This tutoral focused on creating a python app which at its heart, lets a user 
perform CRUD operations on a simple task manager database.
The database is hosted on [mLab](https://mlab.com/)

Remember, CRUD -> ```Create, Read, Update, Delete```

The Learning Outcomes Are:

1 Setting up a MongoDB database in the cloud

   * Register and account with [mLab](https://mlab.com/), 
   * Creating a database
    
2 Accessing MongoDB command line tools to manipulate data

   * Connect using the mongo shell 


3 Connecting to MongoDB using Python

   * Connect using a driver via the standard MongoDB URI
    
4 Create a menu driven database system.

   * Build helper functions that will allow us to use a command line menu to:
   
    1. Add a record
    2. Find a record by name
    3. Edit a record
    4. Delete a record
    5. Exit the program

5 Create a task manager, built using Flask, MongoDB and a front-end framework
called Materialize

## Setting up the Python Flask app:
**(Code Institute Tutorial)**


1 Our pre-requisite Imports:

```python
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
```

2 To connect using a driver via the standard MongoDB URI:

```python
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb://root:dandn72@ds155352.mlab.com:55352/task_manager'
```


## Now lets break it down:
Remember, that this is this excercise, we are going to create infomation, find
find information, update existing information and the remove information. So to do
these things, we create a note pad of each of the app functions.

This is a task manager so what does it need to do?
Well here's our list of things that any good taks manager would let us do:
1 It must show a list of tasks,
2 It must let us use categories to help us sort our information in the future,
3 A Calandar for task would be useful,
4 A way to prioratise a taks with a urgent/not urgent flag is a must,
5 To future-proof our tasks manager, we need to update tasks or category information,
6 Lastly we ahve to be able to delete information when a mistake is made or a
task is complete.

![Task Manager](https://github.com/ddeveloper72/Task-Manager/blob/master/images/TaskManagerDesk.PNG "Fig 1 showing Task Manager")

![Adding a Task](https://github.com/ddeveloper72/Task-Manager/blob/master/images/TaskManagerAddTask.PNG "Fig 2 showing Adding a Task")

![Adding a Date](https://github.com/ddeveloper72/Task-Manager/blob/master/images/TaskManagerCalTask.PNG "Fig 3 showing Adding a Date")

![Adding Categories](https://github.com/ddeveloper72/Task-Manager/blob/master/images/TaskManagerAddCategories.PNG "Fig 3 showing Adding Categories")


So lets note down some steps that we will flesh out:

This is some sample data to help visualise what we are going to be work on:

### Tasks - Our first Boilerplate template made on mLab

```javascript
{
    "_id": {
        "$oid": "5b9fab97ee440cc84eae7ed0"
    },
    "due_date": "31 October, 2018",
    "task_description": "Contact the travel agent.\r\nReference is Sandra.\r\nGive her the booking number.",
    "is_urgent": "on",
    "action": "",
    "category_name": "Vacation",
    "task_name": "Sample Task - Remember to pickup the tickets"
}
```
1 Get - find and read back data then display everything to us.

```python
@app.route('/get_tasks')
```

2 Add - A page with tools on it that lets us add new information to the taks form.

```python
@app.route('/add_task')
```

3 Insert - Takes information typed in by the user as a POST function and sends it to
the database to create a new task in the form of a dictionary 
(see Our first Boilerplate above)

```python
@app.route('/insert_task')
```

4 Edit - Like the add function, edit brings us to a page with tools on it for 
editing a task.  It does this by first finding the task based on our selection and
the presenting all the task data to us as a editable form.

```python
@app.route('/edit_task/<task_id>')
```

5 Update - Remember that the task is in dictionary format. Update lets us easily iterate through and change each value listed
in the dictionary.


```python
@app.route('/update_task/<task_id>')
```

6 Delete - Finds the id of the object (the dictionary) selected and removes it from the database.

```python
@app.route('/delete_task/<task_id>')
```

Some useful things to remember.  Anything to do with changing the task data, 
uses the task_id to help Flask know exactly which bit of data we are going to be
working on.  That means, the data inside the object, is identified by the id.  
That's why they are in the app.route decorators.
Get, Add & Insert deal with the database that has all the different task ids.  
They are not id specific. Add for instance, tells the database to add a new object and 
when that happens, the database server gives that new object a unique id.

![A look at the tasks on mLab](https://github.com/ddeveloper72/Task-Manager/blob/master/images/mLabTasks.PNG "Fig 4 showing Tasks on mLab")



### Categories -  Our second Boilerplate template made on mLab

```javascript
{
    "_id": {
        "$oid": "5b9a57d1e7179a73d493b5d4"
    },
    "category_name": "Work"
}
```

1 Get - find and read back data then display everything to us.

```python
@app.route('/get_categories')
```

2 Edit - Sends us to a page with tools on it for editing a category. 

```python
@app.route('/edit_category/<category_id>')
```

3 Update - Remember that the category is an object in and has its own unique
id.

```python
@app.route('/update_category/<category_id>')
```

4 Delete - Finds the id of the category object selected and removes it from the database.

```python
@app.route('/delete_category/<category_id>')
```

5 Insert - Takes information typed in by the user as a POST function and sends it to
the database to create a new category in the form of a dictionary. 
(see Our second Boilerplate above)

```python
@app.route('/insert_category')
```

6 New - Sends us to a page with tools on it for adding another category. 

```python
@app.route('/new_category')
```

![A look at the categories on mLab](https://github.com/ddeveloper72/Task-Manager/blob/master/images/mLabCategories.PNG "Fig 5 showing Categories on mLab")
