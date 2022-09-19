s1=["cat","mango","apple","banana"]
s2=["tac","alppe","anaanb","goman"]
i=0
score=0
#while (i<=len(s2)): 
for e in s2:
    print(e)
    a=input("arrange the letters to form a valid word<::> ")
    if(a in s1)==True:
        print("correct")
        score=score+1
    elif(a in s1)==False:
        print("incorrect")
        score=score-1 
print("your Net score is=",score)          
    
    
    



