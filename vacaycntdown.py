from twilio.rest import Client
import json
import datetime

repo_path = '.'

with open(repo_path+'/cfg.json') as json_data_file:
    data = json.load(json_data_file)
    
numDict = data['numbersDict']
sid = data['twilioconfig']['sid']
auth_token = data['twilioconfig']['token']
from_ = data['twilioconfig']['number']

def countdownstr(nstr):
    # str of the format days, hours:minutes:seconds.microseconds
    daystr = nstr.split(',')[0]+','
    hourstr = nstr.split(',')[1].split(':')[0]+' hours, '
    minstr = nstr.split(',')[1].split(':')[1]+' minutes, and '
    secstr = nstr.split(',')[1].split(':')[2].split('.')[0]+' seconds'
    
    return 'Time until vacation is '+daystr+hourstr+minstr+secstr

def timedeltastr():
    vacay = datetime.datetime(2018,8,17,16,1)
    return str(vacay - datetime.datetime.now())
    
to_numbers = [data['numbersDict'][k] for k in data['numbersDict']]

client = Client(sid,auth_token)

timestr = countdownstr(timedeltastr())

for n in to_numbers:
    client.messages.create(to=n,
                       from_=from_,
                       body=timestr)
