
child_meal = float(input('Please enter the price of the Child meal. '))
qty_child = int(input('How many Child meals will you purchase? '))
adult_meal = float(input('Please enter the price of the Adult meal. '))
qty_adult = int(input('How many Adult meals will you purchase? '))
taxrate = float(input(
    'What is the local tax rate?  \nPlease input percent in decimal form. Ex: 8.5% = 0.085 '))
subtotal = (child_meal*qty_child)+(adult_meal*qty_adult)
taxes = taxrate*subtotal
total = subtotal+taxes
print('Child meals: '+str(qty_child)+' @ $' +
      str(child_meal)+' = $'+str(qty_child*child_meal))
print('Adult meals: '+str(qty_adult)+' @ $' +
      str(adult_meal)+' = $'+str(qty_adult*adult_meal))
print('Subtotal   $'+str(subtotal))
print('Tax  @ '+str(taxrate)+' $'+str(round(taxes, 2)))
print('Total      $'+str(round(total, 2)))
print()
print()
