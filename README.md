# Shortly - Flask URL Shortener Web App

Shortly is a simple and efficient Flask URL shortener web application that allows you to shorten long URLs into more manageable and shareable links. With Shortly, you can easily generate short URLs that redirect to the original long URLs, making it convenient to share links in messages, emails, and social media platforms.

## Features

- **URL Shortening**: Convert long URLs into short, easy-to-share links.
- **Custom Short URLs**: Optionally customize the generated short URLs.
- **Link Expiration**: Set an expiration date for short URLs, making them valid only for a limited time.
- **Analytics Dashboard**: Track the number of clicks and other statistics for each short URL.
- **RESTful API**: Integrate Shortly's functionality into your own applications with the API endpoints.
- **User Authentication**: Register and log in to manage your shortened URLs.
- **Admin Panel**: Admin dashboard to monitor and manage the system.

## Demo

Check out the live demo of Shortly [here](https://shortly-url-9hbz.onrender.com/).

## Installation

Follow these steps to set up Shortly on your local machine:

1. Clone the repository:

```bash
git clone https://github.com/your-username/shortly.git
```
2. Navigate to the project directory:
```bash
cd shortly
```
3. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
```
4. Activate the virtual environment:
- Windows (Command Prompt):
```bash
venv\Scripts\activate
```
- Linux/macOS (Bash):
```bash
source venv/bin/activate
```
5. Install the required dependencies:
```bash
pip install -r requirements.txt
```
6. Set up the database:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
7. Configure the environment variables:
Create a .env file in the root directory and provide the necessary configuration values:
```bash
FLASK_APP=run.py
FLASK_ENV=development
# Add other configuration variables here
```
8. Start the development server:
```bash
flask run
```
Visit http://localhost:5000 in your web browser to access Shortly.

## Usage
- Register and log in to Shortly using your credentials.
- On the dashboard, paste the long URL you want to shorten.
- Optionally, customize the short URL or set an expiration date.
- Click the "Shorten" button to generate the short URL.
- You can view and manage your shortened URLs in the dashboard.
- Use the short URL to redirect to the original long URL.
