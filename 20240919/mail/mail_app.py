import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'bhavana9678@gmail.com'
email_passwd = 'oqtc afjh sgop eglz'
connection.login(email_addr, email_passwd)
subject = "Testing"
body = "Hi! this is a test message to test smtp."
message = f'Subject: {subject}\n\n{body}'
connection.sendmail(from_addr=email_addr, to_addrs='gmaheswaranmca@gmail.com',msg=message)
connection.close()


#qwer asdf zxcv
#pwd:oqtc afjh sgop eglz