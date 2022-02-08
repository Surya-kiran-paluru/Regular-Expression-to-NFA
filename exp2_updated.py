p = input("Enter Regular Expression:")

state = [ [ 0, 0, 0] for i in range(50) ]
#print(state)
i=0
j=1
ind_open = j #index of open bracket

while(i < len(p)):
	
	if(i == len(p)-1):
		if p[i]=='a':
			state[j][0] = j+1
			j += 1
		
		if p[i]=='b':
			state[j][1] = j+1
			j += 1

	if(i+1 < len(p)):
		if ( p[i]=='a' and p[i+1]!='*' and p[i+1]!='|'):
			state[j][0] = j+1
			j += 1
	
		if ( p[i]=='b' and p[i+1]!='*' and p[i+1]!='|'):
			state[j][1] = j+1
			j += 1

		if ( p[i]=='a' and p[i+1]=='*' and p[i+1]!='|'):
			state[j][2]=((j+1)*10)+(j+3)
			j += 1
			state[j][0]=j+1
			j += 1
			state[j][2]=((j+1)*10)+(j-1)
			j += 1

		if ( p[i]=='b' and p[i+1]=='*' and p[i+1]!='|'):
			state[j][2]=((j+1)*10)+(j+3)
			j += 1
			state[j][1]=j+1
			j += 1
			state[j][2]=((j+1)*10)+(j-1)
			j += 1

		if(i+2 < len(p)):

			if(p[i]=='a' and p[i+1]=='|' and p[i+2]=='b'):
				
				state[j][2]=((j+1)*10)+(j+3)
				j += 1
				state[j][0]=j+1
				j += 1
				state[j][2]=j+3
				j +=1
				state[j][1]=j+1
				j += 1
				state[j][2]=j+1
				j += 1
				i=i+2

			if(p[i]=='b' and p[i+1]=='|' and p[i+2]=='a'):
				state[j][2]=((j+1)*10)+(j+3)
				j += 1
				state[j][1]=j+1
				j += 1
				state[j][2]=j+3
				j +=1
				state[j][0]=j+1
				j += 1
				state[j][2]=j+1
				j += 1
				i=i+2

		if(p[i]==')' and p[i+1]=='*'):
			state[ind_open-1][2]=((j+1)*10)+1
			state[j][2]=((j+1)*10)+1
			j += 1
	if(p[i]=='('):
		ind_open = j
	i+=1
	
	
		
print("state	a	b	e",end="\n\n")
if(state[0] == [0,0,0]):
	state[0] = [0,0,1]
for i in range(0,j+1):
	print(i,state[i][0],state[i][1],state[i][2],sep="\t")