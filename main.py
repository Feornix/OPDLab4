import unittest

lines = ["User1\n", "12345\n", "User2\n", "1111\n"]
def userAlreadyExist(lines, login):
    for i in range(0, len(lines), 2):
        if lines[i] == login + "\n":
            return True
    return False

def checkEmptyForms(login, password):
    if login == "" or password == "":
        return True
    return False

def checkSpaces(login):
    for i in range(0,len(login)):
        if login[i] == " ":
            return True
    return False

def checkNotEnglishLatters(login, password):
    for i in login:
        if not i.isascii():
            return True
    for j in password:
        if not j.isascii():
            return True
    return False

def checkSymbols(login):
    for i in login:
        if i == "&" or i == "=" or i == "+" or i == "<" or i == ">" or i=="," or i=="\'" or i=="@":
            return True
    return False

def checkAuthorisation(lines, login, password):
    for i in range(0, len(lines), 2):
        if login + "\n" == lines[i]:
            if password + "\n" == lines[i + 1]:
                return True
    return False

def checkRegistration(login, password):
    if checkEmptyForms(login, password):
        return False
    elif checkSpaces(login):
        return False
    elif checkNotEnglishLatters(login, password):
        return False
    elif checkSymbols(login):
        return False
    else:
        return True

class TestLab(unittest.TestCase):

  def test_userAlreadyExists(self):
      self.assertTrue(userAlreadyExist(lines, "User1"))
      self.assertFalse(userAlreadyExist(lines, "User3"))

  def test_checkRegistration(self):
      self.assertFalse(checkRegistration("", "1234"))
      self.assertFalse(checkRegistration("User", ""))
      self.assertFalse(checkRegistration("", ""))
      self.assertFalse(checkRegistration("@", "1234"))
      self.assertFalse(checkRegistration("User&", "1234"))
      self.assertFalse(checkRegistration("       ", "1234"))
      self.assertFalse(checkRegistration("абвгд", "1234"))
      self.assertFalse(checkRegistration("User", "абвгд"))
      self.assertTrue(checkRegistration("User1", "12345"))

  def test_Authorisation(self):
      self.assertFalse(checkAuthorisation(lines,"User", "1234"))
      self.assertFalse(checkAuthorisation(lines, "", ""))
      self.assertFalse(checkAuthorisation(lines, "User1", "1111"))
      self.assertFalse(checkAuthorisation(lines, "12345", "User2"))
      self.assertTrue(checkAuthorisation(lines, "User1", "12345"))
      self.assertTrue(checkAuthorisation(lines, "User2", "1111"))


if __name__ == '__main__':
    unittest.main()