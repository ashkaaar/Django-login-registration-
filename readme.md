This is the Section 1 of devzery assigments. Total 40+ commits

#### Login Functionality:

- **User Registration and Authentication**:
  - Implement a user registration system with fields for username, email, and password.
  - Upon registration, send a confirmation email with a verification link. Users should only be able to log in after email verification.Users will only be able to log in after clicking the link to confirm their email addresses. Backend logic will validate the token and update the user's account status upon successful verification.

- **Profile Page**:
  - Create a user dashboard where registered users can:
    - View and edit their profiles (username, email).
    - View all the profiles registered.

- **Password Reset**:
  - Allow users to request a password reset via email. Generate a secure token for resetting the password.
 
# Installation and Setup

To test this on your local machine, follow these steps:

### Prerequisites

Before you begin, make sure you have the following installed:

- Python
- pip (Python package manager)
- Node.js (with npm, the Node.js package manager)

### Step 1: Clone the Repository

Open your terminal and navigate to the directory where you want to store the project. Then, run the following command to clone the repository:

```bash
git clone https://github.com/ashkaaar/devzery-assignment/
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
Navigate into the project directory:
```bash 
cd devzery-assignment
```

Create a virtual environment to isolate project dependencies:
```bash 
python -m venv venv
```

Activate the virtual environment:

On macOS or Linux:
```bash 
source venv/bin/activate
```

On Windows (Command Prompt)::
```bash 
venv\Scripts\activate
```

### Step 3: Install Backend Dependencies
While in the project directory and with your virtual environment activated, install the required backend dependencies using pip:

```bash
pip install -r requirements.txt
```
### Step 4: Configure the Database and Start Django Server
By default, the project uses a SQLite database. Initialize the database by running the following command:

```bash
python manage.py migrate
```

### Step 5: Create Superuser to Access Admin Portal
```bash
python manage.py createsuperuser
```

### Step 6: Start Development Server
```bash
python manage.py runserver
```
This will start the backend development server at http://127.0.0.1:8000/.

### Step 7: Install and Run the React Frontend
Navigate to the "frontend" directory:
```bash
cd frontend
```

Install the required frontend dependencies using npm:
```bash
npm install
```

Start the React development server:
```bash
npm start
```
This will start the frontend development server, and you should see output indicating that the server is running. Open your web browser and go to http://localhost:3000 to access the React Frontend.



Screenshots:
![Registration](https://github.com/ashkaaar/devzery-assignment/blob/main/registration.png)
![Profiles](https://github.com/ashkaaar/devzery-assignment/blob/main/profiles.png)
![actions](https://github.com/ashkaaar/devzery-assignment/blob/main/account_actions.png)


