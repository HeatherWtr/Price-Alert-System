import requests
import smtplib
from email.message import EmailMessage

class PriceAlertSystem:
    def __init__(self, api_url, coin_symbol, email_config):
        self.api_url = api_url
        self.coin_symbol = coin_symbol
        self.email_config = email_config

    def fetch_price_data(self):
        # Fetch real-time price data from the cryptocurrency API:
        url = f"{self.api_url}/price/{self.coin_symbol}"
        response = requests.get(url)
        if response.status_code == 200:
            price_data = response.json()
            current_price = price_data['price']
            return current_price
        else:
            print("Error fetching price data from the API.")
            return None

    def send_alert_notification(self, current_price, threshold):
        # Send alert notification using the configured email service
        msg = EmailMessage()
        msg.set_content(f"Price alert for {self.coin_symbol}! Current price: {current_price}")

        msg['Subject'] = f"Price Alert - {self.coin_symbol}"
        msg['From'] = self.email_config['sender_email']
        msg['To'] = self.email_config['recipient_email']

        try:
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as smtp:
                smtp.starttls()
                smtp.login(self.email_config['sender_email'], self.email_config['sender_password'])
                smtp.send_message(msg)
                print("Alert notification sent successfully!")
        except Exception as e:
            print("Error sending alert notification:", str(e))

# Example usage:

# Define API URL, coin symbol, and email configuration
api_url = "https://api.example.com"
coin_symbol = "BTC/USD"

email_config = {
    'smtp_server': 'smtp.example.com',
    'smtp_port': 587,
    'sender_email': 'sender@example.com',
    'sender_password': 'sender_password',
    'recipient_email': 'recipient@example.com'
}

# Create an instance of PriceAlertSystem
alert_system = PriceAlertSystem(api_url, coin_symbol, email_config)

# Fetch current price data
current_price = alert_system.fetch_price_data()
if current_price is not None:
    # Define price thresholds for alert notifications
    upper_threshold = 50000
    lower_threshold = 40000

    # Check if current price crosses the thresholds
    if current_price > upper_threshold:
        alert_system.send_alert_notification(current_price, upper_threshold)
    elif current_price < lower_threshold:
        alert_system.send_alert_notification(current_price, lower_threshold)
    else:
        print("Price is within the desired range.")
