---
categories: null
date: 2022-01-16 19:46:28
tags:
- leetcode
- blob
- problems
- github
- master
title: leetcode
---

> 

<!--more-->

# 剑指 offer

## 赋值运算符

```cpp
class CMyString{
public:
    CMyString(char* pData = nullptr);
    CMyString(const CMyString& str);
    CMyString& operator=(const CMyString &str);
    ~CMyString(void);
    -
private:
    char* m_pData;
}

CMyString& CMyString::operator=(const CMyString &str){
    if(this != &str){
        CMyString strtmp(str);
        char* ptmp = strtmp.m_pData;
        strtmp.m_pData = m_pData;
        m_pData = ptmp;
    }
    return *this;
}
```

## 面试题3：数组中重复的数字

题目一：找出数组中重复的数字。
在一个长度为n的数组里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组(2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。

```cpp
//hash table
int findRepeatNumber(vector<int>& nums) {
    vector<bool> map(nums.size(), false);
    for(auto i: nums){
        if(map[i])
            return i;
        else
            map[i] = true;
    }
    return 0;
}

//节省空间, 对原数组进行操作
int findRepeatNumber(vector<int>& nums) {
    int i=0;
    while(i<nums.size()){
        if(nums[i] == i)
            i++;
        else{
            if (nums[nums[i]] == nums[i])
                return nums[i];
            else 
                swap(nums[nums[i]], nums[i]);
        }
    }
    return 0;
}
```

在一个长度为n+1的数组里的所有数字都在1～n的范围内，所以数组中至少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能修改输入的数组。例如，如果输入长度为8的数组{2,3,5,4,3,2,6,7}，那么对应的输出是重复的数字2或者3。

```cpp
//不修改原数组
int countRange(vector<int> nums, int start, int end){
    int count = 0;
    for(int i=0; i<nums.size(); i++){
        if(nums[i]>=start && nums[i]<=end)
            count++;
    }
    return count;
}

int findRepeatNumber(vector<int>& nums) {
    int start = 1;
    int end = nums.size()-1;
    while(end>=start){
        int mid = ((end-start)>>1)+start;
        int count = countRange(nums, start, middle);
        if(end == start){
            if(count>1)
                return start;
            else
                break;
        }
        if(count>(mid-start+1))
            end = mid;
        else   
            start = mid+1;
    }
    return 0;
}

```

## 面试题4：二维数组中的查找

题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

```cpp
bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
  if(matrix.empty())
    return false;
  int width = matrix[0].size();
  int height = matrix.size();
  int i=height-1, j=0;
  while(i>=0 && j<width){
    if(matrix[i][j]==target)
      return true;
    else if(target<matrix[i][j])
      i--;
    else if(target>matrix[i][j])
      j++;
  }
  return false;
}
```

字符串存储问题

```cpp
int tmain(int argc, _TCHAR* argv[]) { 
  char str1[] = "hello world";
  char str2[] = "hello world":

  char* str3 = "hello world";
  char* str4 = "hello world":

  if(strl == str2)
  	printf("str1 and str2 are same\n");
	else 
  	printf("str1 and str2 are not same\n");
//not same
  
  if(str3 == str4)
		printf("str3 and str4 are same.\n");
  else 
  	printf("str3 and str4 are not same. \n");
//same
  
  return 0
}
```

## 面试题5：替换空格

 题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如， 输入“We are happy.”，则输出“We%20are%20happy.”

1. 新分配字符串

```cpp
string replaceSpace(string s) {
  string ans;
  for(char i:s){
    if(i == ' ')
      ans.append("%20");
    else
      ans.push_back(i);
  }
  return ans;
}
```

2. 在原有字符串上修改(先估计大小, 后从后往前更新)

```cpp
string replaceSpace(string s) {
  int space_count = 0;
  for(char i:s){
    if(i == ' ')
      space_count+=1;
  }
  int i=s.length()-1;
  int length = s.length() + space_count*2;

  s.resize(length);
  length -= 1;//下标-1
  for(; i>=0 && length>=i; i--){
    if(s[i] == ' '){
      s[length--] = '0';
      s[length--] = '2';
      s[length--] = '%';
    }
    else
      s[length--] = s[i];
  }
  return s;
}
```

## 面试题6：从尾到头打印链表 

题目：输入一个链表的头节点，从尾到头反过来打印出每个节点的值。 链表节点定义如下：

```cpp
struct ListNode{
	int m_nkey; 
  ListNode* m_pNext;
};
```

不改变原链表结构

```cpp
vector<int> reversePrint(ListNode* head) {
  stack<int> s;
  ListNode* p = head;
  while(p){
    s.push(p->val);
    p = p->next;
  }
  vector<int> ans;
  while(!s.empty()){
    ans.push_back(s.top());
    s.pop();
  }
  return ans;
}
```

链表反转

```cpp
vector<int> reversePrint(ListNode* head) {
  vector<int> ans;
  ListNode* cur = head, * pre = NULL, *next;
  while(cur){
    next = cur->next;
    cur->next = pre;
    pre = cur;
    cur = next;

  }
  while(pre){
    ans.push_back(pre->val);
    pre = pre->next;
  }
  return ans;

}
```

## 树

树的遍历: 递归迭代, 宽度遍历

树的特例: 二叉搜索树, 堆, 红黑树

## 面试题7：重建二叉树

题目：输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如，输入 前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则 重建如图所示的二叉树并输出它的头节点。二叉树节点的定义如下：

```cpp
struct BinaryTreeNode
{  
  int m_nValue;
  BinaryTreeNode* m_pLeft;
  BinaryTreeNode* m_pRight;
}
```

```cpp
class Solution {
public:
    vector<int> preorder;
    vector<int> inorder;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.empty() || inorder.empty())
            return nullptr;
        this->inorder = inorder;
        this->preorder = preorder;
        return ConstructCore(0, this->inorder.size()-1, 0, this->preorder.size()-1);
    }

    TreeNode* ConstructCore(int startin, int endin, int startpre, int endpre){
        int rootvalue = preorder[startpre];
        TreeNode* root = new TreeNode(rootvalue);

        if(startpre == endpre)
            if(startin == endin && preorder[startpre] == inorder[startin])
                return root;
            else
                cout<<"invalid";
        
        int rootin = startin;
        while(rootin<=endin && inorder[rootin]!=rootvalue)
            ++rootin;
        if(rootin == endin && inorder[rootin]!=rootvalue)
            cout<<"invalid";
        
        int leftlength = rootin - startin;
        int leftpreend = startpre + leftlength;
        if(leftlength>0){
            root->left = ConstructCore(startin, rootin-1,startpre+1, leftpreend);
        }

        if(leftlength<endpre-startpre)//?
        {
            root->right = ConstructCore(rootin+1, endin, leftpreend+1, endpre);
        }
        return root;

    }
};

```

## 面试题8：二叉树的下一个节点 

题目：给定一棵二叉树和其中的一个节点，如何找出中序遍历序列的 下一个节点？树中的节点除了有两个分别指向左、右子节点的指针，还有 1个指向父节点的指针。

```cpp
TreeNode* solution(TreeNode* pnode){
    TreeNode* ans = nullptr;
    if(pnode->right != nullptr){
        TreeNode* pright = pnode->right;
        while(pright->left!=nullptr)
            pright = pright->left;
        ans = pright;
    }
    else if(pnode->parent!=nullptr){
        TreeNode* pcur = pnode;
        TreeNode* pparent = pnode->parent;
        while(pparent!=nullptr && pcur == pparent->right){
            pcur = pparent;
            pparent = pparent->parent;
        }
        ans = pparent;
    }
}
```



## 面试题9：用两个栈实现队列

题目：用两个栈实现一个队列。队列的声明如下，请实现它的两个函 数 appendTail 和 deleteHead，分别完成在队列尾部插入节点和在队列头部删 除节点的功能。

```cpp
class CQueue {
public: 
    CQueue() {

    }
    
    void appendTail(int value) {
        s1.push(value);
    }
    
    int deleteHead() {
        if(s2.empty()){
            while(!s1.empty()){
                int tmp = s1.top();
                s1.pop();
                s2.push(tmp);
            }
        }
        if(s2.empty()){
            cout<<"invalid";
            return -1;
        }
        int ret = s2.top();
        s2.pop();
        return ret;
    }
private:
    stack<int> s1;
    stack<int> s2;
};
```

## 面试题10：斐波那契数列

 题目一：求斐波那契数列的第n项。 写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。

**注意取模!**

```cpp
class Solution {
public:
    int fib(int n) {
        vector<int> hash {0, 1};
        if(n<2)
            return hash[n];
        long long n1=0;
        long long n2=1;
        long long ans = 0;
        for(int i=2; i<=n; i++){
            ans = (n1+n2)%int(1e9+7);
            n1 = n2%int(1e9+7);
            n2 = ans%int(1e9+7);
        }
        return ans%int(1e9+7);
    }
};
```

## 快速排序

```cpp
int Partition(int data[], int length, int start, int end){
    if(data==nullptr||length<=0||start<=0||end>=length)
        return -1;
    int index = start;//可以随机数
    swap(&data[index], &data[end]);//把基准放在最后

    int small = start-1;
    for(index=start; index<end; index++){
        if(data[index]<data[end]){
            ++small;
            if(small!=index)
                swap(&data[index], &data[small]);
        }
    }
    ++small;
    swap(&data[small], &data[end]);
    return small;
}

void QuickSort(int data[], int length, int start, int end){
    if(start == end)
        return;
    int index = Partition(data, length, start, end);
    if(index>start)
        QuickSort(data, length, start, index-1);
    if(index<end)
        QuickSort(data, length, index+1, end);
}
```

## 面试题11：旋转数组的最小数字

题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为 数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小 元素。例如，数组(3, 4, 5, 1, 2}为{1,  2, 3, 4, 5}的一个旋转，该数组的最小值为1。

```cpp
int minArray(vector<int>& numbers) {
    if(numbers.empty())
        return -1;
    int start = 0;
    int end = numbers.size()-1;
    int mid = start + ((end-start)>>1);
    while(start<end){
        mid = start + ((end-start)>>1);
        if(numbers[mid]>numbers[end])
            start = mid+1;
        else if(numbers[mid] < numbers[end])
            end = mid;
        else
            end-=1;
    }
    return numbers[start];
}
```

## 面试题12：矩阵中的路径 

题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某 字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以 在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格， 那么该路径不能再次进入该格子。

```cpp
class Solution {
    int row, col;
public:
    bool check(vector<vector<char>>& board, int i, int j, string word, int k){
        if(i<0 || i>=row || j<0 || j>=col || board[i][j]!=word[k])
            return false;
        if(k == word.size()-1)
            return true;

        board[i][j] == '\0';
        bool res = 
        check(board, i+1, j, word, k+1)||
        check(board, i-1, j, word, k+1)||
        check(board, i, j+1, word, k+1)||
        check(board, i, j-1, word, k+1);

        board[i][j] = word[k];

        return res;
    }

    bool exist(vector<vector<char>>& board, string word) {
        if(board.empty())
            return false;

        row = board.size();
        col = board[0].size();
        for(int i=0; i<row; i++)
            for(int j=0; j<col; j++)
                if(check(board, i, j, word, 0))
                    return true; 
        return false;
    }
};
```

## 面试题14：剪绳子

题目：给你一根长度为n的绳子，请把绳子剪成m段（m、n都是整数， n>1并且m＞1)，可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的段，此时得到的最大乘积是18。

```cpp
class Solution {
public:
    int cuttingRope(int n) {
        if(n<=3)
            return n-1;
        vector<int> hash(n+1);
        hash[1] = 1;
        hash[2] = 2;
        hash[3] = 3;
        int ans = 0;
        for(int i=4; i<=n; i++){
            for(int j=1; j<=i/2; j++){
                ans = max(ans, hash[j]*hash[i-j]);
                hash[i] = ans;
            }
            
        }
            
        return hash[n];
    }
};
```

## 面试题15：二进制中1的个数

题目：请实现一个函数，输入一个整数，输出该数二进制表示中1 的 个数。例如，把9表示成二进制是1001，有2位是1。因此，如果输入9, 则该函数输出2。

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        while(n>0){
            ans += n&1;
            n=n>>1;
        }
        return ans;
    }
};

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        while(n>0){
            n = n&(n-1);
            ++ans;
        }
        return ans;
    }
};
```

把一个整数减去1之后再和原来的整数做位与运算，得到的结果相当 于把整数的二进制表示中最右边的1变成0。很多二进制的问题都可以用这 种思路解决。

## 面试题 16：数值的整数次方

题目：实现函数 double Power(double base, int exponent)，求 base 的 exponent 次方。不得使用库函数，同时不需要考虑大数问题

```cpp
class Solution {
public:
    double qpow(double a, unsigned int n){
        double ans = 1;
        while(n){
            if(n&1)
            ans*=a;
            a*=a;
            n>>=1;
        }
        return ans;
    }

    double myPow(double x, int n) {
        if(x==0.0)
            return 0;
        if(n==0)
            return 1;
        double ans = 1;
        if(n<0){
            unsigned int nnew = (unsigned int)n;
            ans = 1.0/qpow(x, -nnew);
        }
        else{
            ans = qpow(x, n);
        }
        return ans;
    }
};
```

注意 unsigned int 用法

### 快速幂

```cpp
int qpow(int a, int n){
  if(n==0)
    return 1;
  else if(n&1 == 1)
    return qpow(a, n-1) * a;
  else{
    int tmp = qpow(a, n>>1);
    return tmp*tmp;
  }
}

int qpow(int a, int n){
  int ans = 1;
  while(n){
    if(n&1)
      ans*=a;
    a*=a;
    n>>=1;
  }
  return ans;
}
```

## 面试题17：打印从1到最大的n位数

题目：输入数字 n，按顺序打印出从1到最大的n位十进制数。比如输 入3，则打印出1、2、3一直到最大的3位数999。

?大数问题, 字符串表示数

## 面试题18：删除链表的节点

题目一：在0(1)时间内删除链表节点。 给定单向链表的头指针和一个节点指针，定义一个函数在0(1)时间内 删除该节点。链表节点与函数的定义如下：

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* deleteNode(ListNode** head, ListNode* tobedelete) {
        ListNode* next = tobedelete->next;
        if(*head == tobedelete){
            delete tobedelete;
            tobedelete = nullptr;
            *head = nullptr;
        }
            
        else if(next!=nullptr){
            tobedelete->val = next->val;
            tobedelete->next = next->next;

            delete next;
            next = nullptr;
        }
        else{
            ListNode* cur = *head;
            while(cur->next!=tobedelete)
                cur = cur->next;
            cur->next = nullptr;
            delete tobedelete;
            tobedelete = nullptr;
        }

    }
};
```

题目二：删除链表中重复的节点。 在一个排序的链表中，如何删除重复的节点？

## 面试题19：正则表达式匹配 

![截屏2022-08-31 14.19.11](https://tva1.sinaimg.cn/large/e6c9d24ely1h5pxclxi0uj20wi06s767.jpg)

```cpp
class Solution {
public:
    string m_s;
    string m_p;

    char star = '*';
    char dot = '.';

    bool isMatch(string s, string p) {
        

        m_p = p;
        m_s = s;

        return isMatchIndex(0, 0);
    }

    bool isMatchIndex(int i_s, int i_p){
        if(i_s == m_s.size() && i_p == m_p.size())
            return true;
        if(i_s!=m_s.size() && i_p == m_p.size())
            return false;

        if(i_p+1<m_p.size() && m_p[i_p+1] == star){
            if((m_p[i_p]==dot && i_s!=m_s.size()) || m_p[i_p]==m_s[i_s])
                return  isMatchIndex(i_s+1, i_p+2) || isMatchIndex(i_s+1, i_p) || isMatchIndex(i_s, i_p+2);
            return isMatchIndex(i_s, i_p+2);
            
        }
        if((m_p[i_p] == dot && i_s!=m_s.size()) || m_p[i_p] == m_s[i_s]){
            return isMatchIndex(i_s+1, i_p+1);
        }
        return false;
    }
};

```

## 面试题 20：表示数值的字符串

题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小 数）。例如，字符串"+100"、"5e2”、"-123"、"3.1416"及"-1E-16"都表示数 值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

```cpp
class Solution {
public:
    string m_s;

    void fit(string& s){
        while(s.front()==' ')
            s.erase(s.begin());
        while(s.back()==' ')
            s.pop_back();
    }

    int isInt(int &i){
        while(m_s[i]>=48 && m_s[i]<=57)
            ++i;
        return i;
    }

    int isE(int &i){
        if(m_s[i]=='e' || m_s[i]=='E')
            return ++i;
        return i;
    }

    int isPN(int &i){
        if(m_s[i]=='-' || m_s[i]=='+')
            return ++i;
        return i;
    }

    int isdot(int &i){
        if(m_s[i]=='.')
            return ++i;
        return i;
    }

    bool isNumber(string s) {
        m_s = s;
        fit(m_s);
        int cur = 0;
        vector<int> check;//数值开始, 小数点, 数值结束, e 开始, 而结束
        check.push_back(isPN(cur));
        check.push_back(isInt(cur));
        check.push_back(isdot(cur));
        check.push_back(isInt(cur));
        if(check[0]==check[3])//no number
        {
            cout<<"no number";
            return false;
        }    
        if(check[1]!=check[2] && (check[0]+1==check[3]))//.+null
        {
            cout<<"no dot";
            return false;
        } 
        
        check.push_back(isE(cur));
        check.push_back(isPN(cur));
        check.push_back(isInt(cur));
        if(check[3]!=check[4] && check[5]==check[6])
        {
            cout<<"no e";
            return false;
        } 
        if(check[3]==check[4] && check[4]!=check[5])
            return false;
        
        if(cur==m_s.size())
            return true;
        return false;

    }
};
```

## 面试题 21：调整数组顺序使奇数位于偶数前面

题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序， 使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

```cpp
class Solution {
public:
    bool isOdd(int i){
        return i&1;
    }

    vector<int> exchange(vector<int>& nums) {
        int even = 0;
        int odd = nums.size()-1;
        while(even<odd){
            bool isodd = isOdd(nums[odd]);
            bool iseven = !isOdd(nums[even]);
            if(!isodd)
                odd--;
            if(!iseven)
                even++;
            if(isodd && iseven){
                swap(nums[odd], nums[even]);
                odd--;
                even++;
            }
            
        }
        return nums;
    }
};
```

注意解耦合

## 面试题 22：链表中倒数第k个节点

题目：输入一个链表，输出该链表中倒数第k个节点。为了符合大多 数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例 如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、 6。这个链表的倒数第3 个节点是值为4的节点。

```cpp
class Solution {
public:
    ListNode* getKthFromEnd(ListNode* head, int k) {
        int forward = 0;
        ListNode* p = head;
        while(p!=NULL){
            p = p->next;
            forward++;
        }
        if(k>forward)
            return NULL;
        int reverse = forward - k;
        p = head;
        while(reverse!=0){
            p = p->next;
            reverse--;
        }
        return p;
    }
};

//只遍历一边
class Solution {
public:
    ListNode* getKthFromEnd(ListNode* head, int k) {
        ListNode* p1 = head;
        while(p1!=NULL && k>0){
            p1 = p1->next;
            k--;
        }
        ListNode* p2 = head;
        while(p1!=NULL){
            p1 = p1->next;
            p2 = p2->next;
        }
        return p2;
    }
};
```

## 面试题 23：链表中环的入口节点

题目：如果一个链表中包含环，如何找出环的入口节点？例如，在如 图3.8所示的链表中，环的入口节点是节点3。

```CPP
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if(head == nullptr)
            return nullptr;
        
        ListNode* pslow = head->next;
        if(pslow==nullptr)
            return nullptr;
        ListNode* pfast = pslow->next;
        while(pfast!=nullptr && pfast!=pslow){
            pslow = pslow->next;
            pfast = pfast->next;
            if(pfast)
                pfast = pfast->next;
        }

        if(pfast==nullptr)
            return nullptr;
        ListNode* pcircle = pfast->next;
        int circle_len = 1;
        while(pcircle!=pfast){
            pcircle = pcircle->next;
            circle_len++;
        }

        ListNode* pcirclestart = head;
        pcircle = head;
        for(int i=0; i<circle_len; i++)
            pcircle = pcircle->next;
        while(pcircle!=pcirclestart){
            pcircle = pcircle->next;
            pcirclestart = pcirclestart->next;
        }

        return pcirclestart;

    }
};
```

先快慢指针, 后转圈统计环长, 后先后指针找环开始端

## 24 反转链表

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {

        ListNode* cur = head;
        ListNode* next = nullptr;
        ListNode* pre = nullptr;

        while(cur){
            next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
            
        }
        return pre;
    }
};

class Solution{
  public ListNode* reverseList(ListNode* head){
    if(head == null || head->next == null)
      return head;
    ListNode* newhead = reverseList(head->next);
    head->next->next = head;
    head->next = null;
    return newhead;
  }
};
```

## 面试题 25：合并两个排序的链表

题目：输入两个递增排序的链表，合并这两个链表并使新链表中的节 点仍然是递增排序的。例如，输入图3.11中的链表1和链表2，则合并之 后的升序链表如链表 3 所示。链表节点定义如下：

```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* cur = l1;
        ListNode head;
        cur = &head;
        while(l1!=nullptr && l2!=nullptr){
            if (l1->val<l2->val){
                cur->next = l1;
                l1 = l1->next;
            }
            else{
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        if(l1 == nullptr)
            cur->next = l2;
        else
            cur->next = l1;
        return head.next;
    }
};
```

首节点

## 面试题26：树的子结构

题目：输入两棵二叉树A和B，判断B是不是A的子结构。二叉树节 点的定义如下：

```cpp
class Solution {
public:
    bool isSubStructure(TreeNode* A, TreeNode* B) {
        return (A!=nullptr && B!=nullptr) && (recur(A, B) || isSubStructure(A->left, B) || isSubStructure(A->right, B));
    }

    bool recur(TreeNode* A, TreeNode* B){
        if(B==nullptr)
            return true;
        if(A==nullptr || A->val!=B->val)
            return false;
        return recur(A->left, B->left) && recur(A->right, B->right);
    }
};


```



# 面试题

## 实现一个trie树

要提供insert（插入一个word），search（查询，返回命中的word列表）（最好C++实现）



## 线段相交

https://blog.csdn.net/wlxsq/article/details/47356905

问题描述：最近阿里的某同学（阳阳）从阿里毕业了（实现了财富自由），但是他从小就有一个梦想，他想回到他的老家经营一个农场，因此就需要在农场设计一些沟渠用来排水。为了设计这个沟渠，他不惜花费重金请来了物理系毕业的大学同学（天天）来帮他设计整个农场的沟渠系统。假设每条构建都是一条折线（即有多条首尾相连的线段组成），由于阳阳特别相信风水（风水先生告诉他，他的农场的沟渠路线的相交点不能超过5个），由于天天设计的沟渠系统十分复杂，作为程序员的你，能否设计一个程序帮助阳阳判断，这个沟渠系统能否满足要求。

​         程序输入：

​            第一行：整数 N （表示多条沟渠）

​            第2-(N+1)行：第一个数M(沟渠折线的顶点，沟渠的线段数 = M -1), 后面接着 2 * M个float，每两个float表示一个点。

​            输出：bool：true(符合要求)， false（不符合要求）。

​        

​           程序输入示例：

​         2

​         4 1.7 1.8 2.4 2.9 3.8 4.5  5.9 7.0

​         3 1.0 1.0 2.0 1.0 2.0 8.0          



## 质串

​      假设一个字符串由n个字符构成，字符只能是a或者b，如果一个字符串能由他的某个子串重复多次拼接而成，那么这种串就被命名为 "复数串"， 否则就被命名为 "质串"。

​     例如：abab 为复数串（因为它可以有ab重复2次拼接二次） abba为质串。

​    请你设计一个程序，判断一个长度为n的串，有多少个是『质串』,最后的结果 mod 2022 。

例如：n = 1,  那么长度为1的所有串中，有2个质串，分别是 a 和 b。

​            n = 2,  那么长度为2的所有串中，有2个质串，分别是 ab 和 ba。

​            n = 3, 那么长度为3的所有串中，有6个质串，分别是（aab, aba, baa, abb, bab, bba）.

判断一个数是否为质数

```cpp
bool isPrime(int n){
  if(n<=1)
    return false;
  for(int=2; i*i<=n; i++)
    if(n%i==0) 
      return false;
  return true;
}
```

素数筛(埃氏)

```cpp
int prime[n+1], isprime[n+1];
int sieve(int n){
  int p=0;
  for(int i=0; i<=n; i++)
    isprime[i] = 1;
  isprime[0] = 0;
  isprime[1] = 1;
  for(int i=2; i<=n; i++){
    if(isprime[i]){
      prime[p++] = i;
      for(int j=2*i; j<=n; j+=i)
        isprime[j] = 0;
    } 
  }
  return p;
}
```

欧拉筛

```cpp
const int maxn = 100;
int prime[maxn] {0};
int vis[maxn] {0};//0表示质数

void eulasieve(){
  for(int i=2; i<maxn; i++){
    if(!vis[i])
      prime[++prime[0]] = i;
    for(int j=1; j<=prime[0]&&i*prime[j]<=maxn; j++){
      vis[i*prime[j]] = 1;
      if(i%prime[j] == 0)
        break;
    }
  }
}
```



# 其他 leetcode

## 点灯

每个点是一个按钮，每个按钮里面有一个小灯。如上图，红色代表灯亮，白色代表灯灭。每当按下按钮，此按钮的灯以及其上下左右四个方向按钮的灯状态会改变（如果原来灯亮则灯灭，如果原来灯灭则灯亮）。如果小张通过按按钮将灯全部熄灭则能可以打开箱子。

现在小张给你一些密码锁的状态，请你告诉他最少按几次按钮能够把灯全部熄灭。

Input

第一行两个整数n, m

接下来n行，每行一个长度为m的01字符串，0表示灯初始状态灭，1表示灯初始状态亮。

Output

一行一个整数，表示最少按几次按钮可以把灯全部熄灭。
```cpp

#include <vector>
#include <string>
#include <iostream>
using namespace std;
#define MAX 1024
void change(int i, int j, vector<vector<bool>> &map);
void changefirstline(vector<vector<bool>> map, int j, int count);
int dfs(vector<vector<bool>> &map, int count);
int ans = MAX;

void changefirstline(vector<vector<bool>> map, int j, int count){
    if(j<map[0].size()){
        changefirstline(map, j+1, count);
        change(0, j, map);
        changefirstline(map, j+1, count+1);
    }
    else
        ans = min(dfs(map, count), ans);
    
}

int dfs(vector<vector<bool>> &map, int count){
    int n = map.size();
    int m = map[0].size();

    for(int i=0; i<n-1; i++){
        for(int j=0; j<m; j++){
            if(map[i][j]){
                change(i+1, j, map);
                ++count;
            }
        }
    }
    for(int j=0; j<m; j++)
        if(map[n-1][j])
            return MAX;
    return count;
 
}

void change(int i, int j, vector<vector<bool>> &map){
    int n = map.size();
    int m = map[0].size();
    
    map[i][j] = !map[i][j];
    vector<pair<int, int>> direction{{1,0}, {-1,0}, {0,1}, {0,-1}};
    for(auto p : direction){
        int newi = i+p.first;
        int newj = j+p.second;
        
        if(newi>=n || newi<0 || newj>=m || newj<0)
            continue;
        map[newi][newj] = !map[newi][newj];
    }
}


int main(){
    int n, m;
    
    scanf("%d %d\n", &n, &m);
    vector<vector<bool>> map(n, vector<bool>(m, false));
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            char c = getchar();
            if(c=='1')
                map[i][j] = true;
        }
        getchar();
    }
    
    changefirstline(map, 0, 0);
    cout<<ans<<endl;
}

```

## 二进制加法

和十进制不同的是：二进制运算“逢二进一”。下面举一个二进制加法的运算实例:


   11101

   \-  110

--------
  100011
下面请你模拟这个过程。

Input
第一行输入一个正整数 T 表示接下来有 T 组数据；
接下来 T 行，每行输入两个二进制串 a 和 b 中间用空格隔开，并且没有前导 0。
Output
对于每组数据，请按模拟二进制加法，按题目描述的格式输出正确的运算结果，注意换行，没有多余的空格和换行。

```cpp

#include <vector>
#include <string>
#include <iostream>
using namespace std;

struct tri{
    string var1;
    string var2;
    string res;
};

void calculate(tri &t);
string fillblank(const string& s, int len);
void print(const tri &t);
void rev(string &str);

void rev(string &str){
    int len = str.length();
    int n = len-1;
    int i = 0;
    while(i<=n){
        //Using the swap method to switch values at each index
        swap(str[i],str[n]);
        n = n-1;
        i = i+1;
    }
}

void calculate(tri &t){
    if(!(t.res.empty()))
        return;

    string::reverse_iterator i1 = t.var1.rbegin();
    string::reverse_iterator i2 = t.var2.rbegin();
    int bit1=0;
    int bit2=0;
    int bitres = 0;
    int carry = 0;
    while(i1!=t.var1.rend() || i2!=t.var2.rend() || carry!=0){
        if(i1==t.var1.rend())
            bit1 = 0;
        else{
            bit1 = *i1-48;
            i1++;
        }
        
        if(i2==t.var2.rend())
            bit2 = 0;
        else{
            bit2 = *i2-48;
            i2++;
        }
        bitres = (bit1+bit2+carry)%2;
        carry = (bit1+bit2+carry)>>1;
        
        t.res.push_back(bitres+48);

    }
    rev(t.res);
    return ;
}




void print(const tri &t){
    int len = t.res.size();
    string div(len+2, '-');
    string blank("  ");
    cout<<blank<<fillblank(t.var1, len)<<endl;
    cout<<"+ "<<fillblank(t.var2, len)<<endl;
    cout<<div<<endl;
    cout<<blank<<t.res<<endl;
    
}



string fillblank(const string& s, int len){
    string res = s;
    while(res.size()<len)
        res.insert(0, " ");
    return res;
}

int main(){
    int t;
    cin>>t;
    vector<tri> v(t);
    
    for(int i=0; i<t; i++){
        cin>>v[i].var1 >>v[i].var2;
        calculate(v[i]);
    }
    
    for(auto i:v)
        print(i);
}
```



## 大实数加减法

```cpp

#include <vector>
#include <string>
#include <iostream>
using namespace std;

struct tri{
    string var1;
    string var2;
    string res;
};
void calculate(tri &tr);
void print(tri t);
void rev(string &str);

void rev(string &str){
    int len = str.length();
    int n = len-1;
    int i = 0;
    while(i<=n){
        //Using the swap method to switch values at each index
        swap(str[i],str[n]);
        n = n-1;
        i = i+1;
    }
}

void fit(string& str, int len_i, int len_f){
//    while(str.front()=='0')
//        str.erase(0, 1);
    //cout<<"?"<<str<<"?"<<len_i<<len_f<<endl;
    if(str.front()=='.'||str.empty())
        str.insert(0, "0");
    int dot = str.find('.')==-1 ? str.size() : str.find('.');
    int i = len_i - dot;
    for(int j=0; j<i; j++){
        str.insert(0, " ");
    }
    int back0 = len_i+len_f - str.size();
    if(len_f!=0)
        back0+=1;
    for(int j=0; j<back0; j++){
        str.append(" ");
    }
    //cout<<"!"<<str<<endl;
}

void calculate(tri &tr){
    if(!(tr.res.empty()))
        return;
    tri t = tr;
    
    int dot1 = t.var1.find(".");
    if(dot1==-1){
        dot1 = t.var1.size();
        t.var1.push_back('.');
    }
    int dot2 = t.var2.find(".");
    if(dot2==-1){
        dot2 = t.var2.size();
        t.var2.push_back('.');
    }
    string &s = dot1<dot2 ? t.var1 : t.var2;
    for(int i=0; i<abs(dot1-dot2); i++){
        s.insert(0, "0");
    }
    string &s2 = t.var1.size()<t.var2.size() ? t.var1 : t.var2;
    while(t.var1.size()!=t.var2.size()){
        s2.push_back('0');
    }
    
    string::reverse_iterator i1 = t.var1.rbegin();
    string::reverse_iterator i2 = t.var2.rbegin();
    int bit1=0;
    int bit2=0;
    int bitres = 0;
    int carry = 0;
    while(i1!=t.var1.rend() && i2!=t.var2.rend()){
        if(*i1=='.'){
            t.res.push_back('.');
            i1++;
            i2++;
            continue;
        }
        bit1 = *i1-48;
        i1++;
        
        bit2 = *i2-48;
        i2++;
        
        bitres = (bit1+bit2+carry)%10;
        carry = (bit1+bit2+carry)/10;
        t.res.push_back(bitres+48);
    }
    t.res.push_back(carry+48);
    rev(t.res);
    while(t.res.front()=='0')
        t.res.erase(0, 1);
    if(t.res.front()=='.')
        t.res.insert(0, "0");
    if(t.res.back()=='.')
        t.res.pop_back();
    tr.res = t.res;
    return ;
}

void print(tri t){
    int len_i = 0;
    int len_f = 0;
    
    if(t.var1.find('.') == -1)
        len_i = t.var1.size();
    if(t.var2.find('.') == -1)
        len_i = max(len_i, (int)t.var2.size());
    if(t.res.find('.') == -1)
        len_i = max(len_i, (int)t.res.size());
    else
        len_f = t.res.size() - t.res.find('.')-1;
    len_i = max(len_i , (int)t.var1.find('.'));
    len_i = max(len_i, (int)t.var2.find('.'));
    len_i = max(len_i, (int)t.res.find('.'));
    
    
    fit(t.var1, len_i, len_f);
    fit(t.var2, len_i, len_f);
    fit(t.res, len_i, len_f);
    string div(t.res.size()+3, '-');
    string blank("   ");
    cout<<blank<<t.var1<<endl;
    cout<<"+  "<<t.var2<<endl;
    cout<<div<<endl;
    string s = t.res;
    cout<<blank<<s<<endl;
    
}

int main(){
    tri t;
    cin>>t.var1 >>t.var2;
    calculate(t);
    print(t);
}

```

```cpp

#include <vector>
#include <string>
#include <iostream>
using namespace std;

const string target = "fattyhappy";
const int length = 10;

pair<int, int> check(int index, string str){
    pair<int, int> ans(-1, -1);
    string sub = str.substr(index, length);
    int count = 0;
    vector<int> v;
    for(int i=0; i<length; i++){
        if(sub[i] != target[i]){
            count++;
            v.push_back(i);
        }
    }

    if(count==0)
        return pair<int, int>(2+index, 3+index);
    else if (count==1){
        for(int i=0; i<str.size(); i++){
            if(i>=index && i<index+length)
                continue;
            if(str[i] == target[v.front()]){
                ans.first = min(i, index+v.front());
                ans.second = max(i, index+v.front());
                return ans;
            }
        }
    }
    else if(count==2){
        swap(sub[v[0]], sub[v[1]]);
        if(sub == target){
            ans.first = v[0]+index;
            ans.second = v[1]+index;
            return ans;
        }
    }
    return ans;
}

pair<int, int> findexchange(string str){
    pair<int, int> ans;
    ans.first = -1;
    int len = str.size();
    for(int i=0; i+length<=len; i++){
        ans = check(i, str);
        if(ans.first!=-1){
            return ans;
        }
        
    }
    return ans;
}


int main(){
    int t = 0;
    cin>>t;
    vector<string> v(t);
    for(int i=0; i<t; i++)
        cin>>v[i];
    for(int i=0; i<t; i++){
        pair<int, int> ans = findexchange(v[i]);
        if(ans.first == -1)
            cout<<"-1"<<endl;
        else
            cout<<ans.first+1<<" "<<ans.second+1<<endl;
    }
    //    pair<int, int> ans = findexchange("fattyhappyasdasdas");
    //    cout<<ans.first+1<<" "<<ans.second+1<<endl;
    //    return 0;
    
}

```



```cpp

#include <vector>
#include <string>
#include <iostream>
#include <stack>
using namespace std;


enum direction{LEFT=-1, RIGHT=1, EMPTY=0};
struct brid{
    bool valid=false;
    direction d;
    int count=0;
    string str;
};



void rev(string &str){
    int len = str.length();
    int n = len-1;
    int i = 0;
    while(i<=n){
        //Using the swap method to switch values at each index
        swap(str[i],str[n]);
        n = n-1;
        i = i+1;
    }
}




void check(brid& b){
    string& str = b.str;
    stack<char> s;
  int length = str.size();
    for(int i=0; i<length; i++){
        if(s.empty())
            s.push(str[i]);
        else{
            if(s.top()=='(' && str[i]==')')
                s.pop();
            else
                s.push(str[i]);
        }
    }
    str.clear();
    while(!s.empty()){
        str.push_back(s.top());
        s.pop();
    }
    rev(str);
    
    b.valid = true;
    if(b.str.find('(')!=-1){
        b.d = LEFT;
        if(b.str.find(')')!=-1){
            b.valid = false;
            return ;
        }
    }
    else
        b.d = RIGHT;
    if(b.str.empty())
        b.d = EMPTY;
    b.count = b.str.size();
}

int main(){
    int t = 0;
    cin>>t;
    vector<string> v(t);
    vector<brid> vnew;
    int ans = 0;
    for(int i=0; i<t; i++){
        cin>>v[i];
        brid b;
        b.str = v[i];
        check(b);
        if(b.valid)
            vnew.push_back(b);
    }
    
    t = vnew.size();
    for(int i=0; i<t; i++){
        for(int j=i+1; j<t; j++){
            if(vnew[i].valid && vnew[j].valid&&(vnew[i].d + vnew[j].d) == 0 && vnew[i].count == vnew[j].count )
            {
                vnew[i].valid = false;
                vnew[j].valid = false;
                ans++;
            }
        }
    }
    cout<<ans<<endl;
    
}




```

## 任务安排

![截屏2022-08-27 22.50.56](https://tva1.sinaimg.cn/large/e6c9d24ely1h5lpnu7a7mj21300koaco.jpg)

```c
#include<stdio.h>
#include<stdlib.h>

#define N 500000

typedef struct timelimit
{
    long long int s;
    long long int e;
}timelimit;
timelimit T[N];

int compare(const void* a,const void* b)
{
    return (*(timelimit*)a).e-(*(timelimit*)b).e;
}

int main()
{
    long long int n, ans = 0, i;
    scanf("%lld",&n);
    for(i=0;i<n;i++)
    {
        scanf("%lld",&(T[i].s));
        scanf("%lld",&(T[i].e));
    }
    qsort (T, n, sizeof(timelimit), &compare);
    long long int end = 0;
  
    for(i=0;i<=n-1;i++)
    {
        if(T[i].s>=end)
        {
            end = T[i].e;
            ans=ans+1;
        }
    }
    
    printf("%lld\n",ans);
    return 0;
}

```

## 刷房子

```cpp
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;
typedef struct building_{
    int h;
    int c;
}building;

int main(){
    int n;
    cin>>n;
    vector<vector<int>> ans(n);
    for(int i=0; i<n; i++){
        int amount;
        cin>>amount;
        vector<building> buildings(amount);
        for(int j=0; j<amount; j++)
            cin>>buildings[j].c;
        for(int j=0; j<amount; j++)
            cin>>buildings[j].h;
        
        stack<building> s;
        vector<vector<int>> colors(amount);
        ans[i].push_back(1);
        colors[0].push_back(buildings[0].c);
        
        
        for(int j=0; j<amount; j++){
            int tallest = j;
            vector<int> newcolor;
            int k;
            for(k=j-1; k>=0; k--){
                if(buildings[k].h<=buildings[tallest].h){

                }
                else{
                    colors[j] = colors[k];
                    if(find(colors[j].begin(), colors[j].end(), buildings[j].c)==colors[j].end()){
                        colors[j].push_back(buildings[k].c);
                    }
                    break;
                }
            }
            
            if(k==-1)
                colors[j].push_back(buildings[j].c);
            
            ans[i].push_back(colors[j].size());
        }

    }
    
    
    for(int i=0; i<ans.size(); i++){
        for(int j=0; j<ans[i].size()-1; j++){
            cout<<ans[i][j]<<" ";
        }
        cout<<ans[i].back()<<endl;
    }
        
    
    
    
}
//        for(int j=0; j<amount; j++)
//            cout<<buildings[j].c<<"?"<<buildings[j].h<<endl;

```





# 简单难度题目合集

这里的题目难度比较小， 大多是模拟题，或者是很容易看出解法的题目，另外简单题目一般使用暴力法都是可以解决的。 这个时候只有看一下数据范围，思考下你的算法复杂度就行了。

当然也不排除很多 hard 题目也可以暴力模拟，大家平时多注意数据范围即可。

以下是我列举的经典题目（带 91 字样的表示出自 **91 天学算法**活动）：

## [面试题 17.12. BiNode](https://github.com/azl397985856/leetcode/blob/master/problems/binode-lcci.md) 👍
## [0001. 两数之和](https://github.com/azl397985856/leetcode/blob/master/problems/1.two-sum.md)

unordered_map

## [0020. 有效的括号](https://github.com/azl397985856/leetcode/blob/master/problems/20.valid-parentheses.md)

## [0021. 合并两个有序链表](https://github.com/azl397985856/leetcode/blob/master/problems/21.merge-two-sorted-lists.md)

递归?

## [0026. 删除排序数组中的重复项](https://github.com/azl397985856/leetcode/blob/master/problems/26.remove-duplicates-from-sorted-array.md)

使用快慢指针来记录遍历的坐标。

- 开始时这两个指针都指向第一个数字
- 如果两个指针指的数字相同，则快指针向前走一步
- 如果不同，则两个指针都向前走一步
- 当快指针走完整个数组后，慢指针当前的坐标加 1 就是数组中不同数字的个数

## [0053. 最大子序和](https://github.com/azl397985856/leetcode/blob/master/problems/53.maximum-sum-subarray-cn.md)

前缀和, 动态规划

## [0066. 加一](https://github.com/azl397985856/leetcode/blob/master/problems/66.plus-one.md) 91
## [0088. 合并两个有序数组](https://github.com/azl397985856/leetcode/blob/master/problems/88.merge-sorted-array.md)
## [0101. 对称二叉树](https://github.com/azl397985856/leetcode/blob/master/problems/101.symmetric-tree.md)

how to recursive

## [0104. 二叉树的最大深度](https://github.com/azl397985856/leetcode/blob/master/problems/104.maximum-depth-of-binary-tree.md)

try iteration

## [0108. 将有序数组转换为二叉搜索树](https://github.com/azl397985856/leetcode/blob/master/problems/108.convert-sorted-array-to-binary-search-tree.md)

二叉搜索树是一种节点值之间具有一定数量级次序的二叉树，对于树中每个节点：

- 若其左子树存在，则其左子树中每个节点的值都不大于该节点值；
- 若其右子树存在，则其右子树中每个节点的值都不小于该节点值。

## [0121. 买卖股票的最佳时机](https://github.com/azl397985856/leetcode/blob/master/problems/121.best-time-to-buy-and-sell-stock.md)



## [0122. 买卖股票的最佳时机 II](https://github.com/azl397985856/leetcode/blob/master/problems/122.best-time-to-buy-and-sell-stock-ii.md)
## [0125. 验证回文串](https://github.com/azl397985856/leetcode/blob/master/problems/125.valid-palindrome.md)
## [0136. 只出现一次的数字](https://github.com/azl397985856/leetcode/blob/master/problems/136.single-number.md)

异或

## [0155. 最小栈](https://github.com/azl397985856/leetcode/blob/master/problems/155.min-stack.md) 👍

???

## [0160. 相交链表](https://github.com/azl397985856/leetcode/blob/master/problems/160.Intersection-of-Two-Linked-Lists.md) 91

unordered_map count, insert

- 例如使用 a, b 两个指针分别指向 A, B 这两条链表, 两个指针相同的速度向后移动,
- 当 a 到达链表的尾部时,重定位到链表 B 的头结点
- 当 b 到达链表的尾部时,重定位到链表 A 的头结点。
- a, b 指针相遇的点为相交的起始节点，否则没有相交点

## [0167. 两数之和 II 输入有序数组](https://github.com/azl397985856/leetcode/blob/master/problems/167.two-sum-ii-input-array-is-sorted.md)
## [0169. 多数元素](https://github.com/azl397985856/leetcode/blob/master/problems/169.majority-element.md)

多数元素是指在数组中出现次数 **大于** `⌊ n/2 ⌋` 的元素。

投票算法



## [0172. 阶乘后的零](https://github.com/azl397985856/leetcode/blob/master/problems/172.factorial-trailing-zeroes.md)

trick count 5

## [0190. 颠倒二进制位](https://github.com/azl397985856/leetcode/blob/master/problems/190.reverse-bits.md)

位运算

## [0191. 位 1 的个数](https://github.com/azl397985856/leetcode/blob/master/problems/191.number-of-1-bits.md)

就是`n & (n - 1)` 可以`消除` n 最后的一个 1 的原理。

## [0198. 打家劫舍](https://github.com/azl397985856/leetcode/blob/master/problems/198.house-robber.md)
## [0203. 移除链表元素](https://github.com/azl397985856/leetcode/blob/master/problems/203.remove-linked-list-elements.md)

重要※

## [0206. 反转链表](https://github.com/azl397985856/leetcode/blob/master/problems/206.reverse-linked-list.md)

⭐️

## [0219. 存在重复元素 II](https://github.com/azl397985856/leetcode/blob/master/problems/219.contains-duplicate-ii.md)

hash

## [0226. 翻转二叉树](https://github.com/azl397985856/leetcode/blob/master/problems/226.invert-binary-tree.md)

迭代

## [0232. 用栈实现队列](https://github.com/azl397985856/leetcode/blob/master/problems/232.implement-queue-using-stacks.md) 👍 91



## [0263. 丑数](https://github.com/azl397985856/leetcode/blob/master/problems/263.ugly-number.md)

use for and function call

## [0283. 移动零](https://github.com/azl397985856/leetcode/blob/master/problems/283.move-zeroes.md)



## [0342. 4 的幂](https://github.com/azl397985856/leetcode/blob/master/problems/342.power-of-four.md) 👍
## [0349. 两个数组的交集](https://github.com/azl397985856/leetcode/blob/master/problems/349.intersection-of-two-arrays.md)
## [0371. 两整数之和](https://github.com/azl397985856/leetcode/blob/master/problems/371.sum-of-two-integers.md)
## [401. 二进制手表](https://github.com/azl397985856/leetcode/blob/master/problems/401.binary-watch.md)
## [0437. 路径总和 III](https://github.com/azl397985856/leetcode/blob/master/problems/437.path-sum-iii.md)

!

## [0455. 分发饼干](https://github.com/azl397985856/leetcode/blob/master/problems/455.AssignCookies.md)
## [0504. 七进制数](https://github.com/azl397985856/leetcode/blob/master/problems/504.base-7.md)
## [0575. 分糖果](https://github.com/azl397985856/leetcode/blob/master/problems/575.distribute-candies.md)
## [0665. 非递减数列](https://github.com/azl397985856/leetcode/blob/master/problems/665.non-decreasing-array.md)
## [821. 字符的最短距离](https://github.com/azl397985856/leetcode/blob/master/problems/821.shortest-distance-to-a-character.md) 91
## [0874. 模拟行走机器人](https://github.com/azl397985856/leetcode/blob/master/problems/874.walking-robot-simulation.md)
## [1128. 等价多米诺骨牌对的数量](https://github.com/azl397985856/leetcode/blob/master/problems/1128.number-of-equivalent-domino-pairs.md)
## [1260. 二维网格迁移](https://github.com/azl397985856/leetcode/blob/master/problems/1260.shift-2d-grid.md)
## [1332. 删除回文子序列](https://github.com/azl397985856/leetcode/blob/master/problems/1332.remove-palindromic-subsequences.md)

# 中等难度题目合集

中等题目是力扣比例最大的部分，因此这部分我的题解也是最多的。 大家不要太过追求难题，先把中等难度题目做熟了再说。

这部分的题目要不需要我们挖掘题目的内含信息， 将其抽象成简单题目。 要么是一些写起来比较麻烦的题目， 一些人编码能力不行就挂了。因此大家一定要自己做， 即使看了题解”会了“，也要自己码一遍。自己不亲自写一遍，里面的细节永远不知道。

以下是我列举的经典题目（带 91 字样的表示出自 **91 天学算法**活动）：

## [面试题 17.09. 第 k 个数](https://github.com/azl397985856/leetcode/blob/master/problems/get-kth-magic-number-lcci.md)
## [面试题 17.23. 最大黑方阵](https://github.com/azl397985856/leetcode/blob/master/problems/max-black-square-lcci.md)
## [面试题 16.16. 部分排序](https://github.com/azl397985856/leetcode/blob/master/problems/sub-sort-lcci.md)
## [Increasing Digits](https://github.com/azl397985856/leetcode/blob/master/problems/Increasing-Digits.md) 👍
## [Longest Contiguously Strictly Increasing Sublist After Deletion](https://github.com/azl397985856/leetcode/blob/master/problems/Longest-Contiguously-Strictly-Increasing-Sublist-After-Deletion.md) 👍
## [Consecutive Wins](https://github.com/azl397985856/leetcode/blob/master/problems/consecutive-wins.md)
## [Sort-String-by-Flipping](https://github.com/azl397985856/leetcode/blob/master/problems/Sort-String-by-Flipping.md)
## [Number of Substrings with Single Character Difference](https://github.com/azl397985856/leetcode/blob/master/problems/Number-of-Substrings-with-Single-Character-Difference.md)
## [Bus Fare](https://github.com/azl397985856/leetcode/blob/master/problems/Bus-Fare.md) 👍
## [Minimum Dropping Path Sum](https://github.com/azl397985856/leetcode/blob/master/problems/Minimum-Dropping-Path-Sum.md)
## [Longest-Matrix-Path-Length](https://github.com/azl397985856/leetcode/blob/master/problems/Longest-Matrix-Path-Length.md)
## [Every Sublist Min Sum](https://github.com/azl397985856/leetcode/blob/master/problems/Every-Sublist-Min-Sum.md)
## [Maximize the Number of Equivalent Pairs After Swaps](https://github.com/azl397985856/leetcode/blob/master/problems/Maximize-the-Number-of-Equivalent-Pairs-After-Swaps.md)
## [0002. 两数相加](https://github.com/azl397985856/leetcode/blob/master/problems/2.add-two-numbers.md)
## [0003. 无重复字符的最长子串](https://github.com/azl397985856/leetcode/blob/master/problems/3.longest-substring-without-repeating-characters.md)
## [0005. 最长回文子串](https://github.com/azl397985856/leetcode/blob/master/problems/5.longest-palindromic-substring.md)
## [0011. 盛最多水的容器](https://github.com/azl397985856/leetcode/blob/master/problems/11.container-with-most-water.md)
## [0015. 三数之和](https://github.com/azl397985856/leetcode/blob/master/problems/15.3sum.md)
## [0017. 电话号码的字母组合](https://github.com/azl397985856/leetcode/blob/master/problems/17.Letter-Combinations-of-a-Phone-Number.md)
## [0019. 删除链表的倒数第 N 个节点](https://github.com/azl397985856/leetcode/blob/master/problems/19.removeNthNodeFromEndofList.md)
## [0022. 括号生成](https://github.com/azl397985856/leetcode/blob/master/problems/22.generate-parentheses.md)
## [0024. 两两交换链表中的节点](https://github.com/azl397985856/leetcode/blob/master/problems/24.swapNodesInPairs.md)
## [0029. 两数相除](https://github.com/azl397985856/leetcode/blob/master/problems/29.divide-two-integers.md)
## [0031. 下一个排列](https://github.com/azl397985856/leetcode/blob/master/problems/31.next-permutation.md)
## [0033. 搜索旋转排序数组](https://github.com/azl397985856/leetcode/blob/master/problems/33.search-in-rotated-sorted-array.md)
## [0039. 组合总和](https://github.com/azl397985856/leetcode/blob/master/problems/39.combination-sum.md)
## [0040. 组合总和 II](https://github.com/azl397985856/leetcode/blob/master/problems/40.combination-sum-ii.md)
## [0046. 全排列](https://github.com/azl397985856/leetcode/blob/master/problems/46.permutations.md)
## [0047. 全排列 II](https://github.com/azl397985856/leetcode/blob/master/problems/47.permutations-ii.md)
## [0048. 旋转图像](https://github.com/azl397985856/leetcode/blob/master/problems/48.rotate-image.md)
## [0049. 字母异位词分组](https://github.com/azl397985856/leetcode/blob/master/problems/49.group-anagrams.md)
## [0050. Pow(x, n)](https://github.com/azl397985856/leetcode/blob/master/problems/50.pow-x-n.md) 👍
## [0055. 跳跃游戏](https://github.com/azl397985856/leetcode/blob/master/problems/55.jump-game.md)
## [0056. 合并区间](https://github.com/azl397985856/leetcode/blob/master/problems/56.merge-intervals.md)
## [0060. 第 k 个排列](https://github.com/azl397985856/leetcode/blob/master/problems/60.permutation-sequence.md) 👍
## [0061. 旋转链表](https://github.com/azl397985856/leetcode/blob/master/problems/61.Rotate-List.md) 91
## [0062. 不同路径](https://github.com/azl397985856/leetcode/blob/master/problems/62.unique-paths.md)
## [0073. 矩阵置零](https://github.com/azl397985856/leetcode/blob/master/problems/73.set-matrix-zeroes.md)
## [0075. 颜色分类](https://github.com/azl397985856/leetcode/blob/master/problems/75.sort-colors.md) 👍
## [0078. 子集](https://github.com/azl397985856/leetcode/blob/master/problems/78.subsets.md)
## [0079. 单词搜索](https://github.com/azl397985856/leetcode/blob/master/problems/79.word-search.md)
## [0080. 删除排序数组中的重复项 II](https://github.com/azl397985856/leetcode/blob/master/problems/80.remove-duplicates-from-sorted-array-ii.md)
## [0086. 分隔链表](https://github.com/azl397985856/leetcode/blob/master/problems/86.partition-list.md)
## [0090. 子集 II](https://github.com/azl397985856/leetcode/blob/master/problems/90.subsets-ii.md)
## [0091. 解码方法](https://github.com/azl397985856/leetcode/blob/master/problems/91.decode-ways.md)
## [0092. 反转链表 II](https://github.com/azl397985856/leetcode/blob/master/problems/92.reverse-linked-list-ii.md)
## [0094. 二叉树的中序遍历](https://github.com/azl397985856/leetcode/blob/master/problems/94.binary-tree-inorder-traversal.md) 👍
## [0095. 不同的二叉搜索树 II](https://github.com/azl397985856/leetcode/blob/master/problems/95.unique-binary-search-trees-ii.md)
## [0096. 不同的二叉搜索树](https://github.com/azl397985856/leetcode/blob/master/problems/96.unique-binary-search-trees.md)
## [0098. 验证二叉搜索树](https://github.com/azl397985856/leetcode/blob/master/problems/98.validate-binary-search-tree.md)
## [0102. 二叉树的层序遍历](https://github.com/azl397985856/leetcode/blob/master/problems/102.binary-tree-level-order-traversal.md)
## [0103. 二叉树的锯齿形层次遍历](https://github.com/azl397985856/leetcode/blob/master/problems/103.binary-tree-zigzag-level-order-traversal.md)
## [0113. 路径总和 II](https://github.com/azl397985856/leetcode/blob/master/problems/113.path-sum-ii.md)
## [0129. 求根到叶子节点数字之和](https://github.com/azl397985856/leetcode/blob/master/problems/129.sum-root-to-leaf-numbers.md) 👍
## [0130. 被围绕的区域](https://github.com/azl397985856/leetcode/blob/master/problems/130.surrounded-regions.md)
## [0131. 分割回文串](https://github.com/azl397985856/leetcode/blob/master/problems/131.palindrome-partitioning.md)
## [0139. 单词拆分](https://github.com/azl397985856/leetcode/blob/master/problems/139.word-break.md)
## [0144. 二叉树的前序遍历](https://github.com/azl397985856/leetcode/blob/master/problems/144.binary-tree-preorder-traversal.md)
## [0147. 对链表进行插入排序](https://github.com/azl397985856/leetcode/blob/master/problems/147.insertion-sort-list.md)
## [0150. 逆波兰表达式求值](https://github.com/azl397985856/leetcode/blob/master/problems/150.evaluate-reverse-polish-notation.md)
## [0152. 乘积最大子数组](https://github.com/azl397985856/leetcode/blob/master/problems/152.maximum-product-subarray.md)
## [0153. 寻找旋转排序数组中的最小值](https://github.com/azl397985856/leetcode/blob/master/problems/153.find-minimum-in-rotated-sorted-array.md)
## [0199. 二叉树的右视图](https://github.com/azl397985856/leetcode/blob/master/problems/199.binary-tree-right-side-view.md) 👍
## [0200. 岛屿数量](https://github.com/azl397985856/leetcode/blob/master/problems/200.number-of-islands.md) 👍
## [0201. 数字范围按位与](https://github.com/azl397985856/leetcode/blob/master/problems/201.bitwise-and-of-numbers-range.md)
## [0208. 实现 Trie (前缀树)](https://github.com/azl397985856/leetcode/blob/master/problems/208.implement-trie-prefix-tree.md)
## [0209. 长度最小的子数组](https://github.com/azl397985856/leetcode/blob/master/problems/209.minimum-size-subarray-sum.md)
## [0211. 添加与搜索单词 ## 数据结构设计](https://github.com/azl397985856/leetcode/blob/master/problems/211.add-and-search-word-data-structure-design.md)
## [0215. 数组中的第 K 个最大元素](https://github.com/azl397985856/leetcode/blob/master/problems/215.kth-largest-element-in-an-array.md)
## [0220. 存在重复元素 III](https://github.com/azl397985856/leetcode/blob/master/problems/220.contains-duplicate-iii.md)
## [0221. 最大正方形](https://github.com/azl397985856/leetcode/blob/master/problems/221.maximal-square.md)
## [0227. 基本计算器 II](https://github.com/azl397985856/leetcode/blob/master/problems/227.basic-calculator-ii.md)
## [0229. 求众数 II](https://github.com/azl397985856/leetcode/blob/master/problems/229.majority-element-ii.md)
## [0230. 二叉搜索树中第 K 小的元素](https://github.com/azl397985856/leetcode/blob/master/problems/230.kth-smallest-element-in-a-bst.md)
## [0236. 二叉树的最近公共祖先](https://github.com/azl397985856/leetcode/blob/master/problems/236.lowest-common-ancestor-of-a-binary-tree.md)
## [0238. 除自身以外数组的乘积](https://github.com/azl397985856/leetcode/blob/master/problems/238.product-of-array-except-self.md)
## [0240. 搜索二维矩阵 II](https://github.com/azl397985856/leetcode/blob/master/problems/240.search-a-2-d-matrix-ii.md)
## [0279. 完全平方数](https://github.com/azl397985856/leetcode/blob/master/problems/279.perfect-squares.md)
## [0309. 最佳买卖股票时机含冷冻期](https://github.com/azl397985856/leetcode/blob/master/problems/309.best-time-to-buy-and-sell-stock-with-cooldown.md)
## [0322. 零钱兑换](https://github.com/azl397985856/leetcode/blob/master/problems/322.coin-change.md) 👍
## [0328. 奇偶链表](https://github.com/azl397985856/leetcode/blob/master/problems/328.odd-even-linked-list.md)
## [0331. 验证二叉树的前序序列化](https://github.com/azl397985856/leetcode/blob/master/problems/328.odd-even-linked-list.md)
## [0334. 递增的三元子序列](https://github.com/azl397985856/leetcode/blob/master/problems/334.increasing-triplet-subsequence.md)
## [0337. 打家劫舍 III](https://github.com/azl397985856/leetcode/blob/master/problems/337.house-robber-iii.md)
## [0343. 整数拆分](https://github.com/azl397985856/leetcode/blob/master/problems/343.integer-break.md)
## [0365. 水壶问题](https://github.com/azl397985856/leetcode/blob/master/problems/365.water-and-jug-problem.md)
## [0378. 有序矩阵中第 K 小的元素](https://github.com/azl397985856/leetcode/blob/master/problems/378.kth-smallest-element-in-a-sorted-matrix.md)
## [0380. 常数时间插入、删除和获取随机元素](https://github.com/azl397985856/leetcode/blob/master/problems/380.insert-delete-getrandom-o1.md)
## [0385. 迷你语法分析器](https://github.com/azl397985856/leetcode/blob/master/problems/385.mini-parser.md)
## [0394. 字符串解码](https://github.com/azl397985856/leetcode/blob/master/problems/394.decode-string.md) 91
## [0416. 分割等和子集](https://github.com/azl397985856/leetcode/blob/master/problems/416.partition-equal-subset-sum.md)
## [0424. 替换后的最长重复字符](https://github.com/azl397985856/leetcode/blob/master/problems/424.longest-repeating-character-replacement.md)
## [0438. 找到字符串中所有字母异位词](https://github.com/azl397985856/leetcode/blob/master/problems/438.find-all-anagrams-in-a-string.md)
## [0445. 两数相加 II](https://github.com/azl397985856/leetcode/blob/master/problems/445.add-two-numbers-ii.md)
## [0454. 四数相加 II](https://github.com/azl397985856/leetcode/blob/master/problems/454.4-sum-ii.md)
## [0456. 132 模式](https://github.com/azl397985856/leetcode/blob/master/problems/456.132-pattern.md)
## [0457.457. 环形数组是否存在循环](https://github.com/azl397985856/leetcode/blob/master/problems/457.circular-array-loop.md)
## [0464. 我能赢么](https://github.com/azl397985856/leetcode/blob/master/problems/464.can-i-win.md)
## [0470. 用 Rand7() 实现 Rand10](https://github.com/azl397985856/leetcode/blob/master/problems/470.implement-rand10-using-rand7.md)
## [0473. 火柴拼正方形](https://github.com/azl397985856/leetcode/blob/master/problems/473.matchsticks-to-square.md) 👍
## [0494. 目标和](https://github.com/azl397985856/leetcode/blob/master/problems/494.target-sum.md)
## [0516. 最长回文子序列](https://github.com/azl397985856/leetcode/blob/master/problems/516.longest-palindromic-subsequence.md)
## [0513. 找树左下角的值](https://github.com/azl397985856/leetcode/blob/master/problems/513.find-bottom-left-tree-value.md) 91
## [0518. 零钱兑换 II](https://github.com/azl397985856/leetcode/blob/master/problems/518.coin-change-2.md)
## [0525. 连续数组](https://github.com/azl397985856/leetcode/blob/master/problems/525.contiguous-array.md)
## [0547. 朋友圈](https://github.com/azl397985856/leetcode/blob/master/problems/547.friend-circles.md)
## [0560. 和为 K 的子数组](https://github.com/azl397985856/leetcode/blob/master/problems/560.subarray-sum-equals-k.md)
## [0609. 在系统中查找重复文件](https://github.com/azl397985856/leetcode/blob/master/problems/609.find-duplicate-file-in-system.md)
## [0611. 有效三角形的个数](https://github.com/azl397985856/leetcode/blob/master/problems/611.valid-triangle-number.md) 👍
## [0673. 最长递增子序列的个数](https://github.com/azl397985856/leetcode/blob/master/problems/673.number-of-longest-increasing-subsequence.md)
## [0686. 重复叠加字符串匹配](https://github.com/azl397985856/leetcode/blob/master/problems/686.repeated-string-match.md)
## [0718. 最长重复子数组](https://github.com/azl397985856/leetcode/blob/master/problems/718.maximum-length-of-repeated-subarray.md)
## [0714. 买卖股票的最佳时机含手续费](https://github.com/azl397985856/leetcode/blob/master/problems/714.best-time-to-buy-and-sell-stock-with-transaction-fee.md)
## [0735. 行星碰撞](https://github.com/azl397985856/leetcode/blob/master/problems/735.asteroid-collision.md) 👍
## [0754. 到达终点数字](https://github.com/azl397985856/leetcode/blob/master/problems/754.reach-a-number.md)
## [0785. 判断二分图](https://github.com/azl397985856/leetcode/blob/master/problems/785.is-graph-bipartite.md)
## [0790. 多米诺和托米诺平铺](https://github.com/azl397985856/leetcode/blob/master/problems/790.domino-and-tromino-tiling.md)
## [0799. 香槟塔](https://github.com/azl397985856/leetcode/blob/master/problems/799.champagne-tower.md)
## [0801. 使序列递增的最小交换次数](https://github.com/azl397985856/leetcode/blob/master/problems/801.minimum-swaps-to-make-sequences-increasing.md)
## [0816. 模糊坐标](https://github.com/azl397985856/leetcode/blob/master/problems/816.ambiguous-coordinates.md)
## [0820. 单词的压缩编码](https://github.com/azl397985856/leetcode/blob/master/problems/820.short-encoding-of-words.md)
## [0838. 推多米诺](https://github.com/azl397985856/leetcode/blob/master/problems/838.push-dominoes.md)
## [0873. 最长的斐波那契子序列的长度](https://github.com/azl397985856/leetcode/blob/master/problems/873.length-of-longest-fibonacci-subsequence.md)
## [0875. 爱吃香蕉的珂珂](https://github.com/azl397985856/leetcode/blob/master/problems/875.koko-eating-bananas.md)
## [0877. 石子游戏](https://github.com/azl397985856/leetcode/blob/master/problems/877.stone-game.md)
## [0886. 可能的二分法](https://github.com/azl397985856/leetcode/blob/master/problems/886.possible-bipartition.md)
## [0898. 子数组按位或操作](https://github.com/azl397985856/leetcode/blob/master/problems/898.bitwise-ors-of-subarrays.md)
## [0900. RLE 迭代器](https://github.com/azl397985856/leetcode/blob/master/problems/900.rle-iterator.md)
## [0911. 在线选举](https://github.com/azl397985856/leetcode/blob/master/problems/911.online-election.md)
## [0912. 排序数组](https://github.com/azl397985856/leetcode/blob/master/problems/912.sort-an-array.md)
## [0932. 漂亮数组](https://github.com/azl397985856/leetcode/blob/master/problems/932.beautiful-array.md)
## [0935. 骑士拨号器](https://github.com/azl397985856/leetcode/blob/master/problems/935.knight-dialer.md)
## [0947. 移除最多的同行或同列石头](https://github.com/azl397985856/leetcode/blob/master/problems/947.most-stones-removed-with-same-row-or-column.md)
## [0959. 由斜杠划分区域](https://github.com/azl397985856/leetcode/blob/master/problems/959.regions-cut-by-slashes.md)
## [0978. 最长湍流子数组](https://github.com/azl397985856/leetcode/blob/master/problems/978.longest-turbulent-subarray.md)
## [0987. 二叉树的垂序遍历](https://github.com/azl397985856/leetcode/blob/master/problems/987.vertical-order-traversal-of-a-binary-tree.md) 91
## [1004. 最大连续 1 的个数 III](https://github.com/azl397985856/leetcode/blob/master/problems/1004.max-consecutive-ones-iii.md)
## [1011. 在 D 天内送达包裹的能力](https://github.com/azl397985856/leetcode/blob/master/problems/1011.capacity-to-ship-packages-within-d-days.md)
## [1014. 最佳观光组合](https://github.com/azl397985856/leetcode/blob/master/problems/1014.best-sightseeing-pair.md)
## [1015. 可被 K 整除的最小整数](https://github.com/azl397985856/leetcode/blob/master/problems/1015.smallest-integer-divisible-by-k.md)
## [1019. 链表中的下一个更大节点](https://github.com/azl397985856/leetcode/blob/master/problems/1019.next-greater-node-in-linked-list.md)
## [1020. 飞地的数量](https://github.com/azl397985856/leetcode/blob/master/problems/1020.number-of-enclaves.md)
## [1023. 驼峰式匹配](https://github.com/azl397985856/leetcode/blob/master/problems/1023.camelcase-matching.md)
## [1031. 两个非重叠子数组的最大和](https://github.com/azl397985856/leetcode/blob/master/problems/1031.maximum-sum-of-two-non-overlapping-subarrays.md)
## [1043. 分隔数组以得到最大和](https://github.com/azl397985856/leetcode/blob/master/problems/1043.partition-array-for-maximum-sum.md)
## [1104. 二叉树寻路](https://github.com/azl397985856/leetcode/blob/master/problems/1104.path-in-zigzag-labelled-binary-tree.md)
## [1129. 颜色交替的最短路径](https://github.com/azl397985856/leetcode/blob/master/problems/1129.shortest-path-with-alternating-colors.md)
## [1131.绝对值表达式的最大值](https://github.com/azl397985856/leetcode/blob/master/problems/1131.maximum-of-absolute-value-expression.md)
## [1138. 字母板上的路径](https://github.com/azl397985856/leetcode/blob/master/problems/1138.alphabet-board-path.md)
## [1186. 删除一次得到子数组最大和](https://github.com/azl397985856/leetcode/blob/master/problems/1186.maximum-subarray-sum-with-one-deletion.md)
## [1218. 最长定差子序列](https://github.com/azl397985856/leetcode/blob/master/problems/1218.longest-arithmetic-subsequence-of-given-difference.md)
## [1227. 飞机座位分配概率](https://github.com/azl397985856/leetcode/blob/master/problems/1227.airplane-seat-assignment-probability.md) 👍
## [1261. 在受污染的二叉树中查找元素](https://github.com/azl397985856/leetcode/blob/master/problems/1261.find-elements-in-a-contaminated-binary-tree.md)
## [1262. 可被三整除的最大和](https://github.com/azl397985856/leetcode/blob/master/problems/1262.greatest-sum-divisible-by-three.md)
## [1297. 子串的最大出现次数](https://github.com/azl397985856/leetcode/blob/master/problems/1297.maximum-number-of-occurrences-of-a-substring.md)
## [1310. 子数组异或查询](https://github.com/azl397985856/leetcode/blob/master/problems/1310.xor-queries-of-a-subarray.md)
## [1334. 阈值距离内邻居最少的城市](https://github.com/azl397985856/leetcode/blob/master/problems/1334.find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance.md)
## [1371.每个元音包含偶数次的最长子字符串](https://github.com/azl397985856/leetcode/blob/master/problems/1371.find-the-longest-substring-containing-vowels-in-even-counts.md)
## [1381. 设计一个支持增量操作的栈](https://github.com/azl397985856/leetcode/blob/master/problems/1381.design-a-stack-with-increment-operation.md) 91
## [1423. 可获得的最大点数](https://github.com/azl397985856/leetcode/blob/master/problems/1423.maximum-points-you-can-obtain-from-cards.md)
## [1438. 绝对差不超过限制的最长连续子数组](https://github.com/azl397985856/leetcode/blob/master/problems/1438.longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit.md)
## [1558. 得到目标数组的最少函数调用次数](https://github.com/azl397985856/leetcode/blob/master/problems/1558.minimum-numbers-of-function-calls-to-make-target-array.md)
## [1574. 删除最短的子数组使剩余数组有序](https://github.com/azl397985856/leetcode/blob/master/problems/1574.shortest-subarray-to-be-removed-to-make-array-sorted.md)
## [1589. 所有排列中的最大和](https://github.com/azl397985856/leetcode/blob/master/problems/1589.maximum-sum-obtained-of-any-permutation.md)
## [1631. 最小体力消耗路径](https://github.com/azl397985856/leetcode/blob/master/problems/1631.path-with-minimum-effort.md)
## [1658. 将 x 减到 0 的最小操作数](https://github.com/azl397985856/leetcode/blob/master/problems/1658.minimum-operations-to-reduce-x-to-zero.md)
## [1697. 检查边长度限制的路径是否存在](https://github.com/azl397985856/leetcode/blob/master/problems/1697.checking-existence-of-edge-length-limited-paths.md)
## [1737. 满足三条件之一需改变的最少字符数](https://github.com/azl397985856/leetcode/blob/master/problems/1737.change-minimum-characters-to-satisfy-one-of-three-conditions.md)
## [1834. 单线程 CPU](https://github.com/azl397985856/leetcode/blob/master/problems/1834.single-threaded-cpu.md)
## [1899. 合并若干三元组以形成目标三元组](https://github.com/azl397985856/leetcode/blob/master/problems/1899.merge-triplets-to-form-target-triplet.md) 👍
## [1904. 你完成的完整对局数](https://github.com/azl397985856/leetcode/blob/master/problems/1904.the-number-of-full-rounds-you-have-played.md)
## [1906. 查询差绝对值的最小值](https://github.com/azl397985856/leetcode/blob/master/problems/1906.minimum-absolute-difference-queries.md)
## [2007. 从双倍数组中还原原数组](https://github.com/azl397985856/leetcode/blob/master/problems/2007.find-original-array-from-doubled-array.md)
## [2008. 出租车的最大盈利](https://github.com/azl397985856/leetcode/blob/master/problems/2008.maximum-earnings-from-taxi.md)
## [5935. 适合打劫银行的日子](https://github.com/azl397985856/leetcode/blob/master/problems/5935.find-good-days-to-rob-the-bank.md)
## [5936. 引爆最多的炸弹](https://github.com/azl397985856/leetcode/blob/master/problems/5936.detonate-the-maximum-bombs.md)
## [5965. 相同元素的间隔之和](https://github.com/azl397985856/leetcode/blob/master/problems/5965.intervals-between-identical-elements.md)

# 困难难度题目合集

困难难度题目从类型上说多是：

## 图
## 设计题
## 游戏场景题目
## 中等题目的 follow up

从解法上来说，多是：

## 图算法
## 动态规划
## 二分法
## DFS & BFS
## 状态压缩
## 剪枝

从逻辑上说， 要么就是非常难想到，要么就是非常难写代码。 这里我总结了几个技巧：

1. 看题目的数据范围， 看能否暴力模拟
2. 暴力枚举所有可能的算法往上套，比如图的题目。
3. 总结和记忆解题模板，减少解题压力

以下是我列举的经典题目（带 91 字样的表示出自 **91 天学算法**活动）：

## [LCP 20. 快速公交](https://github.com/azl397985856/leetcode/blob/master/problems/lcp20.meChtZ.md)
## [LCP 21. 追逐游戏](https://github.com/azl397985856/leetcode/blob/master/problems/lcp21.Za25hA.md) 👍
## [Number Stream to Intervals](https://github.com/azl397985856/leetcode/blob/master/problems/Number-Stream-to-Intervals.md)
## [Triple Inversion](https://github.com/azl397985856/leetcode/blob/master/problems/Triple-Inversion.md) 91
## [Kth Pair Distance](https://github.com/azl397985856/leetcode/blob/master/problems/Kth-Pair-Distance.md) 91
## [Minimum Light Radius](https://github.com/azl397985856/leetcode/blob/master/problems/Minimum-Light-Radius.md) 91
## [Largest Equivalent Set of Pairs](https://github.com/azl397985856/leetcode/blob/master/problems/Largest-Equivalent-Set-of-Pairs.md) 👍
## [Ticket-Order.md](https://github.com/azl397985856/leetcode/blob/master/problems/Ticket-Order.md)
## [Connected-Road-to-Destination](https://github.com/azl397985856/leetcode/blob/master/problems/Connected-Road-to-Destination.md)
## [0004. 寻找两个正序数组的中位数](https://github.com/azl397985856/leetcode/blob/master/problems/4.median-of-two-sorted-arrays.md) 👍
## [0023. 合并 K 个升序链表](https://github.com/azl397985856/leetcode/blob/master/problems/23.merge-k-sorted-lists.md)
## [0025. K 个一组翻转链表](https://github.com/azl397985856/leetcode/blob/master/problems/25.reverse-nodes-in-k-groups.md) 👍
## [0030. 串联所有单词的子串](https://github.com/azl397985856/leetcode/blob/master/problems/30.substring-with-concatenation-of-all-words.md)
## [0032. 最长有效括号](https://github.com/azl397985856/leetcode/blob/master/problems/32.longest-valid-parentheses.md)
## [0042. 接雨水](https://github.com/azl397985856/leetcode/blob/master/problems/42.trapping-rain-water.md)
## [0052. N 皇后 II](https://github.com/azl397985856/leetcode/blob/master/problems/52.N-Queens-II.md)
## [0057. 插入区间](https://github.com/azl397985856/leetcode/blob/master/problems/57.insert-interval.md)
## [0065. 有效数字](https://github.com/azl397985856/leetcode/blob/master/problems/65.valid-number.md)
## [0084. 柱状图中最大的矩形](https://github.com/azl397985856/leetcode/blob/master/problems/84.largest-rectangle-in-histogram.md)
## [0085. 最大矩形](https://github.com/azl397985856/leetcode/blob/master/problems/85.maximal-rectangle.md)
## [0087. 扰乱字符串](https://github.com/azl397985856/leetcode/blob/master/problems/87.scramble-string.md)
## [0124. 二叉树中的最大路径和](https://github.com/azl397985856/leetcode/blob/master/problems/124.binary-tree-maximum-path-sum.md)
## [0128. 最长连续序列](https://github.com/azl397985856/leetcode/blob/master/problems/128.longest-consecutive-sequence.md)
## [0132. 分割回文串 II](https://github.com/azl397985856/leetcode/blob/master/problems/132.palindrome-partitioning-ii.md) 👍
## [0140. 单词拆分 II](https://github.com/azl397985856/leetcode/blob/master/problems/140.word-break-ii.md)
## [0145. 二叉树的后序遍历](https://github.com/azl397985856/leetcode/blob/master/problems/145.binary-tree-postorder-traversal.md)
## [0146. LRU 缓存机制](https://github.com/azl397985856/leetcode/blob/master/problems/146.lru-cache.md)
## [0154. 寻找旋转排序数组中的最小值 II](https://github.com/azl397985856/leetcode/blob/master/problems/154.find-minimum-in-rotated-sorted-array-ii.md)
## [0212. 单词搜索 II](https://github.com/azl397985856/leetcode/blob/master/problems/212.word-search-ii.md)
## [0239. 滑动窗口最大值](https://github.com/azl397985856/leetcode/blob/master/problems/239.sliding-window-maximum.md) 👍
## [0295. 数据流的中位数](https://github.com/azl397985856/leetcode/blob/master/problems/295.find-median-from-data-stream.md)
## [0297. 二叉树的序列化与反序列化](https://github.com/azl397985856/leetcode/blob/master/problems/297.serialize-and-deserialize-binary-tree.md) 91
## [0301. 删除无效的括号](https://github.com/azl397985856/leetcode/blob/master/problems/301.remove-invalid-parentheses.md)
## [0312. 戳气球](https://github.com/azl397985856/leetcode/blob/master/problems/312.burst-balloons.md)
## [330. 按要求补齐数组](https://github.com/azl397985856/leetcode/blob/master/problems/330.patching-array.md)
## [0335. 路径交叉](https://github.com/azl397985856/leetcode/blob/master/problems/335.self-crossing.md)
## [0460. LFU 缓存](https://github.com/azl397985856/leetcode/blob/master/problems/460.lfu-cache.md)
## [0472. 连接词](https://github.com/azl397985856/leetcode/blob/master/problems/472.concatenated-words.md)
## [0480. 滑动窗口中位数](https://github.com/azl397985856/leetcode/blob/master/problems/480.sliding-window-median.md)
## [0483. 最小好进制](https://github.com/azl397985856/leetcode/blob/master/problems/483.smallest-good-base.md)
## [0488. 祖玛游戏](https://github.com/azl397985856/leetcode/blob/master/problems/488.zuma-game.md)
## [0493. 翻转对](https://github.com/azl397985856/leetcode/blob/master/problems/493.reverse-pairs.md)
## [0664. 奇怪的打印机](https://github.com/azl397985856/leetcode/blob/master/problems/664.strange-printer.md)
## [0679. 24 点游戏](https://github.com/azl397985856/leetcode/blob/master/problems/679.24-game.md)
## [0715. Range 模块](https://github.com/azl397985856/leetcode/blob/master/problems/715.range-module.md) 👍
## [0726. 原子的数量](https://github.com/azl397985856/leetcode/blob/master/problems/726.number-of-atoms.md)
## [0768. 最多能完成排序的块 II](https://github.com/azl397985856/leetcode/blob/master/problems/768.max-chunks-to-make-sorted-ii.md) 91
## [0805. 数组的均值分割](https://github.com/azl397985856/leetcode/blob/master/problems/805.split-array-with-same-average.md)
## [0839. 相似字符串组](https://github.com/azl397985856/leetcode/blob/master/problems/839.similar-string-groups.md)
## [0887. 鸡蛋掉落](https://github.com/azl397985856/leetcode/blob/master/problems/887.super-egg-drop.md)
## [0895. 最大频率栈](https://github.com/azl397985856/leetcode/blob/master/problems/895.maximum-frequency-stack.md)
## [0909. 蛇梯棋](https://github.com/azl397985856/leetcode/blob/master/problems/909.snakes-and-ladders.md)
## [0975. 奇偶跳](https://github.com/azl397985856/leetcode/blob/master/problems/975.odd-even-jump.md)
## [0995. K 连续位的最小翻转次数](https://github.com/azl397985856/leetcode/blob/master/problems/995.minimum-number-of-k-consecutive-bit-flips.md)
## [1032. 字符流](https://github.com/azl397985856/leetcode/blob/master/problems/1032.stream-of-characters.md)
## [1168. 水资源分配优化](https://github.com/azl397985856/leetcode/blob/master/problems/1168.optimize-water-distribution-in-a-village.md)
## [1178. 猜字谜](https://github.com/azl397985856/leetcode/blob/master/problems/1178.number-of-valid-words-for-each-puzzle.md)
## [1203. 项目管理](https://github.com/azl397985856/leetcode/blob/master/problems/1203.sort-items-by-groups-respecting-dependencies.md)
## [1255. 得分最高的单词集合](https://github.com/azl397985856/leetcode/blob/master/problems/1255.maximum-score-words-formed-by-letters.md)
## [1345. 跳跃游戏 IV](https://github.com/azl397985856/leetcode/blob/master/problems/1435.jump-game-iv.md)
## [1449. 数位成本和为目标值的最大数字](https://github.com/azl397985856/leetcode/blob/master/problems/1449.form-largest-integer-with-digits-that-add-up-to-target.md)
## [1494. 并行课程 II](https://github.com/azl397985856/leetcode/blob/master/problems/1494.parallel-courses-ii.md)
## [1521. 找到最接近目标值的函数值](https://github.com/azl397985856/leetcode/blob/master/problems/1521.find-a-value-of-a-mysterious-function-closest-to-target.md)
## [1526. 形成目标数组的子数组最少增加次数](https://github.com/azl397985856/leetcode/blob/master/problems/1526.minimum-number-of-increments-on-subarrays-to-form-a-target-array.md)
## [1649. 通过指令创建有序数组](https://github.com/azl397985856/leetcode/blob/master/problems/1649.create-sorted-array-through-instructions.md)
## [1671. 得到山形数组的最少删除次数](https://github.com/azl397985856/leetcode/blob/master/problems/1671.minimum-number-of-removals-to-make-mountain-array.md)
## [1707. 与数组中元素的最大异或值](https://github.com/azl397985856/leetcode/blob/master/problems/5640.maximum-xor-with-an-element-from-array.md)
## [1713. 得到子序列的最少操作次数](https://github.com/azl397985856/leetcode/blob/master/problems/1713.minimum-operations-to-make-a-subsequence.md)
## [1723. 完成所有工作的最短时间](https://github.com/azl397985856/leetcode/blob/master/problems/1723.find-minimum-time-to-finish-all-jobs.md)
## [1787. 使所有区间的异或结果为零](https://github.com/azl397985856/leetcode/blob/master/problems/1787.make-the-xor-of-all-segments-equal-to-zero.md)
## [1835. 所有数对按位与结果的异或和](https://github.com/azl397985856/leetcode/blob/master/problems/1835.find-xor-sum-of-all-pairs-bitwise-and.md)
## [1871. 跳跃游戏 VII](https://github.com/azl397985856/leetcode/blob/master/problems/1871.jump-game-vii.md) 👍
## [1872. 石子游戏 VIII](https://github.com/azl397985856/leetcode/blob/master/problems/1872.stone-game-viii.md)
## [1883. 准时抵达会议现场的最小跳过休息次数](https://github.com/azl397985856/leetcode/blob/master/problems/5775.minimum-skips-to-arrive-at-meeting-on-time.md)
## [1970. 你能穿过矩阵的最后一天](https://github.com/azl397985856/leetcode/blob/master/problems/1970.last-day-where-you-can-still-cross.md)
## [2009. 使数组连续的最少操作数](https://github.com/azl397985856/leetcode/blob/master/problems/2009.minimum-number-of-operations-to-make-array-continuous.md)
## [2025. 分割数组的最多方案数](https://github.com/azl397985856/leetcode/blob/master/problems/2025.maximum-number-of-ways-to-partition-an-array.md)
## [2030. 含特定字母的最小子序列](https://github.com/azl397985856/leetcode/blob/master/problems/2030.smallest-k-length-subsequence-with-occurrences-of-a-letter.md)
## [2102. 序列顺序查询](https://github.com/azl397985856/leetcode/blob/master/problems/2102.sequentially-ordinal-rank-tracker.md)

##  
