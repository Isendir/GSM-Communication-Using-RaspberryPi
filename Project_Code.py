#!/usr/bin/env python
import serial,time,MySQLdb   # Importing required modules
db = MySQLdb.connect("127.0.0.1","root","iiitn","NoticesDB" ) # Connecting to MySQL Database
cursor = db.cursor() # Initializing connection stream
port = serial.Serial(baudrate=115200, port='/dev/ttyUSB0', timeout=5) # Serial port initialization
#port.open()
allow=["+919966228935","+919705896317"] # Add allowed Numbers here
phBook = {"+919966228935":"Manager","+919705896317":"Deputy Manager"}
port.write('AT+CMGF=1\r\n')      #set text mode
port.write('AT+CSCS="UCS2"\r\n') #set encoding to UCS2
port.write('AT+CMGL="REC UNREAD"\r\n')  #to get all messages
def messages(str):
    '''Decryting Hexadecimal Code into Unicode String'''
    ustr = u''
    str = str.strip().replace('"', '')
    for i in range(len(str)):
        if not i % 4:
            ustr += unichr(int(str[i:i+4], 16))
    return ustr
gotmsg = False
while 1: # For Infinite execution
	line = port.readline() # Reading Serialport response line by line
	if(line.startswith("+CMTI:")): # Condition for new incoming message
		num=int(line.split(",")[1]) # Getting message ID
		port.write('AT+CMGR='+str(num)+'\r\n') # AT Command to read Message by it's ID
		c=0
		while(1):#Infinte loop to get message line by line
			mes=port.readline()#Readin new message
			n=mes.split("\n")
			c=c+1
			if(c==2):
				num=messages(n[0].split(",")[1])#This is to get sender number
				if num not in allow:#Condition for checking sender is in given allow list or not
					break # Quit When we found some another number not in our list sending messages.
				print num
			if(c==3):
				mes=messages(n[0][0:-1]) # Extracting&Decrypting Hex message into unicode message
				Time=time.strftime("%d %b %Y %r",time.gmtime()) # To get localtime in specified format
				sql = """INSERT INTO Updates(HEAD,BODY,CREATEDAT)
         VALUES ('"""+mes+"""', '"""+mes+"""','"""+Time+"""')""" # SQL Query to insert new message into Web Portal Database.
				cursor.execute(sql) # Executing SQL Query
				db.commit() # Commiting changes to Database
				print phBook[num]+": "+mes # Printing Message & Sender Details
				print Time # Printing time
				break # Quitting when we are finished with our job
		port.write('AT+CMGD='+str(num)+'\r\n') # Deleting message to make space.
