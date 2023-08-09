# akkoma-blocklist-importer
### a tool to help clean up CSV block lists and put them into a format akkoma recognizes ###

## Why ##
Akkoma does not allow for importing block lists via CSV. However, based on their [documentation](https://docs.akkoma.dev/stable/administration/CLI_tasks/config/#loading-specific-configuration-values-from-json), properly formatted JSON can be imported.

**Please Note** - Following the instructions overwrites any existing entries you have in your MRF Simple policy. 

## Steps ##
1. run this script using `python python.py` - make sure you drop your CSV file into the same directory and match the filename specified at the top of the python.py file ('blocklist.csv')
2. Copy the outputted JSON file to your server using scp: `scp /your/dir/here/output.json user@remote.serv:/tmp/output.json`
3. On your akkoma server, become the akkoma user: `su akkoma` (you may need to be root before you can do this)
4. Navigate to your akkoma directory (for OTP it's usually /var/www/akkoma/live) and run the command specified in the documentation above: `./bin/pleroma_ctl config load_from_file /tmp/output.json`
5. Reboot your akkoma server.
