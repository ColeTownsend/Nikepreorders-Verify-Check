from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from config import *

with open(VERIFIED_ACCOUNTS, 'r') as myfile:
    emails = myfile.read().split('\n')
if FROM_BNB == 'y':
    emails = [(s.split('\t'))[0] for s in emails]

i = 0
log = ''
accounts = ''

for EMAIL in emails:
    Driver = webdriver.Chrome(CHROMEDRIVER)
    Driver.get('http://api.nikepreorders.com/isverified/')

    account = Driver.find_element_by_css_selector('input#id_account')
    password = Driver.find_element_by_css_selector('input#id_password')

    account.send_keys(EMAIL)
    password.send_keys(PASSWORD)
    password.send_keys(Keys.RETURN)

    if 'Not Verified' in Driver.page_source:
        print '{} is NOT verified'.format(EMAIL)
        log += '{} is NOT verified\n'.format(EMAIL)
        i += 1
    else:
        print '{} is verified'.format(EMAIL)
        log += '{} is verified\n'.format(EMAIL)
        if BNB_FORMAT == 'y':
            accounts += '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(EMAIL, PASSWORD, SIZE, TWEET_KEYWORDS, COLLECTION_KEYWORDS, EARLY_LINKS, STYLE_CODE, NOTIFICATION_EMAIL, CARRIER, PHONE_NUMBER)
        else:
            accounts += '{}\t{}\n'.format(EMAIL, PASSWORD)
    Driver.close()

print 'All accounts checked...you need {} replacements'.format(str(i))
log += '\nAll accounts checked...you need {} replacements'.format(str(i))

with open(LOG, 'w') as myfile:
    myfile.write(log)
with open(WORKING_ACCOUNTS, 'w') as myfile:
    myfile.write(accounts)