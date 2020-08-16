学习笔记

Lecture 16 bitwise operation

指定位置的位运算
1. 将 x 最右边的 n 位清零：x & (~0<<n)
2. 获取x的第n位值（0或者1）：(x >>n) & 1
3. 获取x的第n位的幂值：x&(1<<n)
4. 仅将第n位设置为1：x|(1<<n)
5. 仅将第n为设置为0：x&(~(1<<n))
6. 将x最高位至第n位（含）清零：x&((1<<n)-1)
7. 将第n为至第0为（含）清零：x & (~((1<<n+1)-1))

实战
```
判断奇偶：
x%2 == 1 -> (x&1) == 1
            取最后一位
x%2 == 0 -> (x&1) == 0


x >> 1 -> x / 2
mid = (left + right) / 2 -> (left + right) >> 1

x = x&(x-1) 清零最低位的1
x& -x => 得到最低位的1

x& ~x => 0
```


Lecture 17 布隆过滤器，LRU cache

Bloom filter：
优点是空间效率和查询时间都远远超出一般的算法
缺点时候有一定的误识别和删除困难

LRU cache（两个要素：大小，替换策略）
Hashtable + Double linkedList
O(1) find
O(1) 修改 更新


Lecture 18 Sorting

初级排序 O(n^2)

selection sort
insertion sort
bubble sort

```java

public void selectionSort(int[] arr) {

    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        int tempp = arr[minIndex];
        arr[minIndex] = arr[i];
        arr[i] = temp;
    }

}

```

```java
public void insertionSort(int[] arr) {
    int n = arr.length; 
    for (int i = 1; i < n; ++i) { 
        int key = arr[i]; 
        int j = i - 1; 

        while (j >= 0 && arr[j] > key) { 
            arr[j + 1] = arr[j]; 
            j = j - 1; 
        } 
        arr[j + 1] = key; 
    } 
}

```

```java
public void bubbleSort() {
    int n = arr.length; 
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) { 
                // swap arr[j+1] and arr[i] 
                int temp = arr[j]; 
                arr[j] = arr[j+1]; 
                arr[j+1] = temp; 
            } 
        }
    }
}

```

高级排序！O(nlogn)

quick sort
merge sort

特殊排序学习笔记