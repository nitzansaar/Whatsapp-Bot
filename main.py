from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for user to scan QR code
input("Press Enter after scanning the QR code")

# Search and open the chat
chat_name = "PCD"  # Replace with the name of the chat
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][1]')
search_box.click()
search_box.send_keys(chat_name)
search_box.send_keys(Keys.RETURN)

# Initialize the previous message count
previous_message_count = 0

# Function to print new messages
def print_new_messages():
    global previous_message_count

    # Find all message elements
    messages = driver.find_elements(By.XPATH, '//div[contains(@class,"message-in") or contains(@class,"message-out")]//div[@class="copyable-text"]')

    # Get the current message count
    current_message_count = len(messages)

    # If the current message count is greater than the previous count, print the new messages
    if current_message_count > previous_message_count:
        new_messages = messages[previous_message_count:current_message_count]
        for message in new_messages:
            message_text = message.text
            print(f"New Message: {message_text}")
        
        # Update the previous message count
        previous_message_count = current_message_count

# Continuously check for new messages and print them
while True:
    print_new_messages()
    time.sleep(5)  # Check every 5 seconds
