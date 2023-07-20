# PyDo

PyDo is a command-line task manager application built using Python. It allows users to manage their tasks, track their performance, and redeem rewards based on their completed tasks. The application includes a child and parent account system, enabling parents to manage tasks and rewards for their children.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

PyDo offers the following features:

1. User Authentication:
   - Users can create an account and log in to the application.
   - Usernames and passwords are securely stored in a mySQL database.

2. Child and Parent Accounts:
   - Parents can create child accounts under their parent account.
   - Child accounts are linked to parent accounts for management purposes.
   - Parents have access to task and reward management for their children.
   - Children can log in to their accounts and manage their own tasks and rewards.

3. Task Management:
   - Users can add, view, edit, and delete tasks.
   - Tasks are stored in the user's personal task table in the database.
   - Each task includes details such as task name, due date, points, and status.
   - Tasks can be in one of the following modes:
     - Incomplete: Tasks that are not yet completed or overdue.
     - Complete: Tasks that have been successfully completed.
     - Overdue: Tasks that have passed the due date without being completed.
   - Users can mark tasks as complete or overdue based on the due date.
   - Completed tasks can be viewed and deleted.

4. Points and Rewards System:
   - Users can earn points for completing tasks.
   - Points are tracked in the database and can be used to redeem rewards.
   - Users can view their total points and available rewards.
   - Rewards include a name and point value.
   - Users can redeem rewards if they have enough points.
   - Rewards can be viewed, edited, or deleted.

5. Performance Tracking:
   - Users can view their task performance in the form of a bar chart.
   - The chart shows the count of tasks based on their status (incomplete, complete, overdue, etc.).
   - Performance data is retrieved from the database.


## Usage

1. Registration and Login:

- Parent accounts only work when there is already a Child Account.
- Use the application's registration feature to create a new account.
- Log in with your username and password to access the task manager.

2. Child and Parent Accounts:

   a. Creating a Parent Account:
   - Parents can create a parent account by selecting the "Create Parent Account" option during registration.
   - Provide the required details to create the parent account.

   b. Creating a Child Account:
   - Parents can create child accounts from their parent account.
   - Log in to the parent account and select the "Create Child Account" option.
   - Provide the required details to create the child account.
   - Child accounts are linked to the parent account for management purposes.

   c. Switching between Parent and Child Accounts:
   - Parents can switch between their parent account and their children's accounts.
   - After logging in as a parent, select the "Switch to Child Account" option.
   - Choose the child account you want to manage from the available options.
   - Task and reward management will be specific to the selected child account.

3. Task Management:

- Use the provided menu options to add, view, edit, or delete tasks.
- Tasks can be in one of the following modes:
  - Incomplete: Tasks that are not yet completed or overdue.
  - Complete: Tasks that have been successfully completed.
  - Overdue: Tasks that have passed the due date without being completed.
- Mark tasks as complete or overdue based on the due date.
- View completed tasks and delete them if needed.

4. Points and Rewards:

- Earn points by completing tasks.
- View your total points and available rewards.
- Redeem rewards if you have enough points.
- View, edit, or delete rewards as desired.

5. Performance Tracking:

- View your task performance in a bar chart.
- The chart shows the count of tasks based on their status.
- Use the menu option to access the performance chart.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
