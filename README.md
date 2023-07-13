# Task Manager Application

This is a command-line task manager application built using Python. It allows users to manage their tasks, track their performance, and redeem rewards based on their completed tasks.

## Features

1. User Authentication
   - Users can create an account and log in to the task manager application.
   - Usernames and passwords are stored securely in a PostgreSQL database.

2. Task Management
   - Users can add, view, edit, and delete tasks.
   - Tasks are stored in the user's personal task table in the database.
   - Tasks include details such as task name, due date, points, and status.
   - Users can mark tasks as complete or overdue based on the due date.
   - Completed tasks can be viewed and deleted.

3. Points and Rewards System
   - Users can earn points for completing tasks.
   - Points are tracked in the database and can be used to redeem rewards.
   - Users can view their total points and available rewards.
   - Rewards include a name and point value.
   - Users can redeem rewards if they have enough points.
   - Rewards can be viewed, edited, or deleted.

4. Performance Tracking
   - Users can view their task performance in the form of a bar chart.
   - The chart shows the count of tasks based on their status (complete, overdue, etc.).
   - Performance data is retrieved from the database.

## Usage

1. Registration and Login
   - Use the application's registration feature to create a new account.
   - Log in with your username and password to access the task manager.

2. Task Management
   - Use the provided menu options to add, view, edit, or delete tasks.
   - Mark tasks as complete or overdue based on the due date.
   - View completed tasks and delete them if needed.

3. Points and Rewards
   - Earn points by completing tasks.
   - View your total points and available rewards.
   - Redeem rewards if you have enough points.
   - View, edit, or delete rewards as desired.

4. Performance Tracking
   - View your task performance in a bar chart.
   - The chart shows the count of tasks based on their status.
   - Use the menu option to access the performance chart.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. 
