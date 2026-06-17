'''
def display(s,ind):
    if ind == len(s):       
        return              
                            
    print(s[:ind+1])
    display(s,ind+1)

display("Vamsi",0)
=============================================
def display(s, ind, k):
    if ind == len(s) - k + 1:
        return
    print(s[ind:ind+k])
    display(s, ind+1, k)

display("python", 0, 3)
=============================================
def display(l,ind):
    if ind == len(l):
        return 0
    return l[ind]+display(l,ind+1)

l = [1,2,3,4,5,6,7,8,9]
 (display(l,0))
============================================='''
def display(s,i):
    if i == len(s):
        return 0
    if s[i] in 'aeiouAEIOU':
        return 1+display(s,i+1)
    else:
        return display(s,i+1)

s ="python programming"
print(display(s,0))
