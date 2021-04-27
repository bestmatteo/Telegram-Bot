<h1>Telegram-Bot</h1>

### An Selenium-way to forward messages automatically 

## Get started 

1. Install the requirements

```
pip install -r requirements.txt
```

2. Setup your new account

```
python setup.py
```
Enter any key beside 0, chrome will open up and after that you must enter your telegram account.
After 30 seconds or more, you will be able to continue the process after entering your telegram account by pressing any key.

3. Setup groups/channels and PMs
Enter any key beside 0 and type:
```
0 to exit
1 to setup group 1
2 to setup group 2
3...
4...
5 to setup group 5
9 to setup ALL the five groups
```
Enter the url of your group/channels or PM one by one (With https://)

Chrome will open up and setup the group.

4. Find your chrome's profile path
Open webscraping.py with a text editor, go to line 92 and edit the path to your user's path.
Example: 
```C:\\Users\\gusta\\AppData\\Local\\Google\\Chrome\\User Data\\Default```

## Setup the group that will receive the messages

Open Telegram via cellphone app and Pin the group at the top of your conversation history (Must the the first one pinned). 

## Start Forwarding 
Enter: 

```python webscraping.py``` 

Now the bot will keep tracking your new messages.

<h1>The end</h1>
