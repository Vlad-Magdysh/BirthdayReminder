# BirthdayReminder

## About this project
The Birthday Reminder is a handy tool designed to ensure that you never forget the important task of wishing your loved ones on their special day. This daily reminder system, which will be available on Linux and Windows platforms, leverages the power of SQL databases to maintain a list of birthdays and send out timely reminders. You can say goodbye to last-minute scrambles and missed birthdays, making celebrations more meaningful and stress-free.

## Architecture

<details>
<summary>Core</summary>

**Daily task**: The Python code, that manages existing birthdays. It decodes encrypted (optional) database, reads existing records, process them and produce detected birthdays.

**Service**: The Python code, that provides handlers for the UI, such as adding new birthdays, removing existing, editing, filtering.

**Installers:** Bash script, that executes UI and plan daily task.

- Windows installer: adds to the Task Scheduler
- Linux installer: adds to the Linux cron job
- Classes Structure
    
    BaseInstaller - a common class for all installers
    
    - WindowsInstaller - class that adds a new task to the Windows Task Scheduler
    - LinuxInstaller - class that adds a new cronjob for the Linux. Perhaps, it will add a systemctl task. TODO research cron VS systemctl

</details>

<details>
<summary>UI</summary>

Desktop application for Linux, Windows, macOS for managing birthdays

<details>
<summary>Classes Structure</summary>
TODO: Check if it is mandatory to define separate interfaces for operating systems.
</details>

</details>

<details>
<summary>Storage</summary>

Initially it will be a SQL database (SQLite), but I think about using Controllers as wrappers with a standardized interface for any database. 
<details>
<summary>Classes Structure</summary>
BaseController - the basic abstract class with the standardized interface of the all classes. All

- SQLController - the base class for all SQL-like databases. It is also an abstract class, which marks a group of controllers and extends BaseController with specific methods for the SQL databases (connections, models, etc).
    - SQLiteController - class with implementation of necessary methods, which uses SQLite database.
- NoSQLController - the base class for all NoSQL databases, like MongoDB, Elasticsearch, etc. It is also an abstract class, which is basic for all NoSQL controllers.
</details>

</details>

## Common Features & Options

<details>
<summary>Add/Update/Erase Birthday from the Database</summary>
This feature allows you to easily add a new birthday to the database, update an existing one, or erase an unwanted record. This ensures that your list of birthdays is always up-to-date.
</details>

<details>
<summary>Review all records in the Database</summary>
This feature provides a comprehensive view of all your records in the database. It allows you to easily navigate through your records and find the information you need.
</details>

<details>
<summary>Edit Record in the Database</summary>
This feature allows you to make changes to an existing record in the database. This is useful for updating information or correcting mistakes.
</details>

<details>
<summary>Choose the Time to Remind About the Birthday</summary>
This feature lets you select the specific time you would like to be reminded about a birthday. This ensures that you receive the reminder at a time that is most convenient for you.
</details>

## Advanced Features & Options

<details>
<summary>Pre-Reminders</summary>
In addition to the normal reminders on the day of the birthday, the system can be set to send out pre-reminders. This can be useful for those who want to prepare in advance.
</details>

<details>
<summary>Remind Me Later</summary>
If you can't attend to the reminder right away, you can choose the "remind me later" option. This will cause the system to send another reminder after a specified amount of time.
</details>

