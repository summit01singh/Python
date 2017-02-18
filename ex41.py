def final_amt(p,r,n,t):
    '''Apply compund interest formula to p
    to produce the final amount'''
    a = p * (1+r/n) ** (n*t)
    return a

#Now as we have function , lets call it.
toinvest = float(input("How much amount you want to invest?"))
fa = final_amt(toinvest, 0.08, 12, 5)
print ("At the end of the period you'll have R", fa)
