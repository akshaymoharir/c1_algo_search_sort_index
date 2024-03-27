
def swap(x,y):
    temp = x
    x = y
    y = temp
    return x,y

def sort_descending(A):
    loop_count = 0
    for j in range(len(A)):
        for i in reversed(range(j)):
            loop_count+=1
            if A[i]<A[i+1]:
                A[i],A[i+1] = swap(A[i],A[i+1])
            else:
                break

# Function to sort given array in ascending order
def sort_ascending(A):
    loop_count = 0
    for j in range(len(A)):                     # This loop iterates over each element in array   
        for i in reversed(range(j)):            # This loop iterates over dynamically from 1st element till jth element 
            loop_count+=1
            if A[i]>A[i+1]:
                A[i],A[i+1] = swap(A[i],A[i+1])
            else:
                break

# Test cases
A1 = [1,34,5,0,1,2,7,10,67,4]
A2 = [0,-3,5,0,45,2,6]
A3 = [1,4,3]

for A in [A1,A2,A3]:
    print("\nInput A:",A)
    sort_ascending(A)
    print("Ascending Sorted:",A)
    sort_descending(A)
    print("Descending Sorted:",A,"\n")
