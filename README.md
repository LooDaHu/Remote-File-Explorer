# Welcome to Remote File Explorer!

Hi! This web application can help you access your personal computer at your mobile devices. And also, if this readme is not shown properly, you can download README.html for a better read experience.


# How It Works
```mermaid
graph LR
A[Mobile devices, Client] --> B((Internet or LAN))
B --> D{This web application, Server}
D --> B
B --> A
```
# How To Set Up
## 1. System Requirement
1. ANY version of Windows10
2. Python3.6 or higher
## 2. Install
1. Open CMD.
2. Run command 
> python install.py
3. Now, Installation has done.
Note: Please Don't run install.py script at IDE environment, it may casue incorrect python path setting.
![cmd_shell](./static/Photos/cmd_shell.gif)
## 3. Start Up
1. Just double click start_up.bat, then enjoy.
![cmd_shell_start_up](./static/Photos/cmd_shell_start_up.gif)
 
 # How To Use It
 1. Open up your browser.
 
 2. Let's recall what is the IP address and port of our running application. Yes, you can see it is http://192.168.64.1:8000 in this case. And let's go for it. 
 
 3. Now, we can see the login page, let's login with our username and password. Don't forget you can do settting of your username and password at config.py
![login_page](./static/Photos/login_page.gif)
 
 4. Then we can see, the home page. You can upload files in your mobile devices and go through files of your PC at remote side.
 ![home_page](./static/Photos/home_page.gif)
 ![root_page](./static/Photos/root_page.gif)
 ![sub_page](./static/Photos/sub_screen_LI.jpg)
 
 5. Let's have a look on some different pages for different types of files.
	### 1. PDF file
	![pdf_file](./static/Photos/pdf_screen_LI.jpg)

	### 2. Picture file
	![pic_file](./static/Photos/pic_screen.jpg)

	### 3. Music file
	![music_file](./static/Photos/music_screen.jpg)

	### 4. Video file
	![video_file](./static/Photos/video_screen.jpg)

	### 5. Other file
	When you try to open other types of files, it will start downloading automatically.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU4MTU4MzQ0MCwtNTU2MTAwNzc4XX0=
-->