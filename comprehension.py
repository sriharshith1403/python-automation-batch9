#dict

d= {num: num*2 for num in range(1,4)}

states = ["ap","wb","tn"]
capitals = ["am","kolkata","chennai"]

d1={state: capital for state, capital in zip(states,capitals)}

#set
a=[1,1,2,2,]
s={n for n in a if n%2 == 0}
