def not_string(stuff):
    """
    Given a string, return a new string where "not " has been added to the front.
    However, if the string already begins with "not",
    return the string unchanged.
    """
  new_string = ""
  word_check = "not"

  if word_check in stuff[0:3]:
    print stuff[0:3]
  else:
    new_string = word_check + ' ' + stuff
    print new_string

not_string("pizza")
