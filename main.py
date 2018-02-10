import requests
from config import *

def find_between(soup, first, last):
  try:
      start = soup.index( first ) + len( first )
      end = soup.index( last, start )
      return soup[start:end]
  except ValueError:
      return ''

def verify_check():
  with open(VERIFIED_ACCOUNTS, 'r') as myfile:
      emails = myfile.read().split('\n')
  if FROM_BNB == 'y':
      emails = [(s.split('\t'))[0] for s in emails]

  i = 0
  log = ''
  accounts = ''
  emails = [email for email in emails if email != '']
  print 'Checking {} accounts...'.format(str(len(emails)))
  for EMAIL in emails:
    session = requests.Session()
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }
    response = requests.get('http://api.nikepreorders.com/isverified/', headers=headers)
    token = find_between(response.content, "name='csrfmiddlewaretoken' value='", "'")
    headers = {
        'Origin': 'http://api.nikepreorders.com',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'http://api.nikepreorders.com/isverified/',
        'Connection': 'keep-alive',
    }
    cookies = {
        'csrftoken': '{}'.format(token),
    }
    data = [
      ('csrfmiddlewaretoken', '{}'.format(token)),
      ('account', '{}'.format(EMAIL)),
      ('password', '{}'.format(PASSWORD)),
    ]
    response = session.post('http://api.nikepreorders.com/isverified/', headers=headers, cookies=cookies, data=data)
    if response.status_code == 200:
      result = find_between(response.content, '{}: '.format(EMAIL), '\n')
      print '{}: {}'.format(EMAIL, result)
      log += '{}: {}\n'.format(EMAIL, result)
      if 'Not' in result:
        i += 1
      else:
        if BNB_FORMAT == 'y':
            accounts += '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(EMAIL, PASSWORD, SIZE, TWEET_KEYWORDS, COLLECTION_KEYWORDS, EARLY_LINKS, STYLE_CODE, NOTIFICATION_EMAIL, CARRIER, PHONE_NUMBER)
        else:
            accounts += '{}\t{}\n'.format(EMAIL, PASSWORD)
  print 'All accounts checked...you need {} replacements'.format(str(i))
  log += '\nAll accounts checked...you need {} replacements'.format(str(i))
  with open(LOG, 'w') as myfile:
    myfile.write(log)
  with open(WORKING_ACCOUNTS, 'w') as myfile:
    myfile.write(accounts)

def add_replacements():
    with open(WORKING_ACCOUNTS, 'r') as myfile:
        accounts = myfile.read()
    with open(REPLACEMENTS, 'r') as myfile:
        replacements = myfile.read().split('\n')
    for EMAIL in replacements:
        if BNB_FORMAT == 'y':
            accounts += '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(EMAIL, PASSWORD, SIZE, TWEET_KEYWORDS, COLLECTION_KEYWORDS, EARLY_LINKS, STYLE_CODE, NOTIFICATION_EMAIL, CARRIER, PHONE_NUMBER)
        else:
            accounts += '{}\t{}\n'.format(EMAIL, PASSWORD)
    with open(WORKING_ACCOUNTS, 'w') as myfile:
        myfile.write(accounts)
    print '{} replacements added to working accounts'.format(str(len(replacements)))

def decision():
  choice = raw_input('\nSelect an option by entering the corresponding number.\n\nCheck Verified Accounts (1) | Add Replacement Accounts (2)\nChoice: ')
  print ''
  if choice == '1':
    verify_check()
  elif choice == '2':
    add_replacements()
  else:
    'You did not choose a valid option, try again'
    decision()

while True:
    decision()
    raw_input('Task completed, hit enter to run again.')