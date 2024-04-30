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

def checkAuthorisation(lines, login, password):
    for i in range(0, len(lines), 2):
        if login + "\n" == lines[i]:
            if password + "\n" == lines[i + 1]:
                return True
    return False

class TestLab(unittest.TestCase):

  def test_userAlreadyExists(self):
      self.assertTrue(userAlreadyExist(lines, "User1"))
      self.assertFalse(userAlreadyExist(lines, "User3"))

  def test_emptyForms(self):
      self.assertTrue(checkEmptyForms("", "1234"))
      self.assertTrue(checkEmptyForms("User", ""))
      self.assertTrue(checkEmptyForms("", ""))
      self.assertFalse(checkEmptyForms("User1", "12345"))

  def test_Authorisation(self):
      self.assertFalse(checkAuthorisation(lines,"User", "1234"))
      self.assertFalse(checkAuthorisation(lines, "", ""))
      self.assertFalse(checkAuthorisation(lines, "User1", "1111"))
      self.assertFalse(checkAuthorisation(lines, "12345", "User2"))
      self.assertTrue(checkAuthorisation(lines, "User1", "12345"))
      self.assertTrue(checkAuthorisation(lines, "User2", "1111"))


if __name__ == '__main__':
    unittest.main()