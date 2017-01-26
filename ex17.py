print "Type your sample file name"
sample = raw_input ('>>==========>>>>')

print 'This is your sample file name %r' % sample
file = open (sample)

print file.read()
