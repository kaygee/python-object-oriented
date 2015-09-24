# Now, add a method named hours that returns "We're open from {} to {}.".
# Replace the first placeholder with the open time and the second with the close
# time. Remember you need to pass keywords to .format() if your placeholders have names.

class Store:
  open = 1
  close = 2

  def hours(self):
    return "We're open from {} to {}.".format(self.open, self.close)
