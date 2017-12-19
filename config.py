VERIFIED_ACCOUNTS = 'Verified Accounts.txt' #Text file where accounts are located
FROM_BNB = 'y' #Specifies whether or not VERIFIED_ACCOUNTS is an exported text file from BNB...change y to n and VERIFIED_ACCOUNTS will be treated as the format of the text file received from Nikepreorders
PASSWORD = '' #Password for accounts
LOG = 'log.txt' #Text file where you'd like results to be stored
WORKING_ACCOUNTS = 'workingaccounts.txt' #Text file where you'd like working accounts to be stored
BNB_FORMAT = 'y' #By default WORKING_ACCOUNTS is formatted to suport BNB Nike import...if you don't need that change y to n and WORKING_ACCOUNTS will just have emails and passwords
#All of the following have to do with BNB therefore they should be self explanatory
SIZE = 'RANDOM'
TWEET_KEYWORDS = '' #Separate multiple values with a comma
COLLECTION_KEYWORDS = '' #Separate multiple values with a comma
EARLY_LINKS = '' #Separate multiple values with a comma...begin link with http://
STYLE_CODE = ''
NOTIFICATION_EMAIL = '' #Defaults to account email
CARRIER = ''
PHONE_NUMBER = '' #No spaces