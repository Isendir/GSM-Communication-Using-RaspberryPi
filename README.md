
**# **GSM COMMUNICATION (SIM900) USING RASPBERRY PI:****

First of all the main idea of this project is to receive a message (By using GSM) sent by a typical cell phone and display it on a monitor of any sort with the use of web browser , which serves as an electronic notice board.
Here we use Python programming language to read the incoming messages and display them on notice boards. As Raspberry Pi uses Linux based operating systems, we can happily program with python language.
After running the python program in terminal of the Raspberry Pi processor, The console starts waiting for the incoming messages. As soon as the message is received, It is decoded and mobile number of the sender and message will be displayed and again waits for the next message. We can use a database query language to insert these messages in a web site or blog and display using large screens which serves as Notice Board.

**Components Needed for Project:**
1. Raspberry pi
2. SIM900
3. Serial lo USB connection
4. Monitor
5. Internet Connection

**# Step 1: Raspberry Pi Setup...** 
 
The first step in Project is Booting up and configuring Raspberry Pi .

For this you have to download the Raspian OS from http://www.raspberrypi.org
And you have to unzip the OS image to file SD card using win32DiskImager software.

Below are the steps to Setup the Raspberry pi..

1. Download the distribution(Raspian OS) from the raspberrypi.org downloads page or from a mirror or torrent. Make sure the distribution is for the Raspberry Pi, as others will not work. Usually these are zipped (compressed) files ending in .zip or .gz (something like "distribution-name.zip"). Extract the image file from the downloaded .zip file, so you now have "distribution-name.img".
2. Insert the SD card into your SD card reader and check what drive letter it was assigned. You can easily see the drive letter (for example G:) by looking in the left column of Windows Explorer. You can use the SD Card slot (if you have one) or a cheap Adapter in a USB slot.
3. Download the Win32DiskImager utility (it is also a zip file). You can run this from a USB drive. Extract the executable from the zip file and run the Win32DiskImager utility; you may need to run the utility as Administrator! Right-click on the file, and select 'Run as Administrator' Select the image file you extracted above. 
4. Select the drive letter of the SD card in the device box. Be careful to select the correct drive; if you get the wrong one you can destroy your data on the computer's hard disk! If you are using an SD Card slot in your computer (if you have one) and can't see the drive in the Win32DiskImager window, try using a cheap Adapter in a USB slot. 
5. Click Write and wait for the write to complete. Exit the imager and eject the SD card. 
You are now ready to plug the card into your Raspberry Pi. 


**Booting your Raspberry Pi for the first time**

1. On first boot you will come to the Raspi-config window 
2. Change settings such as timezone and locale if you want 
3. Finally, select the second choice: expand_rootfs and say ‘yes’ to a reboot 
4. The Raspberry Pi will reboot and you will see raspberrypi login: 
5. Type: pi 
6. You will be asked for your Password Type: raspberry 
7. You will then see the prompt: pi@raspberry ~ $ 
8. Start the desktop by typing: startx

**# Step 2: Connecting GSM Module to Raspberry pi...**
 
In second step we have to connect the above SIM900 module to Raspberry Pi . We can directly use a HDMI to USB cable in which HDMI port is at SIM900 and the other end is connectd to female USB port of Raspberry Pi.




**# Step 3: Coding Part of the Project:**

  
After Connecting the SIM900 module to Raspberry pi. Open IDLE in Raspberry Pi and write the above code (I am explained each step of code in the images so refer image). And the save file as filename.py.






**# Step 4: Installing Apache and Mysql and Connecting Python to Mysql using MySqlDB Module:**

 
1. Before running the code we have to install some packages because because we are using apache and mysql in python language.
2. For downloading apache and mysql please refer this link http://www.instructables.com/id/Raspberry-Pi-Web-Server/step7/Install-Apache-with-PHP/
3. Next We have to download the MySqlDb for Connecting python to webbrowser. 
You can download it from https://pypi.python.org/pypi/MySQL-python/1.2.5
After downloading the zip extract the zip file and open the root terminal . Go to the extracted folder directory using cd command in terminal and install the mysqldb module using commands below.
Python setup.py build 
python setup.pyinstall
4 .Now you installed the necessary Packages for Project so go to the next step.



**# Step 5: Finally the Running the Program and Results Page: **

 
 
Finally We came to ending Stage of Project i.e. Running the Program and Results of the program.

1. We have to run the python program by using python filename.py command in terminal.
2. When ever we sent a message to gsm module, The Gsm module receives the message and checks wheather the sender is in allowed list or not if sender is in allowed list then it displays the message in terminal and it insert the message in webportal.



**Thank you .. For your Interest on project....**

**# Quries/Suggestions...**

1. If you have any quries or suggestions on this project send me reply or contact me through my mail id: vamsi.patchava@gmail.com. 
