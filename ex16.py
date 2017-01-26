print "Type the file name"
file_name = raw_input ('$')

print "Your file name is %r" % file_name
file = open (file_name)
print file.read()
