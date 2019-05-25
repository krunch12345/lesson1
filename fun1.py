def get_summ(one, two, delimiter='&'):
   txt = one + delimiter + two
   return txt

ln = get_summ('Learn', 'python')
print(ln)
LN = ln.upper()
print(LN)