import sys
sys.path.append('/../)
#path to location of twilio keys    


from twilio.rest import TwilioRestClient
from bs4 import BeautifulSoup as bs
import urllib.request
import urllib
import time
import twilio_keys as tk


client = TwilioRestClient(tk.account_sid, tk.auth_token)



class url_alert:

    def link_count(self, url):
        while True:
            try:
                page = urllib.request.urlopen(url)
                soup = bs(page, "lxml") 
                links=[]
                for link in soup.findAll('a'):
                    links.append(link.get('href'))
                print('found', len(links), 'links')
                time.sleep(60)
            except:
                print('...going to sleep')
                time.sleep(300)
            finally:
                return len(links)
    
    def phone(self):
        message = client.messages.create(to="+", from_="+",body=" ") 
        print('notified')


    def looper(self, url): 
        first_count = self.link_count(url)
        
        print('about to enter the while loop...')
        while True:
            if first_count < self.link_count(url):
                self.phone()
                break

alert = url_alert()
url = 'https://twitter.com/tweebot5/with_replies'
alert.looper(url)