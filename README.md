# Study App - Tkinter

This is a study app built using Tkinter to help with task management and studying. I created this app as a part of my learning journey.
I used PyInstaller to convert the `.py` script into an executable (`.exe`). I also added this executable to the Windows startup so that it automatically starts when the computer boots up and prompts for today's task list.

## Features

The app has 4 main tabs:

1. **To-Do List**
   - Add tasks
   - Mark tasks as completed or delete tasks

2. **Reminder**
   - Choose a task and set a message and reminder time (notification)

3. **Pomodoro Technique**
   - 25-minute timer with a 5-minute break after each session
   - Play music during the Pomodoro session

4. **Filter Tasks**
   - Filter tasks by date

## Libraries Used

- `pygame`: Used for playing music during Pomodoro sessions.
- `plyer`, `notify_py`: Used for notifications.
- `pymongo`: Used to connect to MongoDB.

## Issues

1. **Freezing on Setting Reminder**:
   When setting a reminder for a notification, the app freezes until the notification appears. For example, if you set a reminder for 5 minutes, the app will freeze for 5 minutes.


## Notifications

- I used `notify_py` for setting reminders and notifications in the app.

## Screenshots of Study App

- <img src="https://github.com/user-attachments/assets/6b87a107-93cf-4c00-837d-9d200589c595" width="400" />
  
- <img src="https://github.com/user-attachments/assets/2717aef4-ea64-41a3-99cd-3c4221f395a4" width="400" />
  
- <img src="https://github.com/user-attachments/assets/9fcce3c2-928c-45f6-b678-781ba641c0b5" width="400" />
  
- <img src="https://github.com/user-attachments/assets/8a3868a5-1430-4df9-8a68-4ca6062fc52e" width="400" />

## Screenshot of Notification

- <img src="https://github.com/user-attachments/assets/46ad2faa-b652-4f1c-a0d0-12ebea37e2b8" width="400" />

## Screenshot of MongoDB Cluster

- <img src="https://github.com/user-attachments/assets/1fd01ef4-20df-4995-a4e6-2b8827e64eab" width="400" />
