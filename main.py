import requests
import time
import random
import string

webhook_url = "PUT_YOUR_WEBHOOK_URL_HERE"

start_time = time.time()

for i in range(50):
    print(f"Sending message {i+1}...")


    random_letters_1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    random_letters_2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))


    message = f"{random_letters_1}@everyone ≽^•⩊•^≼.dox{random_letters_2}"

    response = requests.post(webhook_url, json={'content': message})
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Error sending message: {response.status_code}")

    time.sleep(0.020) 

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to send 50 messages: {elapsed_time:.2f} seconds")
