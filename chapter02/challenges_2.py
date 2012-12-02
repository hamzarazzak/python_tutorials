bill = int(input('Enter the total bill here: '))
# print(bill)
charge1 = bill * 20 / 100
charge2 = bill * 15 / 100
print ('The total cost including a tip of 20% will be ', int(charge1 + bill))
print ('The total cost including a tip of 15% will be ', int(charge2 + bill))
