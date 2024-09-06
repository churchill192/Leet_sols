z = {'.':"yes", '..':"food"}
x = ".¦/..¦/"
#y=[]
s = ""
res = ""
for i in x.split('¦'):
    c = i.split('/')
    for j in c:
        #y.append(j)
        s+=j
        if j in z:
            res+=z[j]
    s+=" "
    res+=" "
#print(y)
print(s)
print(res)
print(x.split('¦'))

# x = {'yes': ".", 'no': "-", 'food': "..", 'water': "--", 'okay': ".-",'thankyou': "-.",
#                      'restroom': "...", 'turn': "..-", 'bath': ".-.", 'medicine': ".--", 'bed': "-..",'blanket': "-.-",
#                      'doctor': "--.", 'sleep': "---", 'quiet': "....", 'routine': "...-", 'allergy': "..-.",'medicine name': "..--",
#                      'hot': ".-..", 'cold': ".-.-", 'nausea': ".--.", 'breathing': ".---", 'dizzyness': "-...",'anxiety': "-..-",
#                      'fall risk': "-.-.", 'pain': "-.--",'itchy': "--..", 'help': "--.-", 'time': "---.", 'family': "----",
#                      'emergency':"......"}
# print(len(list(x.values())))
