def reverse_range(array,start_range,end_range):
    while(end_range>start_range):
       array[start_range], array[end_range]=array[end_range],array[start_range]
       end_range-=1
       start_range+=1
        
    return array
        
    
    
array=list(map(int,input().split()))
start_range =int(input())
end_range=int(input())
print(reverse_range(array,start_range,end_range))