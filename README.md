# Simple-Webhook-spammer                         24/9/11/
-------------------------------------------------------------
Created by kyc :3 <33              

 
Change "PUT_YOUR_WEBHOOK_URL_HERE" To your webhook url.
Then adjust your message:

Find the following line :

message = f"{random_letters_1}@everyone ≽^•⩊•^≼.dox{random_letters_2}"

Then change "@everyone ≽^•⩊•^≼.dox" to your own message example:

@everyone lol


This is how it should look like:

message = f"{random_letters_1}@everyone lol{random_letters_2}"

Then adjust the delay:

time.sleep(0.020) 

Change 0.020 To whatever delay you want, I recommend using 0.1 to avoid rate limits.
