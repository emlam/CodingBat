def not_string(stuff):
  new_string = ""
  word_check = "not"

  if word_check in stuff[0:3]:
    print stuff[0:3]
  else:
    new_string = word_check + ' ' + stuff
    print new_string

not_string("pizza")
