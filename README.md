# PyDo - Command-line Task Manager Application

PyDo is a feature-rich command-line task manager application built using Python **made by Sridhar**. It enables users to efficiently manage tasks, track performance, and redeem rewards for completed tasks. The application also incorporates a child and parent account system, allowing parents to oversee and manage tasks and rewards for their children.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

1. **User Authentication:**
   - Create an account and log in securely using a MySQL database for storage.

2. **Child and Parent Accounts:**
   - Parents can create and manage child accounts linked to their parent account.
   - Children can independently log in and manage their tasks and rewards.

3. **Task Management:**
   - Add, view, edit, and delete tasks.
   - Mark tasks as complete or overdue based on their due date.
   - View and delete completed tasks.

4. **Points and Rewards System:**
   - Earn points for completing tasks.
   - Points are tracked and can be used to redeem rewards.
   - View total points and available rewards.
   - Create, edit, or delete rewards.

5. **Performance Tracking:**
   - Visualize task performance through a bar chart.
   - The chart displays task status counts.

## Usage

1. **Registration and Login:**

   - To create a new account, use the registration feature.
   - Log in with your credentials to access the task manager.

2. **Child and Parent Accounts:**

   a. **Creating a Parent Account:**
   - During registration, select "Create Parent Account" to create one.
   - Provide the required details to set up the parent account.

   b. **Creating a Child Account:**
   - Parents can create child accounts from their parent account.
   - Log in as a parent, select "Create Child Account," and provide necessary details.
   - Child accounts are linked to the parent account for easy management.

   c. **Switching between Parent and Child Accounts:**
   - Parents can switch between their parent and children's accounts.
   - After logging in as a parent, choose "Switch to Child Account" and select the child account to manage.
   - Task and reward management will be specific to the selected child account.

3. **Task Management:**

   - Use the provided menu options for task management.
   - Tasks are categorized based on their status (Incomplete, Complete, Overdue).
   - Mark tasks as complete or overdue based on the due date.
   - View and delete completed tasks.

4. **Points and Rewards:**

   - Earn points by completing tasks.
   - View total points and available rewards.
   - Redeem rewards using points.
   - Create, edit, or delete rewards.

5. **Performance Tracking:**

   - View task performance through a bar chart.
   - The chart displays task status counts.
   - Access the performance chart from the menu.

## Contributing

Contributions are highly appreciated! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
