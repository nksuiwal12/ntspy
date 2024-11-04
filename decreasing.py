def main():
    arr=list(map(int,input("enter the array elemnts").split()))
    if(arr[0]<arr[1]):
        print(arr[-1])
    else:
        if arr[1]==max(arr[1:len(arr)]):
            print(arr[0])
        else:
            print(arr[-1])
    
if __name__=="__main__":
    main()