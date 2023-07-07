import json


class Database:

  def insert(self, name, email, password):
    '''
    this method will inser values inside the jason file:

    1. First it will check is there any email with that email in the dictionary
    2. If the email is available then it will throw an error user already available
    3. Else it will add the email as a key and [name, password]
    '''

    # lets read the jason file

    with open('user.json', 'r') as rf:
      users = json.load(rf)
      if email in users:
        return 0
      else:
        users[email] = [name, password]
    with open('user.json', 'w') as wf:
      json.dump(users, wf)
      return 1

  def search(self, email, password):
    with open('user.json', 'r') as rf:
      users = json.load(rf)
      if email in users:
        if users[email][1] == password:
          return 1
        else:
          return 0
      else:
        return -1
