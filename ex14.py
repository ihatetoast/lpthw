from sys import argv

script, user_fname, user_lname = argv
prompt = 'Answer: '

print "Hi %s %s. I'm the %s script." % (user_fname, user_lname, script)
print "I'd like to ask you a few questions."
print "Do you go by %s or %s?" % (user_fname, user_lname)
prefers = raw_input(prompt)
print "Do you like me, %s?" % (prefers)
likes = raw_input(prompt)

print "where do you live, %s?" % (prefers)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer)
