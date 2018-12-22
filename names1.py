#print full name from first name and last of the following formats
#the name is captilazed indepdendent of form entered and prints both
#the classic Firstname Lastname as well as system-preferred Lastname, Firstname
#Example: set firstname as foo and lastname as Bar, the output is Foo Bar and Bar, Foo

firstname = "foo"
lastname = "BAR"
fmt1 = firstname.capitalize()+" "+lastname.capitalize()
fmt2 = lastname.capitalize()+firstname.capitalize()
print "Classic format ", fmt1
print "System-preferred ",fmt2
