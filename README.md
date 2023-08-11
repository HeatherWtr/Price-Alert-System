# Price Alert System

A python project to create an alert system that sends notifications when cryptocurrency prices reach predefined levels.

In this Price Alert System script, i have implemented the following features:

__1. Data Retrieval:__

 - The ```fetch_price_data``` method fetches real-time price data from the cryptocurrency API using the provided coin symbol and returns the current price.
   
__2. Alert Notification:__

 - The ```send_alert_notification``` method sends an alert notification using the configured email service. It creates an email message with the current price and sends it to the recipient email address specified in the email configuration.
   
__Usage:__

 -  The following libraries are required to be installed before running the code.
   ```bash
   pip install requests
   ```

 The following library is not mandatory. It should be installed depending on your needs.
    
   ```bash
   pip install smtplib
   ```
 - To use this code, replace the ```api_url``` variable with the actual API endpoint to fetch real-time price data for your desired cryptocurrency and trading pair. Additionally, customize the email configuration dictionary in the ```email_config``` variable to match your SMTP server and email credentials.
   
