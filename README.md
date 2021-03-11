# SURF Information Discord Bot

Discord Bot that shows the information of an address in the surf ecosystem, that is set by the user.

## Commands

!myaddy <ethereum address> -  Set your ethereum address to your user, stored in the user.json file created when the bot is started.
if the ethereum address is invalid it doesn't set it.
  
!info - Shows the info of the ethereum address, shows whirlpool stats, leviathan stats, and board holder stats, they only show up if ethereum address is holding one of these, if they don't they don't show up


## Setup

1. Install the requirements (Discord.PY, web3, cryptoaddress)
```
pip install discord.py
pip install asyncio
pip install web3
pip install cryptoaddress
```
2. Open main.py and replace the token variable, and put your Infura api key in the file.


## Disclaimer

Code is very rushed and not very optimized and probably could be better, but it works!


