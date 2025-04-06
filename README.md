🔐 Password Manager GUI 
![image](https://github.com/user-attachments/assets/bae49162-5a67-4c42-a07e-921eb39b9770)


A secure desktop application built with Python and Tkinter that generates, stores, and manages your passwords with encrypted JSON storage.

✨ Features
🛠️ Strong Password Generation: Creates 12-16 character passwords with mixed case letters, numbers, and symbols

💾 Encrypted Storage: Saves credentials in JSON format with clear structure

🔍 Quick Search: Retrieve passwords by website name

📋 Auto-Copy: Generated passwords are copied to clipboard automatically

🚦 Input Validation: Ensures no empty fields are submitted



🛠️ Installation

Prerequisites
  Python 3.6+
  pip package manager

Steps
1- Clone the repository:
git clone https://github.com/yourusername/password-manager.git
cd password-manager


2- Install required packages:
pip install -r requirements.txt

3- Run the application:
python password_manager.py


🖥️ Usage
Add New Entry:

  Enter website URL (e.g., github.com)

  Input email/username

  Click "Generate" to create a strong password

  Click "Add" to save

Retrieve Password:

  Enter website name

  Click "Search"

  Password will be displayed and copied automatically



📂 File Structure:
.
├── password_manager.py     # Main application
├── data.json              # Password storage (created after first save)
├── logo.png               # Application icon
└── requirements.txt       # Dependencies
