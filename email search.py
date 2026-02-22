from re import findall

email_logs="""recieved from musabbas989@gmail.com.
            hello musasahh090@net.com
            musa smma755@yaho.net"""
#using regular expression command to find emails
pattern=r"ts\w+\d"
emailpattern=r"\w+@\w+\.\w+"
print(findall(emailpattern,email_logs))

print(findall(pattern, "tsnow0, tshah6, bmoreno8"))

