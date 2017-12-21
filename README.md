#Willybot900

This is my attempt at learning Python while building a quotes bot for Scarizard's Discord server.
Most likely not useful to anyone outside of the ScarizardPlays community, but you be the judge.

## Notes

A random smattering of information I'm braindumping.

### Quote text file
I read `quotes.txt` (in the working directory) into a list object so I can address it using `array[index]` notation.
This is probably the wrong way to do it, but it's fairly fast at the current number of quotes.

```python
with open("quotes.txt", "r", encoding="utf-8") as quotes:
    for line in quotes:
        quote_list.append(line)
```

This `with` keyword automatically closes the file when it reaches the end of the block. `"r"` specifies read-only. `encoding="utf-8"` is important
because for whatever reason `'` (apostrophes) don't output correctly otherwise.  When adding to the file, I use another `with` statement, but instead
specify `"a"` for append.

### Asynchronous functions

The `global` keyword is used to specify that a variable is being referenced globally rather than in function scope.

In order to properly debounce command usage, I implemented a semaphore called `quotes_on_cooldown`.  If `False`, the command can
execute.  At the beginning of execution, it is set to `True` to block other async calls.  After the command does its thing, the function sleeps
for a cooldown length defined by `quote_cooldown_length` (in seconds), after which the semaphore is released.  Effectively, this prevents any user
from calling the `!quote` command until the cooldown period is over.  Alternatively, I could implement a queue feature to prevent spam, but that doesn't
seem useful.

## discord.py Documentation

[Latest documentation](https://discordpy.readthedocs.io/en/latest/)
 (including everything below)

[Client API](https://discordpy.readthedocs.io/en/latest/api.html#client)

### Objects
[Message](https://discordpy.readthedocs.io/en/latest/api.html#message)

Useful properties:
* author `Member` (who sent the message)
    - Used to get the **top_role** of the sender to authorize them for a command
* content `str` (contents of the message)
    - Used to parse the message to find the command and parameter
* channel `Channel` (channel the message was sent to)
    - Used to reply to the command in the same channel the command was sent from

[Server](https://discordpy.readthedocs.io/en/latest/api.html#server)

Useful properties:
* roles `Role` list (All the roles available on the server)
    - Used to find the role objects on a server for later comparison during command authorization

[Member](https://discordpy.readthedocs.io/en/latest/api.html#member)

Useful properties:
* top_role `Role` (highest level role a member has on a particular server)
    - Used during authorization to authorize a sender for a command
    - When comparing roles, be sure to compare between roles on the same server or an exception will be raised

## Built with
* Python
* Visual Studio
* [discord.py](https://github.com/Rapptz/discord.py)

## Authors
* **William Buddenberg** - *Python code*
* Patrick **Scarizard** Scarborough and his Twitch community - *quotes.txt* - [ScarizardPlays on Twitch dot television](https://www.twitch.tv/scarizardplays)

## Acknowledgments
* Viewers like you
