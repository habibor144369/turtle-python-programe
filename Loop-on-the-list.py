# loop on the list---- and string count....

saarc = ['Bangladesh', 'Afghanistan', 'Bhutan', 'Nepal', 'India', 'Pakistan', 'Sri Lanka']
text = 'is member of saarc'
count = len(text)

for country in saarc:
    count2 = len(country)
    totalString = count2 + count
    print(country, text,'=',totalString)
print(saarc, len(saarc))
