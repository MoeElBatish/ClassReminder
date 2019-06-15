# ClassReminder
This is a class Reminder application that sends you texts every morning informing the user where and when his classes will be that day.
There are 2 ways to use this Application.
1. Keep it running on a server such that the user will get the text at the preferred time. ( you will need to edit TextReminder.py slightly for this to work)
2. Download Cron to use it to run the script every 24h.

Make sure that you have ClassReminder.py and TextReminder.py in the same folder. These are the only two python scrips that are needed to make this run.

You will need to subscribe to Twilio after your trial is over. However the trial lasts quite a bit.
If you have any suggestions please let me know.

Future plans will be to add the email functionality such that users can be notified via email every morning.

Libraries used:
    
    1.Twilio (third party) --> the only library you will need to install
    2.DateTime --> included with python
    3.Pickle --> included with python
Languages used:
    Python 3.7.1