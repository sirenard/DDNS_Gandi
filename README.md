# DDNS_Gandi
A Dynamic DNS script for gandi.net services

## Usage

```
usage: main.py [-h] --token TOKEN --fqdn FQDN --rrset_name RRSET_NAME [--create_if_not_exist] [--verbose]

Update a Gandi DNS record (type A) with current IP if the 2 values are different

optional arguments:
  -h, --help            show this help message and exit
  --token TOKEN         Api Key of your Gandi Account
  --fqdn FQDN           Full qualified domain name
  --rrset_name RRSET_NAME
                        Name of the record
  --create_if_not_exist
                        If True, create the DNS record with current IP address if it doesn't exist
  --verbose             Print information if True
```

Example: `python3 main.py --token {myToken} --fqdn blabla.be --rrset_name test` will update the record for *test.blabla.be* with your current IP.

It can be simply executed every X minutes with a cron Task

## Api Key/token

To have your Api key or see <https://docs.gandi.net/en/domain_names/advanced_users/api.html>:


* After logging in, click the down arrow next to your username in the top left corner.
* Scroll down and select “Change password & configure access restrictions.”
* Select Generate the API key if you have not yet generated an API key. Or, select “Regerate the API key” if you have already generated a key.
* Enter your account password.
* Click “Save.”

