import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables
load_dotenv()

def make_call(to_number: str) -> bool:
    """
    Make a phone call using Twilio API.
    The call will play Twilio's demo XML voice response by default.
    """
    try:
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_number = os.getenv("TWILIO_PHONE_NUMBER")

        if not all([account_sid, auth_token, from_number]):
            print("❌ Missing Twilio configuration in environment variables.")
            return False

        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        # Make the call (Twilio fetches instructions from URL)
        call = client.calls.create(
            url="http://demo.twilio.com/docs/voice.xml",  # TwiML URL
            to=to_number,
            from_=from_number
        )

        print(f"📞 Calling {to_number}...")
        print(f"✅ Call initiated! Call SID: {call.sid}")
        return True

    except Exception as e:
        print(f"❌ Error making call: {e}")
        return False


if __name__ == "__main__":
    # Get recipient number from user
    recipient = input("Enter phone number to call (with country code, e.g. +91XXXXXXXXXX): ")
    make_call(recipient)
