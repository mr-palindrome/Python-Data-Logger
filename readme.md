# Python-Data-Logger
An example of python data logger script to store data from microcontroller sensors to sqlite3.

<h2>Overview</h2>
These are the scripts where we are storing data from microcontroller sensors to sqlite3.

The scripts use the **psutil** library to collect information from the sensors. To install this library: 
<h4>For Linux</h4>

```
sudo apt-get update
sudo apt-get upgrade
sudo pip3 install psutil
```

<h4>For Windows</h4>

```
pip install psutil
```

The **sqlite** version required that sqlite be install. It will come with python already. However, if you want to work with sqlite outside of python to create and query the day, you may need to install with `sudo apt-get install sqlite3`. When you open up a connect to a SQLite database, the database will be created if it does not exist. To open the database from the command prompt, navigate to the database directly and type `sqlite3 DBNAME.db` where DBNAME is the name of your database. You can [find more information](https://sqlite.org/index.html) about SQLite on their database.

Create a table in that database according to your requirements. You can [find more information](https://sqlite.org/index.html) about SQLite.

SQLite is the database that I used in this example, but you can substitute any other type of database in the script that I've provided. Typically a connection string is required in more traditional databases in the `connect()` call. However, you should consult the API of the database you would like to use for more details about connection methods.
