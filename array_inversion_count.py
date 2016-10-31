#inputArray = list(map(int,input().split(' ')))
inputArray = [2,4,1,3,5]
tempArray = inputArray
def main(inputArray):
    length = len(inputArray) - 1
    return countInversions(inputArray,0,length)

def countInversions(a,left,right):
    mid = 0
    inv_count = 0
    if right > left:
        mid = abs((left + right) / 2)
        inv_count = countInversions(a,left,mid)
        inv_count = countInversions(a,mid+1,right)
        inv_count += merge(inputArray,left,mid+1,right,tempArray)
    return inv_count

def merge(a,left,mid,right,tempArray):
    i=left
    j=mid
    inv_count = 0
    k = left
    while i<=mid-1 and j<=right:
        if a[i] <= a[j]:
            #tempArray.append(a[i])
            tempArray[k] = a[i]
            k = k+1
            i = i+1
        else:
            #tempArray.append(a[j])
            tempArray[k] = a[j]
            k = k + 1
            j = j+1
            inv_count = inv_count + (mid - i)

    while i <= mid-1:
        tempArray[k] = a[i]
        k = k + 1
        i = i+1

    while j <= right:
        tempArray[k] = a[j]
        k = k + 1
        j = j+1

    for i in range(left,right+1):
        inputArray[i] = tempArray[i]

    return inv_count

print(main(inputArray))
