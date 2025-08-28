# 📌 Python Multi-Task Automation Project

This project is a **menu-driven Python automation program** that integrates multiple functionalities such as:  
- Sending Emails  
- Sending SMS (via Twilio)  
- Making Phone Calls (via Twilio)  
- Posting Messages on LinkedIn  
- Posting Tweets on Twitter  
- Posting on Facebook  
- Posting on Instagram  
- Sending WhatsApp Messages  

It helps you automate social media posting, communication, and notifications — all from one place! 🚀  

---

## 📂 Project Structure

multi_task_automation/
│── main.py # Main menu-driven Python script
│── .env # Environment variables file


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/multi-task-automation.git
cd multi-task-automation
```
### 2️⃣ Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

### 3️⃣ Install Required Dependencies
```
pip install -r requirements.txt
```
🔑 API Setup & Configuration
📧 Gmail (for Sending Emails)

Enable 2FA for your Gmail account.

Generate an App Password from Google Account Security
.

Add credentials in .env file:
SENDER_EMAIL=your-email@gmail.com
EMAIL_PASSWORD=your-app-password


📱 Twilio (for SMS, Calls, WhatsApp)

Create an account at Twilio
.

Get your Account SID, Auth Token, and Twilio Number.

Add them to .env file:
TWILIO_ACCOUNT_SID=your-account-sid
TWILIO_AUTH_TOKEN=your-auth-token
TWILIO_PHONE_NUMBER=your-twilio-number

💼 LinkedIn API (for Posting)

Create an app at LinkedIn Developers
.

Get your Access Token.

Add to .env file:
LINKEDIN_ACCESS_TOKEN=your-linkedin-access-token

🐦 Twitter API (for Tweeting)

Apply for a developer account at Twitter Developer Portal
.

Get your API Key, API Secret, Access Token, Access Token Secret.

Add to .env file:
TWITTER_API_KEY=your-api-key
TWITTER_API_SECRET=your-api-secret
TWITTER_ACCESS_TOKEN=your-access-token
TWITTER_ACCESS_SECRET=your-access-secret


📘 Facebook Graph API (for Posting)

Go to Meta for Developers
.

Create an app and get a Page Access Token.

Add to .env file:
FACEBOOK_PAGE_ACCESS_TOKEN=your-facebook-page-token
FACEBOOK_PAGE_ID=your-page-id


📸 Instagram Graph API (for Posting)

Create a Facebook app linked with Instagram.

Get Instagram User ID and Access Token from Meta Graph API Explorer
.

Add to .env file:
INSTAGRAM_ACCESS_TOKEN=your-instagram-token
INSTAGRAM_USER_ID=your-user-id

▶️ How to Run the Project

Run the main program:
python main.py
You’ll see a menu like this:

========= Python Automation Menu =========
1. Send Email
2. Send SMS
3. Make Phone Call
4. Post on LinkedIn
5. Post on Twitter
6. Post on Facebook
7. Post on Instagram
8. Send WhatsApp Message
9. Exit
=========================================


Choose any option by entering its number.




👨‍💻 Author

Ritik Kumar Sahu
Cybersecurity & DevOps Enthusiast | Python Automation
