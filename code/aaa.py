#
'''
a = input()
b = input()
a1 = ""
a2 = ""
b1=""
b2=""
for i in range(len(a)):
    if a[i] == '+' and a[i+1] !='-':
        if a[i+1]!='i':
            a1 = a[:i]
            a2 = a[i + 1:len(a)-1]
            break
        else:
            a1 = a[:i]
            a2 = '1'
    elif a[i]=='+' and a[i+1] =='-':
        if a[i+2]!='i':
            a1 = a[:i]
            a2 = a[i + 1:len(a) - 1]
            break
        else:
            a1=a[:i]
            a2='1'
for i in range(len(b)):
    if b[i] == '+' and b[i+1] !='-':
        if b[i+1]!='i':
            b1 = b[:i]
            b2 = b[i + 1:len(b)-1]
            break
        else:
            b1 = b[:i]
            b2 = '1'
    elif b[i]=='+' and b[i+1] =='-':
        if b[i+2]!='i':
            b1 = b[:i]
            b2 = b[i + 1:len(b) - 1]
            break
        else:
            b1=b[:i]
            b2='1'


res1=int(a1)*int(b1)-int(a2)*int(b2)
res2=int(a2)*int(b1)+int(a1)*int(b2)

if res1>=0:
    res1=str(res1)
else:
    res1="-"+str(res1)
if res2>=0:
    res2=str(res2)
else:
    res2="-"+str(res2)

print(res1, "+", res2,"i")

'''



'''
time=input()

year=int(time[:4])
month=int(time[5:7])
day=int(time[8:])


if year%4==0 or year%100==0 and year % 400!=0:
    months=[31,29,31,30,31,30,31,31,30,31,30,31]
else:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

first=day
for i in range(12):
    if i<month-1:
        first+=months[i]
print(first)

while(1):
    a=list(map(int,input().split(',')))
    N=a[0]
    M=a[1]
    count=0
    if M==2:
        for i in range(1,N):
            for ii in range(1,N):
                if i+ii==N:
                    count+=1
        print(count)
        count=0
    elif M==3:
        for i in range(1,N):
            for ii in range(1,N):
                for iii in range(1,N):
                    if i+ii+iii==N:
                        count+=1
        print(count)


'''
import sys


def printMatrix(num,n,res,start,end):
    if start>=end or end<=0:  # 偶数阶矩阵和奇数阶矩阵最后的形式不同
        if n%2!=0:
            res.append(num[start][end])
        return
    i =start
    while i<=end:  # 从上到下
        res.append(num[i][start])
        i+=1
    i=start+1
    while i<=end:  # 从左到右
        res.append(num[end][i])
        i+=1
    i=end-1
    while i>=start:  # 从下到上
        res.append(num[i][end])
        i-=1
    i=end-1
    while i>start:  # 从右到左
        res.append(num[start][i])
        i-=1
    printMatrix(num,n,res,start+1,end-1) # 采用递归的形式


if __name__ == "__main__":
    # 读取第一行的n
    a = list(map(int, (sys.stdin.readline().strip().split(" "))))
    n = a[0]
    m = a[1]
    if m >= 1 and m <= 1000 and n >= 1 and m <= 1000:
        num = []
        res = []
        for i in range(n):
            # 读取每一行
            line = sys.stdin.readline().strip()
            # 把每一行的数字分隔后转化成int列表
            values = list(map(int, line.split(" ")))
            num.append(values)

        printMatrix(num, n,res, 0, n-1)
        print(res)
        print(' '.join(map(str,res)))




'''
def solution(total_disk, total_memory, app_list):
    # TODO Write your code here
    dp = []
    for i in range(total_disk):
        dp1=[]
        for j in range(total_memory):
            dp1.append(0)
        dp.append(dp1)
    pass


if __name__ == "__main__":
    input1 = input()
    disk = int(input1.split()[0])
    memory = int(input1.split()[1])
    input2 = input1.split()[2]
    app_list = [[int(j) for j in i.split(',')] for i in input2.split('#')]
    print(len(app_list))
    app_list = sorted(app_list)
    print(app_list)
    print(solution(disk, memory, app_list))

'''





















