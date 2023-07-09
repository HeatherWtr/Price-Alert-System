# Price Alert System
A python project to create an alert system that sends notifications when cryptocurrency prices reach predefined levels.

In this Price Alert System script, i have implemented the following features:

__1. Data Retrieval:__

 - The ```fetch_price_data``` method fetches real-time price data from the cryptocurrency API using the provided coin symbol and returns the current price.
   
__2. Alert Notification:__

 - The ```send_alert_notification``` method sends an alert notification using the configured email service. It creates an email message with the current price and sends it to the recipient email address specified in the email configuration.
   
