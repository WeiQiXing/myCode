**逆时针读取矩阵**
顺时针和逆时针的方法类似，只需调整打印方向的顺序即可，这里默认行数等于列数。


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


**将一个二维数组顺时针旋转90度**
主要规律：a[i][j]=a[n-1-j][i],n=阶数


public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n/2; i++) {
            for (int j = i; j < n-1-i; j++)
{
                int temp = matrix[i][j];
                matrix[i][j] =matrix[n-1-j][i];
                matrix[n-1-j][i] =matrix[n-1-i][n-1-j];
                matrix[n-1-i][n-1-j] =matrix[j][n-1-i];
                matrix[j][n-1-i] = temp;
            }
        }
}





















