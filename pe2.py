def main():
    f=[]
    f.append(1)
    f.append(1)
    i=1
    while(f[i]+f[i-1]<=4000000):
        f.append(f[i]+f[i-1])
        i=i+1
    sum=0
    for n in f:
        if n%2==0:
            sum=sum+n
    print(sum)
if __name__=="__main__":
    main()