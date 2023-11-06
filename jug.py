capacity=(12,8,5)
x=capacity[0]
y=capacity[1]
z=capacity[2]
memory={}
ans=[]
def get_all_status(state):
    a=state[0]
    b=state[1]
    c=state[2]

    if(a==6 and b==6):
        ans.append(state)
        return True
    if((a,b,c) in memory):
        return False

    memory[(a,b,c)]=1

    if(a>0):
        if(a+b<=y):
            if(get_all_status((0,a+b,c))):
                ans.append(state)
                return True
        else:
            if(get_all_status((a-(y-b),y,c))):
                ans.append(state)
                return True
        if (a+c<=z):
            if (get_all_status((0,b,a+c))):
                ans.append(state)
                return True
        else:
            if (get_all_status((a-(z-c),b,z))):
                ans.append(state)
                return True



    if (b>0):
        if(a+b<=x):
            if (get_all_status((a+b,0,c))):
                ans.append(state)
                return True
        else:
            if (get_all_status((x,b-(x-a),c))):
                ans.append(state)
                return True

        if (b+c <= z):
            if (get_all_status((a,0, b+c))):
                ans.append(state)
                return True
        else:
            if (get_all_status((a,b-(z-c),z))):
                ans.append(state)
                return True



    if(c>0):
        if (a + c<= x):
            if (get_all_status((a+c,b,0))):
                ans.append(state)
                return True
        else:
            if (get_all_status((x,b,c-(x-a)))):
                ans.append(state)
                return True
        if (b+c<= y):
            if (get_all_status((a, b+c, 0))):
                ans.append(state)
                return True
        else:
            if (get_all_status((a, y, c - (y - b)))):
                ans.append(state)
                return True
    return False
initial_state=(12,0,0)
print("Starting work")
get_all_status(initial_state)
ans.reverse()
for i in ans:
    print(i)
