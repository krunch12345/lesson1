def get_summ(one, two, delimiter='&'):
   txt = one + delimiter + two
   print(txt)
   return txt

LN = get_summ('Learn', 'python').upper()
print(LN)