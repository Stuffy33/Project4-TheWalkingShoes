i got this error when trying to deploy to heroku:
    "TypeError: a bytes-like object is required, not 'str'"
solution: i relised that i put the env.py file inside the "thewalkingshoes" folder

*REMOVE*
remove DISABLE_COLLECTSTATIC 1 from Heroku