from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd3a4f5be64825819d0fc74bfefa1367b"
auth_token  = "ce2f7eb628ac342e4af5af2c9141e123"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi, This is twilio send Message Test",
    to="+18094389815",    # Replace with your phone number
    from_="+18299463872") # Replace with your Twilio number
print message.sid
