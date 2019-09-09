# Welcome to Remote File Explorer!

Hi! This web application can help you access your personal computer at your mobile devices. 


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
![enter image description here](https://lh3.googleusercontent.com/Nwe7LqLFazBxMxu0ckEi6B0KiASMPYiPXtaTgEZ9TqtTcCHKmjSFM39Cv-8x22ErSX6wKG9kYE8)
## 3. Start Up
1. Just double click start_up.bat, then enjoy.
![enter image description here](https://lh3.googleusercontent.com/VM3gdovtOVPogro8cPGqaqftVdtloAyqIni66KxLx4TbJEwzwB02ea_mtvqE-HG79PKDlr6QPw4)
 
 # How To Use It
 1. Open up your browser.
 
 2. Let's recall what is the IP address and port of our running application. Yes, you can see it is http://192.168.64.1:8000 in this case. And let's go for it. 
 
 3. Now, we can see the login page, let's login with our username and password. Don't forget you can do settting of your username and password at config.py
![enter image description here](https://lh3.googleusercontent.com/w3RfwVpqoBTGA9clmoftyQqem4i0D1L-SJ9GrRwQbtb__Z6fUSIflH-ssZkOyup-E85qtiPPZ-Y)
 
 4. Then we can see, the home page. You can upload files in your mobile devices and go through files of your PC at remote side.
 ![enter image description here](https://lh3.googleusercontent.com/u12z0bQctTeHgBElH5I8k3B9cBdDXlgjizzBBFjJ8zNpNatKPRYQlQH4styITVXUmev9rL9EFH_U)
 ![enter image description here](https://lh3.googleusercontent.com/1v4t9nornw18qImbLvXG9zlMER3gpP0WiPiDVQF7MoH99PagYIZDLV0uQ9IlERkOODjZMi5Q6GsU)
 ![enter image description here](https://lh3.googleusercontent.com/jRqj5eXxOg1A7dwdIgicgJvsARW4ay26C1EN5BxY9Y69ECDvIaitCuehgl3dUCczlGg3Fljk-qrg)
 
 5. Let's have a look on some different pages for different types of files.
	### 1. PDF file
	![enter image description here](https://lh3.googleusercontent.com/0rk4osu7L76_1o5tR9pp5-Rp_vN9fZuB-6kdZLGsIxfBzwH5dfYFR1BtMkndFEFYSBwof13XFN25)

	### 2. Picture file
	![enter image description here](https://lh3.googleusercontent.com/mMp7RkNIs5AjUo2uhQxLW-P8LkbXG3fKu9bc3jpJyT3YZek8TruYcY1A_xJQIOT0AElqo9u8fyMb)

	### 3. Music file
	![enter image description here](https://lh3.googleusercontent.com/I3xCtX8dV1fQTqa462buVRnOJNpaufIl22HKcllS1zZwZ0X-0jhSqBLcrf9z4UwM-scD_MuXeY5M)

	### 4. Video file
	![enter image description here](https://lh3.googleusercontent.com/slhBgoX9uzVt5UnQghs_c01gS6i2SLKsyh78yCkJ6eRH4wnrBrKQ8_ardn59H-RTICw2BFPf3UTj)

	### 5. Other file
	When you try to open other types of files, it will start downloading automatically.

## Create files and folders

The file explorer is accessible using the button in left corner of the navigation bar. You can create a new file by clicking the **New file** button in the file explorer. You can also create folders by clicking the **New folder** button.

## Switch to another file

All your files and folders are presented as a tree in the file explorer. You can switch from one to another by clicking a file in the tree.

## Rename a file

You can rename the current file by clicking the file name in the navigation bar or by clicking the **Rename** button in the file explorer.

## Delete a file

You can delete the current file by clicking the **Remove** button in the file explorer. The file will be moved into the **Trash** folder and automatically deleted after 7 days of inactivity.

## Export a file

You can export the current file by clicking **Export to disk** in the menu. You can choose to export the file as plain Markdown, as HTML using a Handlebars template or as a PDF.


# Synchronization

Synchronization is one of the biggest features of StackEdit. It enables you to synchronize any file in your workspace with other files stored in your **Google Drive**, your **Dropbox** and your **GitHub** accounts. This allows you to keep writing on other devices, collaborate with people you share the file with, integrate easily into your workflow... The synchronization mechanism takes place every minute in the background, downloading, merging, and uploading file modifications.

There are two types of synchronization and they can complement each other:

- The workspace synchronization will sync all your files, folders and settings automatically. This will allow you to fetch your workspace on any other device.
	> To start syncing your workspace, just sign in with Google in the menu.

- The file synchronization will keep one file of the workspace synced with one or multiple files in **Google Drive**, **Dropbox** or **GitHub**.
	> Before starting to sync files, you must link an account in the **Synchronize** sub-menu.

## Open a file

You can open a file from **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Open from**. Once opened in the workspace, any modification in the file will be automatically synced.

## Save a file

You can save any file of the workspace to **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Save on**. Even if a file in the workspace is already synced, you can save it to another location. StackEdit can sync one file with multiple locations and accounts.

## Synchronize a file

Once your file is linked to a synchronized location, StackEdit will periodically synchronize it by downloading/uploading any modification. A merge will be performed if necessary and conflicts will be resolved.

If you just have modified your file and you want to force syncing, click the **Synchronize now** button in the navigation bar.

> **Note:** The **Synchronize now** button is disabled if you have no file to synchronize.

## Manage file synchronization

Since one file can be synced with multiple locations, you can list and manage synchronized locations by clicking **File synchronization** in the **Synchronize** sub-menu. This allows you to list and remove synchronized locations that are linked to your file.


# Publication

Publishing in StackEdit makes it simple for you to publish online your files. Once you're happy with a file, you can publish it to different hosting platforms like **Blogger**, **Dropbox**, **Gist**, **GitHub**, **Google Drive**, **WordPress** and **Zendesk**. With [Handlebars templates](http://handlebarsjs.com/), you have full control over what you export.

> Before starting to publish, you must link an account in the **Publish** sub-menu.

## Publish a File

You can publish your file by opening the **Publish** sub-menu and by clicking **Publish to**. For some locations, you can choose between the following formats:

- Markdown: publish the Markdown text on a website that can interpret it (**GitHub** for instance),
- HTML: publish the file converted to HTML via a Handlebars template (on a blog for example).

## Update a publication

After publishing, StackEdit keeps your file linked to that publication which makes it easy for you to re-publish it. Once you have modified your file and you want to update your publication, click on the **Publish now** button in the navigation bar.

> **Note:** The **Publish now** button is disabled if your file has not been published yet.

## Manage file publication

Since one file can be published to multiple locations, you can list and manage publish locations by clicking **File publication** in the **Publish** sub-menu. This allows you to list and remove publication locations that are linked to your file.


# Markdown extensions

StackEdit extends the standard Markdown syntax by adding extra **Markdown extensions**, providing you with some nice features.

> **ProTip:** You can disable any **Markdown extension** in the **File properties** dialog.


## SmartyPants

SmartyPants converts ASCII punctuation characters into "smart" typographic punctuation HTML entities. For example:

|                |ASCII                          |HTML                         |
|----------------|-------------------------------|-----------------------------|
|Single backticks|`'Isn't this fun?'`            |'Isn't this fun?'            |
|Quotes          |`"Isn't this fun?"`            |"Isn't this fun?"            |
|Dashes          |`-- is en-dash, --- is em-dash`|-- is en-dash, --- is em-dash|


## KaTeX

You can render LaTeX mathematical expressions using [KaTeX](https://khan.github.io/KaTeX/):

The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

> You can find more information about **LaTeX** mathematical expressions [here](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference).


## UML diagrams

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

```mermaid
sequenceDiagram
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

Bob-->Alice: Checking with John...
Alice->John: Yes... John, how are you?
```

And this will produce a flow chart:

```mermaid
graph LR
A[Square Rect] -- Link text --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNzk3NzkyODYsMTM5OTg0NTAxNSwtMz
M5NDE5OTY2LC05MzA0NDI0NzFdfQ==
-->