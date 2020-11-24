class Category:
  def __init__(self,name):
    self.name = name
    self.ledger = list()

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    avail = self.check_funds(amount)
    if avail :
      self.ledger.append({"amount": amount * (-1), "description": description})
      return True
    else :
      return False
    
  def check_funds(self, amount):
    funds = self.get_balance()
    if funds < amount :
      return False 
    else :
      return True

  def transfer(self, amount, cat): 
    avail = self.check_funds(amount)
    if avail :
      self.withdraw(amount, 'Transfer to ' + cat.name)
      cat.deposit(amount, 'Transfer from ' + self.name)
      return True
    else :
      return False

  def get_balance(self):
    balance = 0
    for item in self.ledger :
      balance += item['amount']
    return balance
    
  def __str__(self):
        title = ""
        for x in range(15 - (len(self.name)//2)):
            title += "*"
        title += self.name    
        for x in range(30 - len(title)):
            title += "*"           
        content = ""
        for item in self.ledger:
            content += item["description"][:23:]
            for x in range(24 - len(item["description"][:23:])):
                content += " "
            content += "{:.2f}".format(item["amount"])
            content += "\n"
        content += "Total: {:.2f}".format(self.get_balance())    
        return title + "\n" + content


def create_spend_chart(categories):
    output = "Percentage spent by category\n"
    # get withdraws for each category for percentages
    withdrawTotals = dict([(x.title, sum([(lump if (lump := int(transaction['amount'])) < 0 else 0) for transaction in x.ledger])) for x in categories])

    # get withdraws for each category for percentages
    total = sum([withdrawTotals[x] for x in withdrawTotals])
    
    # create vertical bars
    for i in range(11):
        cAmount = 100 - (i * 10)
        output += f"{cAmount:3d}| "
        output += "  ".join([str('o' if (withdrawTotals[x.title]/total * 100) >= cAmount else ' ') for x in categories])
        output += '  \n'
        
    # create seperator
    output += "    " + ('-' *(3 * (len(categories))+1)) + '\n'

    # Create vertical text
    # Find max length
    max_length = max(list(map(lambda x : len(x.title), categories)))
    for i in range(max_length):
        output += "   "
        for x in categories:
            output += "  "
            try:
                output += x.title[i]
            except:
                output += ' '
        output += '  \n' if i != (max_length-1) else "  "

    return output