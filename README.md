# tw-unblock
A CLI Tool to Unblock Twitter Accounts.

1. Install script requirements, `pip install -r requirements.txt`.
2. Obtain a Twitter Developer API key and create a `config.json` per the template in the working directory.
3. Run the command `python main.py unblock` or `python main.py unmute`.

## Sample `config.json`
```json
{
    "consumer_key": "xxxxxxxxxxxxxxxxxxxxxxxxx",
    "consumer_secret": "xxxxxxxxxxxxxxxxxxxxxxxxx",
    "access_token": "xxxxxxxxxxxxxxxxxxxxxxxxx",
    "access_token_secret": "xxxxxxxxxxxxxxxxxxxxxxxxx"
}
```