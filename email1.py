#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'myforum0007@gmail.com'
PASSWORD = 'M@mayank9404'

def get_contacts(Id):
    name=''
    email=''
    filename='contact.txt'
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            if Id==a_contact.split()[0]:
                name=a_contact.split()[1]
                email=a_contact.split()[2]
    return Id,name,email



def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def mailing(ID):
    Id,name,email=get_contacts(ID)
    if Id=='' or name=='' or email=='':
        print('Invalid Input')
    else:
        
        message_template = read_template('message.txt')

        # set up the SMTP server
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)

        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title(), ID=ID)

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="Attendance Updated"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

        # Terminate the SMTP session and close the connection
        s.quit()



# In[ ]:





# In[ ]:




