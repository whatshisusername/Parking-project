import os
from twilio.rest import Client


account_sid = "ACe00ba29c55f2b2f7270510f0130ee104"
auth_token = "862df713c0275f8766c111ec731f08e8"

client = Client(account_sid, auth_token)

client.messages.create(from_='+15044146681',
                      to='',
                      body='hi manav')