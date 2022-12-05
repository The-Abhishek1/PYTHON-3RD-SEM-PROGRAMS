min=int(input("Enter the Starting Number:"))
max=int(input("Enter the Ending Number:"))
min_1=min
min_2=min
total=0

#Sum of even numbers using while loop
while min <= max:
  if(min % 2 == 0):
    total+=min
    min+=1
  else:
    min+=1
    continue
  

print("The Sum of Even Numbers from ",min_1,"to ",max,"is = ",total)


#Sum of even numbers using For loop
for min in range(min_2):
  if(min % 2 == 0):
    total+=min
  else:
    continue

print("The Sum of Even Numbers from ",min_1,"to ",max,"is = ",total)
