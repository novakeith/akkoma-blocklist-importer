# relevant page in the docs on how to import/export this via cmd line:
# https://docs.akkoma.dev/stable/administration/CLI_tasks/config/#loading-specific-configuration-values-from-json
# Instructions: scp this file to your akkoma server. Follow instructions above
# YOU MAY NEED TO EDIT THE OUTPUT FILE to fix some formatting near the top and bottom. 
# the last tuple will have a comma after the closing curly bracket } - remove it

# open CSV file of your choice - change this and make sure the 
# CSV is saved to the same directory the python is being executed in
myFile = "blocklist.csv"
f = open(myFile, "r")

# output file. Change name if you want
outFile = "output.json"
o = open(outFile, "w")

# write beginning of json file
o.write('''
{
  "group": ":pleroma",
  "key": ":mrf_simple",
  "value": [
    {
      "tuple": [
        ":reject",
        [
''')

# read CSV line by line
for line in f:

    # split URL (position 0)
    url = line.split(",")[0]

    # write tuple for this URL. You can add your own reason where it says "blocklist"
    tupStr = """          {
            "tuple": [
              "%s",
              "Blocklist"
            ]
          }, """ % (url)
    o.write(tupStr)

    #to-do - determine if its last line in file and don't print the closing commma in the tuples

# write end of json file
o.write('''        ]
      ]
    }
  ]
}''')

# close files
f.close()
o.close()

# relevant page in the docs on how to import/export this via cmd line:
# https://docs.akkoma.dev/stable/administration/CLI_tasks/config/#loading-specific-configuration-values-from-json
# Instructions: scp this file to your akkoma server. Follow instructions above
# YOU MAY NEED TO EDIT THE OUTPUT FILE to fix some formatting near the top and bottom. 
# the last tuple will have a comma after the closing curly bracket } - remove it
