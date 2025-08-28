import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from twilio.rest import Client
import requests
import tweepy
import pywhatkit as kit

# Load environment variables
load_dotenv()

# ========== EMAIL ==========
def send_email(to_email, subject, body):
    try:
        sender_email = os.getenv("SENDER_EMAIL")
        password = os.getenv("EMAIL_PASSWORD")

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, to_email, message.as_string())
        server.quit()

        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")


# ========== SMS ==========
def send_sms(to_number, message_body):
    try:
        client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        message = client.messages.create(
            body=message_body,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=to_number
        )
        print(f"✅ SMS sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"❌ Failed to send SMS: {e}")


# ========== PHONE CALL ==========
def make_call(to_number):
    try:
        client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        call = client.calls.create(
            url="http://demo.twilio.com/docs/voice.xml",
            to=to_number,
            from_=os.getenv("TWILIO_PHONE_NUMBER")
        )
        print(f"📞 Calling {to_number}... Call SID: {call.sid}")
    except Exception as e:
        print(f"❌ Error making call: {e}")


# ========== WHATSAPP ==========
def send_whatsapp(to_number, message):
    try:
        # Send instantly (you need WhatsApp web logged in for pywhatkit)
        kit.sendwhatmsg_instantly(to_number, message, wait_time=10)
        print("✅ WhatsApp message sent!")
    except Exception as e:
        print(f"❌ Failed to send WhatsApp message: {e}")


# ========== TWITTER ==========
def post_twitter(message):
    try:
        auth = tweepy.OAuth1UserHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET"),
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_SECRET")
        )
        api = tweepy.API(auth)
        api.update_status(status=message)
        print("✅ Tweet posted successfully!")
    except Exception as e:
        print(f"❌ Error posting on Twitter: {e}")


# ========== FACEBOOK ==========
def post_facebook(message):
    try:
        access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")
        page_id = os.getenv("FACEBOOK_PAGE_ID")
        url = f"https://graph.facebook.com/{page_id}/feed"
        response = requests.post(url, data={"message": message, "access_token": access_token})
        if response.status_code == 200:
            print("✅ Facebook post created successfully!")
        else:
            print(f"❌ Failed: {response.text}")
    except Exception as e:
        print(f"❌ Error posting on Facebook: {e}")


# ========== INSTAGRAM ==========
def post_instagram(message):
    try:
        access_token = os.getenv("INSTAGRAM_ACCESS_TOKEN")
        ig_user_id = os.getenv("INSTAGRAM_USER_ID")

        url = f"https://graph.facebook.com/v17.0/{ig_user_id}/media"
        payload = {"caption": message, "access_token": access_token}
        response = requests.post(url, data=payload)

        if "id" in response.json():
            creation_id = response.json()["id"]

            # Publish media
            publish_url = f"https://graph.facebook.com/v17.0/{ig_user_id}/media_publish"
            publish_response = requests.post(publish_url, data={"creation_id": creation_id, "access_token": access_token})

            if publish_response.status_code == 200:
                print("✅ Instagram post published successfully!")
            else:
                print(f"❌ Failed to publish: {publish_response.text}")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Error posting on Instagram: {e}")


# ========== MENU ==========
def menu():
    while True:
        print("\n📌 MENU")
        print("1. Send Email")
        print("2. Send SMS")
        print("3. Make Phone Call")
        print("4. Send WhatsApp Message")
        print("5. Post on Twitter")
        print("6. Post on Facebook")
        print("7. Post on Instagram")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            to = input("Enter recipient email: ")
            subject = input("Enter subject: ")
            body = input("Enter message: ")
            send_email(to, subject, body)

        elif choice == "2":
            to = input("Enter recipient phone number (+91...): ")
            body = input("Enter SMS message: ")
            send_sms(to, body)

        elif choice == "3":
            to = input("Enter phone number to call (+91...): ")
            make_call(to)

        elif choice == "4":
            to = input("Enter WhatsApp number (+91...): ")
            body = input("Enter WhatsApp message: ")
            send_whatsapp(to, body)

        elif choice == "5":
            msg = input("Enter tweet content: ")
            post_twitter(msg)

        elif choice == "6":
            msg = input("Enter Facebook post content: ")
            post_facebook(msg)

        elif choice == "7":
            msg = input("Enter Instagram post content: ")
            post_instagram(msg)

        elif choice == "8":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    menu()
