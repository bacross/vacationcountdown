# vacationcountdown

This is a twilio enabled python script that sends a countdown to a vacation datetime to a list of text addresses.  The main requirement is a twilio id and auth_token - full explanation here: https://www.fullstackpython.com/blog/send-sms-text-messages-python.html

config file is a json of the general form:

{
    "twilioconfig":{
        "sid":"XXXXXXXXXXXXXXXXXXXXX",
        "token":"XXXXXXXXXXXXXXXXXXXXX"
		"number":"xxxxxxxxxx"
    },
	"numbersDict":{
		"name1":"xxxxxxxxxx",
		"name2":"xxxxxxxxxx"
	},
	"vacay_date":[yyyy,mm,dd,hh,mm]
}
