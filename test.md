# 基础

## 数据类型

### char

#### 多种表示法

zfx\_1='a';//直接用单引号限制的一个字符赋值，注意c不是字符是变量，’c’是字符

zfx\_2=97;//直接用字符对应的ASCII码值10进制赋值

ASCII码，a是97，A是65，可以通过char ch=‘a’；cout << int（ch）<<endl；查看

zfx\_3=0141;//8进制标志以0开头

zfx\_5='\141';//用3位8进制数转义字符，不用0开头

zfx\_6='\0141';//如果用0表示，则成了两个字符\014和 1两个字符，所以警告

zfx\_4=0x61;//16进制标志以0x开头

zfx\_7='\x61';//x是16进制的标志，用2位16进制数转义

zfx\_8='\0x61';//不能用0x作16进制的标志，则成了两个字符\0x6 和 1,所以警告

不存在‘\’字符，’\\’才是

NULL为一个宏 (void\*)0,故可以理解为'\0'

\n换行，\r回车（本行首），\t水平制表（补空隔到8各字符，如aa\tbb，aa后面会补6个空隔，aaaa\tbb，aaaa后面则补4个空隔）

#### ASCII表

A+32=a，注意是数字→大写字母→小写字母

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ASCII值** | **控制字符** | **ASCII值** | **字符** | **ASCII值** | **字符** | **ASCII值** | **字符** |
| 0 | NUT | 32 | (space) | 64 | @ | 96 | 、 |
| 1 | SOH | 33 | ! | 65 | A | 97 | a |
| 2 | STX | 34 | " | 66 | B | 98 | b |
| 3 | ETX | 35 | # | 67 | C | 99 | c |
| 4 | EOT | 36 | $ | 68 | D | 100 | d |
| 5 | ENQ | 37 | % | 69 | E | 101 | e |
| 6 | ACK | 38 | & | 70 | F | 102 | f |
| 7 | BEL | 39 | , | 71 | G | 103 | g |
| 8 | BS | 40 | ( | 72 | H | 104 | h |
| 9 | HT | 41 | ) | 73 | I | 105 | i |
| 10 | LF | 42 | \* | 74 | J | 106 | j |
| 11 | VT | 43 | + | 75 | K | 107 | k |
| 12 | FF | 44 | , | 76 | L | 108 | l |
| 13 | CR | 45 | - | 77 | M | 109 | m |
| 14 | SO | 46 | . | 78 | N | 110 | n |
| 15 | SI | 47 | / | 79 | O | 111 | o |
| 16 | DLE | 48 | 0 | 80 | P | 112 | p |
| 17 | DCI | 49 | 1 | 81 | Q | 113 | q |
| 18 | DC2 | 50 | 2 | 82 | R | 114 | r |
| 19 | DC3 | 51 | 3 | 83 | S | 115 | s |
| 20 | DC4 | 52 | 4 | 84 | T | 116 | t |
| 21 | NAK | 53 | 5 | 85 | U | 117 | u |
| 22 | SYN | 54 | 6 | 86 | V | 118 | v |
| 23 | TB | 55 | 7 | 87 | W | 119 | w |
| 24 | CAN | 56 | 8 | 88 | X | 120 | x |
| 25 | EM | 57 | 9 | 89 | Y | 121 | y |
| 26 | SUB | 58 | : | 90 | Z | 122 | z |
| 27 | ESC | 59 | ; | 91 | [ | 123 | { |
| 28 | FS | 60 | < | 92 | / | 124 | | |
| 29 | GS | 61 | = | 93 | ] | 125 | } |
| 30 | RS | 62 | > | 94 | ^ | 126 | ` |
| 31 | US | 63 | ? | 95 | \_ | 127 | DEL |

#### 常用函数

```
函数 定义 : intisdigitint c);

一 、 头 文件 8
由 于 isdisit() 函数 是 属于 C 语 言 中 的 一 个 函数 ， 因 此 头 文件 为

在 C++ 中 如 下 应 用 :

二 、 函 数 说 明

检查 参数 c 是 否 为 阿拉 伯 数 字 0 到 9。

三 、 返 回 值

若 参 数 c 为 阿拉 伯 数字 0~9， 则 返回 非 0 值 ， 否 则 返回 0。
```

判断是否为数字

同头文件还有int isalnum(char c)，判断字符c是大小写字母或数字

char tolower(char c)，字符c是大写字母就返回小写，否则原样返回c

char toupper(char c)

### string

使用string时需要#include <string>，一般还是无法识别，记得using namespace std;

string可以直接赋值，比字符数组需要调用字符串操作函数（strcpy（）等）方便很多，详见STL-容器-string

string str=str1；

string中涉及windows路径时记得用’\\’，因为’\’的话没有表示出\，而是解析为’\H’

![](test_assets/image_002.png)

char 有一个字节表示，wchar\_t 宽体字符，由两个字符表示。char16\_t，char32\_t C++ 11 新增的字符类型，char16\_t 占两个字节，char32\_t 占四个字节。

初始化方法不同

```
DESO NONE
a

PR
GNRS

BWNE

#include <iostream>
#include <string>

using namespace std;

int main()

{
char nameChar[] = "This is a char array";
wehar_t nameWchar{] = L"This is a wchar array";
char16_t nameChari6[] u"This is a chari6 array
char32_t nameChar32[] = U"This is a char32 array
cin.get();

char chif ‘at }; // or { u8'a’ }
wehar_t ch2{ L'a‘ };
charl6_t ch3{ u'a’ };
char32_t ch4{ U'a' };
```

```
在 C++ 标准 库 中 ， 每 个 basic_string RAGSAT ESTHET TS.

当 字 符 的 类 型 为 char 时 ， 使 用 std-string;
std:-u16string 字符 类 型 char16 ft
std:-u32string 字符 类 型 char32_ft
std:-wstring 字符 类 型 wchar t

表示 文本 的 其 他 类 型 ， 包 括 std::stringstream 和 std::cout 专用 于 罕 字 符 串 和 宽 字 符 串 。

1
2
3
4

typedef basic_string<char> string;
typedef basic_string<wchar_t> wstrin
typedef basic_string<charl6_t> uléstring; //C++11
typedef basic_string<char32_t> u32string; //C++11
```

### float/double

由于计算机二进制表示浮点数有精度的问题，0.0实际上不是0，而是非常接近零的小数。

因此对于一个浮点变量float a或double a，a==0.0永远为false，不能用a==0.0来判断a是否为0

在ANSIC C中定义了FLT\_EPSILON、DBL\_EPSILON、LDBL\_EPSILON来用于浮点数与零的比较，一般if(fabs(a)<FLT\_EPSILON)或if(fabs(a)< DBL\_EPSILON)就可以表示a是否“为0”。

3.14默认是double类型，赋值时会做相应的转换。加后缀可以声明常量数据类型，如3.14f则是float类型

c++中输出一个小数，无论是float还是double类型，都只会保留6位有效数字

小数点一边如果全为0可以省略，如160.，.18，-.18都合法，两边都省略只剩.不合法

科学计数法是浮点型的指数形式，其一般形式为a e n，a为十进制数，n为十进制整数，都不可省略。如3e2为3\*102、1.e0为1.0、.2e0为0.2合法，.e5前面只有小数点、-e3前面只有-是不合法的

浮点数的无穷，用DBL\_MAX（而不是DOUBLE\_MAX）表示正无穷，DBL\_MIN表示负无穷，需要包含文件float.h。

### 枚举（枚举类）

```
enum KeyLen {

| Lenl6 = 16,
| Len24 = 24,
;Len32 = 32
}:
```

1.使用枚举类型名作为参数，可以限制参数只能为枚举出的值

2.使用特定名称来代表某些值，使得其含义更清晰

应使用枚举类，详见[C++11枚举类——enum class-CSDN博客](https://blog.csdn.net/weixin_42817477/article/details/109029172)

作用：

1. 降低命名空间污染
2. 避免发生隐式转换
3. 可以前置声明

C++11后用enum会有警告，让你用enum class，工作中把这玩意当作错误

解决方案：A type = getType()改为getType()，哪里用就哪里调，不设成员变量就没有这个警告

### 数组

数组名包含信息：

比如数组名为a，知道数组占用内存sizeof（a），知道数组元素占用内存sizeof（a[0]），知道数组元素个数sizeof（a）/ sizeof（a[0]），知道首地址与每一个元素的地址(int)&arr[0]或arr

二维数组：

缺省定义，a[][3]={1，2，3，4，5，6};定义时有初始化可以缺少行数

i%n(列)和i/n(行)搭配，可一个for循环遍历二维数组，其中n是矩阵的列数，搞错过成i%m和i/n，把行数m放了进去

数组和动态内存赋初值是良好的编程习惯，防止将未被初始化的内存作为右值使用。

vector会自动初始化，但C形式的定义type v[10]不会（试了类中定义地址类型的数组成员，值默认不是NULL），所以要记得初始化

指针操作数组：

```
int @p)[4], /该 语句 是 定义 一 个 数组 指针 ， 指 向 含 4 个 元 素 的 一 维 数组
```

```
f/#@Li] +9). #4 @H) 49). @@H) LI]. plillil. Hh, HEB. O>lb*. /这 几 种 操作 方式 都 是 合法 的 。
```

用变量定义数组：

定义数组时，往往长度不是一成不变的，此时就需要用其他参数来确定，但一旦定义变量n，再用变量n来定义数组，编译器将报错

解决方案是使用malloc

```
C 语 言 要 想 实 现 动态 数组 ， 就 只 能 通过 malloc 函 数 动态 分 配 空间
将 int a[n];
给 成 int* a=(int *)malloc (sizeof(int)*n) ;
```

### 引用

给一个变量（一块内存空间）起别名，两个名字等效

#### 语法

数据类型 &别名 = 原名; 例如int a=10;int &b=a;那么a和b都是指这个10，改b的值a的值也改

注意：

1. 引用必须要初始化，因为本质上是int\* const ref=&a，const修饰必须初始化
2. 引用一旦初始化就不能改了
3. 不能有NULL引用。必须确保引用是和一块合法的存储单元关联

对数组建立引用

```
int arr[] = { 1, 2, 3, 4, 5};

// 第 一 种 方法

/1/1. 定 义 数 组 类 型

typedef int (MY_ARR) [5] ;// 数 组 类 型

//2. 建立 引用

MY_ARR &arref = arr;// 建 立 引 用 ，int &b=a;

// 第 二 种 方法
// 直 接 定义 引用
int (&arref2) [5] = arr;// int &b=a

// 第 三 种 方法
typedef int (&MY_ARR3) [5] ; // 建 立 引 用 数组 类 型
MY_ARR3 arref3 =
```

常用第二种

对指针建立引用：

|  |
| --- |
| **int\*** pointer **=** **NULL;**  int**\* &p** **=** pointer**;** |

#### 常量引用

定义格式:

|  |
| --- |
| const Type**&** ref **=** val**;** |

注意：

- 不能通过const修饰的引用来修改值，但可以通过原变量名修改

|  |
| --- |
| void test01**(){**  int a **=** 100**;**  const int**&** aRef **=** a**;** //此时aRef就是a  //aRef = 200; 不能通过aRef修改内存的值  a **=** 100**;** //OK  cout **<<** "a:" **<<** a **<<** endl**;**  cout **<<** "aRef:" **<<** aRef **<<** endl**;**  **}** |

- 字面量不能赋给引用，但是可以赋给const引用

```
z7 非 常量 引用 的 初始 值 必 须 为 堪 值
ffinth ref = 100

const int& ref = 100

cout << ref << endl

JR RBA

cout << fret < endl

int* p = (int*) (ref)

Ap = 200

JAERRD HAS AIRAARESRRMAEER: BAF ARB
cout << ref << endl

return 0
```

实际上编译器自动转换为

int temp = 200;

const int& ret = temp;

#### 引用传递

1.引用作为函数参数

定义函数int function (int &a, int &b)，调用函数function(a, b)，这种函数的形参改变实参也会改变

和地址传递效果一样int function(int \*a, int \*b)，function(&a, &b)且更简便

常量引用：不想修改原值的话，使用const来防止修改int function(const int &a, const int &b)

|  |
| --- |
| struct Teacher**{**  int mAge**;**  **};**  //指针间接修改teacher的年龄  void AllocateAndInitByPointer**(**Teacher**\*\*** teacher**){**  **\***teacher **=** **(**Teacher**\*)**malloc**(sizeof(**Teacher**));**  **(\***teacher**)->**mAge **=** 200**;**  **}**  //引用修改teacher年龄  void AllocateAndInitByReference**(**Teacher**\*&** teacher**){**  teacher**->**mAge **=** 300**;**  **}**  void test**(){**  //创建Teacher  Teacher**\*** teacher **=** **NULL;**  //指针间接赋值  AllocateAndInitByPointer**(&**teacher**);**  cout **<<** "AllocateAndInitByPointer:" **<<** teacher**->**mAge **<<** endl**;**  //引用赋值,将teacher本身传到ChangeAgeByReference函数中  AllocateAndInitByReference**(**teacher**);**  cout **<<** "AllocateAndInitByReference:" **<<** teacher**->**mAge **<<** endl**;**  free**(**teacher**);**  **}** |

2.引用作为函数返回值

int& sum(int a, int b)

{

int c=a+b;

return c;

}

返回局部变量c而不是c的值，即返回左值。如sum(a,b)=1000;返回引用的函数可以被赋值，相当于c被赋值1000

由于是局部变量，c只能用一次（编译器保留），第二次就已经被释放了，所以不要返回局部变量的引用（可以声明static放全局区就不会被释放）

正确用法是把传进来的引用参数处理后传出去

#### 本质

指针常量

int a=10;

int& ref=a;//相当于int\* const ref=&a

ref=20;//发现是ref引用编辑器自动改为\*ref=20;

### 右值

**左值右值**

在c++中可以放在赋值操作符左边的是左值，可以放到赋值操作符右面的是右值。

有些变量即可以当左值，也可以当右值。

左值为Lvalue，L代表Location，表示内存可以寻址，可以赋值。

右值为Rvalue，R代表Read,就是可以知道它的值。

比如:int temp = 10; temp在内存中有地址，10没有，但是可以Read到它的值。

**Move使用场景**

1.移动构造和移动赋值

2.插入容器。比如push\_back(std::move());

```
在 对 容器 进行 插入 或 删除 操作 时 ， 使 用 std: :move 可 以 避免 额外 的 数据 拷贝 。

std::vector<std::string> sourceVec = {"A", "B", "C"};

// 4% sourceVec /W7#E

BF targetVec
std::vector<std::string> targetVec;
for (auto&& element : sourceVec) {

targetVec.push_back(std: :move(element) );

// 在 人 sourceVec 形 动 后 ，sourceVec *HHA/RA HICH

任 这 个 示例 中 ， 我 们 通过 使 用 std: :move 将 sourceVec 中 的 元 素 移动 到 targetvec 中 ， 避 免
了 元 素 的 不 必要 拷贝 操作 。
```

另一种使用方式为

```
std: :move(lastFtrExtractOpList.begin(), lastFtrExtractOpList.end(), std: :back_ins

ten(pFtrExtractOpList) );
```

3.函数返回值（编译器默认ROV）

```
在 函数 返回 时 ， 可 以 使 用 std: :move 将 局 部 对 象 的 所 有 权 转 移 给 返回 的 右 值 ， 避 免 不 必 要 的 拷
贝 。

std::string createLargeString() {
std::string largeString = "Very large string";
[V] FEOEAE

return std::move(largeString) ;

企 这 个 示例 中 ， 我 们 使 用 std: :move 将 局 部 对 象 largestring 的 所 有 权 转 移 给 函数 返回 的 右
值 ， 避 免 了 拷贝 大 字符 串 的 开销 。
```

这一步不要我们写，编译器ROV优化到甚至连移动构造都不会调用，写了纯负优化

4.move有用的前提是，该类型有移动构造。

### 结构体

struct tag {

member-list

member-list

member-list

...

} variable-list ;

tag 是结构体标签。

member-list 是标准的变量定义，比如 int i; 或者 float f，或者其他有效的变量定义。

variable-list 结构变量，定义在结构的末尾，最后一个分号之前，您可以指定一个或多个结构变量。

结构体指针用->来访问成员，结构体名用.

结构体变量名不代表该结构体在内存的首地址，所以函数参数是结构体时值传递是复制一份

为了节省空间常传结构体指针给函数，但是又会使得结构体的数据可能被修改，此时可以在函数的参数列表使用const修饰，如结构体student的打印函数void printstudent(const student \*s)，传入地址但是该函数不能修改该结构体

#### 内存对齐等易错点

1.结构类型无法将自己的类型作为其成员的类型，因为自己的类型定义尚不完整，要在结束的大括号（}）后才算定义完整。

2.基于内存的对齐原则，一个结构体变量定义完之后，其在内存中的存储并不等于其所包含元素的宽度之和。从结构体存储的首地址开始，每一个元素放置到内存中时，它都会认为内存是以它自己的大小来划分的，因此元素放置的位置一定会在自己宽度的整数倍上开始（以结构体变量首地址为0计算）

3.只有结构变量的成员可以进行关系运算，结构体变量之间不可以进行关系运算

4.末尾的;易漏

#### memset易错点

```
struct SecKeyInfo
{
Hiatt
SeckeyInfo()
{
key = string();
clientID = string();

status = true;
}
/1/ SCRE,
string key;
/1/ 如 果 鉴 别 这 个 秘 钥 属于 谁 -> GiBPAA IT RREClient IDiserver IDM THiS
string clientID;
string serverID;
// D& -> 稀有 ID
int seckeyID;
1) Ti -> PARES
bool status; // true: 可 用 ，false: 不 可 用
》

SeckeyInfo info;
menset (&info,

sizeof(info)); // error， 成 员 是 string 不 能 做 memset 抬 作
```

如果一个struct中有string成员（显然是c++语法），那么使用memset来初始化struct将出错，因为memset无法初始化string，应该用c++的初始化方法——构造函数。

#### struct在C和C++中的区别

![](test_assets/image_015.png)

//1. 结构体中即可以定义成员变量，也可以定义成员函数

struct Student**{**

string mName**;**

int mAge**;**

void setName**(**string name**){** mName **=** name**; }**

void setAge**(**int age**){** mAge **=** age**; }**

void showStudent**(){**

cout **<<** "Name:" **<<** mName **<<** " Age:" **<<** mAge **<<** endl**;**

**}**

**};**

```
2. 使 用 时 的 区 别 : C 中 使 用 结构 体 需要 加 上 struct 关键 字 ， 或 者 对 结构 体 使 用 typedef 取 别 名 ， 而 C++ 中 可 以 省 略 struct 关键 字 直 接 使 用 ， 例 如

struct Student{ int iAgeNum; string strName; } typedef struct Student Student2; //C 中 取 别 名 struct Student stul; // C 中 正常 使 用 Student2 stu2;  // C 中 通过 取 别 名 的 使 用 Student stu3;  // C++ 中 使 用
```

#### C++中struct和class的区别

```
1. struct 一 般 用 于 描述 一 个 数据 结构 集合 ， 而 class 是 对 一 个 对 象 数据 的 封装 ;
2. struct 中 默认 的 访问 控制 权限 是 public 的 ， 而 class 中 默认 的 访问 控制 权限 是 private 的 ， 例 如 :

struct A{ int iNum, // 默认 访问 控制 权限 是 public } class B{ int iNum，// 默认 访问 控制 权限 是 private }

3. 在 继承 关系 中 ，struct 默认 是 公有 继承 ， 而 class 是 私有 继承 ;
4. Class 关键 字 可 以 用 于 定义 模板 参数 ， 就 像 ypename， 而 struct 不 能 用 于 定义 模板 参数 ， 例 如 :

template<typename T，typename Y> // 可 以 把 typename 换 成 class int Func(const T& t, const Ye y) {

//T0D0 ]
```

#### 变长结构体

比如有一个double数组，但是不知道具体个数，要用结构体去接，怎么才能够接完呢？

可以这样：

```
struct BSurfParam

{

' int
int
int
int
int
int
int
int

cp.-----------------
Sa

Uorder;

Vorder;
NumColumnsControlPoints;
NumRowsControlPoints;
Uperiodicity;
Vperiodicity;
DimensionControlPoints;
dummy ;

double data[1];
```

最后是个double数组，但只有1个，明显这样定义数组没意义

目的是获得一个指针double\* data，然后用指针访问

### 字面量

#### 为什么要？

```
C++ 自 带 4 种 字面 量 :
+ 整形 123

* 浮 点 型 12.3
“字符 1

+ 字符 串 “123”

*。 无 符号 整形 ( unsigned int ): 123u
”长 整形 ( long ): 1231

在 C++03 中 ， 我 们 可 以 定义 一 个 浮 点 数 height
double height = 3.4
那么 ， 痛 点 来 了 ， 此 处 的 height 的 单位 是 什么 呢 ? 米 》 厘 米 ? 又 或 是 英尺 ?

height = 3cm;

// ratio = (3 * 10) /2
ratio = 3cm / 2mm;
```

#### 用法

```
C++ 1A REFS

long double
operator"" _cm(long double x) {
return x * 10;

long double
operator" _m(long double x) {
return x * 1000;

long double
operator"" _mm(long double x) {

return x;
// height = 30.0
auto height = 3.0_cm;

// Length = 1230.0
suto lensth = 1.22 m:
```

可以设置constexpr

```
如 果 使 用 这 种 写法 ， _cm ，_m ，_mm 等 函数 将 在 运行 时 被 调用
后 缀 国 数 ， 则 需要 把 函数 定义 为 constexpr ， 例 如

constexpr long double
operator"”_cm(long double x) {
return x * 10;

了

， 如 果 希 望 在 编译 时 就 调用 字面 量
```

类型限制

![](test_assets/image_022.png)

### POD

POD类型，plain old data。Plain代表数据是普通类型，old代表能与C兼容支持memcpy、memset等函数。

POD分为两个部分，trivial(平凡的)和(standard layout)标准布局的，必须同时满足才是POD类型。

#### trivial

平凡的类或结构体必须满足以下的条件：

- 平凡的默认构造函数和析构函数。只要是自己定义了函数，即使实现为空，也不再平凡。所以就是说不能自定义默认构造函数和析构函数。

- 平凡的拷贝构造函数和移动构造函数。

- 平凡的赋值构造函数。

- 不能包含虚函数和虚基类。

```
class TrivialA {
33

class TrivialB {

public :
int a;
33
class Trivialc {
Trivialc() {} MA] BRUPERR, BPA
33

class TrivialD {

TrivialD(const TrivialD& a) {} // AMMEMERE, BFA

3
class TrivialE {

TrivialE(TrivalE&& a) {} // BEANVEBR, BPA
3

class TrivialF {

TrivialF& operator=(const TrivialF& a) {} // AMER, KPA

33
class TrivialG {
virtual void func() = 9; // AkeBR, BA
33
class TrivialH: virtual public TrivialA { I! GIEBE, BFA

35
```

可以用std::is\_trivial<T>::value来判断是不是一个平凡类型

```
int main(int argc, char **argv)

{

std::cout
std::cout
std::cout
std::cout
std::cout
std::cout
std::cout
std::cout
return @;

<<
<<
<<
<<
<<
<<
<<
<<

std:
std:
std:
std:
std:
std:
std:
std:

:is_trivial<TrivialA>:
:is_trivial<TrivialB>:
:is_trivial<Trivialc>:
:is_trivial<TrivialD>:
:is_trivial<TrivialE>:
:is_trivial<TrivialF>:
:is_trivial<TrivialG>:

:is_trivial<TrivialH>:

:Value
:Value
:Value
:Value
:Value
:Value
:Value

:Value

<<
<<
<<
<<
<<
<<
<<
<<

std:
std:
std:
std:
std:
std:
std:
std:

:endl;
:endl;
:endl;
:endl;
:endl;
:endl;
:endl;
:endl;

// 1
// 1
// SBET SG HEO
```

#### trivially\_copyable

```
是 平凡 类 型 的 一 个 扩展 ， 它 不 仅 包括 所 有 平凡 类 型 ， 还 包括 那些 可 以 安全 地 被 复制 和 移动 的 类 型 ， 即 使 这
些 类 型 不 是 平凡 类 型 。 例 如 ， 一 个 类 可 能 有 一 个 自 定 义 的 构造 函数 ， 但 如 果 它 保证 对 象 的 内 容 可 以 通过 简单 的
位 拷贝 (bitwise copy) 来 复制 ， 那 么 它 也 可 以 被 认为 是 平凡 可 复制 的 。 它 必须 满足 两 个 条 件 :

。 类 型 可 以 被 复制 或 移动 ， 且 不 需要 特殊 的 资源 管理 。

构 函 数 ) 都 是 平凡 的 或 者 被 删除 的 (deleted) 。
下 列 类 型 统称 为 可 丈 凡 复制 类 型 :
。 标量 类 型
。 可 平凡 复制 类 类 型
。 上 述 类 型 的 数组
。 这些 类 型 的 有 cv 限定 版 本

说 明 :
一 般 来 阅 ， 对 于 任何 可 平凡 复制 类 型 T 及 T 对 象 obj1， 能 复制 objl 的 底层 字 节
到 char BK unsigned char By std::byte (C++17 起 ) 的 数组 中 ， 或 到 T 的 另 一 不 同 对 象 obj2 中 。
objl 与 obj2 均 不 可 为 潜在 重 亚 的 子 对 象 。
如 果 复 制 objl 的 底层 字 节 到 这 种 数组 中 ， 然 后 复制 结果 内 容 回 objl 中 ， 那 么 objl 将 保有 其 原
值 。 如 果 复 制 objl 的 底层 字 节 到 obj2 中 ， 那 么 obj2 将 保有 objl WIE.
底层 字 节 能 由 std::memcpy 或 std::memmove 复制 ， 只 要 不 访问 存活 的 volatile 对 象 即 可 。
```

在 C++11 及其之后的版本中，如果一个类型是可平凡复制的，那么你可以安全地通过 memcpy 或 memmove 等函数进行复制，而不需要担心可能的副作用（如析构函数的调用或虚函数的重新定向等）。然而，你应该注意，即使一个类型是可平凡复制的，也并不意味着你应该总是使用 memcpy 来进行复制；在许多情况下，使用赋值操作符或复制构造函数是更安全、更清晰的选择。

一些例子帮助理解：

```
#include <type_traits>

struct A { int m; };

static_assert(std::is_trivially_copyable_v<A> == true);

struct B { B(B const&) {} };

static_assert(std::is_trivially_copyable_v<B> == false);

struct C { virtual void foo(); };

static_assert(std::is_trivially_copyable_v<C> == false);

struct D
{

int m;

D(D const&) = default; // -> YAH
D(int x) : m(x +1) {}
33

static_assert(std::is_trivially_copyable_v<D> == true);

int main() {}
```

```
在 这 个 示例 中 :

1) A 是 一 个 平凡 可 复制 类 型 ， 因 为 它 没 有 自 定 义 的 特殊 成 员 函 数 ， 且 可 以 被 简单 地 复制 和 移动 。

2) B 有 一 个 自 定义 的 拷贝 构造 函数 ” ， 所 以 它 不 是 平凡 可 复制 的 。 尽 管 它 的 赋值 操作 可 能 是 平凡 的 ， 但
拷贝 构造 函数 的 存在 使 得 整个 类 型 不 是 平凡 可 复制 的 。

3) C 有 一 个 虚 函 数 ， 这 使 和 也 不 是 平凡 可 复制 的 。 虚 函数 的 存在 意味
BREE Ame (viable) ， 这 违反 了 平凡 可 复制 类 型 的 定义 。

4) D 昌 然 有 -个 自 定义 的 指 风 构 和 数 ， 但 是 有 一 个 使 用 =default 的 构造 函数 ， 所 以 它 也 是 平凡 可 复制
的 。

平凡 可 复制 类 型 在 C++ 中 很 重要 ， 因 为 它们 可 以 被 编译 器 优化 为 没有 额外 开销 的 位 拷贝 操作 ， 这 对 于 性 能
敏感 的 程序 是 非常 有 益 的
```

```
4h

RP CV EME Y SUPYYUECS

class A

{

33

~A() = default;

AQ) {}

A(const A &) = default;
A(A &&) = default;

//
//
//
//

A &operator=(const A &) = default; //

A &operator=(A &&) = default;

//

trivially
trivially
trivially
trivially
trivially
trivially

copyable
copyable
copyable
copyable
copyable
copyable
```

```
class B

{
// REALE ALEX FAPTAMEEK not trivially copyable
virtual void foo() = 0; // not trivially copyable

// ~B() = delete; // not trivially copyable
// ~B() {} // not trivially copyable
// B(const B &) {} // not trivially copyable
// B(B &&) {} // not trivially copyable
// B &operator=(const B &) {} // not trivially copyable
// B &operator=(B &&) {} // not trivially copyable

33
```

```
// not trivially copyable
class C : public B

{

33

// trivially copyable

class D

{

public:
explicit D(int val) : d(val) {}
int d;

33
```

#### standard

标准布局的类或结构体必须满足以下的条件：

一、所有非静态成员有相同的访问权限。

二、在类或结构体继承时满足以下两个条件之一：

1、派生类中有非静态成员，且只有仅包含静态成员的基类。

2、基类有非静态成员，而派生类没有非静态成员。

其实就是派生类和基类中不允许同时出现非静态成员，因为同时有非静态成员就无法进行memcpy

三、类中第一个非静态成员的类型与基类不同。

C++标准允许，在基类没有成员时，派生类第一个成员与基类共享地址。

但是当派生类中第一个数据成员类型为基类类型时，有趣的问题就来了。

首先，这时派生类的内存布局包括基类部分的内存布局，同时自己又添加了另外一个基类类型的变量

如果编译器优化实现第一个成员和基类部分共享地址，那么就违背了C++标准的另一个要求，同类型的不同对象地址必须不同。

四、没有虚函数和虚基类。

五、所有非静态成员均符合标准布局，其基类也符合标准布局。

标准布局类型的一个重要特性是它们的内存布局在不同的编译器和平台上是一致的，这对于跨平台的二进制数据交换非常重要

```
class StdLayoutA {
33
class StdLayoutB {
public :
int a;
int b;
33
class StdLayoutC : public
public:
int a;
int b;
void fun() {}
33
class StdLayoutD : public
public:
int a;
StdLayoutA sla;
33
class StdLayoutE : public
33
class StdLayoutF {
public:
static int a;
33
class StdLayoutG : public
public:
int a;

}8

StdLayoutA {

StdLayoutA {

StdLayoutA , public StdLayoutC {

StdLayoutF {
```

![](test_assets/image_032.png)

针对POD类型也有模板类：std::is\_pod<T>::value

```
int main(int argc, char **argv)

{

std:
std:
std:
std:
std:
std:
std:
std:
std:
std:
std:

scout
scout
scout
scout
scout
scout
scout
scout
scout
scout

scout

<<
<<
<<
<<
<<
<<
<<
<<
<<
<<
<<

std::is_standard_layout<StdLayoutA>::
std::is_standard_layout<StdLayoutB>::
std::is_standard_layout<StdLayoutC>::
std::is_standard_layout<StdLayoutD>::
std::is_standard_layout<StdLayoutE>::
std:
std::is_standard_layout<StdLayoutG>::
std::is_standard_layout<StdLayoutH>::
std::is_standard_layout<StdLayoutI>::
std::is_standard_layout<StdLayoutJ>::
std::is_standard_layout<StdLayoutK>::

:is_standard_layout<StdLayoutF>::

value
value
value
value
value
value
value
value
value
value

value

:endl;
:endl;
:endl;
:endl;
:endl;
:endl;
:endl;
:endl;
:endl;
:endl;
:endl;

// 以 上 都 是 1， 从
```

#### 好处

![](test_assets/image_034.png)

## 运算和赋值

### 自增自减运算符

```
11.16 说 说 运算 符 i++ 和 ++i 的 区 别

Hinclude <stdio.h>
int mainO {
int i = 2;

int j = 2;

j + i++ //SeIvAEAO

printf (“i= Wd, j= Sd\n,i, §); //i= 3，j= 4

i= 2;

j= 2;

J: (OEE

printf (“i= %d, j= %d",i, 5); //i= 3，j= 5
}

1 赋值 顺序 不 同 : ++ i 是 先 加 后 赋值 ; i++ 是 先 赋值 后 加 ; +++ em see,
2 效率 不 同 : 后 二 ++ 执 行 速度 比 前 填 的 慢 。
pe ee eee
3. i++ 不 能 作为 左 值 ， 而 ++i 可 以 :
一

inti

int+ pl = &(+ti); 7/ 正确
Af int p2 = &G++t)i7/ 错 误
+H = 1 正确

ff at = 1;// 错 误

4 两 者 都 下 是 原子 操作 。
```

### 位运算符

&

按位与运算符，只有1&1=1

|

按位或运算符，只有0|0=0

^

按位异或运算符。参与运算的两个值，如果两个相应位相同，则结果为0，否则为1。即：0^0=0， 1^0=1， 0^1=1， 1^1=0

性质1：0^n=n

性质2：满足交换律和结合律

**用法：**

1若数组中只有一个元素是奇数个，其他元素都是偶数个，那么数组中所有数异或，结果就是奇数个的元素

2. (a^b)>=0说明同号，否则异号

（浮点数不能直接位运算要强转为int，由于会保留符号，所以可以这么做）

（实测上面的方法在浮点数下判断同号不一定正确，还是用官方接口signbit（a）==signbit（b）来判断）

按位取反。其规则是~0=1, ~1=0, 如二进制0101 0101取反后就是1010 1010

<<

二进制左移运算符。将一个运算对象的各二进制位全部左移若干位（左边的二进制位丢弃，右边补0）。A << 2 将得到 240，即为 1111 0000

>>

二进制右移运算符。将一个数的各二进制位全部右移若干位，正数左补0，负数左补1，右边丢弃。A >> 2 将得到 15，即为 0000 1111

用法：替换/2

### 算数运算符

+

两个int相加，要条件反射意识到可能会溢出

\*

两个int相乘，要条件反射意识到可能会溢出

此外还有一细节：long a,b; long c=a\*b;。a和b不定义为long的话，a\*b得到右值的过程中报错

/

a/b，a和b都是整型（short int long）时，结果也是整型，小数部分舍弃

**向上取整**

a/b=c，/本身是向下取整的，要向上取整。

以前是判断a%b!=0，结果就+1，效率低

可以直接返回(a+b-1)/b

%

两个数进行取余运算，两边必须为整数，结果的符号由被取余数决定，即-5%3=-2，5%-3=2，-5%-3=-2.

算法题中常取余，%1000000007行，%(1e9+7)不行，因为1e9+7默认是double类型

### 逻辑运算符

&&

两边为真才为真，需注意前面为假后面的表达式不执行，为了速度

||

一边为真就为真，需注意前面为真后面的表达式不执行，为了速度

！

非

展开规则：非展开会改变内部符号，可拓展至多项，如

!(A&&B)=!A || !B !(A&&B&&C)=!A || !B || !C

!(A||B)=!A && !B !(A||B||C)=!A && !B && !C

中望题目![](test_assets/image_036.png)，等效a&&b&&c

### 三目运算符

a>b?a:b返回的是左值（占内存空间的变量）而不是右值（常量），即可以赋值（a>b?a:b）=100;这里a和b中大的那个被赋值100（一个if和else能完成的条件判断，需要简洁时用三目运算符）

C语言则返回右值

- c语言三目运算表达式返回值为数据值，为右值，不能赋值。

|  |
| --- |
| int a **=** 10**;**  int b **=** 20**;**  printf**(**"ret:%d\n"**,** a **>** b **?** a **:** b**);**  //思考一个问题，(a > b ? a : b) 三目运算表达式返回的是什么？    //(a > b ? a : b) = 100;  //返回的是右值 |

- c++语言三目运算表达式返回值为变量本身(引用)，为左值，可以赋值。

|  |
| --- |
| int a **=** 10**;**  int b **=** 20**;**  printf**(**"ret:%d\n"**,** a **>** b **?** a **:** b**);**  //思考一个问题，(a > b ? a : b) 三目运算表达式返回的是什么？  cout **<<** "b:" **<<** b **<<** endl**;**  //返回的是左值，变量的引用  **(**a **>** b **?** a **:** b**)** **=** 100**;**//返回的是左值，变量的引用  cout **<<** "b:" **<<** b **<<** endl**;** |

### 逗号表达式

逗号表达式，依次计算，整体的值为最后结果。

比如a=3\*5 , a\*4; 先计算a＝3\*5，所以a的值是15，再计算a\*4，由于没有再进行赋值运算，所以a的值还是15，不过整体表达式的值是60。

### 运算符优先级

说明：

同一优先级的运算符，运算次序由结合方向所决定。

#### C

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **优先级** | **运算符** | **名称或含义** | **使用形式** | **结合方向** | **说明** |
| 1 | [] | 数组下标 | 数组名[常量表达式] | 左到右 |  |
| () | 圆括号 | （表达式）/函数名(形参表) |  |
| . | 成员选择（对象） | 对象.成员名 |  |
| -> | 成员选择（指针） | 对象指针->成员名 |  |
| 2 | - | 负号运算符 | -表达式 | 右到左 | 单目运算符 |
| (类型) | 强制类型转换 | (数据类型)表达式 |  |
| ++ | 前置自增运算符 | ++变量名 | 单目运算符 |
| ++ | 后置自增运算符 | 变量名++ | 单目运算符 |
| -- | 前置自减运算符 | --变量名 | 单目运算符 |
| -- | 后置自减运算符 | 变量名-- | 单目运算符 |
| \* | 取值运算符 | \*指针变量 | 单目运算符 |
| & | 取地址运算符 | &变量名 | 单目运算符 |
| ! | 逻辑非运算符 | !表达式 | 单目运算符 |
| ~ | 按位取反运算符 | ~表达式 | 单目运算符 |
| sizeof | 长度运算符 | sizeof(表达式) |  |
| 3 | / | 除 | 表达式/表达式 | 左到右 | 双目运算符 |
| \* | 乘 | 表达式\*表达式 | 双目运算符 |
| % | 余数（取模） | 整型表达式/整型表达式 | 双目运算符 |
| 4 | + | 加 | 表达式+表达式 | 左到右 | 双目运算符 |
| - | 减 | 表达式-表达式 | 双目运算符 |
| 5 |  | 左移 | 变量 | 左到右 | 双目运算符 |
| >> | 右移 | 变量>>表达式 | 双目运算符 |
| 6 | > | 大于 | 表达式>表达式 | 左到右 | 双目运算符 |
| >= | 大于等于 | 表达式>=表达式 | 双目运算符 |
|  | 小于 | 表达式 | 双目运算符 |
|  | 小于等于 | 表达式 | 双目运算符 |
| 7 | == | 等于 | 表达式==表达式 | 左到右 | 双目运算符 |
| != | 不等于 | 表达式!= 表达式 | 双目运算符 |
| 8 | & | 按位与 | 表达式&表达式 | 左到右 | 双目运算符 |
| 9 | ^ | 按位异或 | 表达式^表达式 | 左到右 | 双目运算符 |
| 10 | | | 按位或 | 表达式|表达式 | 左到右 | 双目运算符 |
| 11 | && | 逻辑与 | 表达式&&表达式 | 左到右 | 双目运算符 |
| 12 | || | 逻辑或 | 表达式||表达式 | 左到右 | 双目运算符 |
| 13 | ?: | 条件运算符 | 表达式1? 表达式2: 表达式3 | 右到左 | 三目运算符 |
| 14 | = | 赋值运算符 | 变量=表达式 | 右到左 |  |
| /= | 除后赋值 | 变量/=表达式 |  |
| \*= | 乘后赋值 | 变量\*=表达式 |  |
| %= | 取模后赋值 | 变量%=表达式 |  |
| += | 加后赋值 | 变量+=表达式 |  |
| -= | 减后赋值 | 变量-=表达式 |  |
|  | 左移后赋值 | 变量 |  |
| >>= | 右移后赋值 | 变量>>=表达式 |  |
| &= | 按位与后赋值 | 变量&=表达式 |  |
| ^= | 按位异或后赋值 | 变量^=表达式 |  |
| |= | 按位或后赋值 | 变量|=表达式 |  |
| 15 | , | 逗号运算符 | 表达式,表达式,… | 左到右 | 从左向右顺序运算 |

#### C++

|  |  |  |  |
| --- | --- | --- | --- |
| 运算符 | 描述 | 例子 | 可重载性 |
| **第一级别** |  |  |  |
| :: | 作用域解析符 | Class::age = 2; | 不可重载 |
| **第二级别** |  |  |  |
| () | 函数调用 | isdigit('1') | 可重载 |
| () | 成员初始化 | c\_tor(int x, int y) : \_x(x), \_y(y\*10){}; | 可重载 |
| [] | 数组数据获取 | array[4] = 2; | 可重载 |
| -> | 指针型成员调用 | ptr->age = 34; | 可重载 |
| . | 对象型成员调用 | obj.age = 34; | 不可重载 |
| ++ | 后自增运算符 | for( int i = 0; i < 10; i++ ) cout | 可重载 |
| -- | 后自减运算符 | for( int i = 10; i > 0; i-- ) cout | 可重载 |
| const\_cast | 特殊属性转换 | const\_cast(type\_from); | 不可重载 |
| dynamic\_cast | 特殊属性转换 | dynamic\_cast(type\_from); | 不可重载 |
| static\_cast | 特殊属性转换 | static\_cast(type\_from); | 不可重载 |
| reinterpret\_cast | 特殊属性转换 | reinterpret\_cast(type\_from); | 不可重载 |
| typeid | 对象类型符 | cout « typeid(var).name();  cout « typeid(type).name(); | 不可重载 |
| **第三级别**(具有右结合性) |  |  |  |
| ! | 逻辑取反 | if( !done ) … | 可重载 |
| not | ! 的另一种表达 |  |  |
| ~ | 按位取反 | flags = ~flags; | 可重载 |
| compl | ~的另一种表达 |  |  |
| ++ | 预自增运算符 | for( i = 0; i < 10; ++i ) cout | 可重载 |
| -- | 预自减运算符 | for( i = 10; i > 0; --i ) cout | 可重载 |
| - | 负号 | int i = -1; | 可重载 |
| + | 正号 | int i = +1; | 可重载 |
| \* | 指针取值 | int data = \*intPtr; | 可重载 |
| & | 值取指针 | int \*intPtr = &data; | 可重载 |
| new | 动态元素内存分配 | long \*pVar = new long;  MyClass \*ptr = new MyClass(args); | 可重载 |
| new [] | 动态数组内存分配 | long \*array = new long[n]; | 可重载 |
| delete | 动态析构元素内存 | delete pVar; | 可重载 |
| delete [] | 动态析构数组内存 | delete [] array; | 可重载 |
| (type) | 强制类型转换 | int i = (int) floatNum; | 可重载 |
| sizeof | 返回类型内存 | int size = sizeof floatNum;  int size = sizeof(float); | 不可重载 |
| **第四级别** |  |  |  |
| ->\* | 类指针成员引用 | ptr->\*var = 24; | 可重载 |
| .\* | 类对象成员引用 | obj.\*var = 24; | 不可重载 |
| **第五级别** |  |  |  |
| \* | 乘法 | int i = 2 \* 4; | 可重载 |
| / | 除法 | float f = 10.0 / 3.0; | 可重载 |
| % | 取余数(模运算) | int rem = 4 % 3; | 可重载 |
| **第六级别** |  |  |  |
| + | 加法 | int i = 2 + 3; | 可重载 |
| - | 减法 | int i = 5 - 1; | 可重载 |
| **第七级别** |  |  |  |
|  | 位左移 | int flags = 33 | 可重载 |
| >> | 位右移 | int flags = 33 >> 1; | 可重载 |
| **第八级别** |  |  |  |
|  | 小于 | if( i < 42 ) … | 可重载 |
|  | 小于等于 | if( i | 可重载 |
| > | 大于 | if( i > 42 ) … | 可重载 |
| >= | 大于等于 | if( i >= 42 ) ... | 可重载 |
| **第九级别** |  |  |  |
| == | 恒等于 | if( i == 42 ) ... | 可重载 |
| eq | == 的另一种表达 |  |  |
| != | 不等于 | if( i != 42 ) … | 可重载 |
| not\_eq | !=的另一种表达 |  |  |
| **第十级别** |  |  |  |
| & | 位且运算 | flags = flags & 42; | 可重载 |
| bitand | &的另一种表达 |  |  |
| **第十一级别** |  |  |  |
| ^ | 位异或运算 | flags = flags ^ 42; | 可重载 |
| xor | ^的另一种表达 |  |  |
| **第十二级别** |  |  |  |
| | | 位或运算 | flags = flags | 42; | 可重载 |
| bitor | |的另一种表达 |  |  |
| **第十三级别** |  |  |  |
| && | 逻辑且运算 | if( conditionA && conditionB ) … | 可重载 |
| and | &&的另一种表达 |  |  |
| **第十四级别** |  |  |  |
| || | 逻辑或运算 | if( conditionA || conditionB ) ... | 可重载 |
| or | ||的另一种表达 |  |  |
| **第十五级别**(具有右结合性) |  |  |  |
| ? : | 条件运算符 | int i = (a > b) ? a : b; | 不可重载 |
| **第十六级别**(具有右结合性) |  |  |  |
| = | 赋值 | int a = b; | 可重载 |
| += | 加赋值运算 | a += 3; | 可重载 |
| -= | 减赋值运算 | b -= 4; | 可重载 |
| \*= | 乘赋值运算 | a \*= 5; | 可重载 |
| /= | 除赋值运算 | a /= 2; | 可重载 |
| %= | 模赋值运算 | a %= 3; | 可重载 |
| &= | 位且赋值运算 | flags &= new\_flags; | 可重载 |
| and\_eq | &= 的另一种表达 |  |  |
| ^= | 位异或赋值运算 | flags ^= new\_flags; | 可重载 |
| xor\_eq | ^=的另一种表达 |  |  |
| |= | 位或赋值运算 | flags |= new\_flags; | 可重载 |
| or\_eq | |=的另一种表达 |  |  |
|  | 位左移赋值运算 | flags | 可重载 |
| >>= | 位右移赋值运算 | flags >>= 2; | 可重载 |
| **第十七级别** |  |  |  |
| throw | 异常抛出 | throw EClass(“Message”); | 不可重载 |
| **第十八级别** |  |  |  |
| , | 逗号分隔符 | for( i = 0, j = 0; i < 10; i++, j++ ) … | 可重载 |

## 命名空间

### ::作用域运算符

通常情况下，如果有两个同名变量，一个是全局变量，另一个是局部变量，那么局部变量在其作用域内具有较高的优先权，它将屏蔽全局变量。

|  |
| --- |
| //全局变量  int a **=** 10**;**  void test**(){**  //局部变量  int a **=** 20**;**  //全局a被隐藏  cout **<<** "a:" **<<** a **<<** endl**;**  **}** |

程序的输出结果是a:20。在test函数的输出语句中，使用的变量a是test函数内定义的局部变量，因此输出的结果为局部变量a的值。

作用域运算符可以用来解决局部变量与全局变量的重名问题

|  |
| --- |
| //全局变量  int a **=** 10**;**  //1. 局部变量和全局变量同名  void test**(){**  int a **=** 20**;**  //打印局部变量a  cout **<<** "局部变量a:" **<<** a **<<** endl**;**  //打印全局变量a  cout **<<** "全局变量a:" **<<** **::**a **<<** endl**;**  **}** |

这个例子可以看出，作用域运算符可以用来解决局部变量与全局变量的重名问题，即在局部变量的作用域内，可用::对被屏蔽的同名的全局变量进行访问。

### 名字控制

创建名字是程序设计过程中一项最基本的活动，当一个项目很大时，它会不可避免地包含大量名字。c++允许我们对名字的产生和名字的可见性进行控制。

我们之前在学习c语言可以通过static关键字来使得名字只得在本编译单元内可见，在c++中我们将通过一种通过命名空间来控制对名字的访问。

#### C++命名空间(namespace)

在c++中，名称（name）可以是符号常量、变量、函数、结构、枚举、类和对象等等。工程越大，名称互相冲突性的可能性越大。另外使用多个厂商的类库时，也可能导致名称冲突。为了避免，在大规模程序的设计中，以及在程序员使用各种各样的C++库时，这些标识符的命名发生冲突，标准C++引入关键字namespace（命名空间/名字空间/名称空间），可以更好地控制标识符的作用域。

#### 命名空间使用语法

- 创建一个命名空间:

|  |
| --- |
| **namespace** A**{**  int a **=** 10**;**  **}**  **namespace** B**{**  int a **=** 20**;**  **}**  void test**(){**  cout **<<** "A::a : " **<<** A**::**a **<<** endl**;**  cout **<<** "B::a : " **<<** B**::**a **<<** endl**;**  **}** |

- - 命名空间只能全局范围内定义（**以下错误写法**）

|  |
| --- |
| void test**(){**  **namespace** A**{**  int a **=** 10**;**  **}**  **namespace** B**{**  int a **=** 20**;**  **}**  cout **<<** "A::a : " **<<** A**::**a **<<** endl**;**  cout **<<** "B::a : " **<<** B**::**a **<<** endl**;**  **}** |

- - 命名空间中变量的重复定义问题

|  |
| --- |
| test.h中  #pragma once  namespace A{  int ma;  void func();  }  test.cpp中  #include "test.h"  main.cpp中  #include "test.h" |

- 命名空间可嵌套命名空间

|  |
| --- |
| **namespace** A**{**  int a **=** 10**;**  **namespace** B**{**  int a **=** 20**;**  **}**  **}**  void test**(){**  cout **<<** "A::a : " **<<** A**::**a **<<** endl**;**  cout **<<** "A::B::a : " **<<** A**::**B**::**a **<<** endl**;**  **}** |

- - 命名空间是开放的，即可以随时把新的成员加入已有的命名空间中，但只能在加入后使用

|  |
| --- |
| **namespace** A**{**  int a **=** 10**;**  **}**  **namespace** A**{**  void func**(){**  cout **<<** "hello namespace!" **<<** endl**;**  **}**  **}**  void test**(){**  cout **<<** "A::a : " **<<** A**::**a **<<** endl**;**  A**::**func**();**  **}** |

- 声明和实现可分离

![](test_assets/image_037.png)

|  |
| --- |
| #pragma once  **namespace** MySpace**{**  void func1**();**  void func2**(**int param**);**  **}** |

![](test_assets/image_038.png)

|  |
| --- |
| void MySpace**::**func1**(){**  cout **<<** "MySpace::func1" **<<** endl**;**  **}**  void MySpace**::**func2**(**int param**){**  cout **<<** "MySpace::func2 : " **<<** param **<<** endl**;**  **}** |

- 无名命名空间，意味着命名空间中的标识符只能在本文件内访问，相当于给这个标识符加上了static，使得其可以作为内部连接

|  |
| --- |
| **namespace{**    int a **=** 10**;**  void func**(){** cout **<<** "hello namespace" **<<** endl**;** **}**  **}**  void test**(){**  cout **<<** "a : " **<<** a **<<** endl**;**  func**();**  **}** |

- 命名空间别名

|  |
| --- |
| **namespace** veryLongName**{**  int a **=** 10**;**  void func**(){** cout **<<** "hello namespace" **<<** endl**;** **}**  **}**  void test**(){**  **namespace** shortName **=** veryLongName**;**  cout **<<** "veryLongName::a : " **<<** shortName**::**a **<<** endl**;**  veryLongName**::**func**();**  shortName**::**func**();**  **}** |

#### using声明

using声明可使得指定的标识符可用。

|  |
| --- |
| **namespace** A**{**  int paramA **=** 20**;**  int paramB **=** 30**;**  void funcA**(){** cout **<<** "hello funcA" **<<** endl**;** **}**  void funcB**(){** cout **<<** "hello funcA" **<<** endl**;** **}**  **}**  void test**(){**  //1. 通过命名空间域运算符  cout **<<** A**::**paramA **<<** endl**;**  A**::**funcA**();**  //2. using声明  **using** A**::**paramA**;**  **using** A**::**funcA**;**  cout **<<** paramA **<<** endl**;**  //cout << paramB << endl; //不可直接访问  funcA**();**  //3. 同名冲突  //int paramA = 20; //相同作用域注意同名冲突  **}** |

using声明碰到函数重载

|  |
| --- |
| **namespace** A**{**  void func**(){}**  void func**(**int x**){}**  int func**(**int x**,**int y**){}**  **}**  void test**(){**  **using** A**::**func**;**  func**();**  func**(**10**);**  func**(**10**,** 20**);**  **}** |

如果命名空间包含一组用相同名字重载的函数，using声明就声明了这个重载函数的所有集合。

#### using编译指令

using编译指令使整个命名空间标识符可直接使用.

|  |
| --- |
| **namespace** A**{**  int paramA **=** 20**;**  int paramB **=** 30**;**  void funcA**(){** cout **<<** "hello funcA" **<<** endl**;** **}**  void funcB**(){** cout **<<** "hello funcB" **<<** endl**;** **}**  **}**  void test01**(){**  **using** **namespace** A**;**  cout **<<** paramA **<<** endl**;**  cout **<<** paramB **<<** endl**;**  funcA**();**  funcB**();**  //不会产生二义性  int paramA **=** 30**;**  cout **<<** paramA **<<** endl**;**  **}**  **namespace** B**{**  int paramA **=** 20**;**  int paramB **=** 30**;**  void funcA**(){** cout **<<** "hello funcA" **<<** endl**;** **}**  void funcB**(){** cout **<<** "hello funcB" **<<** endl**;** **}**  **}**  void test02**(){**  **using** **namespace** A**;**  **using** **namespace** B**;**  //二义性产生，不知道调用A还是B的paramA  //cout << paramA << endl;  **}** |

|  |
| --- |
| **注意：使用using声明或using编译指令会增加命名冲突的可能性。也就是说，如果有名称空间，并在代码中使用作用域解析运算符，则不会出现二义性。** |

#### 命名空间使用

我们刚讲的一些东西一开始会觉得难一些，这些东西以后还是挺常用，只要理解了它们的工作机理，使用它们非常简单。

需要记住的关键问题是当引入一个全局的using编译指令时，就为该文件打开了该命名空间，它不会影响任何其他的文件，所以可以在每一个实现文件中调整对命名空间的控制。比如，如果发现某一个实现文件中有太多的using指令而产生的命名冲突，就要对该文件做个简单的改变，通过明确的限定或者using声明来消除名字冲突，这样不需要修改其他的实现文件。

## 预处理

### #include头文件

<>是系统文件，如string需要include标准库<string>；“”是自定义文件，#include “xxx.h”

编译器预处理阶段查找头文件的路径不同：

1.<>时，编译器直接从系统类库目录里查找头文件，如果类库目录下查找失败，编译器会终止查找。

2.“”时，编译器默认从当前文件所在目录下查找头文件，如果查找失败，再从项目工程中设置的头文件引用目录查找，在 Linux GCC 编译环境下，则一般通过使用 -L 参数指定引用目录，如果项目配置的头文件引用目录中仍然查找失败，再从系统类库目录里查找头文件。

头文件中声明类的全局变量和函数

头文件为了只编译一次防止重复编译，通常有两种手段

1. #pragma once
2. #ifndef ABCD\_H（代表头文件abcd.h）

#define ABCD\_H

…头文件其他部分

#endif // ABCD\_H

#### 循环引用问题

vs提示为 unknown override specifier

说明A文件中include了B文件，B文件中include了A文件

解决方案是把一处换成指针类型，然后就不用include头文件仅需进行类声明

<https://blog.csdn.net/stockholmrobber/article/details/81161546>

经验：进行类声明时，有命名空间记得声明在命名空间内，否则会重定义

### #define

#undef 取消宏的定义

c++中不建议使用宏（直接替换有的错误不好调试出来） -> 常量/枚举/内联->空间换时间

#### 1.不带参数的宏定义

又称为标识符定义

#定义 标识符 内容

#define name stuff

程序预处理阶段，编译器会将name替换为stuff

尽量不用不带参数的宏定义，const更好的实现其功能

const和#define区别总结:

|  |
| --- |
| 1. const有类型，可进行编译器类型安全检查。#define无类型，不可进行类型检查. 2. const有作用域，而#define是在预处理阶段替换，范围默认是定义处到文件结尾.如果定义在指定作用域下有效的常量，那么#define就不能用。 |

1. 宏常量没有类型，所以调用了int类型重载的函数。const有类型，所以调用希望的short类型函数？

|  |
| --- |
| #define PARAM 128  const short param **=** 128**;**  void func**(**short a**){**  cout **<<** "short!" **<<** endl**;**  **}**  void func**(**int a**){**  cout **<<** "int" **<<** endl**;**  **}** |

2. 宏常量不重视作用域.

|  |
| --- |
| void func1**(){**  const int a **=** 10**;**  #define A 20  //#undef A //卸载宏常量A  **}**  void func2**(){**  //cout << "a:" << a << endl; //不可访问，超出了const int a作用域  cout **<<** "A:" **<<** A **<<** endl**;** //#define作用域从定义到文件结束或者到#undef，可访问  **}**  int main**(){**  func2**();**  **return** EXIT\_SUCCESS**;**  **}** |

**问题:** 宏常量可以有命名空间吗？不能，作用域就是当前行到结尾，和命名空间无关

|  |
| --- |
| **namespace** MySpace**{**  #define NUM 1024  **}**  void test**(){**  //cout << MySpace::NUM << endl; // MySpace::1024非法  //int NUM = 100; //int 1024 = 100;报错  cout **<<** NUM **<<** endl**;**  **}** |

#### 2.带参数的宏定义（宏函数）

#定义 宏名(参数表) 内容

#define name( parament-list ) stuff

注意

1.参数列表的左括号必须与name紧邻

2.如果两者之间有任何空白存在，参数列表就会被解释为stuff的一部分

效果也是替换，如下

#define ADD(a,b) (a + b)

int main()

{

int a = 10;

int b = 20;

int sum = ADD(a, b);

printf("%d\n", sum);

return 0;

}

##### 与函数的区别

上面的宏定义相当于

int main()

{

int a = 10;

int b = 20;

int sum = (a + b);

printf("%d\n", sum);

return 0;

}

而直接使用函数是

int ADD(int x, int y)

{

return x + y;

}

int main()

{

int a = 10;

int b = 20;

int sum = ADD(a, b);

printf("%d\n", sum);

return 0;

}

区别是通过函数调用来实现求和，使用了新的函数栈帧。

优点：

1.对于简单计算，用于调用函数和从函数返回的代码可能比实际执行这个小型计算工作所需要的时间更多，所以宏比函数在程序的规模和速度方面更胜一筹（以空间换时间，适用于短小运算）

2.更为重要的是函数的参数必须声明为特定的类型。

所以函数只能在类型合适的表达式上使用。反之这个宏怎可以适用于整形、长整型、浮点型等可以用于>来比较的类型。宏是类型无关的

![](test_assets/image_039.png)

##### 用于运算时注意

#define SQUAREA(x) (x \* x)

#define SQUAREB(x) ((x) \* (x))

int main()

{

int ansa = SQUAREA(3 + 1);

int ansb = SQUAREB(3 + 1);

printf("%d\n%d\n", ansa, ansb);

return 0;

}

结果是

int ansa = (3 + 1 \* 3 + 1) // 7

int ansb = ((3 + 1) \* (3 + 1)) // 16

用于对数值表达式进行求值的宏定义都应该用这种方式加上括号，避免在使用宏时由于参数中的操作符或邻近操作符之间不可预料的相互作用

##### 被内联函数完美取代

```
#define COMAPD (x, y) (Gx) <(y)? Ge) = Gy)
inline int func(int x, int y)

{
return x < y ? x: yi

}

void test02()

{
inta=1;
int b = 3;
// ((++a) < (b) ? (+a) : (b))
//cout << “COMAPD(x, y)=" << COMAPD(++a, b) << endl; //
cout << “func=”" << fune(t+ta, b) << endl; //2
```

#### #和##

```
# 的 用 法 是 负责 将 其 后 面 的 东西 转化 为

int

Of

cout << TO_STRING(this is a

return @;

， 比 如 :

string) << endl;

这 段 代码

P，TO_STRING 宏 就 会 将 括号 上

的 内 容 转化 为 字符

生成 "this is a string"， 然 后 由 cout 输 出

0
```

```
Ht

才 是 连接 符 ， 将 前 后 两 个 东

接 成 一 个 词 。 比 如 :

Praia

IntVar(i) int_##i

int main(){

int int_1 = 1, int_2
cout << IntVar(1) << ", " << IntVar(2) << endl;

6

这 段 代 码 中 IntVar(1) 就 会 将 前 画

于 IntVar(2) 同 理 。

的 int 与 参数 1 连接 起 来 ， 成 为 int_1， 然 后

cout 输 出

Hint_1 变

对 应 的 值 1。 对
```

### 条件编译

#if 编译预处理中的条件命令，相当于C语法中的if语句

#ifdef 判断某个宏是否被定义，若已定义，执行随后的语句

#ifndef 与#ifdef相反，判断某个宏是否未被定义

#elif 若#if, #ifdef, #ifndef或前面的#elif条件不满足，则执行#elif之后的语句，相当于C语法中的else-if

#else 与#if, #ifdef, #ifndef对应, 若这些条件不满足，则执行#else之后的语句，相当于C语法中的else

#endif #if, #ifdef, #ifndef这些条件命令的结束标志

defined 　与#if, #elif配合使用，判断某个宏是否被定义

## 断言

### 宏控制

```
1, NDEBUG2 Standard C 中 定义 的 宏 ， 专 门 用 来 控制 assert() 的 行为 。 如 果 定 义 了 这 个 宏 ， 则 assert 不 会 起 作用 。

#ifdef NDEBUG
#define assert(x) ((void)0)

#else

2. C Standard 中 规定 了 assert 以 宏 来 实现 。<assert.h> 被 设计 来 可 以 被 多 次 包含 ， 其

由 NDEBUG 宏 来 决定 其 行为 。 如 :

一 上 来 就 undef assert， 然 后
```

### assert()

是个函数，但由于一般仅debug下使用，release是要屏蔽掉的，所以常写成宏

检查表达式值是否为0，0就先向stderr打印一条出错信息，然后调用abort()

运行时检查，对性能有影响

### static\_assert(,)

static\_assert（常量表达式，要提示的字符串）；

如果第一个参数常量表达式的值为false，会产生一条编译错误，错误位置就是该static\_assert语句所在行，第二个参数就是错误提示字符串。

然后通过调用 abort 来终止程序运行。

使用范围：

static\_assert可以用在全局作用域中，命名空间中，类作用域中，函数作用域中，几乎可以不受限制的使用。

作用时机：

编译器在遇到一个static\_assert语句时，通常立刻将其第一个参数作为常量表达式进行演算

用编译器来强制保证一些契约，并帮助我们改善编译信息的可读性

常用于模板：

如果该常量表达式依赖于某些模板参数，延迟到模板实例化时再进行演算，这就让检查模板参数成为了可能

可以确保类型符合要求

性能方面：

由于是static\_assert编译期间断言，不生成目标代码，因此static\_assert不会造成任何运行期性能损失。

## 编译过程

![](test_assets/image_044.png)

![](test_assets/image_045.png)

![](test_assets/image_046.png)

![](test_assets/image_047.png)

![](test_assets/image_048.png)

## 关键字

### new

主要讲new失败的处理，不用new直接万事大吉

set\_new\_handler(func)，指定new出异常时的错误处理函数，func为nullptr时就是默认的抛异常

自定义func需要满足以下原则：

### static

全局/局部静态变量：

定义：在变量前面加上static关键字。直到程序结束，静态变量始终会维持前值

存储区域：初始化的静态变量会在数据段分配内存，未初始化的静态变量会在BSS段分配内存，都在静态存储区

作用域：C++里作用域可分为6种：全局，局部，类，语句，命名空间和文件作用域。静态全局变量：全局作用域+文件作用域，所以无法在其他文件中使用。静态局部变量：局部作用域，只被初始化一次，直到程序结束

生命周期：程序结束时回收内存

类中静态成员变量：

定义：在变量前面加上static关键字。直到程序结束，静态变量始终会维持前值

存储区域：初始化的静态变量会在数据段分配内存，未初始化的静态变量会在BSS段分配内存，都在静态存储区。类中的static静态数据成员拥有一块单独的存储区，而不管创建了多少个该类的对象。所有这些对象的静态数据成员都共享这一块静态存储空间。

作用域：被隐藏在类的内部，即仅有类作用域。

生命周期：超出类作用域时回收内存

静态变量只能在本源文件中使用

静态变量初始化时间：

C++，全局/静态对象当且仅当对象首次用到时才进行构造；

C，全局/静态变量初始化发生在任何代码执行之前，属于编译期初始化。

![](test_assets/image_049.png)

静态函数：

定义：在函数返回类型前加上static关键字，函数即被定义为静态函数。也可定义类中的静态成员函数

存储区域：静态成员函数也是类的一部分，而不是对象的一部分。所有这些对象的静态数据成员都共享这一块静态存储空间。

静态成员函数使用注意：当调用一个对象的非静态成员函数时，系统会把该对象的起始地址赋给成员函数的this指针。而静态成员函数不属于任何一个对象，因此C++规定静态成员函数没有this指针（划重点，面试题常考）。既然它没有指向某一对象，也就无法对一个对象中的非静态成员进行访问。

静态函数只能在本源文件中使用

### Inline（内联函数）

宏函数缺点

1.带参数的宏定义易出现不可预知的出错

2.C++预处理器不允许访问类的成员，也就是说预处理器宏不能作用在类的成员函数上

3.无法限定作用域

内联函数为了继承宏函数的效率，没有函数调用时开销，然后又可以像普通函数那样，可以进行参数，返回值类型的安全检查，又可以作为成员函数。

定义在头文件

定义内联函数，在函数名前面放置关键字inline，那么在编译时编译器会把该函数的代码副本放置在每个调用该函数的地方，省去调用函数的开销，因此有以下特性：

1. 内联函数很短，过长直接作为正常函数即可
2. 必须直接定义在头文件![](test_assets/image_050.png)
3. 对内联函数进行任何修改，都需要重新编译函数的所有客户端，因为编译器需要重新更换一次所有的代码，否则将会继续使用旧的函数

非强制

inline对编译器只是建议，实际不可控，编译器可能会忽略 inline ，也可能加上inline。

忽略inline的情况：

1.函数体过大

2.存在过多的条件判断语句

3.对函数进行取址操作

4.存在while、switch

5.存在递归（函数内调用自身）

```
include <iostream>

using namespace std;

inline int Max(int x, int y)
{
return (x > y)? x: 中

A) 程序 的 主 图 数
int main( )

cout << "Max (20,10): " << Max(20,10) << endl;

cout << "Max (0,200): " << Max(0,200) << endl;

cout << "Max (100,1010): * << Max(100,1010) << endl;
return 05
```

### const

#### const修饰变量

const修饰的变量变成常量，注意要初始化（顶层const就是指向初始化）

与C语言区别很大

```
1 语言 的 const 修 饰 的 变量 都 有 空间
2.C 语 言 的 const 修 饰 的 全 局 变量 具有 外 部 链接 属性
3.C++ 语 言 的 const 修 饰 的 变量 有 时 有 空间 ， 有 时 没有 空间 ( 发 生 常量 折 和 又， 上 且 没 有 对 变量 进行 取 址 操作 )

1
2

9
10
cay
12
13
14
15
16

18

19
20

const int aa = 10;// 没 有 内 存

void test01()

a

// BET RES
cout << “aa=" << aa << end];// 在 编译 阶段 编译 器 : cout<<"aa="<<10<<end1;

// 茜 止 优化 volati1e

//volatile const int bb = 20;//#K

const int bb = 20;

int *p = (int*)&bb;// 进 行 了 取 址 操作 ， 所 以 有 空间
*p = 200; 这 里 与 C 一 样 都 是 伪 常 重 可 以 间接 修改

cout << "bb=" << bb << end];//cout << “bb=" << 20 << endl;

cout << *p << endl;

cout << "a 的 地 址 =”<< (int)&bb << endl;
cout << “p 指 向 的 地 址 ”<< (int)p << end];
```

常量折叠就是编译器直接把变量改成数值，即编译器进行了优化（这个过程发生在编译阶段），在下列情况编译器不进行优化

a.volatile修饰变量

b.使用另一变量初始化

```
int a = 10;

const int b = a;// 如 果 用 变量 给 const 修 饰 的 局 部 变量 赋值 ， 那 么 编译 器 不 会 优化
int #p = (int*)&b;

*p = 100;

cout << “b=” << b << endl;

cout << “*p=” << &p << endl:
```

c.自定义数据类型编译器无法替换

```
// 自 定义 数据 类 型 ， 编 译 器 不 能 优化

astruct Maker

{
1 Maker ()// 构 造 函数

{

a = 100;
}
int a;
```

```
void test02()

{

7

// 数 据 类 型 定义 变量

// 类 实例 化 对 象

const Maker ma;

cout << ma.a << endl;

Maker *p = (Maker*) &ma;

p-a = 200;

cout << maa << endl;// 没 有 优化 ， 因 为 不 能 优化 自 定 义 数据 类 型
```

![](test_assets/image_056.png)

文件1中

![](test_assets/image_057.png)

文件2中

![](test_assets/image_058.png)

文件1中不加extern时文件2无法访问c，添加extern后可以

#### const修饰指针

1. const int \*p=&a;或int const \*p=&a;，指针的指向可以改（p=&b;），不能p指向的内存（\*p=20;报错），即底层const/常量指针

```
int Main\) 1

‘const chark p = “abc”;
\__char* ¢ = (char*)p;
MEE ='s: &
‘cout <<
```

需注意换别的指针来修改这块内存也会报错

1. int \* const p=&a;，指针的指向不能改（p=&b;报错），指针指向的值可以改（\*p=20），即顶层const/指针常量
2. const\*不能通过指针改值，\*const指针指向不能改。也可以const int \* const p=&a使指针不能改，也不能通过指针改值

```
geo

. const int a; // 指 的 是 a 是 一 个 常量 ， 不 允许 修改 。

const int +a; 7/a 指 针 所 指向 的 内 存 里 的 值 不 变 ， 即 (+a) 不 变
int const +a; // 同 const int +a;

int tconst ai /ya 指针 所 指向 的 内 存 地 址 不 变 ， 即 a 不 变

，const int +const ai; //ABAZE, BY (+a) 不 变 ，a 也 不 变
```

#### const修饰函数参数

常常给函数的参数列表中的引用参数加上const来防止修改引用的参数：

1. 传入的引用对象不能改
2. 引用对象被const修饰了，const对象只能调用const函数，这里非常容易报错

```
void printDeque\const deque<int? ad)

for (deque<int>::const_iterator it = d.begin(); it != d.end(); it++)
{ 一 -一

1 Vsit = 100: 修 改 报错

i cout 人 Csit 《CC “:

}

cout << endl;
```

#### const修饰成员函数

**见类封装部分**

![](test_assets/image_062.png)

### Constexpr

设置为编译阶段求值，即字面量。方便该值的同时，不会分配内存，不会有宏难调试的问题

#### 一、在普通函数中的使用

```
#include <iostream>

int Getlen(int a, int b)

{
|

return a + b;

aint main()
{

int array[Getlen(1, 2)];

return 0;
} https:/folog.esdn.netlyao_hou
```

```
#include <iostream>

iconstexpr int Getlen(int a, int b)

{
|

return a + b;

aint main()
{

int array[Getlen(1, 2)];

return 0;
} https://blog.csdn.netlyao_hou
```

数组的大小必须是常量，在声明数组array时，用函数返回值会报错。用constexpr关键字可以解决这种问题

```
当然 ，constexpr 修 饰 的 函数 也 有 一 定 的 限制 :
(1) 函数 体 尽量 只 包含 一 个 returmn 语 句 ， 多 个 可 能 会 编译 出 错 ;
(2) 函数 体 可 以 包含 其 他 语句 ， 但 是 不 能 是 运行 期 语句 ， 只 能 是 编译 期 语句 ;

编译 器 会 将 constexpr 函 数 视 为 内 联 函 数 ! 所 以 在 编译 时 若 能 求 出 其 值 ， 则 会 把 函数 调用 共 换 成 结果 值 。
```

#### 二、在构造函数中

constexpr还能修饰类的构造函数，即保证传递给该构造函数的所有参数都是constexpr，那么产生的对象的所有成员都是constexpr。该对象是constexpr对象了，可用于只使用constexpr的场合。

注意constexpr构造函数的函数体必须为空，所有成员变量的初始化都放到初始化列表中。

```
#include <iostream>
using namespace std;

class Test

{

public:
constexpr Test(int numl, int num2) : mnum1(num1), m_num2(num2)
{

public:
int
int mnum2;
```

```
class Test

public:
constexpr Test(int numl, int num2) : m_numl(numl), m_num2(num2)

cout << “hello C++ 11”;

public:
int m_numl;
int m_num2;
```

#### 三、const和constexpr修饰指针的差别

（1）const 变量的初始化可以延迟到运行时，而 constexpr 变量必须在编译时进行初始化。所有 constexpr 变量均为常量，因此必须使用常量表达式初始化。

（2）constexpr和指针

与const不同，在constexpr声明中如果定义了一个指针，限定符constexpr仅对指针有效，与指针所指对象无关。

constexpr是一种很强的约束，更好的保证程序的正确定语义不被破坏；编译器可以对constexper代码进行非常大的优化，例如：将用到的constexpr表达式直接替换成结果, 相比宏来说没有额外的开销。

#### 四、对引用的修饰

简单的说constexpr所引用的对象必须在编译期就决定地址。

```
int g_tempa =
const int g_conTempa = 4;
constexpr int g_conexprTempA =

int main(void)
{
int tempA = 4;
const int conTempA = 4;
constexpr int conexprTempA = 4;
YI. ERE, BIRR)
const int &conptrA = tempA;
const int &conptrB = conTempA;
const int &conptrc = conexprTempA;

(2. SBPAG: —BASRDEE, FR BRIERE, — BconexprPtrBRconexprPtrCiwix*constexpr const #L, MiFF
constexpr int &conexprPtrA = tempA;

constexpr int &conexprPtrB = conTempA;

constexpr int &conexprPtrc = conexprTempA;

[*3. 8 -TREBT, BBP PBT, BEB 8conexprPtré FconexprPtrF Wiz sconstexpr const #P*/
constexpr int &conexprPtrD = g_tempA;

constexpr int &conexprPtr— = g_conTempA;

constexpr int &conexprPtrF = g_conexprTempA;

[*4, ERE, BARB)

constexpr const int &conexprConPtrD = g_tempA;
constexpr const int &conexprConPtre = g_conTempA;
constexpr const int &conexprConPtrF = g_conexprTempA;

return 0;
```

还有一个奇葩的地方就是可以通过上例conexprPtrD来修改g\_tempA的值，也就是说constexpr修饰的引用不是常量，如果要确保其实常量引用需要constexpr const来修饰

### auto

auto 仅仅是一个占位符，C++ 中的变量必须是有明确类型的，只是这个类型是由编译器自己推导出来的（所以必须初始化），在编译器期间它会被真正的类型所替代。

#### 用途

1. 代替冗长复杂的变量声明(最常用，在for中或者用于替换迭代器)

```
list<int> 11;
11. push_back (1) ;
11. push_back (2);
11. push_back (3);

for (lis
cout
cout

nt>::iterator i = U1.begin(); i!= U.end(); is+){
i.operator->() << endl;
“i << endl;

CaAYVAMAWNHE
```

常用for(auto& i:v)，偶尔见到auto&&（万能引用），既可以引用左值也可以引用右值

2. 定义模板参数时，用于声明依赖模板参数的变量

```
_Ty>

v= xy;
std::cout << v;

OuaWNR
```

3. 模板函数依赖于模板参数的返回值

![](test_assets/image_071.png)

#### 易错

auto 不能作用于类的非静态成员变量（也就是没有 static 关键字修饰的成员变量）中，因为不会初始化

auto 关键字不能定义数组，但可以定义指针

auto可以用作函数返回值

auto 不能用作函数参数，因为编译的时候会根据函数名和参数列表生成对应的符号，这时参数变量类型不确定，所有没法生成符号，所有编译阶段会报错

auto 无法推导出模板参数

（没什么用但要知道的）与const结合使用

```
1. auto 和 const 的 结合 使 用
(1) auto 与 const 结合 的 用 法
a 当 类 型 不 为 引用 时 ，auto 的 推导 结果 将 不 保留 表达 式 的 const 属性 ;
b. 当 类 型 为 引用 时 ，auto 的 推导 结果 将 保留 表达 式 的 const 属性 。
```

```
(2) 程序 实例 下

int x= 0
const auton = xi yn 为 const int ，auto 被 推导 为 int
auto f =n; 7 为 const int, auto 被 推导 为 int (const 属性 被 抽 弃 )

const auto @rl = x; //r1 为 const int& 类 型 ，auto 被 推导 为 int
auto &r2 = rl; //rl 为 const int& 类 型 ，auto 被 推导 为 const int 类 型
a. 第 2 行 代码 中 ，n 为 const int，auto #HES int,
b 第 3 行 代码 中 ，n 为 const int 类 型 ， 但 是 auto 却 被 推导 为 int 类 型 ， 这 说 明 当 = 右 边 的 表达 式 带 有 const 属性 时 ，auto 不 会 ”使 用 const 属性 ， 而 是 直接 推 导出 non-const 类 型 。
< 第 4 行 代码 中 ，auto 被 推导 为 int 类 型 ， 这 个 很 容易 理解 ， 不 再 整 述 。
d 第 5 行 代码 中 ，r1 是 const int & 类 型 ，auto 也 被 推导 为 const int 类 型 ， 这 说 明 当 const 和 引用 结合 时 ，auto 的 推导 将 保留 ”表达 式 的 const 类 型 。
```

### final

![](test_assets/image_074.png)

### override

```
rtual void fun(int a,

publ.

const override

就 说 明 override 关 键 字 可 上 误 。
注意 ， 在 重新 写 虚 函 数 的 时 候 ， 必 须 三 同 返回 值 ， 同 函数 名 ， 同 参数 列表 ， 并 且 const
在 上 面 的 代码 中 ， 如 果 类 Base 中 函数 没有 virtual， 这 就 是 同名 隐藏 ( 重 定义 )。

， 这 叫做 虚 函数 的 同名 覆盖 ( 重 写 )。
```

### typedef

typedef 为C语言的关键字，作用是为一种数据类型定义一个新名字，这里的数据类型包括内部数据类型（int，char等）和自定义的数据类型（struct等）。

typedef 本身是一种存储类的关键字，与 auto、extern、static、register 等关键字不能出现在同一个表达式中。

只有老代码用，新的全用using

#### 语法

在传统的变量声明表达式里，用（新的）类型名替换变量名，然后把关键字 typedef 加在该语句的开头就可以了。

简单示例（给int起名）：

【第一步】：int a; ———— 传统变量声明表达式

【第二步】：int myint\_t; ———— 使用新的类型名myint\_t替换变量名a

【第三步】：typedef int myint\_t; ———— 在语句开头加上typedef关键字，myint\_t就是我们定义的新类型

高级示例（给某函数指针起名）：

【第一步】：void (\*pfunA)(int a); ———— 传统变量（函数）声明表达式

【第二步】：void (\*PFUNA)(int a); ———— 使用新的类型名PFUNA替换变量名pfunA

【第三步】：typedef void (\*PFUNA)(int a); ———— 在语句开头加上typedef关键字，PFUNA就是我们定义的新类型

实际上只有第三步写在代码中

#### 作用

简化一些比较复杂的类型声明，如函数指针类型PFunCallBack，可以方便的定义多个函数指针变量

typedef void (\*PFunCallBack)(char\* pMsg, unsigned int nMsgLen);

更重要的是，当函数的参数是另一个函数时，用函数指针类型简化

RedisSubCommand(const string& strKey, PFunCallBack pFunCallback, bool bOnlyOne);

不简化的形式如下，较长

RedisSubCommand(const string& strKey, void (\*pFunCallback)(char\* pMsg, unsigned int nMsgLen), bool bOnlyOne);

#### 与#define的区别

使用 typedef 定义的变量类型，其作用范围限制在所定义的函数或者文件内（取决于此变量定义的位置），而宏定义则没有这种特性。

通常，使用 typedef 要比使用 #define 要好，特别是在有指针的场合里。

![](test_assets/image_076.png)

```
3.1 示例 2

代码 如 下
1 | typedef char *pstr;
2 | char string[5]="test";
3 | const char *pi=string;
4 | const pStr p2=string;
5 pl++;
6 pas;

在 编译 过 程 中 ， 报 错 如 下

根据 上 述 错误 信息 能 够 看 出 ，p2 为 只 读 常 旦 ， 所 以 p2++ 出 错 了 。 这 个 问题 再 一 次 提醒 我 们 : typedef 和 #define 不 同 ，typedef 不 是 简
单 的 文本 蔷 换 ， 上 述 代码 中 const pStr p2 并 不 等 于 const char * p2, pStr 是 作为 一 个 类 型 存在 的 ， 所 以 const pStr p2 实际 上 是 限制 了
pStr 类 型 的 p2 变量 ， 对 p2 常 旺 进 行 了 只 读 限 制 。 也 就 是 说 ，const pStr p2 和 pStr const p2 本 质 上 没有 区 别 (可 类 比 constint p2 和 int
const p2) ， 都 是 对 变量 p2 进行 只 读 限制 ， 只 不 过 此 处 变量 p2 的 数据 类 型 是 我 们 自己 定义 的 pStr， 而 不 是 系统 固有 类 型 (如 int) 而
已 。

所 以 ，const pStr p2 的 含义 是 : 限定 数据 类 型 为 char * 的 变量 p2 为 只 读 ， 因 此 p2++ 错

注意 : 在 本 示例 中 ，typedef 定义 的 新 类 型 与 编译 系统 固有 的 类 型 没有 差别 。
```

### using

功能和typedef一样都是给类型起别名，但在模板中非常好用

```
使 用 typedef 重 定义 类 型 是 很 方便 的 ， 但 它 也 有 一 些 限制 ， 比 如 ， 无 法 重 定义 一 个 模板 。
想 杀 下 面 这 个 场景:

typedef std:map<std:string, int> map_int

Mm
typedef std:map<std:string, std:string> map_str_t;
Mm
我 们 需要 的 其 实 是 一 个 固定 以 std:string 为 key 的 map， 它 可 以 映射 到 int 或 另 一 个 std:-string。 然 而 这 个 简单 的 需求 仅 通 过 typedef 却 很 难 办 到 -

因此 ， 在 C++98/03 中 往往 不 得 不 这 样 写 :

Ol. template <typenane Yal>

02, struct str_map

03.

04. typedef std::map(std::string, Val> type
05. }

06. fee

07. str_mapint>::type mapl

0B fee

一 个 虽然 简单 但 却 略 显 烦琐 的 str map 外 数 类 是 必要 的 。 这 明显 让 我 们 在 复 用 草 些 泛 型 代码 时 非常 难受 。
```

```
Ol. template <typenane Yal>
02, using str_nap_t = std::ap(std::string, Val>
03. .

04.。 str_map_tGint> mapl

这 里 使 用 新 的 Using 别名 语法 定义 了 std:map 的 模板 别名 str map_t。 比 超前 面 使 用 外 囊 模 板 加 typedef 构建 的 str_ map， 它 完全 就 像 是 一 个 新 的 map 类 模板 ， 因 此 ， 简 洁 了 很 多 .
```

```
01.
02.
03.
04.
05.
08.
07.
08.
09.
to.
i.
12.
13.

J* CH9B/03 +
template <typenane T>
struct func_t
{

typedef void (*type) (T, T)
}
// 使 用 func_t 模板
func_t¢int>::type xx_l
ye cH #/
template <typenane T>
using fane t = void (*) (1, T)
// 使 用 func_t 模板

fanc_tcinty xx_2
```

模板别名不是类

```
需要 注意 的 是 ，Using 语法 和 typedef 一 样 ， 并 不 会 创造 新 的 类 型 。 也 就 是 说 ， 上 面 示例 中 C++11 的 using 写法 只 是 typedef NSM. B%M using 重 定义 的 func_t 是 一 个 模板 ， 但 func t<int> 定义 的 xx_2 并 不 是 一 个 由 类 模板 实例 化 后 的 类 ， 而 是
void(*)(int, int) 的 别名 。

因此 ， 下 面 这 样 写 :

void foo(void (*unc_call)(int, int);
void foo(func t<int> func call); // error: redefinition

同样 是 无 法 实现 重 载 的 ，func_t<int> AS void(*)(int, int) 类 型 的 等 价 物 -

细心 的 读者 可 以 发 现 ，Using 重 定义 的 func t 是 一 个 模板 ， 但 它 既 不 是 类 模板 也 不 是 函数 模板 (函数 模板 实例 化 后 是 一 个 函数 ) ， 而 是 一 种 新 的 模板 形式 : 模板 别名 (alias template) -
```

### Explicit

```
class Point {
public:
int x, y3
Point(int x = 0, int y = 0)

+ x(x), y(y) {}

void displayPoint(const Point& p)
{

cout << "(" << p.x <<

<< pey << ")" << endl;

int main()
{
displayPoint(1);
Point p = 13
```

这里的displayPoint（1）是隐式调用Point构造函数。声明explicit后，禁止隐式调用构造函数，建议所有构造函数都声明为explicit

```
class Point {
public:
int x, y3
explicit Point(int x = 0, int y = 0)

+ x(x), y(y) {}

void displayPoint(const Point& p)
{

cout << "(" << p.x <<
<< pey << ")" << endl;

int main()

{
displayPoint(Point(1));
Point p(1);
```

要这么写

### Noexcept

#### 为什么？

```
void func() throw (int,double);

上 例 就 是 一 个 函数 异常 声明 列表 ， 该 声明 指出 fnc 可 能 抛 出 int 和 double 类 型 的 异常 。 但 是 在 实
际 编程 中 很 少 使 用 这 种 写法 ， 所 以 这 一 特性 在 C+ + 11 中 被 抛 奔 。 另 外 ， 如 果 异 常 声明 列表 写成 如
下 形式 :

void func() throw();

这 种 写法 表示 函数 func 不 抛 出 任何 异常 ， 而 这 种 写法 在 c+ +11 中 被 新 的 关键 字 noexcept 异常
声明 所 取代 。
```

#### 语法

```
语法 上 noexcept 修饰 符 有 两 种 形式 ， 一 种 就 是 简单 地 在 函数 声明 后 加 上 noexcept 关键 字 。 比
如 :

void func() noecept;

另外 一 种 形式 则 是 接受 一 个 常量 表达 式 (参阅 《常量 表达 式 》) 作为 参数 ， 如 下 所 示 :

void func() noexcept( 常 量 表达 式 );

常量 表达 式 的 结果 会 被 转换 成 一 个 bool 类 型 的 值 ， 该 值 为 true， 表 示 函 数 不 会 抛 出 异常 ， 反 之 则
可 能 抛 出 异常 。 而 不 带 常量 表达 式 的 noexcept
相当 于 声明 了 noexcept(true)， 即 不 会 抛 出 异常 。
```

#### 作用：

1. noexcept 可以用来阻止异常的传播和扩散，有异常会调用 std::terminate 中断程序的执行从而阻止了异常的继续传播。
2. ![](test_assets/image_086.png)
3. noexcept 更大的用处就是保证程序的安全。因此出于安全考虑,C++11 标准中类的析构函数默认为 noexcept(true)。

## 内存分区

### 分区模型

![](test_assets/image_087.png)

32位系统中，每一个进程都有一块8G的虚拟内存，，分区如下：

代码区为RO权限；

全局区分为data段和bss段都是RW权限，注意bss除了未初始化还有初始化为0的全局变量；

共享区为共享库加载位置

环境变量就是各种寻找路径，如LD\_LIBRARY\_PATH等

命令行参数就是main函数的argv参数

![https://uploadfiles.nowcoder.com/images/20220225/4107856_1645788015668/798C7A2D023204559B62F88B54E35CBB](test_assets/image_088.png)

![](test_assets/image_089.png)

![](test_assets/image_090.png)

### 代码区

程序运行前就有

### 全局区

程序运行前就有

全局变量在所有函数外，全部函数都能调用，放在全局区；局部变量在函数内，只能在函数内调用，放在栈区；

静态变量为static修饰的局部变量，超出作用域后不会被释放，但也不能被调用，放在全局区（而且类的静态函数和静态变量和类本身相关但与类对象无关，不需要new类也有；静态变量只能在类中声明，在类外定义，类外定义时不能标static）

常量分为字符串和const修饰的变量，超出作用域被释放。字符串放在全局区，const修饰的全局变量在全局区，const修饰的局部变量在栈区

另一种分区模型分为bss和data段，见分区模型

### 栈区

程序运行后才有，每个函数有一个栈帧，由编译器自动分配和释放，存放函数形参、局部变量和临时量（栈基和栈顶）

![](test_assets/image_091.png)

![](test_assets/image_092.png)栈基使栈帧释放时栈顶能回到对应位置

栈结构，先进后出

使用一级缓存速度很快

需要注意函数不要返回函数中局部变量的地址，因为函数运行完局部变量的空间就被释放（虽然现在的编译器会保留直到你使用一次）

### 堆区

程序运行后才有

由程序员来分配和释放，若不释放则程序结束时操作系统自动回收，所以不delete或free也会释放

类似于数组结构

使用二级缓存速度比一级缓存慢

用法：

int \*p=new int(10);即在堆区开辟了int的空间，初始值为10，返回的是这块空间的地址

delete p;释放堆区的这个空间，再访问会报错没有访问权限

int \*arr=new int[10];即在堆区开辟了一个含有10个int大小的空间，返回的是这块空间的地址

delete[] arr;释放堆区的这个空间，再访问会报错没有访问权限，注意删除数组要有【】

为什么用new而不用malloc：因为new构造对象会调用构造函数，malloc不会

同理delete会调用析构函数而free不会

```
日

}

};

public:

Maker ()
{
cout 《《“ 构 造 函 数 ”《〈《 endl;
}
“Maker ()
{

cout << “Prey HRL” << endl;

Bvoid test01()

Maker *m = (Maker*)malloc (sizeof (Maker) ) |
```

![](test_assets/image_094.png)

```
void test02()

Maker *m = aie:
```

![](test_assets/image_096.png)

delete 指针，指针的类型需要是正确的类指针（父类指针的话，若子类有开辟堆区空间，父类析构得是虚函数）

```
//3. delete void*®] fe, 不 会 调用 对 象 的 析 构 函数
void test03()

void *m = new Maker;

// 如 果 用 void# 来 接 new 的 对 象 ， 那 么 delete 时 不 会 调用 析 构 函数
delete m;

1 // 在 编译 阶段 ， 那 么 编译 器 就 确定 好 了 函数 的 调用 地 址 ，
/VC++ 编 译 器 不 认识 voidk, 不 知道 void# 指 向 那个 函数 ， 所 有 不 会 调用 析 构 函数
// 这 种 编译 方式 叫 静 态 联 编
```

![](test_assets/image_098.png)显然没有调用析构函数

C相关malloc、calloc、realloc、free：

void \*calloc(size\_t n, size\_t size)，在堆区/自由存储区（两种说法都有）中分配n个长度为size的连续空间，函数返回一个指向分配起始地址的指针；如果分配不成功，返回NULL（注意一定要判断是否为NULL，否则分配空间失败将导致内存溢出）。动态分配完内存后，自动初始化该内存空间为零。

malloc与calloc的区别是不初始化，里边数据是随机的垃圾数据。

释放堆区空间用free（指针）

```
1.1.17 说 说 new 和 malloc 的 区 别 ， 各 自 底层 实现 原理 。

1. new 是 操作 符 ， 而 malloc 是 函数 。

2. new 在 调用 的 时 候 先 分 配 内存 ， 在 调用 构造 函数 ， 释 放 的 时 候 洞 用 析 构 函 数 ; 而 malloc 没 有 构造 函数 和 析 构 函数 。

3. malloc 需 要 给 定 申请 内 存 的 大 小 ， 返 回 的 指针 需要 强 转 ;，new 会 调用 构造 函数 ， 不 用 指定 内 存 的 大 小 ， 返 回 指针 不 用 温 转 。
4 new 可 以 被 重 载 ; malloc 不 行

5.new 分 瑟 内 存 更 直接 和 安全 。

6. new 发 生 错 误 扫 出 异常 ，malloci 反 回 null

答案 解析

malloc 底 层 实现 : 当 开辟 的 空间 小 于 128K 时 ， 调 用 brk () 函数 ; 当 开 尽 的 空间 大 于 128K 时 ， 调 用 mmap () 。malloc 采 用 的 是
内 存 池 的 管理 方式 ， 以 减少 内 存 碎片 。 先 申请 大 块 内 存 作为 堆 区 ， 然 后 将 堆 区 分 为 多 个 内 存 块 。 当 用 户 申请 内 存 时 ， 直 接 从 堆 区 分
配 一 块 合适 的 空闲 快 。 采 用 隐 式 链表 将 所 有 空闲 块 ， 每 一 个 空闲 块 记录 了 一 个 未 分 配 的 、 连 续 的 内 存 地 址 。

new 底 层 实现 : 关键 字 new 在 洞 用 构造 孙 妆 的 时 候 实际 上 进行 了 如 下 的 几 个 步骤:
1. BUREN

2 HOSEA ERR Nar (BLtAnIS HTT BRS)

3 执行 构造 函数 中 的 代码 (为 这 个 新 对 象 添加 属性 )

4
```

### 内存对齐

```
1.2.9 (RACH ATS

内 存 对 齐 应 用 于 三 种 数据 类 型 中 : structiclass/union

struct/class/union 内 存 对 齐 原则 有 四 个 :

1 数据 成 员 对 章 规则 : 结构 (struct) 或 联合 (union) 的 数据 成 员 ， 第 一 个 数据 成 员 放 在 ofkset 为 0 的 地 方 ， 以 后 每 个 数据 成 员 存 储 的 起 始 位 置 要 从 该 成 员 大 小 或 者 成 员 的 子 成 员 大 小 的 整数 倍 开始 。

2. 结构 体 作为 成 员 - 如 果 一 个 结构 里 有 某 些 结构 体 成 员 , 则 结构 体 成 员 要 从 其 内 部 ' 量 之 基本 类 型 成 员 的 整数 售 地址 开始 存储 。(struct a 里 存 有 struct bb 里 有 charint ,double 等 元 素 , 那 b 应 该 从 8 的 整数 倍 开始 存储 )。

3 . 收尾 工作 结构 体 的 总 大 小 ， 也 就 是 sizeof 的 结果 ， 必 须 是 其 内 部 最 大 成 员 的 "最 完 基 本 类 型 成 员 的 整数 倍 。 不 足 的 要 补 齐 。 (基本 类 型 不 包括 structiclass/uinon)。

4 sizeoftunion)， 以 结构 里 面 size 最 大 元 素 为 union 的 size， 因 为 在 某 一 时 刻 ，union 只 有 一 个 成 员 真正 存储 于 该 地 址 。

答案 解析

1 什么 是 内 存 对 齐 ?
那么 什么 是 字 节 对 齐 ? 在 C 语 言 中 ， 结 构 休 是 一 种 复合 数据 类 型 ， 其 构成 元 素 既 可 以 是 基本 数据 类 型 (如 int、long、float 等 ) 的 变量 ， 也 可 以 是 一 些 复合 数据 类 型 (如 数组 、 结 构 体 、 联 合体 等 ) 的 数据 单元 。
在 结构 体 中 ， 编 译 器 为 结构 体 的 每 个 成 员 按 其 自然 边界 (alignment) 分 配 空间 。 各 个 成 员 按照 它们 被 声明 的 顺序 在 内 存 中 顺序 存储 ， 第 一 个 成 员 的 地 址 和 整个 结构 体 的 地 址 相同 。
为 了 使 CPU 能 够 对 变量 进行 快速 的 访问 ， 变 量 的 起 始 地 址 应 该 具有 某 些 特性 ， 即 所 谓 的 “对齐 "， 比 如 4 字 节 的 int 型 ， 其 起 始 地 址 应 该 位 于 4 字 节 的 边界 上 ， 即 起 始 地 址 能 够 被 4 整除 ， 也 即 对 齐 跟 数 据 在 内 存 中
的 位 置 有 关 。 如 果 一 个 变量 的 内 存 地 址 正好 位 于 它 长 度 的 整数 倍 ， 他 就 被 称 做 自然 对 齐 。
比如 在 32 位 cpu 下 ， 假 设 一 个 整 型 变量 的 地 址 为 0x00000004( 为 4 的 信 数 )， 那 它 就 是 自然 对 齐 的 ， 而 如 果 其 地 址 为 0x00000002 ( 非 4 的 信 数 ) 则 是 非 对 齐 的 。 现 代 计算 机 中 内 存 空间 都 是 按照 byte 划 分 的 ， 从 理
论 上 讲 似乎 对 任何 类 型 的 变量 的 访问 可 以 从 任何 地 址 开始 ， 但 实际 情况 是 在 沪 问 特 十 类 型 变量 的 时 候 经 党 在 特定 的 内 存 地 址 访问 ， 这 就 需要 各 种 类 型 数据 按照 一定 的 规则 在 空间 上 排列 ， 而 不 是 | 抽 闻 的 一 个 接
一 个 的 排 改 ， 这 就 是 对 齐 。

2 为 什么 要 宁 节 对 齐 ?
需要 字 节 对 齐 的 根本 原因 在 于 CPU 访问 数据 的 效率 问题 。 假 设 上 面 整 型 变量 的 地 址 不 是 自然 对 齐 ， 比 如 为 0x00000002， 则 CPU 如 果 取 它 的 值 的 话 需要 访问 两 次 内 存 ， 第 一 次 取 从 0x00000002-0x00000003 的
一 个 short， 第 二 次 取 从 0x00000004-0x00000005 的 一 个 short 然 后 组 合 得 到 所 要 的 数据 ， 如 果 变 量 在 0x00000003 地 址 上 的 话 则 要 访问 三 次 内 存 ， 第 一 次 为 char， 第 二 次 为 short， 第 三 次 为 char， 然 后 组 合 得 到
整 型 数据 。
而 如 果 变 量 在 自然 对 齐 位 置 上 ， 则 只 要 一 次 就 可 以 取出 数据 。 一 些 系统 对 对 齐 要 求 非常 严格 ， 比 如 sparc 系 统 ， 如 果 取 未 对 齐 的 数据 会 发 生 错误 ， 而 在 x86 上 就 不 会 出 现 错误 ， 只 是 效率 下 降 。
各 个 硬件 平台 对 存储 空间 的 处 理 上 有 很 大 的 不 同 。 一 些 平台 对 某 些 特定 类 型 的 数据 只 能 从 某 些 特定 地 址 开始 存 取 。 比 如 有 些 平台 每 次 读 都 是 从 偶 地 址 开始 ， 如 果 一 个 in 卉 (假设 为 32 位 系统 ) 如 果 存 放 在 偶 地

址 开始 的 地 方 ， 那 么 一 个 读 周期 就 可 以 读 出 这 32bit， 而 如 果 存 放 在 奇 地 址 开始 的 地 方 ， 就 需要 2 个 读 周期 ， 并 对 两 次 读 出 的 结果 的 高 低 字 节 进 行 拼凑 才能 得 到 该 32bi 族 据 。 显 然 在 读 取 效 率 上 下 降 很 多 。
3 字 节 对 齐 实例
union example { int a[5]; char b; double c; }; int result = sizeof(example);  /* 如 果 以 最 长 20 字 节 为 惟 ， 内 部 double 占 8 字 节 ， 这 段 内 存 的 地 址 0x00000020 并 不 是 aou
ble 的 整数 倍 ， 只 有 当 最 小 为 0x00000024 时 可 以 满足 整除 double〈8Byte) 同时 又 可 以 容纳 int a[5] 的 大 小 ， 所 以 正确 的 结果 应 该 是 result=24 +/ struct example { int a[5]; char b;
double c;  } test_struct; int result = sizeof(test_struct);  /* 如 果 我 们 不 考虑 字 节 对 齐 ， 那 么 内 存 地 址 0x0021 不 是 double〈8Byte) 的 整数 倍 ， 所 以 需要 字 节 对 齐 ， 那 么 此 时 满足 是 doub1
e (SByte) 的 整数 倍 的 最 小 整数 是 0z0024， 说 明 此 时 char b 对 齐 int 扩 充 了 三 个 字 节 。 所 以 最 后 的 结果 是 resul */ struct example { char b; double ci int a; — } test_struct;

满足 一 个 条 件 ， 那 就 是 占用 的 内 存 空 间 太 小 需要 是 结构 体 中 占用 最 大 内 存 空间 的 类 型 的 整

int result = sizeof (test_struct);  /* 字 节 对 齐 除了 内 存 起 始 地 址 要 是 数据 类 型 的 整数 们 以外， 还
数 倍 ， 所 以 20 不 是 double (8Byte) 的 整数 倍 ， 我 们 还 要 扩充 四 个 字 节 ， 最 后 的 结果 是 result=24 +/
```

上面的两个例子都是对的，注意每一个成员都要从其整数倍开始

### 内存顺序

![](test_assets/image_101.png)

没搞懂似乎和多线程有关

### 内存泄漏

```
3. ARISE:

什么 是 内 存 泄露?
简单 地 说 就 是 申请 了 一 块 内 存 空间 ， 使 用 完毕 后 没有 释放 挤 。 (1) new 和 malloc 申 请 资源 使 用 后 ， 没 有 用 delete 和 free 释 放 ; (2)】 子 类 继承 父 类 时 ， 父 类 析 构 函数 不 是 虚 函 数 。 (3) Windows 句 柄 资源 使 用 后 没有 释放 。
怎么 检测 ?

第 一 : 良好 的 编码 习惯 ， 使 用 了 内 存 分 瑟 的 函数 ， 一 旦 使 用 充 毕 ,要 记得 使 用 其 相应 的 函数 释放 掉 。

第 二 : 将 分 醒 的 内 存 的 指针 以 链表 的 形式 自行 管理 ， 使 用 完毕 之 后 从 链表 中 删除 ， 程 序 结束 时 可 检查 改 链 表 .。
B=: 使 用 智能 指针 。

第 四 : 一 些 常见 的 工具 插件 ， 如 ccmalloc、Dmalloc、Leaky、Valgrind 等 等 .
```

### 其他常见内存错误

![](test_assets/image_103.png)

### 程序启动过程

![](test_assets/image_104.png)

### 虚拟内存

关于虚拟4G内存的描述和解析：

一个进程用到的虚拟地址是由内存区域表来管理的，实际用不了4G。而用到的内存区域，会通过页表映射到物理内存。

所以每个进程都可以使用同样的虚拟内存地址而不冲突，因为它们的物理地址实际上是不同的。内核用的是3G以上的1G虚拟内存地址，

其中896M是直接映射到物理地址的，128M按需映射896M以上的所谓高位内存。各进程使用的是同一个内核。

首先要分清“可以寻址”和“实际使用”的区别。

其实我们讲的每个进程都有4G虚拟地址空间，讲的都是“可以寻址”4G，意思是虚拟地址的0-3G对于一个进程的用户态和内核态来说是可以访问的，而3-4G是只有进程的内核态可以访问的。并不是说这个进程会用满这些空间。

其次，所谓“独立拥有的虚拟地址”是指对于每一个进程，都可以访问自己的0-4G的虚拟地址。虚拟地址是“虚拟”的，需要转化为“真实”的物理地址。

好比你有你的地址簿，我有我的地址簿。你和我的地址簿都有1、2、3、4页，但是每页里面的实际内容是不一样的，我的地址簿第1页写着3你的地址簿第1页写着4，对于你、我自己来说都是用第1页（虚拟），实际上用的分别是第3、4页（物理），不冲突。

内核用的896M虚拟地址是直接映射的，意思是只要把虚拟地址减去一个偏移量（3G）就等于物理地址。同样，这里指的还是寻址，实际使用前还是要分配内存。而且896M只是个最大值。如果物理内存小，内核能使用（分配）的可用内存也小。

## 随机数

rand()生成随机数，可以通过运算来处理随机数如rand()%100来生成0-99的随机数，注意这是伪随机

要真随机得在执行rand()前的非循环位置声明：srand((unsigned int)time(NULL));

然后rand()生成的就是根据时间的随机数。

为了尽量避免产生相同的随机数，可以通过除以浮点10来带上小数点

(rand()%401+600）/10.f

## 属性说明符

用来给编译器下指令的

```
C++ 标准 只 定义 了 如 下 的 attributes (C++20 及 之 前 ) :

*， [[noreturn]]
* [[carries_ dependency]]
* [[deprecated]]
* [[deprecated("reason")]]
* [[fallthrough]]

* [[nodiscard]]

* [[nodiscard("reason"]
* [[maybe_unused]]

* [[likely]]

* [[unlikely]]

* [[no_unique_address]
```

### Noreturn

```
1, [[noreturn]]

用 于 指明 函数 不 会 返回 。 这 个 返回 指 的 不 是 返回 值 (比如 void 什么 的 ， 不 然 void 不 就 足够 了
吗 ? ) ， 而 指 的 是 该 函数 不 会 返回 到 调用 它 的 地 方 。 也 就 是 说 ， 程 序 执行 到 该 函数 里 的 时 候 ， 要 么
一 直 在 该 函数 里 循环 下 去 ， 要 么 退出 程序 ， 总 之 控制 流 不 会 回 到 调用 它 的 地 方 。

回

这 样 做 的 好 处 有 两 个 ， 一 是 可 以 告诉 编译 器 做 出 更 好 的 优化 ， 二 是 给 出 合适 的 编译 告警 (或 者 避免
误 报 警告 ) ， 比 如 :

[[noreturn]]
void myAbort(){
std: :exit(a);
+
int (bool b){
if (b) {
return 7030;
} else {
myAbort() 5
}

如 果 myAbort(0 不 带 有 [[noreturn]] 的 话 ， 程 序 编译 就 会 告警 : warning: control reaches end of
non-void function [-Wreturn-type]。

SEinE, tvGEehl PBA [Inoreturn]]ixfattribute:

° Exit
abort

* exit

quick_exit
terminate
rethrow_exception
rethrow_nested
throw_with_nested
longjmp
```

### Deprecated

```
3, [[deprecated]]

表明 不 推荐 使 用 此 属性 声明 的 名 称 或 实体 ， 即 虽然 允许 使 用 ， 但 由 于 某 种 原因 不 鼓励 使 用 。 有 两 种

* [[deprecated]]
* [[deprecated(‘reason")]]: 参数 就 是 加 个 解释 ， 说 明 不 鼓励 的 原因

这 个 attribute 可 以 用 在 下 列 地 方 :

class/struct/union: struct [[deprecated]] S

typedef-name: [[deprecated]] typedef S* PS. using PS [[deprecated]] = S*
variable: [[deprecated]] int x

non-static data member: union U { [[deprecated]] int n; }

function: [[deprecated]] void f()

namespace: namespace [[deprecated]] NS { int x; }

enumeration: enum [[deprecated]] E {}

enumerator: enum { A [[deprecated]], B [[deprecated]] = 42 }

template specialization: template<> struct [[deprecated]] X<int> {}
```

效果是编译时warning，实测效果是error

```
deprecated] ]
void gemfield1() {
stdz:clog << "gemfield1.\n";

deprecated("Use gem2() instead.")]]
void gemfield2() {
stdz:clog << "gemfield2.\n";

deprecated("Use gemfield4(int).")]]
int gemfield3(int x) {
return x * 2;

int main()

{
gemfield1();
gemfield2();

gemfield.cpp: In function ‘int main()?:
gemfield.cpp:115:14: warning: ‘void gemfieldi()’ is deprecated [-wdeprecated-declarat:
115 gemfield1();

gemfield.cpp:99:6: note: declared here
99 | void gemfield1() {

gemfield.cpp:116:14: warning: ‘void gemfield2()’ is deprecated: Use gem2() instead. [-
116 gemfield2();

gemfield.cpp:104:6: note: declared here
104 | void gemfield2() {

ae »
```

### Fallthrough

```
4, [[fallthrough]]

只 能 用 于 switch 语 句 中 ， 表 明 从 前 一 个 case 标 签 中 没有 中 断 是 故意 的 ， 不 应 由 编译 器 给 出 告警 的 诊
断 。 举 例 :

void g(){}
void h(){}
void i(){}
void f(int n)
{
switch (n){
case 1:
case 2:
a()5
[[fallthrough]];
case 3: // no warning on fallthrough
h()s
case 4: // compiler may warn on fallthrough
if (n < 3){
i103
[[fallthrough]]; // ok
jelse {
return;
t
case 5:

while (false){
[[fallthrough]]; // *@#ill-formed: next statement is not part of th
+

case 6:
[[fallthrough]]; // ill-formed, attribute ‘fallthrough’ not preceding a ca

了
}
4 >

gemfield.cpp: In function ‘void f(int)?:
gemfield.cpp:25:28: warning: attribute ‘fallthrough’ not preceding a case label or def
```

### Nodiscard

```
5, [[nodiscard]]

可 以 出 现在 函数 声明 、 枚 举 声明 、class 声 明 中。 在 下 列 的 使 用 场景 中 ， 如 果 代码 中 没有 接收 返回
值 ， 则 编译 器 将 告警 :

。 带 nodiscard 声 明 的 函数 被 调用 时 ;
。 当 函 数 的 返回 值 为 带 nodiscard 声 明 的 enumeration 或 class， 该 函数 被 调用 时 ;
+ 带 nodiscard 的 构造 函数 被 显 式 类 型 转换 触发 调用 时 。

struct Vector{
bool empty() const{return true;} // iy iB rtrue
a

int main()

{
Vector vec;
vec.empty();

在 上 面 的 程序 中 ，empty( 方 法 是 用 来 判断 是 否 为 空 的， 但 使 用 的 地 方 却 误 认为 是 清空 的 动作 。 而
编译 器 不 知道 你 的 意图 ， 译 是 没 问题 的 。 但 是 ， 如 果 class 的 作者 加 上 [[nodiscard]]:

struct Vector{

[[nodiscard]] bool empty() const{return true;} // “4 P/l/i/aJtrue
a
那么 程序 将 会 告警 :

gemfield.cpp:8:14: warning: ignoring return value of ‘bool vector::empty() const’, dec
8 | vec.empty();
```

一般还要写明原因

```
你 甚至 还 可 以 使 用 新 语法 : [[nodiscard("reason"] ， 代 码 如 下 所 示 :

struct Vector{
[[nodiscard (“may be what you want is clear()?")]] bool empty() const{return true;
a

4

这 样 在 编译 的 时 候 可 以 给 出 更 友好 的 提示 。
```

### Maybeunused

```
6, [[maybe unused]]

对 于 未 使 用 的 entities， 避 免 编译 器 给 出 告警 。 为 什么 会 有 这 种 需求 呢 ? 举 个 例子 :

#include <cassert>

[[maybe_unused]] void f([[maybe_unused]] bool thing1, [[maybe_unused]] bool thing2)

{
[[maybe_unused]] bool genfield = thing1 && thing2;

cteisttj

int main() {}

4

在 release 模 式 中 ，assert 会 被 优化 掉 ， 于 是 布尔 变量 gemfield 就 没有 被 使 用 。 但 由 于 声明 了
[[maybe_unused]]， 编 译 器 不 会 给 出 警告 。

这 个 属性 的 使 用 场景 还 有 :

。 class/struct/union: struct [[maybe_unused]] S;

typedef: [[maybe_unused]] typedef S* PS; 、 using PS [[maybe_unused]] = S*;
variable: [[maybe_unused]] int x;

non-static data member: union U { [[maybe_unused]] int n; };

function: [[maybe_unused]] void f();

enumeration: enum [[maybe_unused]] E {};

enumerator: enum { A [[maybe_unused]], B [[maybe_unused]] = 42 };
structured binding: [[maybe_unused]] auto [a, b] = std::make_pair(42, 0.23);
```

没用的变量不警告

### Likely and unlikely

用来告诉编译器，代码的哪条分支路径更有可能执行。这样就可以优化程序执行速度。

```
namespace with_attributes {
constexpr double pow(double x, long long n) noexcept {
if (n > 0) [[likely]]
return x * pow(x, n - 1)5
else [[unlikely]]
return 1;
+
constexpr long long fact(long long n) noexcept {
if (n > 1) [[likely]]
return n * fact(n - 1);
else [[unlikely]]
return 1;
```

### No\_unique\_address

可以优化掉class中非静态数据成员所占用的空间。但这需要有个前提条件，就是该成员本身为空。

```
struct Empty {}; // empty class
struct x {
int i;
Empty e;
a
struct Y {
int i;
[[no_unique_address]] Empty e;

3
struct z {
char c3
[[no_unique_address]] Empty e1, e2;
3
struct w {
char c[2];
[[no_unique_address]] Empty e1, e2;
3
int main()
{

++ HM. X60

static_assert(sizeof(Empty) >= 1);

no_unique_addres

Vike

std::cout << "sizeof(Y) == sizeof(int) is " << std::boolalpha << (sizeof(Y)

4 el Ail e2 万 为 类 T, Ppl sia 7, Kitétxid [[[no_unique_address]]

c

static_assert(sizeof(Z) >= 2);
```

![](test_assets/image_115.png)

# 面向对象

范围解析运算符 ::

类Box定义中声明了函数double getWidth( void );但没有定义，在外面定义这个函数时需要用::，如下

double Box::getWidth(void)

{

return width ;

}

查看某个类数据结构的方法：

1. 打开开始菜单vs目录下的开发者命令提示符（developer command prompt）

![](test_assets/image_116.png)

1. 进入存放cpp文件的磁盘，如输入F:
2. 进入存放cpp文件的目录，如输入cd F:\VS项目\多态\，进入后显示目录下的文件
3. 输入c1 /d1 reportSingleClassLayout类名 “定义类的cpp文件名”，如下

![](test_assets/image_117.png)

1. 查看类的数据结构

```
:AMYS 项 目 \ 多 态 \ 多 态 >cl /dl 全 人生 “01 多 态 基本 概念 . cpp”
x86 的 Microsoft (R) C/C++ 优化 纺 时 15. 26732. 1 版
权 所 有 (Cj Microsoft Corporation。 保 留

01 多 态 基本 概念 . cpp

C:\Program Files _(x86)\Microsoft Visual_Studio\2017\Commumity\VC\Tools\MSVC\14. 15. 26726\include\:

530: (RANT C++ SORANISIE, CRGRRITEL. WHEE /Elisc

class Animal size):
二 -一

0 | fvtptr}
i

Animal: :$vftable@:
&Animal_meta
0

0 &Animal: :speak

Animal::speak this adjustor: 0
Microsoft (R) Incremental Linker Version 14. 15. 26732. 1
Copyright (C) Microsoft Corporation. All rights reserved.

Here 01 Senin, exe”
1 多 态 基 本 概念 .obj

F:\VWSINA\ SSA
```

## 类封装

class 类名:public 父类

{

public:

对外接口

private:

私有成员

};注意这个分号易漏

类包括成员属性（成员变量）和成员行为（成员函数、成员方法，都是内联函数）

### 访问权限

类内可以访问所有成员，无论是何种权限，如类内函数可以访问所有变量；

类对象（也就是类外）只能访问public部分成员，private和protected部分无法访问；

```
class Basic
{

public:

1
wore

Jint main() {
\__ Basic basic;
cout << basic. ma << basic.mb << basic.

t
```

可见通过对象访问m\_b和m\_c报错了

一般变量都是private，然后提供一些public的函数给外界获取或者修改这些变量，通过函数可以判断用户输入的参数是否合法，直接让用户修改则不行

类访问修饰符

类中的变量一般是private，外部无法直接访问，即类名.变量名会报错（默认，不声明private也可）

类中的函数一般是public，供外部访问，一般通过这些函数来访问private变量

protected（受保护）成员变量或函数与私有成员十分相似，但有一点不同，protected（受保护）成员在派生类（即子类）中是可访问的。

### class和struct区别

```
1. struct 一 般 用 于 描述 一 个 数据 结构 集合 ， 而 class 是 对 一 个 对 象 数据 的 封装 ;
2. struct 中 默认 的 访问 控制 权限 是 public 的 ， 而 class 中 默认 的 访问 控制 权限 是 private 的 ， 例 如 :

struct A{ int iNum, // 默认 访问 控制 权限 是 public } class B{ int iNum，// 默认 访问 控制 权限 是 private }

3. 在 继承 关系 中 ，struct 默认 是 公有 继承 ， 而 class 是 私有 继承 ;
4. Class 关键 字 可 以 用 于 定义 模板 参数 ， 就 像 ypename， 而 struct 不 能 用 于 定义 模板 参数 ， 例 如 :

template<typename T，typename Y> // 可 以 把 typename 换 成 class int Func(const T& t, const Ye y) {

//T0D0 ]
```

### 构造

#### 构造函数调用

分为括号调用，显示调用，隐式转换调用。

```
JA, BSE

//Person pl; // 默 认 构 造 函数 调用
//Person p2(10) ; // 有 参 构 造 函数
//Person p3(p2) ; // 措 贝 构造 函数

// 注 意 事项

// 调 用 默认 构造 函数 时 候 ， 不 要 加 ()

ae AIDE Ace: 编译 器 会 认为 是 一 个 函数 的 声明 , 不 会 认为 在 创建 对 象
/Person pl(
```

错误过：

1.加()这里错误认为调用了默认构造

2.Person p[10];定义数组时调用了10次默认构造，错误认为一次也没有调用

```
@E-\e-Sa@| p2sssneune 了 全 Ri
ABRRERECIs) Pe 53

ee ee eee /2、 显 示 法
NOMA 55 Person pl;
ee 56 Person p2 = Person(10) ; 参 构造
一 57 Person p3 = Person(p2); /拷贝 构造
«Ho 58
, ogeemrearl 59 | //Person(10); // 匿名 对 象 A: 当前 行 执行 结束 后 ， 系 统 会 立即 回收 掉 匿 名 对 象
人 60 /cout << “aaaaa” << endl;
61
62 fo /注意 事项 2
63 // 不 要 利用 拷贝 构造 函数 初始 化 匿名 对 象 ” 编 译 器 会 认为 Person (p3) === Person p3;
= 64 Person (p3)|;
65
66 /3、 隐 式 转换 法

SE [foe [a Seo] OwE0 [|| em inelisence —- PoE
i ie 项 目 ee
€ ©2085 “Person p3- BEN Nemesis 02 构造 男 数 的 分 类 及 调用 ,
```

无参构造不给对象命名，类名()，会返回一个匿名对象在当前行能够正常使用；

```
//3、 隐 式 转换 法
Person p4 = O§ // 相当 于 ST Person p4 = Person(10); “有 参 构造
Person p5 JI/ 拷贝 构造
```

有参构造只有一个参数或后面的参数有默认值时才能隐式转换

```
class Maker
{
public:

explicit Maker (int n)

{

}
};

int main()

{
Maker m = 10;
```

可以通过对有参构造函数声明explicit限定符，来禁止编译器进行隐式转换

#### 深拷贝与浅拷贝（有申请堆区空间时）

浅拷贝就是默认的拷贝构造函数，把变量值都复制一遍，这就会导致下面的问题：

![](test_assets/image_125.png)

拷贝后两个类实例的m\_Height都指向堆区的某个地址，然而析构时第一个析构的就释放了这个堆区地址，后面的重复释放会出错

深拷贝要程序员自己写，重新申请一块堆区空间

```
ral a emg
(SEL RC RA
St (a Height |= NULL)
t

Height = NOLL,
Person p2(p1)

如 果 利 用 编译 器 提供 的
PENI, SANK
找 贝 操作

son HELE” <

int # mH

推 区

sismmpRSVARS AANA SeEMATER
SETTER
```

#### 初始化列表

类名(): 变量A(值), 变量B(值), 变量C(值)

```
onan :m_A(10), m_B(20), m_C(30)
{
|

il
```

成员是基本数据类型

```
Maker2 (int a, int b,int c) :bmw(a), bui(b, c)
{

}

cout << “Maker2#9i#” << endl;
```

成员是自定义数据类型

注意：

1.初始化列表只能写在构造函数

2.如果一个构造函数使用了初始化列表，所有构造函数都要写初始化列表

3.初始化列表中还能有父类的构造

![](test_assets/image_129.png)

#### =delete

1.有时候不允许有拷贝构造、赋值构造、默认构造等函数，但编译器会自动实现，可以使用=delete禁止

```
1
2
3
4
5
6
7
8
9

fe ee ae ee ee
BSRSSSUSRERSES

// copy-constructor using delete operator
#include <iostream>
using namespace std;

class A {
public:
A(int x): m(x) { }

// Delete the copy constructor

A(const A&) = delete;
// Delete the copy assignment operator
A& operator=(const A&) = delete;
int m
+
int main() {

A al(1), a2(2), a3(3);

// Error, the usage of the copy assignment operator is disabled
al = a2;

// Error, the usage of the copy constructor is disabled

a3 = A(a2);

return 0;
```

2. 删除正常成员函数或非成员函数可防止有问题的类型导致调用非预期函数

```
不 需要 的 参数 转换

1| // type conversion using delete operator

2 | #include <iostream>

3 | using namespace std;

4| class a {

5 | public:

6 A(int) {}

7

8 // Declare the conversion constructor as a deleted function. without this step,
9 // even though A(double) isn't defined, the A(int) would accept any double value
10 // for it's argumentand convert it to an int

11 A(double) = delete;

12 |};

13 | int main() {

14 A AL(1);

15 // Error, conversion from double to class A is disabled.

16 A A2(100.1);

17 return 0;

18 | }
```

3.只能第一次出现时=delete

![](test_assets/image_132.png)

#### 委托构造与继承构造

委托构造函数是同一个类中不同构造函数之间的复用，注意

1.实际是链式结构，因此在调用过程中不能形成一个闭环

2.如果要进行多层构造函数的链式调用，建议将构造函数的调用的写在初始列表中而不是函数体内部，否则编译器会提示形参的重复定义

继承构造函数是派生类对父类构造函数的复用

1.继承父类的构造函数

2.在子类中使用父类的隐藏函数（即与子类函数同名但不是虚函数）

```
class Basef

public:
Base(){}
Base(int max1){
‘this->bmax = maxl > 9 ? maxl : 100;
了
Base(int max1, int min1){
‘this->bmax = maxl > 9 ? maxl : 100;//7:
‘this->bmin = minl > © ss mini < maxl ? minl :
了
Base(int maxl，int mini, int mid1){
‘this->bmax = maxl > 9 ? maxl : 100;//7:
‘this->bmin = minl > © ss minl < maxl ? mini : 0;//7
this->bmid = midl > min ss midi < maxl ? midi : 50;
了
int bmax;
int bmin;
int bmid;
7/ 委 磊 西 数 优化
class Basel{
publi
Basel() {}
Basel(int max1){
‘this->bmax = maxl > 9 ? maxl : 100;
了
Basel(int maxl，int min1) :Basel(max1){
this->bmin = minl > © && minl < max1 ? mini : 0;
了
Basel(int maxl，int min1，int mid1):Basel(max1, min1){
this->bmid = midl > minl ss midl < maxl ? midi : 50;
了
int bmax;
int bmin;
int bmid;
1/1 St, 简 TEBLS
class Child:public Basel{

publi
using Basel: :Basel;
hi
int main(){
Basel base = Base1(90, 30, 60);
cout << “min: " << base.bmin << ", middle: " << base.bmid <<",
Child ch = child(80, 20, 40);
cout << “min: " << ch.bmin << ", middle:
system("pause") ;
return 0;

"<< ch.bmid << ", max:

max: " << base.bmax << endl;

"<< ch.bmax << endl;
```

### 析构

析构函数：

1.没有返回值也不写void；

2.函数名为~类名；

3.无参数，不可以重载；

4.对象销毁时，编译器自动调用析构

5.必须是共有权限，需要在类外调用析构对象

6.不写编译器会自动添加默认析构函数，空实现

注意析构函数中不应该有异常：

1.尽量把可能抛异常的函数放到前面执行

2.如果无法避免有抛异常的函数，应该在虚构函数内部try-catch

3.执行完构造函数的对象，析构时才会自动调用析构函数，所以构造函数也不能被异常中断

### 构造与析构调用顺序

构造：

成员类对象构造函数（如有多个成员类对象，构造函数调用顺序为这些成员类的定义顺序）－＞自身构造函数

析构：

自身析构函数->成员类对象析构函数（有多个成员类对象时，跟构造相反的顺序）

详见下面继承部分

### static静态成员

![](test_assets/image_134.png)

静态成员函数

不需要实例也能访问（所以静态函数只能访问静态成员变量，普通成员函数则可以访问静态与非静态成员变量）

可以通过实例化的对象来访问，也可以直接通过类名：：函数名访问，所以常用于create

静态函数同样受访问权限的控制

静态成员变量

在编译阶段分配内存，不需要实例化就分配在全局区，所有对象共享同一份数据（包括子类）

可以通过对象名.变量名访问，也可以直接通过类名：：变量名访问，即不需要实例也能访问；

初始化要在类外，且不能带static，要带类名::变量名（类名：：使得编译器认为在类内，可以访问所有权限的成员），所以即使是private的静态成员变量也能在类外初始化成功

静态变量同样受访问权限的控制（类外初始化除外）

### const变量、常函数与类对象

const修饰成员变量

```
7.const 修 饰 的 静态 成 员 变 量 ， 最 好 在 类 内 初始 化

NV Ounwune

吕 mm

/Vconst 修 饰 的 静态 成 员 变 量 最 好 在 类 内 初始 化
class Maker4
{
public:
const static int a = 20;
const static int b;
];
V/ 类 外 也 可 以 初始 化
const int Maker4::b = 30;
```

const修饰函数（常函数）

```
public:

» //this 指 针 的 本 质 是 指针 常量 ”指针 的 指向 是 不 可 以 修改 的

// const Person * const this;

7/ 在 成 员 函 数 后 面 加 const， 修 饰 的 是 this 指 向 ， 让 指针 指向 的 值 也 不 可 以 修改 |
void showPerson() const

{

/
| //this->m_A = 100;

| | //this = NULL; //this 指 针 不 可 以 修改 指针 的 指向 的
}

int mA;
```

this指针本质是Person \*const this

```
void on () const

{

this->m_B = 10
//thismA = 1
//this = NULL; //this 指 针 不 可 以 修改 指针 的 指向 的

}

int mA;

nt mB; // 特 殊 变量 ， 即 使 在 常 函 数 中 ， 也 可 以 修改 这 个 值
```

指向内存不能改：不可以修改普通成员属性，可以修改静态成员属性；此外还可以修改mutable修饰的成员属性，。

const修饰类对象（常对象）

```
// 常 对 象

void test02()

const Person p; // 在 对 象 前 加 const， 变 为 常 对 象
m_B 是 特殊 值 ， 在 常 对 象 下 也 可 以 修改
```

常对象修饰对象所在内存，和this的指向的对象一致，所以同样不可以修改普通成员属性，可以修改静态成员，此外还可以修改mutable修饰的成员属性

常对象不能修改普通成员，常函数也不能修改普通成员，静态成员函数也不能修改普通成员，而普通函数可以修改普通成员，所以常对象只能调用常函数和静态成员函数，不能调用普通函数；

普通对象则都能调用

### 引用成员

![](test_assets/image_139.png)

### 类的内存（对象模型）

类的非静态成员变量，占用内存属于类对象，sizeof（类对象）；可以体现

类的静态成员变量，在全局区，占用内存不属于类对象，sizeof（类对象）；不体现

类的非静态成员函数，在代码区，占用内存不属于类对象，sizeof（类对象）；不体现

类的静态成员函数，在全局区，占用内存不属于类对象，sizeof（类对象）；不体现

完全空的类也会占一个字节的内存空间，用以区分多个实例，每个实例都有其独自的空间

### this指针

**一、类的非静态成员函数与类对象无关，占同一块空间，那么怎么知道是哪个类对象在调用该函数呢？**

函数在编译器看来是有多一个参数的，这个参数就是this指针，指向调用函数的类对象。

```
c+ + AE RE AS OS DA LE PB Eo

class Test{
public:

Test (int a) {

ma

}
int getaQ {
return ma;
}
static void print() {
cout << “This is class Test!” << endl;
}
private:
int ma; //4 字 节
]}

Test a(10);
a. getA();

Testi:print 0);

struct Test{
int ma

h

void Test_initialize(Test® pri
pThis~>ma = i;

}

int Test_getA(Test® pT
return pThis->ma:

}

void Test_print () {
cout << “hello world!” << endl;
1

Test ai
Test_initialize(@a, 10) ;
Test_getA(@a) ;
Test_print();
```

```
class Maker

编译 器 内 部 把 指向 成 员 变量 的 空间 的 指针 传 入 成 员

public: 函数 中
void func(O) void func (Maker *this)
。 nj 对象 的 空间
b
public:
int a; .
antsb: this

void test ()

Maker m;
```

**二、this指针在哪，明明sizeof（类对象）没有this指针的空间？**

c++规定，this指针是隐含在对象成员函数内的一种指针。当一个对象被创建后，它的每一个成员函数都含有一个系统自动生成的隐含指针this，用以保存这个对象的地址，也就是说虽然我们没有写上this指针，编译器在编译的时候也是会加上的。因此this也称为“指向本对象的指针”，this指针并不是对象的一部分，不会影响sizeof(对象)的结果。

![](test_assets/image_142.png)

**三、this指针怎么用？**

如果成员函数返回值为调用它的类对象本身，要这么写：

类名& 函数名（参数列表）

{

…

return \*this;

}

1.因为this指向调用它的类对象，\*引用就是类对象本身

2.返回类型为类名&，而不能是类名。因为返回类名时是调用了拷贝构造函数，实际上返回的类对象已不是调用它的类对象而是新拷贝的类对象

### 空指针访问成员函数

```
{
public:

void showClassName ()

{
}

cone << “this is Person class” << endl;

void showPersonAge ()

{
}

cout << “age = ” << m Age << endl;

int mAge:
```

```
avoid test0l()
{
Person * p = NULL;
p->showClassName () ;

p~>showPersonAge () :|
```

c++允许空指针访问成员函数，因为成员函数并不依赖类对象，编译时对象就绑定了函数地址。调用showClassName()没问题，但调用showPersonAge()报错，因为showPersonAge()中有用到与类对象一一对应的成员变量m\_Age，在编译器中认为是this->m\_Age，此时this为空指针找不到这个变量报错

```
1.1.12 nullptri FARA? 为 什么 ?

能 .
RA: 因为 在 编译 时 对 象 就 绑 定 了 函数 地 址 ， 和 指针 空 不 空 没关系 。
答案 解析

/给 出 实例
class animal {
public:
void sleep() { cout << “animal sleep” << endl; }
void breathe() { cout << “animal breathe haha” << endl; }
Ds
class fish :public animal {
public:
void breathe() { cout << “fish bubble” << endl; }
Ds
int mainO {
animal *pAnsnullptr;
pAn-breathe(); // 输出 ，animal breathe haha
fish +pFish = nullptr;
pFish->breathe(); // 输出 ,fish bubble
return 0;

}

原因 : 因为 在 编译 时 对 象 就 绑 定 了 函数 地 址 ， 和 指针 空 不 空 没关系 。pAn->breathe(): 编 译 的 时 候 ， 函 数 的 地 址 就 和 指针 pAn 绑 定 了 ; 调用 breath("this), this 就 等 于 pAn。 由 于 函数 中 没有 需要 解 引 用 this 的 地 方 ， 所 以 函数 运行 不 会 出 错 ， 但 是 若 用 到 this， 因 为 this=nullptr， 运 行 出 错 。
```

### 友元

工作中不推荐使用，破坏封装性，不符合面向对象，像Java这种全对象语言就没有友元。

类外友元可以访问类的私有成员，所以A类的友元函数并非A类的成员，所以要在类的顶部访问权限外声明

友元是单向的，如A是B的友元，B不一定是A的友元

1. 全局函数做友元，在类内顶部访问权限域外声明一下friend

```
‘class Building

V/goodGay 全 局 函数 是 Building 好 朋友 ， 可 以 访问 Building 中 私有 成 员
friend void goodGay (Building *building) ;|
```

1. 其他类做友元，在类内顶部访问权限域外声明一下friend

![](test_assets/image_147.png)

注意类作为友元不能继承，比如A是B的友元，A的子类就不是B的友元了

注意类作为友元不能传递，比如A是B的友元，C是B的友元，C不一定是A的友元

1. 其他类的成员函数做友元，在类内顶部访问权限域外声明一下friend

```
//1, Fa ae AIBA PRR, ASAE RAY 25 19)
class Building;// RAK
class GoodGay
{
public:
void func (Building &bud) ;

class Building

(/P condos i MEN conc 0s ding RO TEBE
friend void GoodGay: func (Building &bud) ;
public:
日 Building(O)
{
```

声明GoodGay类的func函数为友元，需要先声明GoodGay类的结构让编译器知道类内部有func函数，然后func函数参数有Building类，所以在上面再声明Building类

## 继承

![](test_assets/image_149.png)

语法：

class 子类（派生类）：继承方式 父类（基类）

作用：

父类代码复用，拓展子类特有功能

### 三种继承方式

public、protected、private，区别如下图

![](test_assets/image_150.png)

不显式指定继承方式，默认private继承

无论何种继承方式，子类都会继承父类所有的非静态成员（静态成员在全局区，父类和子类共享同一份内存，所以不算继承算共享），只是有些成员不可访问（private被编译器隐藏了）。可以通过sizeof（）或者通过命令行查看对象在内存中的模型来验证。

```
查看 类 继承 的 内 部 模型 ; «

找到 vs2013 开发 人 员 命 念 提示 程序 (一 般 在 C:\Program Files (x86)\Microsoft Visual Studio
12.0\Common7\Tools\shortcuts)， 打 开 ， 然 后 复制 你 工程 路 径 ， 命 令 : cd 路 径 ， 进 入 你 工程
文件 夹 中 (如 果 工 程 不 在 盘 的 话 ,要 再 E 下 ), 然 后 命令 :cl/dl reportsingleclassLayout
类 名 文件 名 全 称 "

如 : gl /dl reportsingleClass| tSon test.cppw
```

父类成员继承到子类并且按照继承方式对应的改变访问权限后，子类或子类对象对父类成员的访问符合访问权限限制

1.public继承时，子类内可以访问父类的public和protected成员不能访问private成员，子类对象只能访问父类public成员

2.protected继承时，子类内可以访问父类的public和protected成员不能访问private成员，子类对象无法访问父类任何成员

3.private继承时，子类内可以访问父类的public和protected成员不能访问private成员，子类对象无法访问父类任何成员

### 子类与父类转换

所有子类直接转父类都会成功，因为子类含有父类的全部数据，子类对象的内存包含父类所有成员的内存。可以使用dynamic\_cast< 父类名 >(子类对象名)来转换

但是父类直接转子类一般失败，因为父类没有子类特有的数据，父类对象的内存不包含子类特有成员的内存。于是C++提供了static\_cast< 子类名 >(父类对象名)和dynamic\_cast< 子类名 >(父类对象名)来转换；static\_cast是强制转换，虽然不报错了但是风险依然存在；dynamic\_cast转换安全些会进行类型检查但是运算成本大。

```
1 . 子 类 转换 成 父 类 ( 向 上 转换 ) ; 编译 器 认为 指针 的 寻 址 范围 缩小 了 ， 所 以 是 安全 的
2. 父 类 转换 成 子 类 ( 向 下 转换 ) ; 编译 器 认为 指针 的 寻 址 范围 扩大 了 ， 不 安全
```

![](test_assets/image_153.png)

### 含继承的构造与析构顺序

1.创建派生类的对象，基类的构造函数优先被调用（也优先于派生类里的成员类）;

2.如果类里面有成员类，成员类的构造函数优先被调用；（也优先于该类本身的构造函数）

3.基类构造函数如果有多个基类，则构造函数的调用顺序是某类在类派生表中出现的顺序而不是它们在成员初始化表中的顺序

4.成员类对象构造函数如果有多个成员类对象，则构造函数的调用顺序是对象在类中被声明的顺序而不是它们出现在成员初始化表中的顺序

5.派生类构造函数，作为一般规则派生类构造函数应该不能直接向一个基类数据成员赋值而是把值传递给适当的基类构造函数，否则两个类的实现变成紧耦合的（tightly coupled）将更加难于正确地修改或拓展基类的实现。（基类设计者的责任是提供一组适当的基类构造函数）

6.综上可以得出，初始化顺序：

父类构造函数-＞成员类过象构造函数－＞自身构造函数

其中成员变量的初始化与声明顺序有关，构造函数的调用顺序是类派生列表中的顺序。

析构顺序和构造顺序相反。

由以上顺序，子类构造函数最好显式调用父类构造函数：

如果子类的构造函数没有显式地调用父类的构造函数（或者没有构造函数），则默认地调用父类的不带参数的构造函数。根据构造的性质，如果父类定义了带参数的构造函数，则不会默认定义无参构造函数，此时需要调用显式地调用父类的有参构造函数

```
e 代码 可 以 通过 编译 吗 ?如果 不能 应 该 如 何 修改 ?

‘template<class T> class Foo{

T ters
public:
Foo(T t) : tvar(t) { }
ie
‘template<class T> class FooDerived:public Foo<T>
{
ie
int main()
{
FooDerivedcint> d(5)5
return 05
了

正确 答案 : D ”你 的 答案 A (错误 )

代码 可 以 正确 通过 编译 。

编译 错误 ，FccDez:vea 是 一 个 继承 模板 类 的 非 模板 类 ， 它 的 类 型 不 能 改变 。

编译 错误 ，*Va1 变 量 是 一 个 不 确定 的 类 型 。

编译 错误 ， 可 以 在 ccDezives 类 中 添加 一 个 构造 函数 解决 问题 。
```

### 同名成员

没有同名时直接访问的是父类的，有同名时访问的是子类的，父类的同名成员被隐藏，需要加上作用域

子类有与父类同名的成员，直接访问时访问的是子类s.m\_A，访问父类需要加上作用域s.Base::m\_A。

静态成员也适用，但是静态成员还可以不构造对象通过类名直接访问，故有Son::m\_A、Son::Base::m\_A这种写法来访问子类和父类的成员

上面是成员变量的例子，成员函数一样

多继承语法：![](test_assets/image_155.png)，若父类有同名变量，也需要作用域来区分

```
cout << s.Base2::m_A << endl;
```

，实际开发中不建议使用多继承

### 非自动继承的函数

不是所有的函数都能自动从基类继承到派生类中。构造函数和析构函数用来处理对象的创建和析构操作，构造和析构函数只知道对它们的特定层次的对象做什么，也就是说构造函数和析构函数不能被继承，必须为每一个特定的派生类分别创建。

另外operator=也不能被继承，因为它完成类似构造函数的行为。也就是说尽管我们知道如何由=右边的对象如何初始化=左边的对象的所有成员，但是这个并不意味着对其派生类依然有效。

在继承的过程中，如果没有创建这些函数，编译器会自动生成它们。

### 菱形继承

两个类同一父类，然后又被同一个类继承

![](test_assets/image_157.png)

问题是羊驼继承了两份动物中的属性，而且一摸一样有二义性，这里要用虚继承技术。动物类是虚基类，羊和驼虚继承动物

```
// 动 物 类 ， 在 虚 继 革 中 叫 虚 基 类
class Animal

{

public:

int mAge:

(72, WRI —Fn Age. fl Evirtual se Ame, SEA Rvbptr (virtual base pointer) 指针

class Sheep:virtual public Animal {};

// 陀 类 ， 继 承 了 一 个 m_Age， 加 上 virtual 后 变 为 虑 继承

class Camel :virtual public Animal {};

// 羊 陀 类 ， 原 继承 了 两 个 n_Age， 加 上 virtual 后 变 为 虚 继承 只 继承 了 一 个 m_Age
class Alpaca :public Sheep, public Camel {};

int main()

{

Alpaca enm;
//onm.mAge = 18; 没有 应 继承 时 报错 不 明确
cnm. Sheep: :m Age = 18;// 没 有 庶 继 承 时 需要 添加 作用 域 解决

为 只 有 一 个 age 了 ， 两 个 作用 域 修改 的 都 是 同一 块 内 存 空间
Age <<cnm.m Age << endl:
```

![https://img-blog.csdnimg.cn/20190731215717995.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2ZfX3l1YW4=,size_16,color_FFFFFF,t_70](test_assets/image_159.png)

虚继承子类有虚继承表（指针数组），表中有虚基类指针指向虚基类表，虚基类表中的数据是虚基类指针到基类的存储区域的偏移值（只是到本对象的Animal区域偏移值，不是直接到Animal的成员ma），所以D两个作用域的ma都指向同一个ma（有点类似static成员所有对象共用一份内存，但static成员不需要实例化就能访问，这里要构造子类对象，会自动首先调用Animal类的构造，C++会保证只有一个Animal类对象会被创建）。羊驼类就是继承了这两个vbptr

![https://pic3.zhimg.com/v2-5ed4c36ad3dfc7a3271231cacaada7b2_r.jpg](test_assets/image_160.jpg)

![https://pic1.zhimg.com/v2-b6b07c045aea011d2ff4e8e5f1711004_r.jpg](test_assets/image_161.jpg)

如果没有animal类，羊和驼类是无关的类且都有ma成员变量，此时羊驼类继承两份ma，只能通过父类作用域：：来访问，直接访问有二义性报错且这个问题无法解决，所以不建议使用多继承

## 多态

多态是面向对象的重要特性之一，它是一种行为的封装，就是不同对象对同一行为会有不同的状态。(举例 : 学生和成人都去买票时,学生会打折,成人不会)

![](test_assets/image_162.png)

运算符重载和函数重载（实际上函数并不同名）是静态联编、静态多态、编译时多态。因为在编译阶段就确定了函数调用地址并产生代码（早绑定，C语言是静态联编）

派生类和虚函数（函数真的同名）是动态联编、动态多态、运行时多态，因为编译阶段不能确定函数调用地址要运行时才能确定（晚绑定，C++可以动态联编）

### 静态多态

### 动态多态

#### 作用

一、业务层和实现层都依赖抽象层，修改代码方便

![](test_assets/image_163.png)

```
int myadd(int a, int b)

{
}
// 业 务 层

int doLogin(rule *cal)

{

return a + b;

int a = 10;
int b = 20;

myadd (10, t
```

比如实现层的函数名myadd变了，业务层的代码也要变

![](test_assets/image_165.png)

```
// 抽 和 象 层 bl

iclass rule

{

public:

] virtual int getnum(int a, int b)

{
}

return 0;
```

```
// 实 现 层
aclass plus_rule : rule
{

public:
3 virtual int getnum(int a，int b)
{
return atb;
}

ie
```

```
er.
in’ ogin(rule *cal)

{

int a = 10;
int b = 20;

int ret=cal—>getnum(a, b);
```

```
void test ()
{
rule *r = NULL;
r = new plus_rule;
cout << doLogin(r) << endl
delete r;

r = new miux_rule;
cout <

< giin(r) << endl;
delete
}
```

显然实现层改变，业务层代码不用变

二、开闭原则

业务层和抽象层不给改（闭），但可以自己写实现层来拓展别的功能（开）。

micro-manager写adapter就是很好的例子

#### 满足条件

1. 有继承关系

子类重写父类的虚函数，重写函数声明要完全相同，父类virtual一定要写（不写，父类指针调用的就是父类的函数，子类重写该函数就不叫重写而是重定义），子类的virtual可不写

1. 使用虚函数的是父类的指针或者引用，但指向或引用的是子类对象

```
iclass Dog :public Animal

{
public:
virtual void speak()
{
cout << “Dog speak()” << endl;
}
Les

void test ()

{
全 sam = Dog () ;
animal. speak () ;

}
```

引用本质上也是指针，所以也是dog speak

1. 不能被static修饰，static修饰会在编译时早绑定

```
MATAR

class Animal

{

public:

virtual void speak 0) //X #0 Lvirtual@E BARS J HIRE
{

;cout《《“ 动 物 在 说 话 ”《《 endl;

}

SRE
class Cat:public Animal

public:
void speak ()

cout << “08” << endl;

void doSpeak(Animal& animal)// 前 面 不 加 virtual 的 话 ， 这 里 在 编译 阶段 地 址 已 绑 定 ， 即 输出 动物 在 说 话 。 使 用 时 用 父 类 的 指针 或 引用 ， 指 向 或 引用 的 是 子 类 对 象
{

animal. speak () ;

int main()

Cat cat:
doSpeak (cat) ;
```

#### 实现原理

![](test_assets/image_172.png)

虚表在编译阶段建立，虚表中有存储虚函数地址的数组，该数组以NULL结尾。

虚表指针vptr在构造类对象时建立（运行阶段），根据new的class类型初始化vptr，指向相应类的虚表

对象调用函数时，根据对象的虚表指针去找虚函数表，再找虚函数

```
class Animal

{

public.
// BR
virtual void speak()
{

cout 《《“ 动 物 在 说 话 ”《《 endl;

}

UB

Lf HB

class Cat :public Animal
{
public

// 重 写 ” 国 数 返 回 值 类 型 ”函数 名 参数 列表 完全 相同
virtual void speak ()
{
cout 《《“ 小 猫 在 说 话 ”《< endl:
I

APRESS

子 类 中 的 虚 图 数 表 内 部 会 苦 换 成 子 类 的 虚 国 数 地 址

Animal 类 内 部 结构

vYfptr

vétable — 表 内 记录 虚 国 数 的 地 址

hnimal : : speak

Cat 类 内 部 结构

viptr

v

vftable

@Cat: speak

véptr — Belay (38) 指针
v virtual
£ — function

ptr — pointer

vftable - 虚 函 数 表
Y -virtual
£ - function

table — table

SNA HSH SSBF AISA, RAB
Animal & animal = cat;

animal. speak();
```

子类复制父类的虚函数表，有重写的虚函数就覆盖成子类的，没有重写的就还是父类的，所以没有重写时能调用父类的虚函数

不重写父类虚函数![](test_assets/image_174.png) 重写父类虚函数![](test_assets/image_175.png)

#### 不能虚函数和建议虚函数

不能声明为虚函数的有：构造函数，友元函数，内联函数，静态函数。

一、不能是构造函数的原因：

1.记录虚函数地址的表vftable，存储在对象的内存空间，该空间调用构造函数后才有，构造函数是虚函数的话，都没有这个空间怎么找虚函数地址。

2.虚函数是通过父类的指针或引用类型指向子类对象来调用子类的函数，可子类构造对象时最先调用的就是父类构造函数，此时连子类对象都没有

3.虚函数本身的意义就是在信息不全（不知道子类）的情况下，能够准确调用对应函数（子类才知道自己的情况，要调用自己的函数）。构造函数只有子类调用父类，而没有父类调用子类构造，所以没有意义

二、不能是内联函数的原因：

内联函数是在编译时期展开,而虚函数的特性是运行时才动态联编,所以两者矛盾,不能定义内联函数为虚函数

三、不能是友元函数的原因：

因为C++不支持友元函数的继承，对于没有继承特性的函数没有虚函数的说法。

四、不能是静态函数的原因：

静态成员函数属于类不属于对象，对于每种类的所有对象来说只有一份代码共享，没有this指针，无法到对象的内存空间找vtable

构造函数中不调用虚函数的原因：

可以调用，语法没有问题。但是不能实现虚函数的作用，因为类中构造、虚构函数的this指针就是指向类对象本身，调用的肯定是自己的函数，所以搞成虚函数没有意义。

建议声明为虚函数的有：

1.析构函数。父类的指针或引用指向子类对象，如果析构函数不是虚函数，那么析构子类对象时调用的是父类的析构函数，内存泄漏

#### 纯虚函数和抽象类

多态中父类的虚函数实现往往是没有意义的，主要都是调用子类重写的函数，因此可以把父类中的虚函数写为纯虚函数，含有纯虚函数的类即为抽象类。

```
GRAMS: virtual 返回 值 类 型 函数 名 (参数 列表 ) = 0;
```

纯虚函数的vtable中对应表项被赋值为0，指向一个不存在的函数，编译器不允许有调用一个不存在函数的可能，因此不能生成对象

![](test_assets/image_177.png)可见子类可以不重写纯虚函数，子类将继承该纯虚函数，仍是抽象类

由于不能实例化，所以抽象类不能用作参数类型、函数返回类型或显式转换的类型

#### 虚析构和纯虚析构（父类都应该）

多态的父类析构，都应该做成虚析构

如果子类有属性开辟到堆区，那么父类指针在释放时无法调用到子类的析构代码（显然析构父类不应该把子类也析构了）。

但是一般通过父类指针或引用来析构（父类指针指向子类对象），如果父类析构不是虚的，就不能准确判断要虚构对象的类型，从而不能正确析构。

把父类的析构函数改为虚析构，在子类重写即可正确析构子类

把父类的析构函数改为纯虚析构，纯虚析构没有实现会报错，因此需要在类外部定义实现。这样做的意义在于不给实例化父类。

```
virtual “Animal() = 0
virtual void speak() = 0

'/ 印 虚 析 构 的 话 因为 没有 定义 会 报错 ， 需要 在 外 部 定义
ininmal: : “Animal ()
f

cout << “aninmal 的 纯 虚 析 构 函数 调用 ”<< endl
```

```
虚 析 构 语法 :

virtual ~ 类 各 (){}
纯 虚 析 构 语法 :
virtual ~ 类 名 () = @;

类 名:: MEO
```

#### 不建议使用默认参数

```
#pragma once

class Base {
public:
Base();

~Base();

virtual void setNumber(int num = 2) = 9;

ON AU BWDN PR

33

#include "Base.h"

Base: :Base() {
}

Base: :~Base() {

}

1
2
3
4
5
6
7
```

```
OwoOAN nau BWDN PB

WAN AU BWDN PB

RPRPRPPR
BRWNRO

#pragma once

#include "Base.h"

class A :public Base {
public:
AQ);
~A()5
virtual void setNumber(int num = 4)override;

33

"Ah"

#include <QDebug>

#include

A::A() {
}

A::~A() {

void A::setNumber(int num ) {

qDebug() << num;
```

![](test_assets/image_182.png)

都是动态绑定，注意默认参数规则:

如果虚函数中带有默认值，派生类的指针或对象引用调用该函数时，函数参数总是选择基类的函数的参数默认值，该函数的派生类的同名函数的默认值将不会起任何作用。 ​简单地说就是虚函数中含有默认值，派生类的虚函数的参数值是没有任何作用

# 输入输出流

## 流的概念和流类库的结构

程序的输入指的是从输入文件将数据传送给程序，程序的输出指的是从程序将数据传送给输出文件。

C++输入输出包含以下三个方面的内容：

对系统指定的标准设备的输入和输出。即从键盘输入数据，输出到显示器屏幕。这种输入输出称为标准的输入输出，简称标准I/O。

以外存磁盘文件为对象进行输入和输出，即从磁盘文件输入数据，数据输出到磁盘文件。以外存文件为对象的输入输出称为文件的输入输出，简称文件I/O。

对内存中指定的空间进行输入和输出。通常指定一个字符数组作为存储空间(实际上可以利用该空间存储任何信息)。这种输入和输出称为字符串输入输出，简称串I/O。

C++编译系统提供了用于输入输出的iostream类库。iostream这个单词是由3个部 分组成的，即i-o-stream，意为输入输出流。在iostream类库中包含许多用于输入输出的 类。常用的见表

![](test_assets/image_183.png)

![](test_assets/image_184.png)

注意图中istrstream、ostrstream和strstream是错的，应为istringstream、ostringstream和stringstream

ios是抽象基类，由它派生出istream类和ostream类，两个类名中第1个字母i和o分别代表输入(input)和输出(output)。 istream类支持输入操作，ostream类支持输出操作， iostream类支持输入输出操作。iostream类是从istream类和ostream类通过多重继承而派生的类。其继承层次见上图表示。

C++对文件的输入输出需要用ifstrcam和ofstream类，两个类名中第1个字母i和o分别代表输入和输出，第2个字母f代表文件 (file)。ifstream支持对文件的输入操作， ofstream支持对文件的输出操作。类ifstream继承了类istream，类ofstream继承了类ostream，类fstream继承了 类iostream。见图

![http://c.biancheng.net/cpp/uploads/allimg/140527/1-14052GP142452.png](test_assets/image_185.png)

I/O类库中还有其他一些类，但是对于一般用户来说，以上这些已能满足需要了。

**与iostream类库有关的头文件**

iostream类库中不同的类的声明被放在不同的头文件中，用户在自己的程序中用#include命令包含了有关的头文件就相当于在本程序中声明了所需 要用到的类。可以换 —种说法：头文件是程序与类库的接口，iostream类库的接口分别由不同的头文件来实现。常用的有

- iostream  包含了对输入输出流进行操作所需的基本信息。
- fstream  用于用户管理的文件的I/O操作。
- strstream  用于字符串流I/O。
- stdiostream  用于混合使用C和C + +的I/O机制时，例如想将C程序转变为C++程序。
- iomanip  在使用格式化I/O时应包含此头文件。

**在iostream头文件中定义的流对象**

在 iostream 头文件中定义的类有 ios，istream，ostream，iostream，istream 等。

在iostream头文件中不仅定义了有关的类，还定义了4种流对象，

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **对象** | **含义** | **对应设备** | **对应的类** | **c语言中相应的标准文件** |
| cin | 标准输入流 | 键盘 | istream\_withassign | stdin |
| cout | 标准输出流 | 屏幕 | ostream\_withassign | stdout |
| cerr | 标准错误流 | 屏幕 | ostream\_withassign | stderr |
| clog | 标准错误流 | 屏幕 | ostream\_withassign | stderr |

在iostream头文件中定义以上4个流对象用以下的形式（以cout为例）：
    ostream cout ( stdout);
 在定义cout为ostream流类对象时，把标准输出设备stdout作为参数，这样它就与标准输出设备(显示器)联系起来，如果有
    cout <<3;
就会在显示器的屏幕上输出3。

**在iostream头文件中重载运算符**

“<<”和“>>”本来在C++中是被定义为左位移运算符和右位移运算符的，由于在iostream头文件中对它们进行了重载， 使它们能用作标准类型数据的输入和输出运算符。所以，在用它们的程序中必须用#include命令把iostream包含到程序中。

    #include <iostream>

1. >>a表示将数据放入a对象中。
2. <<a表示将a对象中存储的数据拿出。

## cout，cerr，clog区别

标准I/O对象:cin，cout，cerr，clog

**cout流对象**

cout是console output的缩写，意为在控制台（终端显示器）的输出。强调几点。

1) cout不是C++预定义的关键字，它是ostream流类的对象，在iostream中定义。 顾名思义，流是流动的数据，cout流是流向显示器的数据。cout流中的数据是用流插入 运算符“<<”顺序加入的。如果有:
    cout<<"I "<<"study C++ "<<"very hard. << “hello world !";

按顺序将字符串"I ", "study C++ ", "very hard."插人到cout流中，cout就将它们送到显示器，在显示器上输出字符串"I study C++ very hard."。cout流是容纳数据的载体，它并不是一个运算符。人们关心的是cout流中的内容，也就是向显示器输出什么。
2) 用“cout<<”输出基本类型的数据时，可以不必考虑数据是什么类型，系统会判断数据的类型，并根据其类型选择调用与之匹配的运算符重载函数。这个过程都是自动的， 用户不必干预。如果在C语言中用prinf函数输出不同类型的数据，必须分别指定相应的输出格式符，十分麻烦，而且容易出错。C++的I/O机制对用户来说，显然是方便 而安全的。

1. cout流在内存中对应开辟了一个缓冲区，用来存放流中的数据，当向cout流插人一个endl时，不论缓冲区是否已满，都立即输出流中所有数据，然后插入一个换行符， 并刷新流（清空缓冲区）。注意如果插人一个换行符”\n“（如cout<<a<<"\n"），则只输出和换行，而不刷新cout 流(但并不是所有编译系统都体现出这一区别）。
2. 在iostream中只对"<<"和">>"运算符用于标准类型数据的输入输出进行了重载，但未对用户声明的类型数据的输入输出进行重载。如果用户声明了新的类型，并希望用"<<"和">>"运算符对其进行输入输出，按照重运算符重载来做。

**cerr流对象**

cerr流对象是标准错误流，cerr流已被指定为与显示器关联。cerr的作用是向标准错误设备(standard error device)输出有关出错信息。cerr与标准输出流cout的作用和用法差不多。但有一点不同：cout流通常是传送到显示器输出，但也可以被重定向输出到磁盘文件，而cerr流中的信息只能在显示器输出。当调试程序时，往往不希望程序运行时的出错信息被送到其他文件，而要求在显示器上及时输出，这时 应该用cerr。cerr流中的信息是用户根据需要指定的。

**clog流对象**

clog流对象也是标准错误流，它是console log的缩写。它的作用和cerr相同，都是在终端显示器上显示出错信息。区别：cerr是不经过缓冲区，直接向显示器上输出有关信息，而clog中的信息存放在缓冲区中，缓冲区满后或遇endl时向显示器输出。

缓冲区的概念:

![](test_assets/image_186.png)

## 标准输入流

### cin函数

标准输入流对象cin，重点掌握的函数

cin.get() //一次只能读取一个字符，换行符也会从缓冲区取出

cin.get(a) //读一个字符给a，换行符也可以从缓冲区取出，读入a

cin.get(a，长度) //读字符串到a（字符数组或string），最长为1024，换行符不会从缓冲区取出

cin.getline()//取一行，会读入空格，换行符从缓冲区取出并丢弃

cin.ignore()//缓冲区拿出一个字符，不输出；有参数n就拿出n个字符

cin.peek()//只看不取

cin.putback()//放回缓冲区的原位置

|  |
| --- |
| //cin.get… 输入相关函数  void test01**(){**  #if 0  char ch **=** cin**.**get**();**  cout **<<** ch **<<** endl**;**  cin**.**get**(**ch**);**  cout **<<** ch **<<** endl**;**  //链式编程  char char1**,** char2**,** char3**,** char4**;**  cin**.**get**(**char1**).**get**(**char2**).**get**(**char3**).**get**(**char4**);**  cout **<<** char1 **<<** " " **<<** char2 **<<** "" **<<** char3 **<<** " " **<<** char4 **<<** " "**;**  #endif  char buf**[**1024**]** **=** **{** 0 **};**  //cin.get(buf.1024);  cin**.**getline**(**buf**,**1024**);**  cout **<<** buf**;**  //c++中的用法  string str;  getline(cin,str);  **}**  //cin.ignore  void test02**(){**  char buf**[**1024**]** **=** **{** 0 **};**  cin**.**ignore**(**2**);** //忽略缓冲区当前字符  cin**.**get**(**buf**,**1024**);**  cout **<<** buf **<<** endl**;**  **}**  //cin.putback 将数据放回缓冲区  void test03**(){**  //从缓冲区取走一个字符  char ch **=** cin**.**get**();**  cout **<<** "从缓冲区取走的字符:" **<<** ch **<<** endl**;**  //将数据再放回缓冲区  cin**.**putback**(**ch**);**  char buf**[**1024**]** **=** **{** 0 **};**  cin**.**get**(**buf**,**1024**);**  cout **<<** buf **<<** endl**;**  **}**  //cin.peek 偷窥  void test04**(){**    //偷窥下缓冲区的数据  char ch **=** cin**.**peek**();**  cout **<<** "偷窥缓冲区数据:" **<<** ch **<<** endl**;**  char buf**[**1024**]** **=** **{** 0 **};**  cin**.**get**(**buf**,** 1024**);**  cout **<<** buf **<<** endl**;**  **}**  //练习 作业 使用cin.get和putback完成类似功能  void test05**(){**    cout **<<** "请输入一个数字或者字符串:" **<<** endl**;**  char ch **=** cin**.**peek**();**  **if(**ch **>=** '0' **&&** ch **<=** '9'**){**  int number**;**  cin **>>** number**;**  cout **<<** "数字:" **<<** number **<<** endl**;**  **}**  **else{**  char buf**[**64**]** **=** **{** 0 **};**  cin**.**getline**(**buf**,** 64**);**  cout **<<** "字符串:" **<<** buf **<<** endl**;**  **}**  **}** |

### cin>>

#### 末尾space（enter、tab）保留

以cin>>a为例，从输入缓冲区中读取数据，遇到space（enter、tab）时读取结束，并将space（enter、tab）之前的数据写入a中，但是会将space（enter、tab）遗留在输入缓冲区中。

如下图：

```
while (1)
{

cin >> num;

if (num >= 0 && num <= 10)
{

cout << “4 ATER” << endl;
break;

cout << “Hiri A: ” << endl;
```

![](test_assets/image_188.png)

显然因为换行在缓冲区中导致了无限循环而不是阻塞

要解决这种情况需要清空缓冲区，并且重置错误标志位（cin给int赋值读取到’\n’，已经出错。可以通过cin.fail()查看标志位数值，0正常1出错）

```
while (1)
{

cin >> num;

if (num >= 0 && num <= 10)

{
cout 《《“ 输 入 正确 ”《〈《 endl;
break;

}

c <《“ 重 新 输入 : ” << endl;
m2

c ear ();

// 清 空 缓冲 区

cin. sync () ;
```

有些老版本的vs没有上面的函数，也可以这么清空缓冲区

```
// 重 置 标志 位

cin. clear () ;

// 清 空 缓 冲 区

//cin. syne () ;

//2015

char buf[1024] = { 0};
cin. getline (buf, 104) ;
```

上面说过cin.getline会取出缓冲区中的空格并丢弃

#### 开头space（enter、tab）丢弃

如果输入缓冲区中的数据以space（enter、tab）开头，那么cin>>会抛弃掉这些space（enter、tab），直到遇到非space（enter、tab）的数据才进行读取，此时前面被抛弃掉的space（enter、tab）也不在输入缓冲区中了。

举个例子详细解释：

如下所示：

```
int main()

ft

string a,b,c;
ein>>b:

end:

return 0;
```

这里的cin>>a;cin>>b;cin>>c和cin>>a>>b>>c；是同样的效果。一开始由于输入缓冲区中没有数据，cin会一直阻塞直到数据到来，输入“aaa+空格+bbb+换行+ccc”然后回车，这时实际上输入到缓冲区的字符串是“aaa bbb/nccc/n”；

输入缓冲区中有数据了，此时cin>>a开始将数据读入a中，遇到空格停止，那么实际上读入a的是“aaa”，此时缓冲区中剩下“ bbb/nccc/n”，特别注意这里bbb的前面是有一个空格的，此时cin>>a即执行完毕，开始执行cin>>b；

执行cin>>b时，由于输入缓冲区中有数据，因此cin>>b直接从输入缓冲区中读取数据，由于此时数据以空格符开头，因此cin>>会抛弃开头的空格符，然后读取数据直到遇到换行符/n停止，那么实际上读入b的是“bbb”，此时缓冲区中剩下“/nccc/n”，此时cin>>b执行完毕，开始执行cin>>c；

执行cin>>c同理，最终读入c的是"ccc"，最终缓冲区中还剩下一个换行符“/n”。

#### 返回值

cin是C++的标准输入流，其本身是一个对象，并不存在返回值的概念。

不过经常会有类似于while(cin>>a)的调用，这里并不是cin的返回值，而是>>操作重载函数istream& operator>>(istream&, T &);的返回值，其中第二个参数由cin>>后续参数类型决定。

其返回值类型为istream&类型，大多数情况下其返回值为cin本身（非0值），只有当遇到EOF（即space、enter、tab）输入时，返回值为0。

## 标准输出流

### 字符输出

cout.flush() //刷新缓冲区 Linux下有效

cout.put() //向输出缓冲区写字符，返回cout可以链式

cout.write(char\* buf, int num) //从buffer中写num个字节到当前输出流中。

|  |
| --- |
| [//cout.flush 刷新缓冲区，linux下有效](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)  [void test01](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[(){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** ["hello world"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  [//刷新缓冲区](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[.](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[flush](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[();](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  [//cout.put 输出一个字符](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)  [void test02](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[(){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**    [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[.](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[put](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**['a'](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  [//链式编程](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[.](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[put](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**['h'](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[).](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[put](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**['e'](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[).](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[put](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**['l'](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  [//cout.write 输出字符串 buf,输出多少个](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)  [void test03](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[(){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**    [//char\* str = "hello world!";](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)  [//cout.write(str, strlen(str));](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)  [char](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[\*](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [str](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出) **[=](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** ["\*\*\*\*\*\*\*\*\*\*\*\*\*"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  **[for](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)****[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[int i](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出) **[=](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [1](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [i](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出) **[<=](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [strlen](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[str](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [i](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出) **[++){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[.](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[write](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[str](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[,](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [i](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [endl](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  **[for](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)****[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[int i](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出) **[=](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [strlen](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[str](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [i](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出) **[>](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [0](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [i](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出) **[--){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[.](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[write](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[str](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[,](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [i](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** [endl](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\02 标准输出)** |

### 格式化输出

在输出数据时，为简便起见，往往不指定输出的格式，由系统根据数据的类型采取默认的格式，但有时希望数据按指定的格式输出，如要求以十六进制或八进制形式输出一个整数，对输出的小数只保留两位小数等。有两种方法可以达到此目的。

1）使用控制符的方法；

2）使用流对象的有关成员函数。

使用流对象的有关成员函数

通过调用流对象cout中用于控制输出格式的成员函数来控制输出格式。用于控制输出格式的常用的成员函数如下：

![](test_assets/image_192.png)

cout.width(n)设置宽度，内容不足宽度在左边填充空格，即右对齐；

cout.fill(c)设置填充字符，默认为空格；

流成员函数setf和控制符setiosflags括号中的参数表示格式状态，它是通过格式标志来指定的。格式标志在类ios中被定义为枚举值。因此在引用这些格式标志时要在前面加上类名ios和域运算符“::”。格式标志见表13.5。

![](test_assets/image_193.png)

//通过流成员函数

void test01**(){**

int number **=** 99**;**

cout**.**width**(**20**);**

cout**.**fill**(**'\*'**);**

cout**.**setf**(**ios**::**left**);** //把右对齐改为左对齐，右填充

cout**.**unsetf**(**ios**::**dec**);** //卸载十进制

cout**.**setf**(**ios**::**hex**);**

cout**.**setf**(**ios**::**showbase**);**

cout**.**unsetf**(**ios**::**hex**);**

cout**.**setf**(**ios**::**oct**);**

cout **<<** number **<<** endl**;**

**}**

**控制符格式化输出**

C++提供了在输入输出流中使用的控制符(有的书中称为操纵符)。

```
3.1 a Fat ENS

控制 符 作用
dec 设置 数值 的 基 北 为 10
hex 设置 数值 的 基 北 为 16
oct EES
setfill(c) 设置 填充 字符 c ，< 可 以 是 字符 常量 或 字符 变量

BES SAE AN. EUAN
fixed xe EAD scientific Heer

SAME, nf ERR,

setprecision(n)

setwin)
setiosfla

setio:

setios RET
setios Ra
etios SiR SSS

SHEL TH NS SUASET

SL TH PSL) SS:

setiosflags(

jowpos) HLH IFSYRSH "+"

需要 注意 的 是 : 如 果 使 用 了 控制 符 ， 在 程序 单位 |

开头 除了 要 加 iocs

eam 头 文件 外 ,还 要 加 iomanip 头 文件。
```

更多格式标志见上表

|  |
| --- |
| //使用控制符  void test02**(){**  int number **=** 99**;**  cout **<<** setw**(**20**)**  **<<** setfill**(**'~'**)**  **<<** setiosflags**(**ios**::**showbase**)**  **<<** setiosflags**(**ios**::**left**)**  **<<** hex  **<<** number//比流成员函数更简单，不用卸载  **<<** endl**;**  **}** |

**对程序的几点说明**

1) 成员函数width(n)和控制符setw(n)只对其后的第一个输出项有效。如：

cout. width(6);
    cout <<20 <<3.14<<endl;
 输出结果为 203.14

在输出第一个输出项20时，域宽为6，因此在20前面有4个空格，在输出3.14时，width (6)已不起作用，此时按系统默认的域宽输出（按数据实际长度输出）。如果要求在输出数据时都按指定的同一域宽n输出，不能只调用一次width(n)， 而必须在输出每一项前都调用一次width(n>，上面的程序中就是这样做的。

2) 在表13.5中的输出格式状态分为5组，每一组中同时只能选用一种（例如dec、hex和oct中只能选一，它们是互相排斥的）。在用成员函数setf和 控制符setiosflags设置输出格式状态后，如果想改设置为同组的另一状态，应当调用成员函数unsetf（对应于成员函数self）或 resetiosflags（对应于控制符setiosflags），先终止原来设置的状态。然后再设置其他状态，大家可以从本程序中看到这点。程序在开 始虽然没有用成员函数self和控制符setiosflags设置用dec输出格式状态，但系统默认指定为dec，因此要改变为hex或oct，也应当先 用unsetf 函数终止原来设置。如果删去程序中的第7行和第10行，虽然在第8行和第11行中用成员函数setf设置了hex和oct格式，由于未终止dec格式，因 此hex和oct的设置均不起作用，系统依然以十进制形式输出。

同理，程序倒数第8行的unsetf 函数的调用也是不可缺少的。

3) 用setf 函数设置格式状态时，可以包含两个或多个格式标志，由于这些格式标志在ios类中被定义为枚举值，每一个格式标志以一个二进位代表，因此可以用位或运算符“|”组合多个格式标志。如倒数第5、第6行可以用下面一行代替：

    cout.setf(ios::internal I ios::showpos);  //包含两个状态标志，用"|"组合

1. 可以看到：对输出格式的控制，既可以用控制符(如例13.2)，也可以用cout流的有关成员函数(如例13.3)，二者的作用是相同的。控制符是在头文件iomanip中定义的，因此用控制符时，必须包含iomanip头文件。cout流的成员函数是在头文件iostream 中定义的，因此只需包含头文件iostream，不必包含iomanip。许多程序人员感到使用控制符方便简单，可以在一个cout输出语句中连续使用多种控制符。

## 文件读写

### 文件流类和文件流对象

输入输出是以系统指定的标准设备（输入设备为键盘，输出设备为显示器）为对象的。在实际应用中，常以磁盘文件作为对象。即从磁盘文件读取数据，将数据输出到磁盘文件。

和文件有关系的输入输出类主要在fstream.h这个头文件中被定义，在这个头文件中主要被定义了三个类，由这三个类控制对文件的各种输入输出操作，他们分别是ifstream、ofstream、fstream，其中fstream类是由iostream类派生而来，他们之间的继承关系见下图所示：

![H:\datas\wiz\temp\7a946582-d202-43a8-9ddf-a5b1f3c82ceb_4_files\05cppios04[1].gif](test_assets/image_195.gif)

由于文件设备并不像显示器屏幕与键盘那样是标准默认设备，所以它在fstream头文件中是没有像cout那样预先定义的全局对象，所以我们必须自己定义一个该类的对象。ifstream类，它是从istream类派生的，用来支持从磁盘文件的输入。ofstream类，它是从ostream类派生的，用来支持向磁盘文件的输出。

fstream类，它是从iostream类派生的，用来支持对磁盘文件的输入输出。

它们都是以ascii码的方式读写

首先#include <fstream>

为了防止漏了关闭，可以.open()和.close()一起写

文件类型分为文本文件（以ASCII码形式存储）和二进制文件

操作文件的三个类：

1. ofstream，写操作
2. ifstream，读操作
3. fstream，读写操作

### 打开方式

所谓打开(open)文件是一种形象的说法，如同打开房门就可以进入房间活动一样。 打开文件是指在文件读写之前做必要的准备工作，包括：

1）为文件流对象和指定的磁盘文件建立关联，以便使文件流流向指定的磁盘文件。

2）指定文件的工作方式，如：该文件是作为输入文件还是输出文件，是ASCII文件还是二进制文件等。

以上工作可以通过两种不同的方法实现:

1) 调用文件流的成员函数open。如

ofstream outfile; //定义ofstream类(输出文件流类)对象outfile

outfile.open("f1.dat",ios::out); //使文件流与f1.dat文件建立关联

第2行是调用输出文件流的成员函数open打开磁盘文件f1.dat，并指定它为输出文件， 文件流对象outfile将向磁盘文件f1.dat输出数据。ios::out是I/O模式的一种，表示以输出方式打开一个文件。或者简单地说，此时f1.dat是一个输出文件，接收从内存 输出的数据。

磁盘文件名可以包括路径，如"c:\\new\\f1.dat"，如缺省路径，则默认为当前目录下的文件。

2) 在定义文件流对象时指定参数

在声明文件流类时定义了带参数的构造函数，其中包含了打开磁盘文件的功能。因此，可以在定义文件流对象时指定参数，调用文件流类的构造函数来实现打开文件的功能。

```
32nocreate
noreplace

nlios:out,

213.6 Sa TS

作用
以 往 入 方式 打开 文件
忆 生 出 方式 打开 文件

是 默认 方式 ) ， 如 时 已 有 此 名 字 的 文件 ， 则 将 其 原 育 内 容 全 部 清除
以 入 出 方式 打开 文件 ， 写 入 的 数据 添加 在 文 ( 寺 直 尾
打开 一 个 已 有 的 文件 ， 文 { 身 旧 针 指向 文件 不 尾

打开 一 个 文件 ,如 时 文件 已 存在 ， 则 山 除 其 中
定 了 ios:out 方 式 ， 而 未 指定 ios: :app ,io

已 一 进 制 方式 打开 一 个 文件 ， 如 不 指定 此 方式 则 默认 为

Dee , MRE, Wt
n, 则 同时 默认 此 方式

方式

打开 一 个 已 有 的 文件 ， 如 文件 不 存在 ， 则 打开 失败 。nocrcate 的 意思 和

TAF

ORT eM

LEAS , RFR SEMEL , replace 的 意思 是 不 更 新 原 有 文件
以 畏 入 和 祖 出 方式 打开 文件 ， 文件 可 读 可 写

局 一 进 制 方式 打开 个 往 出 文件

以 一 进 制 方式 打开 个 答 入 文件
```

几点说明：
1) 新版本的I/O类库中不提供ios::nocreate和ios::noreplace。
2) 每一个打开的文件都有一个文件指针，该指针的初始位置由I/O方式指定，每次读写都从文件指针的当前位置开始。每读入一个字节，指针就后移一个字节。当文件指针移到最后，就会遇到文件结束EOF（文件结束符也占一个字节，其值为-1)，此时流对象的成员函数eof的值为非0值(一般设为1)，表示文件结束了。
3) 可以用“位或”运算符“|”对输入输出方式进行组合，如表13.6中最后3行所示那样。还可以举出下面一些例子：
    ios::in | ios:: noreplace  //打开一个输入文件，若文件不存在则返回打开失败的信息
    ios::app | ios::nocreate  //打开一个输出文件，在文件尾接着写数据，若文件不存在，则返回打开失败的信息
    ios::out l ios::noreplace  //打开一个新文件作为输出文件，如果文件已存在则返回打开失败的信息
    ios::in l ios::out I ios::binary  //打开一个二进制文件，可读可写
但不能组合互相排斥的方式，如 ios::nocreate l ios::noreplace。
4) 如果打开操作失败，open函数的返回值为0(假)，如果是用调用构造函数的方式打开文件的，则流对象的值为0。可以据此测试打开是否成功。如
    if(outfile.open("f1.bat", ios::app) ==0)
        cout <<"open error";
或
    if( !outfile.open("f1.bat", ios::app) )
        cout <<"open error";

### C++对ASCII文件的读写操作

如果文件的每一个字节中均以ASCII代码形式存放数据,即一个字节存放一个字符,这个文件就是ASCII文件(或称字符文件)。程序可以从ASCII文件中读入若干个字符,也可以向它输出一些字符。

1. 用流插入运算符“<<”和流提取运算符“>>”输入输出标准类型的数据。“<<”和“ >>”都巳在iostream中被重载为能用于ostream和istream类对象的标准类型的输入输出。由于ifstream和 ofstream分别是ostream和istream类的派生类；因此它们从ostream和istream类继承了公用的重载函数，所以在对磁盘文件的操作中，可以通过文件流对象和流插入运算符“<<”及 流提取运算符“>>”实现对磁盘文件的读写，如同用cin、cout和<<、>>对标准设备进行读写一样。
2. 用文件流的put、get、geiline等成员函数进行字符的输入输出：用C++流成员函数put输出单个字符、C++ get()函数读入一个字符和C++ getline()函数读入一行字符。

|  |
| --- |
| int main**(){**  char**\*** sourceFileName **=** "./source.txt"**;**  char**\*** targetFileName **=** "./target.txt"**;**  //创建文件输入流对象  ifstream ism**(**sourceFileName**,** ios**::**in**);**  //创建文件输出流对象  ofstream osm**(**targetFileName**,**ios**::**out**);**  **if** **(!**ism**){**  cout **<<** "文件打开失败!" **<<** endl**;**  **}**  **while** **(!**ism**.**eof**()){**  char buf**[**1024**]** **=** **{** 0 **};**  ism**.**getline**(**buf**,**1024**);**  cout **<<** buf **<<** endl**;**  osm **<<** buf **<<** endl**;**  **}**  //关闭文件流对象  ism**.**close**();**  osm**.**close**();**  system**(**"pause"**);**  **return** EXIT\_SUCCESS**;**  **}** |

#### 写文件步骤：

1. #include <fstream>
2. 创建流对象ofstream ofs;
3. 打开文件，ofs.open(“文件路径”,打开方式);

文件路径默认起点是当前项目文件夹，打开方式如下：

![](test_assets/image_197.png)

1. 写数据，ofs<<”写入的数据”;
2. 关闭文件，ofs.close();

追加方式写文件易错点：

![](test_assets/image_198.png)正确写法

![](test_assets/image_199.png)易错写法

前两行为易错写法追加内容，第三行为正确写法追加内容，显然易错写法把最后的“，”吞了

![](test_assets/image_200.png)

自己写文件易错点：

自建txtzhi类的文件时，注意编码保存为ANSI格式，默认保存的utf-8格式在程序读取时一般是乱码

#### 读文件步骤

1. #include <fstream>

2.创建流对象ifstream ifs;

3.打开文件，ifs.open(“文件路径”,打开方式);

![](test_assets/image_201.png)注意是按位或而不是逻辑或

4.判断是否打开成功

```
RAAT
if (lifs is_open0)
{

filelsBmpty = true

cout < “PHTFAM" < endl:
ifs. close0:

system("pause"):
aa
```

5.判断文件为空的情况

```
/7/ 空 文件
char ch:
ifs >> ch:

if (ifs. eof 0)
{

况

cout <« “文件 为 空 ” < endl:
filelsEmpty = true:
ifs.close0:

system pause”):

return;
```

在开始读数据后，ifstream对象指针才会指向文件内部，此时ifs.eof()返回为真说明已经到了文件结尾

6.不为空时先放回上一步读的字符

```
1/ 文件 不 为 空
filelsimpty = false:
ifs. putback (ch) : /让 回 上 画 旋 取 的 字符
```

7.读数据，五种方式读取，推荐第三、四种

```
L152 FR VRB IT ES
char buf [1024] = {0};

while (ifs >》buf)//ifs 对 象 会 一 直 该 文件 直到 结束 后 返回 0
{

1 cout << buf << endl;
```

```
// 第 二 种 读数 据 方式

char buf[1024] = { 0};

while (ifs. getline (buf, sizeof (buf)))//ifs. getline 会 访 满 buf
{

cout << buf << endl;
```

```
// 第 三 种 读数 据 方式
string buf;
while (getline(ifs, buf))//HstringA BAe ee

{

cout << buf << endl;
```

```
Soe RRA

string data:
while (ifs >> data) //iBE)2 18 « AAT RMS ARAL Sit POAT — RAI
{

cout << data << endl
```

```
POPE A, AER
char ¢;
while ((c = ifs. get) != EOFP)// 每 次 只 读 一 个 字符 ，EOF 为 end of file 指 文件 ?|

ifs. close() ;
```

8.关闭文件，ifs.close();

补充：若要一次读完全部数据（含空格、换行等），使用ifs.rdbuf()和stringstream

```
int main() {
ifstream ifs(“test. txt”);
stringstream str;
str << ifs. rdbuf () ;
cout << str. str() << endl;

linel
line 2

line three
read it all
```

### C++对二进制文件的读写操作

二进制文件不是以ASCII代码存放数据的，它将内存中数据存储形式不加转换地传送到磁盘文件，因此它又称为内存数据的映像文件。因为文件中的信息不是字符数据，而是字节中的二进制形式的信息，因此它又称为字节文件。

对二进制文件的操作也需要先打开文件，用完后要关闭文件。在打开时要用ios::binary指定为以二进制形式传送和存储。二进制文件除了可以作为输入文件或输出文件外,还可以是既能输入又能输出的文件。这是和ASCII文件不同的地方。

**用成员函数read和write读写二进制文件**

对二进制文件的读写主要用istream类的成员函数read和write来实现。这两个成员函数的原型为
    istream& read(char \*buffer,int len);
    ostream& write(const char \* buffer,int len);
字符指针buffer指向内存中一段存储空间。len是读写的字节数。调用的方式为：
    a. write(p1,50);
    b. read(p2,30);
 上面第一行中的a是输出文件流对象，write函数将字符指针p1所给出的地址开始的50个字节的内容不加转换地写到磁盘文件中。在第二行中，b是输入文件流对象，read 函数从b所关联的磁盘文件中，读入30个字节(或遇EOF结束），存放在字符指针p2所指的一段空间内。

|  |
| --- |
| class Person**{**  public**:**  Person**(**char**\*** name**,**int age**){**  strcpy**(this->**mName**,** name**);**  **this->**mAge **=** age**;**  **}**  public**:**  char mName**[**64**];**  int mAge**;**  **};**  int main**(){**  char**\*** fileName **=** "person.txt"**;**  //二进制模式读写文件  //创建文件对象输出流  ofstream osm**(**fileName**,** ios**::**out **|** ios**::**binary**);**  Person p1**(**"John"**,**33**);**  Person p2**(**"Edward"**,** 34**);**  //Person对象写入文件  osm**.**write**((**const char**\*)&**p1**,sizeof(**Person**));**  osm**.**write**((**const char**\*)&**p2**,** **sizeof(**Person**));**  //关闭文件输出流  osm**.**close**();**  //从文件中读取对象数组  ifstream ism**(**fileName**,** ios**::**in **|** ios**::**binary**);**  **if** **(!**ism**){**  cout **<<** "打开失败!" **<<** endl**;**  **}**    Person p3**;**  Person p4**;**  ism**.**read**((**char**\*)&**p3**,** **sizeof(**Person**));**  ism**.**read**((**char**\*)&**p4**,** **sizeof(**Person**));**  cout **<<** "Name:" **<<** p3.mName **<<** " Age:" **<<** p3.mAge **<<** endl**;**  cout **<<** "Age:" **<<** p4.mName **<<** " Age:" **<<** p4.mAge **<<** endl**;**  //关闭文件输入流  ism**.**close**();**  system**(**"pause"**);**  **return** EXIT\_SUCCESS**;**  **}** |

#### 二进制写文件步骤

二进制写文件的好处，能够写入出了字符以外的其他数据类型入文件

1.#include <fstream>

2.创建流对象ofstream ofs;

3.打开文件，ofs.open(“文件路径”,ios::out|ios::binary);

4.写数据，ofs.write(const char\* p, sizeof(要写入的数据类型))

5.关闭文件，ofs.close();

需要注意的是，写入的数据是任意数据类型（类对象和结构体都可以，如类对象Person p），然后取地址&p，把指针类型转为write函数要求的格式(const char \*) &p，如下

```
int main()

{

ofstream ofs;
ofs. open (“person. txt”, ios: :out| ios: :binary)

Person p = { “8k=",18 };//SA Jad 3 般 会 乱码 ， 但 没关系 再 用 二 进 制 读 就 好 了
ofs. write((const chars)&p, sizeof (Person)) ;

ofs. close() ;
```

#### 二进制读文件步骤

二进制读文件的好处，能够读除了字符以外的其他数据类型入文件

1.#include <fstream>

2.创建流对象ifstream ifs;

3.打开文件，ifs.open(“文件路径”,ios::in|ios::binary);

4.判断是否打开成功，if(!ifs.is\_open()) {cout<<”打开失败”<<endl; return 0;}

5.读数据，ifs.read(char\* p, sizeof(要写入的数据类型))

5.关闭文件，ifs.close();

需要注意的是，读入数据类型需要提前知道并创建容器来接收，然后取地址&p，把指针类型转为read函数要求的格式(char \*) &p，如下

```
int main ()

{

ifstream ifs;
ifs. open(“person. txt”, ios::
if (!ifs. is_open())

lios::binary) ;

{
cout《《“ 文 件 打开 失败 ”<< endl;
|| return 0;
__}
Person p.|

ifs. read((char#)&p, sizeof (Person)) ;
cout << “HS: ” « p.m Name <<” EB. ” << pm Age << endl;
ifs. close ();
```

#### 避免使用string

以类为单位进行二进制读写，类中有成员为string类型

写入过程没有报错，读入过程没有报错，但读完函数结束析构类时出错了

准确来说是析构类中成员string时出错了

![](test_assets/image_213.png)

显然析构时释放非法内存报错了

由于string的空间有可能开辟在栈区，即使在同一main函数中完成读写操作也可能报错

所以字符串成员用char数组不要用string

# 异常

## 3.1 异常基本概念

|  |
| --- |
| **一句话：异常处理就是处理程序中的错误。所谓错误是指在程序运行的过程中发生的一些异常事件（如：除0溢出，数组下标越界，所要读取的文件不存在,空指针，内存不足等等）。** |

**回顾一下：我们以前编写程序是如何处理异常？**

在C语言的世界中，对错误的处理总是围绕着两种方法：一是使用整型的返回值标识错误；二是使用errno宏（可以简单的理解为一个全局整型变量）去记录错误。当然C++中仍然是可以用这两种方法的。

这两种方法最大的缺陷就是会出现不一致问题。例如有些函数返回1表示成功，返回0表示出错；而有些函数返回0表示成功，返回非0表示出错。

还有一个缺点就是函数的返回值只有一个，你通过函数的返回值表示错误代码，那么函数就不能返回其他的值。当然，你也可以通过指针或者C++的引用来返回另外的值，但是这样可能会令你的程序略微晦涩难懂。

**c++异常机制相比C语言异常处理的优势?**

- 函数的返回值可以忽略，但异常不可忽略。如果程序出现异常，但是没有被捕获，程序就会终止，这多少会促使程序员开发出来的程序更健壮一点。而如果使用C语言的error宏或者函数返回值，调用者都有可能忘记检查，从而没有对错误进行处理，结果造成程序莫名其面的终止或出现错误的结果。
- 整型返回值没有任何语义信息。而异常却包含语义信息，有时你从类名就能够体现出来。
- 整型返回值缺乏相关的上下文信息。异常作为一个类，可以拥有自己的成员，这些成员就可以传递足够的信息。
- 异常处理可以在调用跳级。这是一个代码编写时的问题：假设在有多个函数的调用栈中出现了某个错误，使用整型返回码要求你在每一级函数中都要进行处理。而使用异常处理的栈展开机制，只需要在一处进行处理就可以了，不需要每级函数都处理。

|  |
| --- |
| [//如果判断返回值，那么返回值是错误码还是结果？](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)  [//如果不判断返回值，那么b==0时候，程序结果已经不正确](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)  [//A写的代码](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)  [int A\_MyDivide](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[int a](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[,](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[int b](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  **[if](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)****[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[b](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp) **[==](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [0](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  **[return](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)****[-](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[1](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  **[return](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [a](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp) **[/](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [b](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  [//B写的代码](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)  [int B\_MyDivide](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[int a](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[,](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[int b](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  [int ba](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp) **[=](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [a](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp) **[+](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [100](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  [int bb](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp) **[=](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [b](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  [int ret](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp) **[=](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [A\_MyDivide](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[ba](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[,](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [bb](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [//由于B没有处理异常，导致B结果运算错误](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)  **[return](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [ret](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  [//C写的代码](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)  [int C\_MyDivide](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[(){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  [int a](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp) **[=](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [10](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  [int b](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp) **[=](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [0](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  [int ret](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp) **[=](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [B\_MyDivide](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[a](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[,](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [b](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [//更严重的是，由于B没有继续抛出异常，导致C的代码没有办法捕获异常](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)  **[if](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)****[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[ret](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp) **[==](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)****[-](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[1](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  **[return](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)****[-](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[1](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  **[else{](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  **[return](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)** [ret](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)**  [//所以,我们希望：](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)  [//1.异常应该捕获，如果你捕获，可以，那么异常必须继续抛给上层函数,你不处理，不代表你的上层不处理](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp)  [//2.这个例子，异常没有捕获的结果就是运行结果错的一塌糊涂，结果未知，未知的结果程序没有必要执行下去](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\01 传统异常问题抛出.cpp) |

## 3.2 异常语法

### 3.2.1 异常基本语法

**int func(int a, int b)**

**{**

**if (b == 0)**

**{**

**//2.抛出异常**

**throw 10;//抛出一个int类型的异常，**

**}**

**return a / b;**

**}**

**void test()**

**{**

**int a = 10;**

**int b = 0;**

**//1.把有可能出现异常的代码块放到try中**

**try**

**{**

**func(a, b);**

**}**

**catch (int)//3.接收一个int类型的异常**

**{**

**cout << "接收一个int类型的异常" << endl;**

**}**

**}**

**总结:**

- 若有异常则通过throw操作创建一个异常对象并抛出，之后的代码不执行，直接到catch。
- 将可能抛出异常的程序段放到try块之中。
- 如果在try段执行期间没有引起异常，那么跟在try后面的catch字句就不会执行。
- catch子句会根据出现的先后顺序被检查，匹配的catch语句捕获并处理异常(或继续抛出异常)
- 如果匹配的处理未找到，则运行函数terminate将自动被调用，其缺省功能调用abort终止程序。
- 处理不了的异常，可以在catch的最后一个分支，使用throw，向上抛。

c++异常处理使得异常的引发和异常的处理不必在一个函数中，这样底层的函数可以着重解决具体问题，而不必过多的考虑异常的处理。上层调用者可以在适当的位置设计对不同类型异常的处理。

### 3.2.2 异常严格类型匹配

异常机制和函数机制互不干涉,但是**捕捉方式是通过严格类型匹配**。

|  |
| --- |
| [void TestFunction](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[(){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**    [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** ["开始抛出异常..."](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** [endl](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  [//throw 10; //抛出int类型异常](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)  [//throw 'a'; //抛出char类型异常](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)  [//throw "abcd"; //抛出char\*类型异常](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)  [string ex](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[=](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** ["string exception!"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[throw](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** [ex](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  [int main](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[(){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[try{](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  [TestFunction](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[();](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[catch](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)****[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[int](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** ["抛出Int类型异常!"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** [endl](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[catch](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)****[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[char](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** ["抛出Char类型异常!"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** [endl](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[catch](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)****[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[char](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[\*){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** ["抛出Char\*类型异常!"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** [endl](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[catch](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)****[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[string](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** ["抛出string类型异常!"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** [endl](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  [//捕获所有异常](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)  **[catch](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)****[(...){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** ["抛出其他类型异常!"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** [endl](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  [system](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**["pause"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[return](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** [EXIT\_SUCCESS](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\03 c++异常捕获严格匹配类型)** |

### 3.2.3 栈解旋(unwinding)

异常被抛出后，从进入try块起，到异常被抛掷前，这期间在栈上构造的所有对象，都会被自动析构。析构的顺序与构造的顺序相反，这一过程称为栈的解旋(unwinding).

|  |
| --- |
| class Person**{**  public**:**  Person**(**string name**){**  mName **=** name**;**  cout **<<** mName **<<** "对象被创建!" **<<** endl**;**  **}**  **~**Person**(){**  cout **<<** mName **<<** "对象被析构!" **<<** endl**;**  **}**  public**:**  string mName**;**  **};**  void TestFunction**(){**    Person p1**(**"aaa"**);**  Person p2**(**"bbb"**);**  Person p3**(**"ccc"**);**  //抛出异常  **throw** 10**;**  **}**  int main**(){**  **try{**  TestFunction**();**  **}**  **catch** **(...){**  cout **<<** "异常被捕获!" **<<** endl**;**  **}**  system**(**"pause"**);**  **return** EXIT\_SUCCESS**;**  **}** |

### 3.2.4 异常接口声明

- 为了加强程序的可读性，可以在函数声明中列出可能抛出异常的所有类型，例如：void func() throw(A,B,C);这个函数func能够且只能抛出类型A,B,C及其子类型的异常。
- 如果在函数声明中没有包含异常接口声明，则此函数可以抛任何类型的异常，例如:void func()
- 一个不抛任何类型异常的函数可声明为:void func() throw()
- 如果一个函数抛出了它的异常接口声明所不允许抛出的异常,unexcepted函数会被调用，该函数默认行为调用terminate函数中断程序。

|  |
| --- |
| [//可抛出所有类型异常](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)  [void TestFunction01](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[(){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  **[throw](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)** [10](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  [//只能抛出int char char\*类型异常](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)  [void TestFunction02](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[()](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)****[throw(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[int](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[,](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[char](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[,](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[char](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[\*){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  [string exception](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明) **[=](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)** ["error!"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  **[throw](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)** [exception](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  [//不能抛出任何类型异常](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)  [void TestFunction03](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[()](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)****[throw(){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  **[throw](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)** [10](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  [int main](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[(){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  **[try{](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  [//TestFunction01();](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)  [//TestFunction02();](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)  [//TestFunction03();](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  **[catch](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)****[(...){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)** ["捕获异常!"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)** [endl](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**    [system](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**["pause"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  **[return](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)** [EXIT\_SUCCESS](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\05 异常接口声明)** |

Qt、Linux 正确，vs不行

### 3.2.5 异常的对象传递

#### 1.产生三个对象

class Maker

{

public:

Maker()

{

cout << "Maker的构造" << endl;

}

Maker(const Maker &m)

{

cout << "Maker的拷贝构造" << endl;

}

~Maker()

{

cout << "Maker的析构" << endl;

}

};

//产生三个对象

void func1()

{

Maker m;//第一个对象，在异常接收前被释放

throw m;//第二个对象，是第一个对象拷贝过来的（因为栈解旋机制，不是同一个对象）

}

void test01()

{

try

{

func1();

}

catch (Maker m1)//第三个对象，是第二个对象拷贝过来的

{

cout << "接收一个Maker类型的异常" << endl;

//第二个和第三个对象在catch结束时释放

}

}

#### 2.产生二个对象

void func2()

{

//第一个对象

throw Maker();//匿名对象

}

void test02()

{

try

{

func2();

}

catch (Maker m1)//第二个对象

{

cout << "接收一个Maker类型的异常" << endl;

//第一个和第二个对象在catch结束时释放

}

}

#### 3.产生一个对象（常用这个）

void func3()

{

throw Maker();//匿名对象

}

void test03()

{

try

{

func3();

}

catch (Maker &m1)//用引用形式接收，避免值传递

{

cout << "接收一个Maker类型的异常" << endl;

}

}

另一种是地址形式，比引用麻烦一些

void func4()

{

//编译器不允许对栈中的匿名对象取地址操作

//throw Maker();//匿名对象

//编译器允许对堆区中的匿名对象取地址操作

throw new Maker();

}

void test04()

{

try

{

func4();

}

catch (Maker \*m1)

{

cout << "接收一个Maker类型的异常" << endl;

delete m1;

}

}

### 3.2.6 异常的多态使用

//异常基类

class BaseException{

public:

virtual void printError(){};

};

//空指针异常

class NullPointerException : public BaseException{

public:

virtual void printError(){

*cout* << "空指针异常!" << *endl*;

}

};

//越界异常

class OutOfRangeException : public BaseException{

public:

virtual void printError(){

*cout* << "越界异常!" << *endl*;

}

};

void doWork(){

throw NullPointerException();

}

void test()

{

try{

doWork();

}

catch (BaseException& ex){

ex.printError();

}

}

## 3.3 C++标准异常库

### 3.3.1 标准库介绍

标准库中也提供了很多的异常类，它们是通过类继承组织起来的。异常类继承层级结构图如下：

![](test_assets/image_214.png)

每个类所在的头文件在图下方标识出来。

**标准异常类的成员：**

① 在上述继承体系中，每个类都有提供了构造函数、复制构造函数、和赋值操作符重载。

② logic\_error类及其子类、runtime\_error类及其子类，它们的构造函数是接受一个string类型的形式参数，用于异常信息的描述

③ 所有的异常类都有一个what()方法，返回const char\* 类型（C风格字符串）的值，描述异常信息。

**标准异常类的具体描述：**

|  |  |
| --- | --- |
| 异常名称 | 描述 |
| exception | 所有标准异常类的父类 |
| bad\_alloc | 当operator new and operator new[]，请求分配内存失败时 |
| bad\_exception | 这是个特殊的异常，如果函数的异常抛出列表里声明了bad\_exception异常，当函数内部抛出了异常抛出列表中没有的异常，这是调用的unexpected函数中若抛出异常，不论什么类型，都会被替换为bad\_exception类型 |
| bad\_typeid | 使用typeid操作符，操作一个NULL指针，而该指针是带有虚函数的类，这时抛出bad\_typeid异常 |
| bad\_cast | 使用dynamic\_cast转换引用失败的时候 |
| ios\_base::failure | io操作过程出现错误 |
| logic\_error | 逻辑错误，可以在运行前检测的错误 |
| runtime\_error | 运行时错误，仅在运行时才可以检测的错误 |

**logic\_error的子类：**

|  |  |
| --- | --- |
| 异常名称 | 描述 |
| length\_error | 试图生成一个超出该类型最大长度的对象时，例如vector的resize操作 |
| domain\_error | 参数的值域错误，主要用在数学函数中。例如使用一个负值调用只能操作非负数的函数 |
| out\_of\_range | 超出有效范围 |
| invalid\_argument | 参数不合适。在标准库中，当利用string对象构造bitset时，而string中的字符不是’0’或’1’的时候，抛出该异常 |

**runtime\_error的子类：**

|  |  |
| --- | --- |
| 异常名称 | 描述 |
| range\_error | 计算结果超出了有意义的值域范围 |
| overflow\_error | 算术计算上溢 |
| underflow\_error | 算术计算下溢 |
| invalid\_argument | 参数不合适。在标准库中，当利用string对象构造bitset时，而string中的字符不是’0’或’1’的时候，抛出该异常 |

|  |
| --- |
| [#include<stdexcept>](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)  [class Person](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[{](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  [public](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[:](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  [Person](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[int age](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  **[if](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)****[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[age](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类) **[<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)** [0](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类) **[||](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)** [age](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类) **[>](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)** [150](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  **[throw](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)** [out\_of\_range](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**["年龄应该在0-150岁之间!"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  [public](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[:](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  [int mAge](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  **[};](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  [int main](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[(){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  **[try{](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  [Person p](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[151](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  **[catch](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)****[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[out\_of\_range](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[&](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)** [ex](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[){](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  [cout](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类) **[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)** [ex](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[.](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[what](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[()](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)****[<<](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)** [endl](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**    [system](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[(](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**["pause"](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[);](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  **[return](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)** [EXIT\_SUCCESS](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**[;](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)**  **[}](C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Word\\示例代码\\07 标准异常类)** |

### 3.3.2 编写自己的异常类

① 标准库中的异常是有限的；

② 在自己的异常类中，可以添加自己的信息。（标准库中的异常类值允许设置一个用来描述异常的字符串）。

**2. 如何编写自己的异常类？**

① 建议自己的异常类要继承标准异常类。因为C++中可以抛出任何类型的异常，所以我们的异常类可以不继承自标准异常，但是这样可能会导致程序混乱，尤其是当我们多人协同开发时。

② 当继承标准异常类时，应该重载父类的what函数和虚析构函数。

③ 因为栈展开的过程中，要复制异常类型，那么要根据你在类中添加的成员考虑是否提供自己的复制构造函数。

|  |
| --- |
| //自定义异常类  class MyOutOfRange:public *exception*  {  public:  MyOutOfRange(const *string* errorInfo)  {  this->m\_Error = errorInfo;  }  MyOutOfRange(const char \* errorInfo)  {  this->m\_Error = *string*( errorInfo);  }  virtual ~MyOutOfRange()  {    }  virtual const char \* what() const  {  return this->m\_Error.*c\_str*() ;  }  *string* m\_Error;  };  class Person  {  public:  Person(int age)  {  if (age <= 0 || age > 150)  {  //抛出异常 越界  //cout << "越界" << endl;  //throw out\_of\_range("年龄必须在0~150之间");  //throw length\_error("长度异常");  throw MyOutOfRange(("我的异常 年龄必须在0~150之间"));  }  else  {  this->m\_Age = age;  }    }  int m\_Age;  };  void test01()  {  try  {  Person p(151);  }  catch ( *out\_of\_range* & e )  {  *cout* << e.*what*() << *endl*;  }  catch (*length\_error* & e)  {  *cout* << e.*what*() << *endl*;  }  catch (MyOutOfRange e)  {  *cout* << e.*what*() << *endl*;  }  } |

# 模板

## 函数模板

### 定义

建立一个通用函数，函数返回值类型和形参类型不具体确定 ，用一个虚拟的类型代表，语法如下：

template <typename T>

函数声明或定义，其中待定类型用T替换

其中template告诉编译器要创建模板，typename（可以用class替换）告诉编译器后面的是待定数据类型的名称

### 原理

![](test_assets/image_215.png)

二次编译

```
void mySwap(T &a,T &b)// 第 一 次 编译
{

T tmp = a;

a= bi

b = tmp;
```

```
mySwap (a,D);//SSPReRE RSA AR VAAT , ETT SR.

/*
void on int &b)
{

int tmp = a;

a= bi;
b = tmp;

af
```

### 定义在头文件

当你将模板函数的定义（实现）放在 .cpp 文件中，而只将声明放在 .h 文件中时，编译器在编译 .cpp 文件时并不知道将来会有哪些类型会使用这个模板，因此不会为任何类型生成（实例化）代码。等到链接阶段，主函数调用模板函数时，链接器找不到对应的实例化函数，就会报错。

模板实例化发生在编译时。当编译器看到一个对模板函数的调用时，它必须能看到模板的完整定义，才能生成特定类型的代码。将定义放在头文件中，可以确保在每个需要它的编译单元 (.cpp) 中都能看到并实例化它。

放在cpp中有的时候能对，是因为其他文件中的调用，与该cpp中的调用完全一致，所以直接复用

### 调用

调用方法：

1. 自动推导类型。调用函数模板时，传入参数编译器即知道数据类型，但要注意推导出的数据类型必须一致。
2. 显示指定类型。函数名<T的具体数据类型>(参数列表)，调用函数时直接告诉编译器用什么数据类型

调用规则：

首先函数模版和普通函数可以重载，即同名函数函数模版和普通函数共存。函数模版之间也可以重载

```
(/ e938 PB BS eB SOB FA EIU

//1、 如 果 函 数 模板 和 普通 函数 都 可 以 调用 ， 优 先 调用 普通 函数
//2、 可 以 通过 空 模板 参数 列表 强制 调用 函数 模板

//3、 函 数 模板 可 以 发 生 函 数 重 载

//4、 如 果 函 数 模板 可 以 产生 更 好 的 匹配 ， 优 先 调用 函数 模板

void myPrint(int a, int b);

//{

// cout 《《“ 调 用 的 普通 函数 ”< endl;
I

template<class T>
void myPrint(T a, T b)
{
cout << “iA Ra” << endl:
```

第一点即使普通函数没有定义只有声明也是调用普通函数，然后报错

第二点的空模板参数列表指的是myPrint<>(1, 2);此时强制使用函数模板

第三点就是通过参数列表的不同来重载

第四点是，如果调用普通函数时需要隐式类型转换（如myPrint(‘a’, ‘b’);)，那么优先调用函数模板

如果编译器无法判断T类型的，会报错

![](test_assets/image_219.png)

```
TnySwap2<> () ;
```

### 隐式类型转换

```
// 普 通 函数
int myAdd01(int a ，int b)
{

t

void test0l()
{

return a +b;

int a= 10;
int b = 20)
char c='c'; //a-97 c-99
cout << myAddOl (a, ¢) << endl;
```

函数模板用自动类型推导调用不可以发生隐式类型转换，用显示指定类型调用可以发生隐式类型转换（显示指定类型就相当于普通函数了，普通函数可以隐式类型转换）

```
int myAdd01(int a, int b)

return a + b;

}

template<class D>
T myAdd02(T a, T b)

{

! return a + b;
}

REEL

void test01 ()
{

c
7/ 普通 函数 隐 式 类 型 转换
<< myadd01(a，c) << endl;

V/ 目 动 类 型 推导
cout] << Add02(a，c) << endl;

示 指 定 类 型
cout] << myadd02<int>(a，c) << endl;
```

但要注意引用传参时，即使显示指定也无法隐式转换（显然传参过程不应把b1从double变成int）

```
/*

template<class T>// 让 编译 器 看 到 这 句 话 后 面 紧 跟着 的 函数 里 有 T 不 要 报错
void mySwap(T &, T &b)// 第 一 次 编译

{

T tmp = a;

a= b;

b = tmp;
}
*/
int al = 10;
double bl = 20;
mySwap<int>(al, bl
```

### 模板具体化

模板不是万能的。比如比较a==b ? return true; : return false;的模板函数，当a、b不为系统内置的数据类型（比如含姓名和年龄的Person类）时，编译器就不知道怎么比较了。此时可以通过重载运算符的方法解决，也可以给模板在特殊数据类型时的具体实现做个特例。

```
// 利 用 具体 化 Person 的 版 本 实现 代码 ， 有 具体 化 优先 调用

cee bool myCompare (QBEBOH &D1, Person &D2)

{
if (pl.m_ Name == p2.mName && pl.m_Age == p2.m Age)
{ I

return true;
}
else
{
return false;
}
}
```

写在函数模版定义之后

不建议这么用，因为没有通用性

### 模板Lambda函数

C++14起用auto，等效模板

```
auto get_container_size = [] (auto container) { return container.size(); };
```

C++20起

```
auto lambda = []<typename T>(T t){
// do something
35
```

## 类模板

![](test_assets/image_227.png)

### 模板类（实例化）

```
TRB —
template<class NameType, class AgeType> >)
class Person

{

public:
Person (NameType name, AgeType age)
{ I

this->m Name = name;
this->m_Age = age;|
}

NameType m Name;
AgeType m Age;
```

```
void teste1()
{
// 指定 NameType 为 string 兴 型 ，AgeType 为 int 尖 型
Personcstring, int>P1("2MBS", 999);
P1.shouPerson()5
```

这里是显示调用，因为类模板不能自动推导，没有隐式调用

此外类模板再参数列表中可以有默认参数，函数模板则不可以

```
// 兴 模板
cemplatecc1ass NaneType，c1ass AgeType = int>
class Person
4
public

Person(NameType name, AgeType age)
```

```
//2. FARBER MRE BINA PF A AAAS BL
=void test02()
{

Person<string>p("##/\m”, 999) ;

p. showPerson() ;
```

和函数参数默认值类似，左边有默认值右边的全都得有默认值

```
class Maker3
{

aa ee oe

template<class NameType, class AgeType = —
```

![](test_assets/image_233.png)

### 具体化

注意区分实例化与具体化，具体化是某类型时的特例

![](test_assets/image_234.png)

```
Hinclude <iostream

using namespace std;

7/ 1 BARE
template<class T>
struct TemplateStruct
{
TemplateStruct ()
{
cout << sizeof (T) << endl;

/4 总 模板 显示 实例 化

template struct TemplateStruct<int>;

1/43 模板 具体 化
template<》 struct TemplateStruct<double>
{
TemplateStruct() {
cout << “=-8--" << endl;

int main@

{
TemplateStruct<int> intStruct;
TemplateStruct<double> doubleStruct;

/4 #4 模板 隐 式 实例 化

TemplateStruct<char> 11Struct;
```

![](test_assets/image_236.png)

### 模板特化与重载的区别

使用效果类似，但有优先级: 普通函数>模板特化>模板函数

![](test_assets/image_237.png)

### 成员函数创建时机

程序运行到调用成员函数时，才会去创建类模板中的成员函数，见学习文件例子

### 继承类模板

![](test_assets/image_238.png)

### 成员函数类外实现

主要是作用域声明带上<>，让编译器知道这是类模板

```
// 类 模
template<class Tl,class T2>
Iclass Person

public:
Person(Tl name, 12 age);

void showPerson() ;

template<class Tl, class T2>
Person<T1, 12>: :Person (T1 name, T2 age)// 作 用 域 声明 Person《T1, T2> 必 须要 带 人 T1, T2>， 不 然 编 译 器 不 知
{

m_Name = name;
m_Age = age;

template<class Tl, class 12>
lvoid Person<T1, 12>: : showPerson()
{

cout << “HAA: ” « mName 《《“\t 年 龄 为 : “”《《 mAge << endl:
a
```

### 类模板分文件编写

按照一般规则分.h和.cpp会报错

因为类模板里的函数如果有用T类型，本质上是函数模板

而函数模板有二次编译机制，第一次看到知道是函数模板但不会编译（因为无法确定函数内T类型局部变量占用的内存空间），第二次看到是调用时已经知道T类型再编译函数

分开.h和.cpp后，因为读的是.h，看到的是函数模板（第一次编译，无法确定函数内T类型局部变量占用的内存空间，所以没有编译函数即没有函数入口地址，其他函数这会儿已经编译了.cpp中的实现，就在代码区有函数入口地址），调用时已经知道T类型但一般include的是.h没有实现，所以编译器找不到函数实现进行二次编译，报错

解决办法：不要分开，声明和定义写在一起，hpp后缀文件

有一个地方需要注意：

一般定义写在.h中是铁定要报错的，比如一个项目中有这些文件

![](test_assets/image_240.png)

其中test.h中有一个函数写了定义

```
;

DNMOMOLwWYeH

test.cpp* Maker.hpp

#pragma once
: @

svoid mytest ()

{
}

cout << “mytest” << endl;

10%
```

在另一文件中include这个文件

```
i ee eee

4 ae
> B Makerhpp
> B testh
> 36 外 部 依赖 项
4 司 源 文件
”++ 10 类 模版 分 文件 六 写 问题 及 解决 方 ;

Ce

ONIAH WH

11
12
13
14

#include<string?

using namespace std;

| #include” Maker. hpp”
#include” test. h”

日 /来

template<class NameType, cle
Maker<NameType, AgeType>: :Me
{

NameType str;

cout << “fie BR” << endl;
this->name = name;

obs 4 eis tak
```

运行时会报错，因为头文件展开相当于在该文件中重新定义了mytest函数，编译器报错函数重定义

![](test_assets/image_243.png)

但是.hpp中也给了函数实现，并且没有报错，这是因为编译器对类的成员函数做了特殊处理，直接在头文件定义也没问题

![](test_assets/image_244.png)

### 类模板与友元

类内实现和面向对象中的一致，推荐使用

类外实现非常麻烦详见学习文件，不推荐使用

## 可变参数模板

一个可变参数模板就是一个接收可变数目参数的模板函数或模板类。可变数目的参数被称为参数包。存在两种参数包：模板参数包，表示零个或多个模板参数；函数参数包，表示零个或多个函数参数。

### 定义

使用一个省略号来指出一个模板参数或函数参数表示一个包。在一个模板参数列表中，class...或typename...指出接下来的参数表示零个或多个类型的列表；一个类型名后面跟一个省略号表示零个或多个给定类型的非类型参数的列表。在函数参数列表中，如果一个参数的类型是一个模板参数包，则此参数也是一个函数参数包。

```
ORWNR

template<typename T, typename...
void foo(const T& t, const Args&

Args>
- rest);
```

```
RWNE

foo(i, s, 42,
foo(s, 42, "hi

foo(d, s);
foo("hi"
```

### sizeof...

```
template<typename... Args>
void g(Args... args)
{

cout << sizeof... (Args)
cout << sizeof... (args)

endl;
endl;

1
2
3
4
5
6
```

### 可变参数函数模板

可变参数函数通常是递归的。第一步调用处理包中的第一个实参，然后用剩余实参调用自身。print函数是这样的模式，每次递归调用将第二个实参打印到第一个实参表示的流中。为了终止递归，还需要定义一个非可变参数的print函数，它接收一个流和一个对象：

```
// 用 来 终止 递归 并 打印 最 后 一 个 元 ah
J MARR ARTE PT SES AN RASHID Fin tT CZ BPR
template<typename T>

ostream Sprint (ostream& os, const T& t)

{

return os << t;
}
1/8207 BEAT ZINTA SRE CAH rint
template<typename T,typename... Args>
10 | ostream& print(ostream& os, const T& t, const Args&... rest)
11/{
12| os<ct<",*; TEBE
return print(os, rest...); /7 地 上 调用， 打印 其 他 实 参

CaAYVAMAWNHE
```

![](test_assets/image_249.png)

### 拓展

扩展一个包就是将它分解为构成的元素，对每个元素应用模式，获得扩展后的列表。我们通过在模式右边放一个省略号（...）来触发扩展操作。

```
ww IN

oun

template<typename T, typename... Args>
stream& print (ostream& os, const T& t,

os << t <<", "5
re

rn pri

const Args&.

rest)

// 扩 展 Args
```

第一个扩展操作扩展模板参数包，为print生成函数参数列表。第二个扩展操作出现在对print调用。此模式为print调用生成实参列表。

![](test_assets/image_251.png)

```
理解 包 扩展

可 以 编写 第 二 个 可 变 :

9_rep ， 然 后 调用 print 打印 结果 string 。

// 在 print 调 用 中 对 每 个 实 参 调用 debug_rep
template<typename... Args>
ostream& errorMsg(ostream& os, const Args&... rest)

{

//print(os, debug_rep(a1), debug_rep(a2), ..., debug_rep(an))
return print(os, debug_rep(rest)...);

Nouswne

) 。 此 模式 表示 我 们 希望 对 函

素 调用 debug_rep 。 扩 展 :

errorMsg(cerr, fcnName, code.num(), otherData, "other", item);

debug_rep(otherData), debug_rep("otherData")

1

2

3 | print(cerr, debug_rep(fenName), debug_rep(code.num())
4

5 debug_rep(item));

7/ 将 包 传递 给 debug_rep;print(os，debug_rep(al,a2
print(os,debug_rep (rest. . . ))// 错 误 ， 此 调用 无 匹配 区 数

得 的 问题 是 我 调用 中 扩展 了 rest 。 它 等

print(cerr，debug_rep(fcnName，code.num()，otherData，"other"，item));
```

```
class Strvec{
public:
template<class... Args>
void emplace_back(Args&s. .

包 扩展 中 的 模式 是 有 &

template<class...
inline void Strve

{

Args>
::emplace_back(Args&&... args)

chk_n_alloc();
alloc.construct (first_freet+, std::forward<Args>(args)..

OuaWNR
```

## 模板重载

函数需要对不同类型输入做不同处理，用函数重载

模板函数需要对A类型输入是处理方法a，对其他所有类型是处理方法b，用模板特化

模板函数需要对一部分类型（A,B,C,D等满足部分条件的类型）是处理方法a，对其他所有类型是处理方法b，就需要模板重载

但模板函数不能重载，因为无论什么类型都能变成T，实现方法是enable\_if

### SFINAE原则

C++模板函数重载依赖于 SFINAE (substitution-failure-is-not-an-error) 原则，即替换失败不认为是错误，而只是简单地pass掉。

```
#include <iostream>
using namespace std;
void f(double a){
cout<<"in double f()"<<endl;
}
template<typename T>
void f(typename T::noexist a){

cout<<"in T::noexist f()"<<endl;

}

int main(){
#(1);
(1.0);
```

![](test_assets/image_255.png)

可以看到double和int都没有一个叫noexist的类型，所以解析是失败的，但是直接跳过，调用f的时候都转换为double输出。

利用这个原则，我们可以构建一个开关的类，当满足某一条件时，让某类型能出现，不满足时，让他没有该类型，解析失败。

这个开关函数就是 enable\_if。

### Enable\_if

enable\_if是c++的标准模板，其实现非常简单，这里我们给出其实现的一种方式：

```
template<bool B, class T = void>
struct user_enable_if {};
template<class T>
struct user_enable_if<true, T> { typedef T type; };
```

这里我们部分偏特化了当条件B为true时的模板user\_enable\_if，与普通的user\_enable\_if的区别就在于定义了type类型

这样，用户使用typename user\_enable\_if<cond, Type>::type时，当cond为true时，这个表达式是一个类型，而当cond为false时，该表达式解析失败。

### 用法

```
template<bool B, class T = void>
struct user_enable_if {};
template<class T>

struct user_enable_if<true, T> {

struct A{};

template<typename T>

struct Traits{

static const bool is_basic

35

template<>
struct Traits<A>{
static const bool is_basic =

35

template<typename T>

typedef T type; };

true;

false;

void f(T a, typename user_enable_if<Traits<T>::is_basic, void>::type* dump= @){

cout<<"a basic type"<<endl;

template<typename T>

void f(T a, typename user_enable_if<!Traits<T>

cout<<"a class type"<<endl;

int main(){
Aa;
f(1)5
f(a);

::is_basic, void>::type* dump= 6){
```

在这里，当f的输入是1时，Traits::is\_basic为true，user\_enable\_if<Traits::is\_basic>::type能得到一个type(void)，因此能实例化，

而第二个模板不能实例化。而当f的输入是a时，结果正好相反。

但有时后我们对参数个数有限制（例如，我们是重载的operator函数，参数个数被严格限制），这时候我们可以把enable\_if加到返回值上。

```
template<typename T>

typename user_enable_if<Traits<T>::is_basic, T>::type f(T a){

cout<<"a basic type"<<endl;

return a;

template<typename T>
typename user_enable_if<!Traits<T>
cout<<"a class type"<<endl;

return a;

int main(){
Aa;
f(1)5
f(a);

::is_basic, T>

ritype F(T a){
```

## CRTP

# STL（standard template library）

## 六大组件

STL提供了六大组件，彼此之间可以组合套用，这六大组件分别是:容器、算法、迭代器、仿函数、适配器、空间配置器。

**容器：**各种数据结构，如vector、list、deque、set、map等,用来存放数据，从实现角度来看，STL容器是一种class template。

**算法：**各种常用的算法，如sort、find、copy、for\_each。从实现的角度来看，STL算法是一种function tempalte.

**迭代器：**扮演了容器与算法之间的胶合剂，共有五种类型，从实现角度来看，迭代器是一种将operator\* , operator-> , operator++,operator--等指针相关操作予以重载的class template. 所有STL容器都附带有自己专属的迭代器，只有容器的设计者才知道如何遍历自己的元素。原生指针(native pointer)也是一种迭代器。

**仿函数：**行为类似函数，可作为算法的某种策略。从实现角度来看，仿函数是一种重载了operator()的class 或者class template

**适配器：**一种用来修饰容器或者仿函数或迭代器接口的东西。

**空间配置器：**负责空间的配置与管理。从实现角度看，配置器是一个实现了动态空间配置、空间管理、空间释放的class tempalte.

STL六大组件的交互关系，容器通过空间配置器取得数据存储空间，算法通过迭代器存储容器中的内容，仿函数可以协助算法完成不同的策略的变化，适配器可以修饰仿函数。

![](test_assets/image_259.png)

## 容器

![](test_assets/image_260.png)

- 序列式容器就是容器元素在容器中的位置是由元素进入容器的时间和地点来决定。Vector容器、Deque容器、List容器、Stack容器、Queue容器。
- 关联式容器是指容器已经有了一定的规则，容器元素在容器中的位置由容器的规则来决定。Set/multiset容器 Map/multimap容器

### 使用选择

|  | vector | deque | list | set | multiset | map | multimap |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 典型内存结构 | 单端数组 | 双端数组 | 双向链表 | 二叉树 | 二叉树 | 二叉树 | 二叉树 |
| 可随机存取 | 是 | 是 | 否 | 否 | 否 | 对key而言：不是 | 否 |
| 元素搜寻速度 | 慢 | 慢 | 非常慢 | 快 | 快 | 对key而言：快 | 对key而言：快 |
| 元素安插移除 | 尾端 | 头尾两端 | 任何位置 | - | - | - | - |

- vector的使用场景：比如软件历史操作记录的存储，我们经常要查看历史记录，比如上一次的记录，上上次的记录，但却不会去删除记录，因为记录是事实的描述。
- deque的使用场景：比如排队购票系统，对排队者的存储可以采用deque，支持头端的快速移除，尾端的快速添加。如果采用vector，则头端移除时，会移动大量的数据，速度慢。

vector与deque的比较：

一：vector.at()比deque.at()效率高，比如vector.at(0)是固定的，deque的开始位置 却是不固定的。

二：如果有大量释放操作的话，vector花的时间更少，这跟二者的内部实现有关。

三：deque支持头部的快速插入与快速移除，这是deque的优点。

- list的使用场景：比如公交车乘客的存储，随时可能有乘客下车，支持频繁的不确实位置元素的移除插入。
- set的使用场景：比如对手机游戏的个人得分记录的存储，存储要求从高分到低分的顺序排列。
- map的使用场景：比如按ID号存储十万个用户，想要快速要通过ID查找对应的用户。二叉树的查找效率，这时就体现出来了。如果是vector容器，最坏的情况下可能要遍历完整个容器才能找到该用户。

### vector(尾出入，随机访问)

#### 原理与时间复杂度

![](test_assets/image_261.png)在堆中分配内存

动态扩展步骤

![](test_assets/image_262.png)实际内存会比容量大一些；动态扩容的过程中如果开辟到新内存，原迭代器失效

![](test_assets/image_263.png) ![](test_assets/image_264.png)

#### 构造

vector中可以是内置数据类型，还可以是自定义的数据类型，甚至是在嵌套一个vector，学习文件都有示例

```
函数 原型 :

。 vector<T> v5 // 采 用 模板 实现 类 实现 ， 默 认 构 造 函 数
© vector(v.begin(), v.end()); // 将 v[begin(), end() 区 间 中 的 元 素 拷贝 给 本 身 。
e vector(n, elem); // 构 造 函 数 将 n 个 elem 拷 贝 给 本 身 。

e vector(const vector avec); // 拷 贝 构造 函数 。
```

注意：

1.第二个函数中，后面的迭代器是不拷贝的，所以要拷贝全后面用end()即最后元素的下一个位置

```
vector<int> arr={l, 2, 3, 4,5};

vector<int> res (arr. begin(), arr. begin() + 4);
for (int i: res) cout << i;

cout << endl;

vector<int> res1 (arr. begin(), arr. end());

for (int i: resl) cout << i;

cout << endl;

return 0;
```

2.类中定义成员数组会产生歧义，要这么定义

```
// 易 错 :son(26,NULL) 产 生 歧 义 ， 编 译 器 不 知道 是 成 员 变量 还 是 成 员 函 数
vector<TrieNode*> son=vector<TrieNode*>(26,nullptr) ;
```

3.拷贝构造函数会根据size重新分配capacity，所以不是完全一致

```
v. resize (10) ;
cout << “4#:” << v.capacity() << endl;
cout << “K/): ” << v.size() << endl;

cout << “-------------- = ” << endl;
vector<int> v2(v) ;// 调 用 拷贝 构造 ， 容 量 缩小

cout 〈《《“ 容 量 :”《《 v2.capacity() << endl;
cout << "Kab: ” <« v2. size() << endl;
```

![](test_assets/image_269.png)

4.匿名对象容易认不出来，vector<int>(v)这是调用拷贝构造函数构造匿名对象，v是参数

5.构造二维数组不能用c的方式，得用构造函数嵌套

```
vector<vector<int>> res[10][1e];
res[2] [1]=1;

5 结果 wee

编译 出 错

37: Char 18: error: no viable overloaded "=

] {1 ]=1
```

```
36 vector<vector<int>> res(10,vector<int>(18));
37 res[@][1]=1;

试用 例 ”执行 结果 | ESTER

已 完成
```

#### 赋值

```
函数 原型 ;
© vector& operator=(const vector &vec); // 重 载 等 号 操作 符

© assign(beg, end); // 将 [beg, end) 区 间 中 的 数据 拷贝 赋值 给 本 身 。
. Sipe elem); // 将 n 个 elem 拷 贝 赋值 给 本 身 。
```

第二个函数中，后面的迭代器是不拷贝的，所以要拷贝全后面用end()即最后元素的下一个位置

```
vector<int> arr={l, 2, 3, 4,5};

vector<int> res (arr. begin(), arr. begin() + 4);
for (int i: res) cout << i;

cout << endl;

vector<int> res1 (arr. begin(), arr. end());

for (int i: resl) cout << i;

cout << endl;

return 0;
```

#### 容量和大小

```
通 数 原型 ;
© empty();
© capacity(J;
© size();

e resize(int num);

e resize(int num, elem);

/判断 容 器 是 否 为 空

// 容 器 的 容量

// 返 回 容器 中 元 素 的 个 数

// 重 新 指定 容器 的 长 度 为 num， 若 容器 变 长 ， 则 以 默认 值 填 充 新 位 置 。
// 如 果 容 器 变 短 ， 则 未 尾 超出 容器 长 度 的 元 素 被 删除 。

// 重 新 指定 容器 的 长 度 为 num， 若 容器 变 长 ， 则 以 elem 值 填充 新 位 置 。
// 如 果 容 嚣 变 短 ， 则 未 尾 超出 容器 长 度 的 元 素 被 删除
```

1.resize变小，capacity不变小

2.size()返回值是unsigned int，遍历容器int i=0开始没有问题，特殊情况int i=-1开始遍历，i<a.size();就会出问题，压根没有进入循环

3.如果是指针类型的数据，放入NULL后，empty()返回false;

#### 预留空间

![](test_assets/image_275.png)

reserve的len可以通过capacity查看，是新的总长度，而不是原长度加上len

区别于resize加空间会初始化，reserve后面新加的内存空间没有初始化，访问报错

如果知道总数据容量可以提前reverse，不用重新分配内存，大大提升效率

#### 数据存取访问

```
函数 原型:

。 at(int idx); 1/ 返回 索引 idx 所 指 的 数据
eToperator[]; 。 1/ 返 回 索 3lidx 所 指 的 数据

。 freontOi 1/ 返回 容器 中 第 一 个 数据 元 素
。 back(); // 返 回 容器 中 最 后 一 个 数据 元 素
```

at（）和【】的区别在于，at（index）越界会抛出out\_of\_range异常，而【】不抛异常直接出错

#### 插入和删除

```
函数 原型
© push_back(ele); // 尾 部 插入 元 素 ele
e pop_back(); // 捉 除 最 后 一 个 元 素
。 insert(const_iterator pos，ele);  。 // 迁 代 吴 指向 位 置 pos 插 入 元 素 ele
© insert(const_iterator pos, int count, ele); // 迁 代 吨 指向 位 置 pos 插 入 count 个 元 素 ele
© erase(const_iterator pos); BERET
。 erase(const_iterator start, const_iterator end); //HUBREH EE) startBlend ZialaI7CR
© clear{); // 副 除 容器 中 所 有 元 素
```

push\_back()有个相似函数emplace\_back()，区别在于：

```
class Person
{
public:
int mage;
string m_name;
了
stack<Person> s2;
// 对 于 这 种 自 定义 数据 类 型 还 能 进行 如 下 的 插入 操作 吗 ?
s2.push(18, "3zH8") ; ><
// 管 案 是 否定 的
// 若 想 用 push 进 行 插入 ， 只 能 先 将 这 个 对 象 构造 出 来 ， 再 将 这 个 对 象 插入
Person p1(18, "西施 ") ; 国
s2.push(p1);
//[ 或
s2.push(Person(19," 杨 玉环 ") ) // 传 入 时 构造 对 象
```

emplace是构造和插入元素，可以直接传入构造对象需要的元素，然后自己调用其构造函数

push能做的，emplace都能做。push是得传入得对象先得造好，再复制过去插入；而emplace则可以自己拿到构造对象所需得元素构造出来，直接插入即可。

emplace相比于push省去了复制这步，即使用emplace这种操作会更节省内存。

通过迭代器插入和删除，由于底层用一维数组实现，插入本质上是把插入位置后的所有元素后移一位再插入，删除本质上是把删除位置后的所有元素前移一位。

erase删除start和end之间实际上是包含start和end的（因为是迭代器）

erase删除后，后面空出来的空间会初始化为默认值，但不释放内存

clear是循环调用erase实现，所以也不释放内存，内存是在析构函数释放

条件删除用remove\_if配合erase

#### 遍历

```
int main

+

// 新 建 vector 容 器

vector<int> v:

// 往 容器 插入 数据
push_back(10) ;
vy. push_back (20) ;
vy. push_back (30) ;
vy. push_back (40) ;
vy. push_back (50) ;

// 第 一 种 遍历 ， 较 麻烦

// 新 建 选 代 器

vector<int>::iterator itBegin = vbegin (0) ;// 起 始 选 代 器 ， 指 向 容器 中 第 一 个 元 素
vector<int>::iterator itEnd = v.end() ;// 结 束 选 代 器 ， 指 向 容器 中 最 后 一 个 元 素 的 下 一 个 位 置
while (itBegin != itEnd)

{

cout << *itBegin << endl;
itBegin++;

}
// 第 二 种 遍历 ， 常 用

for (vector<int>::iterator it = v.begin(); it != v.end(); it++)

cout << *it << endl;

7/ 第 三 种 通 历 ， 需 要 include <algorithm>

for_each (y.begin()，v.end()，myPrint);// 第 三 个 参数 是 一 个 国 数 名 ， 是 把 vector 值 作为 参数 传 给 这 个 国 数
```

```
void myPrint (int val)
{

cout << val << endl;
```

#### 排序

![](test_assets/image_281.png)

![](test_assets/image_282.png)

#### 最值

max\_element（）与min\_element（）分别用来求最大元素和最小元素的位置。

\*max\_element（）与\*min\_element（）分别用来求最大元素和最小元素的值。

```
vector<int> n;

int maxPosition

int minPosition

max_element(n.begin(),n.end()) - n.begin();

min_element(n.begin(),n.end()) - n.begin();
```

```
int maxValue

int minValue

*max_element(n.begin(),n.end());

*min_element(n.begin(),n.end());
```

#### 互换容器

```
功能 措 述 :
+ 实现 两 个 容器 内 元 素 进行 互 换

函数 原型 :
。 swap(ee); // 梅 vec 与 本 身 的 元 素 互 换
```

实际除了互换，还有一个好处是可以消去resize后大量的冗余空间（实际上是调用拷贝构造来构造匿名对象时消去的）

```
// 实 际 上 好 处 是 收缩 内 存 空间
vector<int> v;
for Cnt i = 0; i < 100000; i++)
{

v. push_back (i) ;
}
cout 《(“v 的 容量 为 : “”《《 v.capacity() << endl;
cout 《(“v 的 大 小 为 :“ 《< v.size( << endl;
vy. resize (3);
cout 《(“resize 后 v 的 容量 为
cout 《《“resize 后 v 的 大 小 为
vector<int>(v). swap (v) ;人 /调用 拷贝 构造 函数 创建 了 匿名 对 象 ， 再 与 交换 ， 匿 名 对 象 下 一 行 系统 自动 释放
cout 《(“swap 后 v 的 容量 为 : ”《《 v.capacity() << endl;
cout 《(“swap 后 v 的 大 小 为 :“《《 v.size() << endl;

” < yv.capacity() << endl;
” « v.sizeQ) << endl;
```

### list（头尾出入，不随机访问）

#### 原理与时间复杂度

普通链表

![](test_assets/image_287.png)

STL链表

![](test_assets/image_288.png)在堆中分配内存

![](test_assets/image_289.png) ![](test_assets/image_290.png)

#### 迭代器

List迭代器必须有能力指向list的节点，并有能力进行正确的递增、递减、取值、成员存取操作。所谓”list正确的递增，递减、取值、成员取用”是指，递增时指向下一个节点，递减时指向上一个节点，取值时取的是节点的数据值，成员取用时取的是节点的成员。但不支持随机访问。***List有一个重要的性质，插入操作和删除操作都不会造成原有list迭代器的失效。***

***使用案例***

#define \_CRT\_SECURE\_NO\_WARNINGS

#include<iostream>

#include<list>

**usingnamespace** std**;**

int main**(){**

list**<**int**>** myList**;**

**for(**int i **=**0**;** i **<**10**;** i **++){**

myList**.**push\_back**(**i**);**

**}**

list**<**int**>::**\_Nodeptr node **=** myList**.**\_Myhead**->**\_Next**; //**\_Myhead在vs2015后变成了\_Myhead（）

**for(**int i **=**0**;** i **<** myList**.**\_Mysize **\***2**;**i**++){ //\*2是展示循环链表**

cout **<<**"Node:"**<<** node**->**\_Myval **<<** endl**; //**\_Myval在vs2015后变成了\_Myval（）

node **=** node**->**\_Next**;**

**if(**node **==** myList**.**\_Myhead**){**

node **=** node**->**\_Next**;**

**}**

**}**

system**(**"pause"**);**

**return** EXIT\_SUCCESS**;**

**}**

#### 构造

```
List<T> Ist; Vist 采 用 采用 模板 类 实现 对 象 的 默认 构造 形式 :
‘List (beg, end) ; // 构 造 函 数 桂 [beg, end) 区 间 中 的 元 素 拷 贝 给 本 身 。
List(n,elem); JADEN elem NEAR,

Lst(const list &lst); NIGER.
```

若使用数组指针，v.end是不拷贝的，所以注意要指向最后一个元素的下一块内存空间；若使用迭代器，那么end（）也拷贝

#### 赋值和交换

```
assign(beg, end); /将 [beg, end) Ris PAGES RBA,
/将 n 个 elem 拷 由 赋值 给 本 身 ,

List& operator-(const list alst); 。。 // 重 载 等 号 操作 符
‘swap(1st); /将 lst 与 本 身 的 元 素 互 换 。

assign(n, ele!
```

若使用数组指针，v.end是不拷贝的，所以注意要指向最后一个元素的下一块内存空间；若使用迭代器，那么end（）也拷贝

#### 插入和删除

```
push_backlelemjV/ 在 容器 尾部 加 入 一 个 元 素
popIback0// 开 除 容 吉 中 是 后 一 个 元 素
push_frontlelemj// 在 容器 开头 插入 一 个 元 素
pop_front(V/ 从 容器 开头 移 除 第 一 个 元 素
insert(pos,elemj/ 在 pos 位 置 播 elem 元 素 的 持 贝 ， 返 回 新 数据 的 位 置 .
insert(pos,nuelem)V/ 在 pos 位 置 插入 n 个 elem 数 据 ， 无 返回 值 .
insert(pos,beg,end)V/ 在 pos 位 置 播 入 [beg'end) 区 间 的 数据 ， 无 返回 值 .
clear(jy/ 移 除 容器 的 所 有 数据
eraselbeg.endj// 误 除 [begend) 区 间 的 数据 ， 返 回 下 一 个 数 据 的 位 置 。
eraselposj// 币 除 pos 位 置 的 数据 ， 返 回 下 一 个 数据 的 位 置 。
removefelem);// 而 除 容器 中 所 有 与 elem 值 匹配 的 元 和
```

位置使用迭代器，end（）也包含

还提供使用回调函数的自定义删除

```
bool myfunc (int val)

{

return val > 300,
```

```
// 要 删除 大 于 300 的 数据

mylist.remove_if(myfunc) ;
```

#### 大小操作

```
// 返 回 容器 中 元 素 的 个 数

/1/ 淹 断 窜 器 是 否 为 空
1/ 重新 指定 容器 的 长 度 为 num， 若 窜 贸 变 长 ， 则 以 靳 认 值 填充 新 位 天

(SORES, UAHA COTTER,
(ESSERE Anum, BSBTK, Melemaarses.
1/ 如果 容器 变 短 ， 则 未 尾 超出 容器 长 度 的 元 素 被 删除 -

size();

pty()

resize(nun);

resize(nun, elen);
```

size()返回值是unsigned int，遍历容器int i=0开始没有问题，特殊情况int i=-1开始遍历，i<a.size();就会出问题，压根没有进入循环

#### 数据存取

```
front(); /返回 第 一
back(); /返回 最 后 一 个 元 素 。
```

#### 反转和排序

```
reverse(); | // 反 转 链表
sort(); // 链 表 排 序
```

注意sort与之前不同,不是<algorithm>的函数而是成员函数,因此是list1.sort();

![](test_assets/image_299.png)

### deque（头尾出入，随机访问）

#### 原理和时间复杂度

![](test_assets/image_300.png)

Deque容器和vector容器最大的差异，一在于deque允许使用常数项时间对头端进行元素的插入和删除操作。二在于deque没有容量的概念，因为它是动态的以分段连续空间组合而成，随时可以增加一段新的空间并链接起来，换句话说，像vector那样，”旧空间不足而重新配置一块更大空间，然后复制元素，再释放旧空间”这样的事情在deque身上是不会发生的。也因此，deque没有必须要提供所谓的空间保留(reserve)功能.

虽然deque容器也提供了Random Access Iterator,但是它的迭代器并不是普通的指针，其复杂度和vector不是一个量级，这当然影响各个运算的层面。因此，除非有必要，我们应该尽可能的使用vector，而不是deque。对deque进行的排序操作，为了最高效率，可将deque先完整的复制到一个vector中，对vector容器进行排序，再复制回deque.

![](test_assets/image_301.png)

Deque是由一段一段的定量的连续空间构成。一旦有必要在deque前端或者尾端增加新的空间，便配置一段连续定量的空间，串接在deque的头端或者尾端。Deque最大的工作就是维护这些分段连续的内存空间的整体性的假象，并提供随机存取的接口，避开了重新配置空间，复制，释放的轮回，代价就是复杂的迭代器架构。既然deque是分段连续内存空间，那么就必须有中央控制，维持整体连续的假象，数据结构的设计及迭代器的前进后退操作颇为繁琐。Deque代码的实现远比vector或list都多得多。

![](test_assets/image_302.png)

#### 构造

```
BURY:

dequect> deqT:
deque(beg, end);

deque(n, elen)

deque(const deque &deq);

1// 蒜 认 构造 形式

// 构 造 函数 将 [beg, end) 区 间 中 的 元 素 拷贝 给 本 身 。
/构造 函数 将 n 个 elem 拷 贝 给 本 身 .

1// 持 贝 构造 函数
```

若使用数组指针，end是不拷贝的，所以注意要指向最后一个元素的下一块内存空间；若使用迭代器，那么end（）也拷贝

#### 赋值

```
函数 原型

© dequeaToperator (const deque &deq); NERS

。 assign(beg, end); /将 [beg, end) Ris PAVE ESAS,
© assign(n, elem); // 将 n 个 elem 拷 由 赋值 给 本 身 。
```

#### 交换

d1.swap(d2) 交换d1和d2元素

#### 大小操作

```
© deque-empty();
© deque.size();

© deque.rdsize(num);

© deque.resize(num, elem);

UNTER SDS

SEPT RAINS
/SSESBOKE Au SSSEK, WU OE,
(SOP RSSS, WARE HERK SHITE RR,
(BREAKS Anum BSR, Miele maar Ts.
SOP RISS, DREHER SATE RRR,
```

注意没有容量，因为可以任意拓展，所以没有capacity函数

size()返回值是unsigned int，遍历容器int i=0开始没有问题，特殊情况int i=-1开始遍历，i<a.size();就会出问题，压根没有进入循环

#### 插入和删除

```
函数 原型 :
两 请 洗 入 操作 :

push_back(elen) 3
push front (elem);
op_back();

op_front();

SEE:

insert(posi ale)
insert (pos,n,eles);
{insert (pos, beg,end);
etear()s
erase(beg,end);

erase(pos);

/在 容器 尾部 添加 一 个 数据
/在 容器 头 部 插入 一 个 数据
7/ 抽 除 容器 最 后 一 个 数据

// 副 除 容器 第 一 个 数据

/在 pos 位 置 插入 一 个 elem 元 素 的 拷贝 ， 返 回 新 数据 的 位 秆 。
1/ 在 pos 位 秆 插入 n 个 eler 数 据 ， 无 返回 值 。

V/ 在 pos 位 置 酝 和 [beg,end) 区 间 的 赦 据 ， 无 返回 值 ,
/清空 容 占 的 所 有 数据

/ 郧 除 [beg,end) 区 间 的 数据 ， 返 回 下 一 个 数据 的 位 置 。

// 副 除 pos 位 置 的 数据 ， 返 回 下 一 个 数据 的 位 置 。
```

由于使用迭代器pos插入，end（）也插入和删除

pos通过迭代器来指定位置，如下面删除第二个元素

```
//JWPR AE ES RELA IAT Ves

deque<int>: :iterator it=d2. begin() ;
itt;

d2. erase (it) ;

printDeque (d2) ;
```

#### 数据存取

```
函数 原型 :

。 at(int idx); /返回 素 引 idx 所 指 的 数据

© operator[]; 。 /返回 索引 idx 所 指 的 数据
front(); 7/ 返回 容器 中 第 一 个 数据 元 素
© back0; I EERE PREECE
```

at（）和【】的区别在于，at（index）越界会抛出out\_of\_range异常，而【】不抛异常直接出错

#### 排序

![](test_assets/image_309.png)

![](test_assets/image_310.png)

### stack（top出入，无法遍历）

![](test_assets/image_311.png)

#### 构造

```
构造 函数 :
© stack<T> stk; AStack 采 用 模板 类 实现 ， stack 对 象 的 球 认 构造 形式
stack(con stack &stk); DEB
```

#### 赋值

```
© stack& operator=(const stack &stk); /BRSSRES
```

#### 数据存取

```
© push(elem); —— //)PGIRA DOC
© pop). USSSTRER BATE

* tops
```

s.top()在栈空时报错，所以常需要搭配!s.empty()使用

top()返回const类型，不能修改

#### 大小操作

```
empty();, PUTER ENE
size(); /返回 栈 的 大 小
```

size()返回值是unsigned int，遍历容器int i=0开始没有问题，特殊情况int i=-1开始遍历，i<a.size();就会出问题，压根没有进入循环

如果是指针类型的数据，放入NULL后，empty()返回false;

### queue（头出尾入，无法遍历）

![](test_assets/image_316.png)

#### 构造

```
queue<T> que; Viqueue 采 用 模板 类 实现 ，queue 对 条 的 默认 构造 形式
queue(const queue &que); (DEE
```

#### 赋值

```
queue& operator=(const queue &que); // 重 载 等 号 操作 符
```

#### 数据存取

```
push(elen) // 往 队 必 添 加 元 素
pop(); /从 队 头 移 除 第 一 个 元 素
backk /返回 最 后 一 个 元 素

front(); /返回 第 一 个 元 素
```

很容易与栈混淆，q.top();是不存在的

插入用push()和emplace()，很容易写成push\_back()和emplace\_back()注意

#### 大小操作

```
empty(); TTR REAS
size()s /返回 栈 的 大 小
```

size()返回值是unsigned int，遍历容器int i=0开始没有问题，特殊情况int i=-1开始遍历，i<a.size();就会出问题，压根没有进入循环

如果是指针类型的数据，放入NULL后，empty()返回false;

### priority\_queue（C++的堆）

在优先队列中，优先级高的元素先出队列，并非按照先进先出的要求，优先队列的本质是组织容器元素的一种特别方式（堆是满足该组织方式的数据结构），具有队列的所有操作特性

O(log n) 的效率查找一个队列中的最大值或者最小值

头文件 <queue>

#### 构造

priority\_queue<Type, Container, Functional>

其中Type 为数据类型， Container 为保存数据的容器（易错，在第二位不是第一位），Functional 为元素比较方式。

1.在STL中，默认情况下（不加后面两个参数）是以vector为容器，以 less<数据类型>为比较方式，此时后面元素比前面小，优先队列默认是一个大顶堆

2.最小堆不能省略参数。STL里面定义了一个仿函数 greater<数据类型>（后面元素比前面大），对于基本类型可以用这个仿函数声明小顶堆

大顶堆（降序）

//构造一个空的优先队列（此优先队列默认为大顶堆）

priority\_queue<int> big\_heap;

//另一种构建大顶堆的方法

priority\_queue<int,vector<int>,less<int> > big\_heap2;

小顶堆（升序）

//构造一个空的优先队列,此优先队列是一个小顶堆

priority\_queue<int,vector<int>,greater<int> > small\_heap;

需要注意的是，如果使用less和greater，需要头文件：#include <functional>

#### 自定义数据类型（pair，tuple）的构造

##### 默认第一个降序

如priority\_queue<tuple<double, int, int>> q;

将自动根据double来降序排列。——经验来自力扣1792题

##### 自己写排序函数

1.类内写静态成员函数

static bool cmp(pair<int,int> &a,pair<int,int> &b)

{

return a.second>b.second;

}

priority\_queue<pair<int,int>,vector<pair<int,int>>,decltype(&cmp)> heap(cmp);

不带static报错![](test_assets/image_321.png)；容器中是作为类型所以要decltype()；decltype(&cmp)或者decltype(cmp)\*是static (\*)(pair<int,int>,pair<int,int>)函数指针类型，decltype(cmp)是static (pair<int,int>,pair<int,int>)函数类型不能赋值也不能调用；heap(cmp)不带(cmp)报错![](test_assets/image_322.png)内存泄漏

2.类外写仿函数

class cmp

{

public:

bool operator()(pair<int,int> &a,pair<int,int> &b)

{

return a.second>b.second;

}

};

class Solution {

public:

priority\_queue<pair<int,int>,vector<pair<int,int>>,cmp> heap;

};

这里有个易错点：在函数如sort中自定义规则是匿名对象作为参数传递要带()，在容器<>中自定义规则是作为类型不带（）

#### 成员函数

函数 描述

push() 它将新元素插入优先队列。

pop() 它将优先级最高的元素从队列中删除。

top() 此函数用于寻址优先队列的最顶层元素。return值为const，不能修改

size() 返回优先队列的大小。

empty() 它验证队列是否为空。基于验证，它返回队列的状态。

swap() 它将优先队列的元素与具有相同类型和大小的另一个队列交换。

emplace() 它在优先队列的顶部插入一个新元素

示例：

```
#include <iostream>

#include<queue>

using namespace std;

int main()

{

priority queue<int> p; // 变量 声明 -
P.push(10); // 插入 10 到 队列 ，tol
p-push(39); // 插入 30 到 队列 ，tol
p.push(29); // 插入 20 到 队列 ，top=29
cout<<" 可 用 元 素 的 数量 到 'p，: "<<p.size()<<endti
while(!p.empty())

9

cout << p.top() <<endl;
P-pop();

了

return 0;

+
```

![](test_assets/image_324.png)

```
如 果 要 按照 最 小 堆 优先 级

priority_queue<Type, Container, Functional>

写 入 程序 中 就 是 priority_queue<int vector<int>, greater<int> > q;

1 | #include<bits/stdc++.h>

2

using namespace std;

3) int main(){

ov oo

10
11
12
13
14
15
16
17

priority_queue<int，vector<int>，greater<int> > q;
for( int i= 0; ix 10; +ti)

{
int temp;
cin>>temp;
q-push (temp) ;
+

while( !q.empty() {
cout << q.top() << endl;
q-pop();

}

getchar();

return 0;
```

#### vector做为堆

注意：堆不是容器，而是组织容器元素的一种特别方式。

```
#include-
#include<v
#include-
using namespace std;

int main() {
vector<int>nums{ 2, 5, 10, 3, 6, 8, 12, 7, 9, 1};
make_heap(nums.begin(), nums.end()) ;
for (int num : nums)

10 cout << num <<" ";
11 return 0;

12 |}

13
```

```
vector<int>nums{ 2
nums )
nums (
for (int num : nums)
cout << num

OuaWNR

1 vector<int>nums{ 2, 5 , 7, Q 1 ha
2 nums

3 nums

4

5 for (int num : nums)

6 cout << num

7 cout endl;

9 nums ), nums )
10 for (int num : nums)

11 cout num

12

14
```

```
堆 的 应 用

题目 转自 LeetCode

题目 描述

给 你 一 个 整数 数组 piles ， 数 组 下 标 从 0 开始 ， 其 中 piles[i] 表示 第 i 堆 石子 中 的 石子 数量 。 另 给 你 一 个 整数 k ， 请 你 执行 下 述 操作 恰好
k 次

注意 : 你 可 以 对 局 一 雄 石 子 多 次 执行 此 操作 。
返回 执行 k 次 操作 后 ， 剩 下 石子 的 最 小 总 数 。
floor(x) ANF RSF x 的 最 太 整 数 。 (BD, Rx 向 下 取 整 ) 。
代码
class Solution
public

int minStonesum 0 piles, int k

make_heap (pi i piles end
for (int i

pop_heap(piles.begin(), piles.end
piles.back piles.back
push_heap(piles.begin(), piles.end

return accumulate(piles.begin(), pile
```

### string

#### 构造

```
构造 函数 原型 :
© string(); /创建 一 个 空 的 字符 串 例如 : string str;
string(const char* s); // 使 用 字符 串 s 初 始 化
© string(const string& str); /使 用 一 个 string 对 象 初始 化 另 一 个 String 对象
© string(int n, char c); /使 用 n 个 字符 c 初 始 化
```

使用char\*构造时，遇到’\0’停止，如果字符数组的末尾不是’\0’，用下面的构造来限定到哪里停止。

string(const char\* s, size\_t count); //

#### 赋值

```
赋值 的 函数 原型 :

string&
string&
string&
string&
string&
string&

string&

operator=(const char* s);
operator=(const string &s);
operator=(char c);
assign(const char *s);
assign(const char *s, int n);
assign(const string &s);

assign(int n, char c);

/char* 类 型 字符 串 赋值 给 当前 的 字符 串
// 把 字符 串 s 赋 给 当前 的 字符 串

// 字 符 赋值 给 当前 的 字符 串

// 把 字符 串 s 赋 给 当前 的 字符 串

// 把 字符 串 s 的 前 n 个 字符 赋 给 当前 的 字符 串
// 把 字符 串 s 赋 给 当前 字符 串

// 用 n 个 字符 < 赋 给 当前 字符 串
```

#### 内存分配机制

string维护一个char\*指针指向存放字符串的地址，当字符串长度在16以内时分配在栈区，长度在16以上分配到堆区，动态分配内存的过程中char\*地址将改变，所以容易导致野指针、野引用

```
string s = “abcde”;
char &a = s[2];
char &b = s[3];

a=’l’;

b= 2;

cout << “a:” << a << endl;

cout << “b:” << b << endl;

cout << s << endl;

cout 《《“ 字 符 串 的 原 空间 地 址 :”《《 (int*)s.c_str() << endl;

= “fdasfdasfdsafdasherewrkewhsaferew’ ;

cout 〈《(“ 字 符 串 的 空间 地 址 :”《《 eGntk)sseostr() << endl;

ane: 是 被 释放 的 s[2] 空 间 的 别名 ， 如 果 操作 非法 的 空间 ， 会 出 错
//a =’3';
```

#### 访问单个字符

```
© char& operator[](int n);  /A@it [tS
e char& at(int n); // 通 过 at 方法 获取 字符
```

```
// 口 和 at 的 区 别 : 口 访问 元 素 时 ， 越 界 不 抛 异 常 ， 直 接 挂 ，at 越 界 ， 会 抛 异常
try
{
//cout << s[100] << endl;
cout << s.at(100) << endl;
}

catch (out_of_range &ex)

cout << ex. wad endl;
cout << “atm F endl;
```

#### 判断字符个数

str.size()和str.length()返回的都是字符串中有多少个字符，不算\0

size()返回值是unsigned int，遍历容器int i=0开始没有问题，特殊情况int i=-1开始遍历，i<a.size();就会出问题，压根没有进入循环

C语言中是strlen（char\*），同样返回字符数不算\0

#### 拼接

```
tk:
«SOMES

函数 原型 :

string®
string
ringa
Stringg
srtnga
ES

strings

operators=(const char? ste)
operatoree(const char);
operatore-(const string str);
sppend(const char 5)
append(const char *s, Int ns

‘append(const string 8);

BREN
ERE
BRL BIER
1/ 反 字符 种 5 连接 到 当前 字符 率 结 尾

OPERA ALES PGE

MBoperator+=(const string& str)

append(const string &s, int pos, int n); /SPRFERSHS posFRAMIN-TPAEREIS SEE
```

注意有“+”拼接，但没有“-”删除

#### 查找替换

```
。 者 找 : SES
。 BR: 在 指定 的 位 置 某 换 字符 串
函数 原型 ;

int find(const string& str, int pos = @) const;
int find(const char* s, int pos = @) const;

int find(const char* s, int pos, int n) const;

int find(const char c, int pos = @) const;

int rfind(const string& str, int pos = npos) const;
int rfind(const char* s, int pos = npos) const;
int rfind(const char* s, int pos, int n) const;
int rfind(const char c, int pos = @) const;
string& replace(int pos, int n, const string& str);

string& replace(int pos, int n,const char* s);

// 查 找 str 第 一 次 出 现 位 置 ,从 pos 开 始 查找
/查找 s 第 一 次 出 现 位 置 ,从 pos 开 始 查找

// 从 pos 位 置 查找 s 的 前 n 个 字符 第 一 次 位 置
// 查 找 字符 < 第 一 次 出 现 位 置

// 查 找 str 最 后 一 次 位 置 ,从 pos 开 始 查找

// 查 找 s 最 后 一 次 出 现 位 置 , 从 pos 开 始 查找
// 从 pos 坦 找 s 的 前 n 个 字符 最 后 次 位 上 ””
// 查 找 字符 < 最 后 一 次 出 现 位 置

// 营 换 从 pos 开 始 n 个 字符 为 字符 串 str

// 营 换 从 pos 开 始 的 n 个 字符 为 字符 串 s
```

注意表格错误，返回值不是int，而是size\_t

找不到时返回的看起来是-1，但用-1或std::string::npos比较debug模式会出错（用返回迭代器的find（）也出错。。）

rfind是从pos位置开始从右往左找第一个的意思

注意所有的pos等位置都是指下标，pos默认值npos指的是结尾

注意替换，第二个参数n不是结束下标，而是从pos开始共去掉n个字符，再在它们的位置插入str

#### 比较

```
功能 描述 :

。 字符 串 之 间 的 比较

比较 方式 :

。 字符 串 比 较 是 按 字符 的 ASCII 码 进行 对 比
= 返回 0

> 返回 1

< 返回 -1

冰 数 原型 ;
© int compare(const string &s) const; // 与 字符 串 s 比 较

© int compare(const char *s) const; // 与 字符 串 st 比 较
```

一般中文的话，都是看==0就相等，！=0不相等

#### 插入和删除

```
函数 原型:
ne insert(int pos, const char* =); ean
« (string insert(int pos, const stringt strji //E/\ S508
© string& insert(int pos, int n, charlc); SECTS
© string& erase(int pos, int n - npos); V/ 囊 除 从 Pos 开 始 的 n 个 字符
```

从pos下标开始插入，原pos处的字符后移

n默认值npos指的是默认删除到结尾

#### 取子串

```
ABR
© string substr(int pos = @, int n = npos) const;  // 返 回 由 pos 开 始 的 n 个 字符 组 成 的 字符 串
```

n默认值npos指的是默认截取到结尾

#### string与其他类型转换

char\*转int：

int num=atoi(“123456”.c\_str()); 其中atoi()的作用是char\*转int，c\_str()的作用是string转char\*

string转int等数字类型：

int num=stoi(“123456”); 输入直接是string不需要转char\*，“123456abcd”也是返回123456

转long用stol，转float用stof，转double用stod

int等数字类型转string：

string str=to\_string(int val); 易错，多次写成toString

显然官方有很多重载

判断string是否为一个数：

bool isNumber(string);

判断string是不是一个数（能识别负数），但是头文件在cppreference中找不到，应该不是标准库函数不要用

string转char\*

主要有三种方法可以将str转换为char\*类型，分别是：data(); c\_str(); copy();

**1.data()**方法，如：

string str = "hello";

const char\* p = str.data();//加const 或者用char \* p=(char\*)str.data();的形式

同时有一点需要说明，这里在devc++中编译需要添加const，否则会报错invalid conversion from const char\* to char \*，这里可以再前面加上const或者在等号后面给强制转化成char\*的类型。

下面解释下该问题，const char\*是不能直接赋值到char\*的,这样编译都不能通过,理由:假如可以的话,那么通过char\*就可以修改const char指向的内容了,这是不允许的。所以char\*要另外开辟新的空间，即上面的形式。

**2.c\_str()**方法，如：

string str=“world”;

const char \*p = str.c\_str();//同上，要加const或者等号右边用char\*

**3.copy()**方法，如：

string str="hmmm";

char p[50];

str.copy(p, 5, 0);//这里5代表复制几个字符，0代表复制的位置，

\*(p+5)=‘\0’;//注意手动加结束符！！！

#### stringstream流

头文件<sstream>

用来format（比如从字符串中提取有用部分，或者利用部分数据合成一个字符串），用 string 对象来代替sprintf 或sscanf的字符数组方式，避免了缓冲区溢出的危险；而且，因为传入参数和目标对象的类型会被自动推导出来，所以不存在错误的格式化符号的问题。

sstream ss(string)，利用string初始化sstream对象

ss.str()，stringstream转string

ss.str(“”)，相当于清空

##### 常用来提取

合成和数据转换，用“+”和to\_string()等更好，只有提取数据时因为直接用string比sscanf的char[]方便

用法如图：

```
stringstream ss(exp.substr(i +
string b;
while (getline(ss, b, ',')) {
```

1.利用字符串构造流对象ss

2.利用getline自定义分隔符，来得到所需的string片段

3.图中ss是“aaaa,,bbbb,cccc”，则while中的b循环四次，分别是”aaaa”、””和”bbbb”和”cccc”(中间的空不会被丢弃)

图中ss是“aaaa,bbbb,cccc,”，则while中的b循环三次，分别是”aaaa”、”bbbb”和”cccc”(末尾的,后没有了，不会有新字符串)

这里特别容易出错，比如ip地址.0.0.0.0.首尾两个点非法，但分隔没看出来，需要单独处理

##### 不常用功能

1.用于转换数据类型相当于上一节的成员函数，但效率更低，建议用to\_string()或snprintf()

非要用的话注意多次不同类型数据转换时要调用一下clear()

```
1| #include <sstream>

2 | #include <iostream>

3

4 using namespace std;

5

6 | int main()

74

8 stringstream sstream;
9 int first, second;
10

11

12 sstream << "456";

13

14 sstream >> first;

15 cout << first << endl;
16

17

18 sstream.clear();

19

20

21 sstream << true;

22

23 sstream >> second;

24 cout << second << endl;
25

26 return 0;

27 +

编译 并 执行 上 述 代码 ， 结 果 如 下

ES: 在 本 示例 涉及 的 场景 下 (多 次 数据 类 型 转换 ) ， 必 须 使 用 clear() 方法 清空 stringstream， 不 使 用 clear() 方法 或 使 用 str(") 方法 ，
都 不 能 得 到 数据 类 型 转换 的 正确 结果 。
```

2.用于拼接相当于+或append()，而且效率更低，不建议用

```
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

int main()
{

stringstream sstream;

// BEPEBMA sstream 内

sstream << "first" << " " << “string,";

sstream << " second string";

cout << "strResult is: " << sstream.str() << endl;

// #2 sstream
sstream.str("");

sstream << “third string"
cout << “After clear, strResult is: " << sstream.str() << endl;

return 0;
```

#### 更多STL算法

见算法部分，如反转、统计、交换等也常用

### set/multiset（自动排序）

#### 原理与时间复杂度

![](test_assets/image_342.png) 不允许有重复元素，重复插入不报错但没有任何效果；元素插入后不允许修改（能删除）

![](test_assets/image_343.png)

set和multiset都只需要#include<set>

#### 迭代器与遍历

我们可以通过set的迭代器改变set元素的值吗？不行，因为set元素值就是其键值，关系到set元素的排序规则。如果任意改变set元素值，会严重破坏set组织。换句话说，set的iterator是一种const\_iterator.

由于都是结点组成，set拥有和list某些相同的性质，当对容器中的元素进行插入操作或者删除操作的时候，操作之前所有的迭代器，在操作完成之后依然有效，被删除的那个元素的迭代器必然是一个例外。

所以遍历中不能用&

```
set<int> se={1,2,3};

for(int& i:se) cout<<i;
```

```
19: Char 18: error: binding reference of type ’int’ to value of type ’const int’ drops ’const’ qualifier
for (int& i:se) cout<<i;
```

#### 构造和赋值

```
构造 :

© setcT> st; ERASER:

© set(const set ast); /拷贝 构造 函数

me:

// 重 载 等 号 操作 符

© seth operator=(const set &st);
```

补充

set<int> s{ nums1.begin(), nums1.end() };//使用数组构造

#### 大小和交换

```
size(); /返回 容器 中 元 素 的 数目
eopty():) PINTER
suap(sth SRNR ERE
```

size()返回值是unsigned int，遍历容器int i=0开始没有问题，特殊情况int i=-1开始遍历，i<a.size();就会出问题，压根没有进入循环

#### 插入和删除

```
insert (elem); /在 容器 中 插入 元 素 .

aear0; 1/ 清除 所 有 元 素

erase(pes); / 届 除 pos 渤 代 器 所 指 的 元 素 ， 返 回 下 一 个 元 素 的 迁 代 咕 。
erase(beg, end); 1/ 除 区 间 [beg.end) 的 所 有 元 素 ， 返 回 下 一 个 元 率 的 渤 代 器 。
erase(elen); 。。。// 囊 除 容器 中 什 为 elemn 的 元 素 .
```

insert返回值是pair，包含插入的位置（迭代器）和是否插入成功（bool）。自行看源码

#### 查找和统计

```
Find(key); // 章 找 key 是 否 存在 , 若 存在 ， 返 回 该 特 的 元 素 的 迁 代 号 。 若 不 存在 ， 返 回 setend()-
‘count (key) ; Uc keyBO TERA
```

对于set，统计个数的返回值值是0或1

```
lower_bound (keyElem) ;// 返 回 第 一 个 key>=keyElem 元 素 的 迭代 器 。
Upper_bound (keyElem) ;// 返 回 第 一 个 key>keyElem 元 素 的 迭代 器 。
```

```
equal_range (keyElem) ;// 返 回 容器 中 key 与 keyElem 相 等 的 上 下 限 的 两 个 迭代 器 ，
```

实际上就是上面两个函数的返回值组合在一起

```
pair<set<int>::iterator, set<int>::iterator> ret=s. equal_range (2) ;
cout << *(ret. first) << endl;
cout << *(ret. second) << endl:
```

#### 排序

易错：仿函数在函数入sort（）中使用带()，在容器<>中使用不带

![](test_assets/image_353.png)

set存放系统数据类型时：

```
修改 排序 规则 一 一 从 大 到 小

class MyCompare

{
public:
bool operator () (int vi, int_v2) const//iX= 27 LE const
{
return v1 > v2;
}
}

void test01()

{
创建 set 时 修改 规则

set<int, MyCompare> s1;

sl. insert (10) ;
sl. insert (40) ;
sl. insert (20) ;
sl. insert (50) ;
sl. insert (30) ;

for (set<int>::iterator it = sl.begin(); it != sl.end(Q); it++)

{

cout << #it <<” 7;
了
cout << endl;

50 40 30 20 10
```

set存放自定义数据类型时：

```
class Person

public:
Person(string name, int age)

// 提 供 排序 规则
class MyCompare
{

public:

' bool operator () (const Person& pl, const Person& p2) const// 订 尾 这 里 要 加 上 const 变 为 党
```

```
void test01()

{

自 定义 的 数据 类 型 ， 创 建 set 时 必须 提供 排序 规则
set<Person, MyCompare> s1;
Person pl (“XI #”, 24) ;
Person p2(“43)", 28);
Person p3(“3K K”, 25);
Person p4(" 赵 云 "，21) ;
sl. insert (pl)
sl. insert (p2) ;
sl. insert (p3) ;
sl. insert (p4) ;

for (set<Person>::iterator it = sl.begin(); it != sl.end(); it++)

{

cout << “HEB: “<< itm Name 《(“/t 年 龄 : “<<it->m_Age << endl;
```

### unordered\_set(哈希表)/unordered\_multiset

C11后能有，都只需要#include < unordered\_set >

![](test_assets/image_357.png)

#### 构造和赋值

```
构造 :

© setcT> st; ERASER:

© set(const set ast); /拷贝 构造 函数

me:

// 重 载 等 号 操作 符

© seth operator=(const set &st);
```

改unordered\_set即可

补充：

unordered\_set<int> us{ nums1.begin(), nums1.end() };//使用数组构造

unordered\_set<string> seen={"0000"};//根数组一样初始化

#### 大小和交换

```
size(); /返回 容器 中 元 素 的 数目
eopty():) PINTER
suap(sth SRNR ERE
```

size()返回值是unsigned int，遍历容器int i=0开始没有问题，特殊情况int i=-1开始遍历，i<a.size();就会出问题，压根没有进入循环

#### 插入和删除

```
insert (elem); /在 容器 中 插入 元 素 .

aear0; 1/ 清除 所 有 元 素

erase(pes); / 届 除 pos 渤 代 器 所 指 的 元 素 ， 返 回 下 一 个 元 素 的 迁 代 咕 。
erase(beg, end); 1/ 除 区 间 [beg.end) 的 所 有 元 素 ， 返 回 下 一 个 元 率 的 渤 代 器 。
erase(elen); 。。。// 囊 除 容器 中 什 为 elemn 的 元 素 .
```

insert返回值是pair，包含插入的位置（迭代器）和是否插入成功（bool）。自行看源码

insert(左值)可以改为insert(move(左值))，相当于insert(右值)，效率提升明显

![](test_assets/image_361.png)

除了insert()还有emplace()，区别同其他容器

#### 访问与遍历

unordered\_map有umap[key]访问对应value的方式，但unordered\_set没有uset[key]的用法（显然用count即可）

要在不知道key的情况下看哈希表有哪些值，可以使用迭代器

全部遍历使用for（不能使用&）

```
for (auto Gmt i: uset)

cout << i < endl
```

```
for (auto std:veonditio.ersterd::tye it-uset.begin() ;it!-uset.end() )it++)
{

}

cout << Hit < endl
```

```
OuaWNR

第 一 种 遍历

unordered_map-

p : count) {
front = p.first;
end = p.second

unordered_map<int, int> count
m.begin() ;it!=m.end() ;it++

front = it->first;
end = it->second;
```

使用&会报错

```
unordered_set<int> s;
```

```
for(int& i:s) m[i]++.
```

```
Char 18: error: binding reference of type ’int’ to value of type ’const int’ drops ’const’ qualifier
for (int& i:s) mli]++;
```

#### 查找和统计

```
Find(key); // 章 找 key 是 否 存在 , 若 存在 ， 返 回 该 特 的 元 素 的 迁 代 号 。 若 不 存在 ， 返 回 setend()-
‘count (key) ; Uc keyBO TERA
```

对于unordered\_set，count统计个数的返回值是0或1

#### key为pair报错

pair 类型和自定义的 class 类型是没有提供默认哈希函数的，必须自己指定一个哈希函数，所以直接构建 pair 类型的 unordered\_set 如 unordered\_set<pair<int, int>> uset 会出现问题（不会在声明时报错，而是在 insert 等操作时）。

这是unordered\_set的类模板信息，可见第二个指定哈希函数

```
1 | template < class Key, | BERTAETRILE
2 class Hash = hash<Key>, // META FAME DAIS

3 class Pred = equal_to<Key>,  // HFS 17H SASS GAIBAT
4
5

class Alloc = allocator<Key>  ///8= ORS RIL!
> class unordered_set;
```

这里提供一个pair<int,int>的最简单哈希函数（两个int按位异或）

在hashset所在类外定义，使用struct仿函数：

struct SimplePairHash

{

size\_t operator()(const pair<int, int>& p) const

{

return p.first ^ p.second;

}

};

unordered\_set<pair<int, int>, SimplePairHash> set;

上面的函数并不好写，所以一般不使用。由于pair作为key一般是保存坐标，防止重复遍历，官解中常用以下替代方案：

1.创建一个二维数组1:1记录

2.后续不会再用到，直接在原数组进行修改

3.直接在原数组修改，后续再用到前复原

### pair

三元及以上没必要学tuple，直接用struct即可

#### 访问两个元素

对组(pair)将一对值组合成一个值，这一对值可以具有不同的数据类型，两个值可以分别用pair的两个公有属性first和second访问（不是first()和second()，犯过这个错误）

类模板：template <class T1, class T2> struct pair.

如何创建对组?

|  |
| --- |
| //第一种方法创建一个对组  pair<string, int> pair1(string("name"), 20);  cout << pair1.first << endl; //访问pair第一个值  cout << pair1.second << endl;//访问pair第二个值  //第二种  //这里是make\_pair而不是makepair，犯过这个错误  pair<string, int> pair2 = make\_pair("name", 30);  cout << pair2.first << endl;  cout << pair2.second << endl;  //pair=赋值  pair<string, int> pair3 = pair2;  cout << pair3.first << endl;  cout << pair3.second << endl; |

#### 使用技巧

1.可以用auto[first, second]来接pair（C++17标准，需要在vs项目属性中修改语言标准为C17）

for (auto& [first, second] : pair组成的数据结构)

{

//代码

}

其中如果有不需要用到的元素，可以使用“\_”替代，是合法的变量名，但不赋予实际的值

```
for (auto &&[_, minutes] : activeMinutes)
```

2. emplace和push对pair有区别。emplace是构造和插入元素，可以直接传入构造对象需要的元素，然后自己调用其构造函数

```
vector<pair<int, int>> num.

num. push back (1, 2)
num, emplace back (Vals 1, isis 2)
```

```
vector<pair<int, int>> num,
tun. push-back (ats ake paix (eM {, Enaa 2))
‘num, enplace back (Tale SEE
```

### tuple

tuple即元组，可以理解为pair的扩展，可以用来将不同类型的元素存放在一起，常用于函数的多返回值。

#### 构造

```
tuple<int,double,string> t3 = {1, 2.0, "3"};
```

#### 访问和赋值

```
可 以 使 用 get< 和 常量 表达 式 >(tuple_name) 来 访问 或 修改 tuple 的 元 素 (返回 引用 )

1 get<@>(t3) = 4;
2 cout << get<1>(t3) << endl;
```

用std::tie来解包tuple和pair

```
tee
std::tie 会 将 变量 的 引用 整合 成 一 个 tuple， 从 而 实现 批量 赋值 。

1 int i; double d; string s;

2 tie(i, d, s) = t3;

3

4 cout << i << " "<< d << "" << s << endl;
会 输出 4 2 3

还 可 以 使 用 std::ignore 忽 略 某 些 tuple 中 的 某 些 返回 值 ， 如

1 tie(i，ignore，s) = t3;
```

```
HEPES, ie TGAERTIGOIREE, LITERS

uP WN PR

int i; double d; string s;
tuple<int,double,string> t3 = {1, 2.0, "3"};
tie(i, d, s) = t3;

t3 = {1, 2.0, "3"};

tie(i, d, s) = {1, 2.0, "3"};
```

c++17后即可直接auto& [a,b]解包

### map/multimap（pair自动排序）

#### 原理与时间复杂度

![](test_assets/image_377.png) ，key插入后不允许修改（能删除），value可以修改

![](test_assets/image_378.png) 红黑树是有序的自平衡二叉树，对应map的key有序；红黑树是左叶子<父节点<右叶子，中序遍历即可从小到大遍历

注意map和set的区别，set是不允许重复值，map是不允许重复key可以重复value

#### 遍历与迭代器

结点，内存不连续，是双向迭代器

因为map的键值关系到map元素的排列规则，任意改变map键值将会严重破坏map组织。如果想要修改元素的实值，那么是可以的

所以在for迭代中不要调用map.erase（key），会改变整个map组织程序崩掉

进行新增操作或者删除操作时，操作之前的所有迭代器，在操作完成之后依然有效，当然被删除的那个元素的迭代器必然是个例外

常见误区：const引用，是要对key而不是整体

```
map<int, vector<string>> my_map;
for (const pair<int, vector<string>>& p : my_map) {} // performance-implicit-conversion-in-loop

// The iterator type is in fact pair<const int, vector<string>>, which means

// that the compiler added a conversion, resulting in a copy of the vectors.
```

#### 构造和赋值

```
构造 :
© imaperg, 12> mp; map Ei ADEES
© map(const map anp): 1/ 搓 由 构造 函数

const map amp); 1/ 重 载 等 号 探 作 符
```

#### 大小和交换

```
Sar:

， sizeQ); ESSE PT ROE
© empty); HRS

。 swap(st); /交换 两 个 集合 容器
```

size()返回值是unsigned int，遍历容器int i=0开始没有问题，特殊情况int i=-1开始遍历，i<a.size();就会出问题，压根没有进入循环

#### 存取访问

map.[key]或map.at（key），返回对应的value

注意map.[key]会插入键值，value是默认值0

使用.at()访问，如不存在则抛异常

```
cout << “size:” << mymap. size() << endl;

cout << oven << endl;
cout << “size:” << mymap. size() << endl;
```

![](test_assets/image_383.png)

#### 插入和删除

```
Ansert(elen);) /在 容器 中 插入 元 素 。

clear0; 1/ 清除 所 有 元 素

‘erase(pos); HPAPSPOSERBATEOITR, TTT RAE.
erase(beg, end); | /1 种 除 区 间 [begendj 的 所 有 元 素 ， 返 回 下 一 个 元 素 的 迭代 中 。
erase(key}s HENGE BPE,
```

插入：

```
// 第 一 种 通过 pair 的 方式 插入 对 象 "
napStu, insert (pair<int, string>(3, “小 张 )) ;#

// 第 二 种 通过 pair 的 方式 插入 对 象 "

napStu. inset (make_pair(-1, “校长 7)) ;9

// 第 三 种 通过 value_type MATAR

napStu. insert (map<int, string>:tvalue_type(1, “小 李 “)) ;«
// 第 四 种 BAA sta}

mapStu[3] = “/)3xI";#

mapStu[5] = “)F";e
```

#### 查找和统计

```
find(key) ;// 查 找 键 key 是 否 存在 , 若 存在 ， 返 回 该 键 的 元 素 的 迭代 器 ，/ 若 不 存在 ， 返 回 map. end () ;
count (keyElem) ;// 返 回 容 器 中 key 为 keyElem 的 对 组 个 数 。 对 map 来 说 ， 要 么 是 0， 要 么 是 1。 对 multim
lower_bound (keyElem) ;// 返 回 第 一 个 key>=keyElem 元 素 的 迭代 器 。

Upper_bound (keyElem) ;// 返 回 第 一 个 key>keyElem 元 素 的 迭代 器 。

equal_range (keyElem) ;// 返 回 容器 中 key 与 keyElem 相 等 的 上 下 限 的 两 个 迭代 器 。
```

equal\_range实际上就是上面两个函数的返回值组合在一起

#### 排序

易错：在函数中如sort（）使用带()，在容器<>中使用不带

![](test_assets/image_387.png)

内置数据类型：

```
class MyCompare

U sts

{bool operator 0 (int v1, int v2) const// 比 较 的 是 key 中 的 int， 所 以 参数 列表 是 int。 另 外 const 要 加
return v1 》v2:// 从 大 到 小

1

void printMap(const map<int, int, MyCompare>& 四 // 使 用 map 的 参数 列表 也 要 同步 修改
for (map<int, int>::const_iterator it = mbegin(); it != mend(Q); it++)

i cout << “key:” << (#it). first << “\tvalue:” << (Fit). second << endl;

cout << endl;

void test01(0)

1 (BR) Rey ABLE, 可 以 修改 排序 规则

| map<int, int, MyCompare> ml;

| ml. insert (make pair (5, 50));

| ml.insert(pair<int, int>(1, 10));

| ml [3]=@, 30) ;// 不 建议 用 来 插入 ， 建 议 用 来 访问
ml. insert (make_pair(4，40))

| ml. insert (make_pair (2, 20));

printMap (m1) ;
```

自定数据类型：

```
class Person

{

public:

| Person(string name, int age)
{
| mName = nane;
| mAge = age;
t
string m Name;
int m Age;

Ib;

class MyCompare

{

public:

bool operator () (const Person& pl, const Person& p2) const//const 要 加
{

1 return pl.mAge > p2.m Age; //#2=88)\AZ))

了
```

```
void printMap(const map<Person, int, MyCompare>& 四 // 使 用 map 的 参数 列表 也 要 同步 修改
for (map<Person, int>::const_iterator it = m begin(); it != mend(); it++)

cout << “HEQ:” << (it). first. m Name<<”\toFie: ” << (Hit). first.mAge«< “\tvalue : ” << (#it). second << endl;

t
cout << endl;
}

void test01()

// 自 定义 key 数 据 类 型 ， 需 提供 排序 规则
map<Person, int, MyCompare> ml;

ml. insert (make pair (Person("¥}#”, 30), 300)) |
ml. insert (make_pair (Person (“###8”, 50), 500);
ml. insert (make_pair (Person (“#4%”, 40), 400);
printMap (ml) ;
```

### unordered\_map/unordered\_multimap

C11后能有，都只需要#include < unordered\_map >

#### 原理与时间复杂度

哈希表（也叫散列表），通过把key值通过hash算法映射到Hash表中一个位置来访问记录，查找时间复杂度可达O（1），其中在海量数据处理中有着广泛应用。但是元素的排列顺序是无序的，也无法范围查询

![](test_assets/image_391.png)

#### 构造和赋值

unordered\_map<T1, T2> ump; //默认构造函数

unordered\_map(const unordered\_map $ump); //拷贝构造函数

unordered\_map& operator=(const unordered\_map &ump); //重载等号操作符

#### 大小和交换

```
Sar:

， sizeQ); ESSE PT ROE
© empty); HRS

。 swap(st); /交换 两 个 集合 容器
```

size()返回值是unsigned int，遍历容器int i=0开始没有问题，特殊情况int i=-1开始遍历，i<a.size();就会出问题，压根没有进入循环

#### 插入和删除

```
Ansert(elen);) /在 容器 中 插入 元 素 。

clear0; 1/ 清除 所 有 元 素

‘erase(pos); HPAPSPOSERBATEOITR, TTT RAE.
erase(beg, end); | /1 种 除 区 间 [begendj 的 所 有 元 素 ， 返 回 下 一 个 元 素 的 迭代 中 。
erase(key}s HENGE BPE,
```

#### 访问与遍历

umap[key]可以访问与赋值对应key的value，访问没有insert的key将默认赋值0并返回0（注意这将导致umap.size()+1）

```
unordered_map<int, int> umap
unap. insert (als pair<int, int>(1, 2))
unap. insert (als make_pair (isl 3, oVai2 4))
cout << unap[1] << endl

cout << unap[2] << endl

cout << unap[3] << endl

unap [4] = 5

cout << umap[4] << endl
```

全部遍历使用for

```
OuaWNR

第 一 种 遍历

unordered_map-

p : count) {
front = p.first;
end = p.second

unordered_map<int, int> count
m.begin() ;it!=m.end() ;it++

front = it->first;
end = it->second;
```

map的键值关系到map元素的排列规则，任意改变map的key将会严重破坏map组织。只能修改value。所以在for迭代中不要调用map.erase（key），会改变整个map组织程序崩掉

#### 查找和统计

```
© Find(key) EttkeyRSE ATE, BORER: BFE, ilElsetend();
© | count(key); MUSitkeyORRNT
```

ump[key]或ump.at（key），返回对应的value

unorder\_map.count()返回值只能是0和1

### STL的浅拷贝与深拷贝

STL容器所提供的都是值(value)寓意，而非引用(reference)寓意，也就是说当我们给容器中插入元素的时候，容器内部实施了拷贝动作，将我们要插入的元素再另行拷贝一份放入到容器中，而不是将原数据元素直接放进容器中，也就是说我们必须提供拷贝构造函数，并且存在指针成员时要写成深拷贝。

#define \_CRT\_SECURE\_NO\_WARNINGS

#include<iostream>

#include<vector>

**usingnamespace** std**;**

class myclass**{**

public**:**

myclass**(**char**\*** data**){**

int len **=** strlen**(**data**)+**1**;**//计算传进来的字符串长度

**this->**data **=new**char**[**len**];**//在堆区分配了len字节内存

strcpy**(this->**data**,** data**);**//将数据拷贝到我们在堆分配的内存中

**}**

//增加拷贝构造函数

myclass**(**const myclass**&** mc**){**

int len **=** strlen**(**mc**.**data**)+**1**;**

**this->**data **=new**char**[**len**];**

strcpy**(this->**data**,** mc**.**data**);**

**}**

//重载operator=操作符

myclass**&operator=(**const myclass**&** mc**){**

if (this->data != NULL){

delete[] this->data;

this->data = NULL;

}

int len **=** strlen**(**mc**.**data**)+**1**;**

**this->**data **=new**char**[**len**];**

strcpy**(this->**data**,** mc**.**data**);**

**return\*this;**

**}**

//既然我们在堆区分配了内存，需要在析构函数中释放内存

**~**myclass**(){**

**if(NULL!=this->**data**){**

**delete[]this->**data**;**

**this->**data **=NULL;**

**}**

**}**

private**:**

char**\*** data**;**

**};**

void test\_deep\_copy**(){**

char**\*** data **=**"abcd"**;**

myclass mc**(**data**);**//创建myclass的实例 并用char\*字符串data初始化对象

vector**<**myclass**>** v**;**//创建vector容器

v**.**push\_back**(**mc**);**//将mc实例插入到vector容器尾部

**}**

int main**(){**

test\_deep\_copy**();**//调用测试函数

system**(**"pause"**);**

**return**0**;**

**}**

### 动态链接容器易出问题

在动态链接库函数内部使用容器也是没有问题的，但是给动态库函数传递容器的对象本身，则会出现内存堆栈破坏的问题。

容器和动态链接库相互支持不够好，动态链接库函数中使用容器时，参数中只能传递容器的引用，并且要保证容器的大小不能超出初始大小，否则导致容器自动重新分配，就会出现内存堆栈破坏问题。

## 函数对象（仿函数）

![](test_assets/image_397.png)

分类:假定某个类有一个重载的operator()，而且重载的operator()要求获取一个参数，我们就将这个类称为“一元仿函数”（unary functor）；相反，如果重载的operator()要求获取两个参数，就将这个类称为“二元仿函数”（binary functor）。

![](test_assets/image_398.png)

### 谓词(\_Pred)

![](test_assets/image_399.png)

```
// 一 元 谓词
class GreaterFive

{

iblic:

bool operator() (int val)
{

{return val >8;

}

void test010

{

vector<int? v;

for (int i= 0; i < 10; i+)
{

v. push_back (i) ;
}

/在 中 查找 5 的 数字 ，

//GreaterFive (是 慰 认 构造 创建 了 一 个 匿名 国教 对 象
vectorkint>::iterator it-find if(v. begin(), v.endQ, GreaterFive():
if (it = vend)

{

cout << “未 找到 <« endl:
```

```
// 二 元 谓词
class MyCompare

{
public:
‘bool operator () (int vi, int v2)
{
return v1 > v2:

void test020
{

vector<int? v;
-v. push_back (10) ;
-v. push_back (40) ;
-y. push_back (20) ;
‘y. push_back (30) ;
‘v. push_back (50) ;
sort (v. begin0 ，v. endO ) :// 黑 让 从 小 到 大

for (vector<int>: :iterator it = wbegin0: it != v.endQ; itt)
{
cout << it <«< endl:
}
cout << endl:
JER
sort (v. begin(, v.end0, MyCompare()):
for (vector<int>: iterator it = v. begin: it != v.endQ; itt)

{

cout << it <«< endl:
}

cout << endl:
```

### 内建函数对象

![](test_assets/image_402.png)

#### 算数仿函数

```
功能 描述 :

实现 四 则 运算

仿 函 数 原型 :

templatecclass 1 T
templatecclass TD T
‘tenplatecclass TD T
‘template<class T> T
teaplatecclass 1 T

tenplatecelass T> T

其 中 negate 是 一 元 运算 ， 其 他 者 是 二 元 运算

ae 88
as AUER
wultipliescts) /法 数
dividesers| 工 // 险 法 函 玫
oduluscT>) ROR
negatect>) (RSA
```

以取反与加法为例：

```
#include <functional>
```

```
void test01()
{

negateCint? n;
cout << n(50) << endl:
```

```
void test02()
{

plusGint> p:
cout << p(10, 20) << endl:
```

#### 关系仿函数

![](test_assets/image_407.png)pair<int,int>也有模板，比较的是第一个int

一般就用大于

```
void test01()
{

for (vector<int>: iterator it = v. begin: it != v.endQ; itt)
{

| cout << it <« endl:

}

cout << endl:

/PASRE GEA RUBlessM NBA» RBRAgreater MAB
sort(v. begin(, v. end, greater<int>0);

for (vector<int>: iterator it = v.begin(: it != v.endQ; itt)

{

| cout < #it <« endl:
}
cout << endl:
```

#### 逻辑仿函数

```
函数 原型
‘© template<class T bool logical_andet> BS
。 template<class T> bool logical_or<t> BBS

© [templatecclass T bool logical_not<t> BE
```

实际开发基本用不到

```
void testl
{

vector<bool> v:
-v. push_back (1):

-v. push_back/(0):

-y. push_back (1):

‘v. push_back/(0):

for (vector<bool>: :iterator i
{

v.beginO: it

cout << it KK endl:
}
cout << endl;

‘vector<bool v2:
v2. resize (v. size 0) .//ATB SABER
‘transform(v. begin(), v.end(), v2. begin), logical_not<bool>()) ; //algorithmlgHAiiitiaE

for (vector<bool>: :iterator it = v2. begin; it != v2.end(Q; itt)
{

cout << it KK endl:
}
cout << endl;
```

### 使用

1.在函数如sort中自定义规则

2.在容器<>中自定义规则

易错：在函数如sort中自定义规则是匿名对象作为参数传递要带()，在容器<>中自定义规则是作为类型不带（）

最重要的特点是可以作为参数传递（其实STL算法中谓词的地方放函数名照样跑通）

```
(71. 起 团 娄 的 代用: BA Ae ENE
class MyAdd

{

public:

| int operator (int vi, int v2)
io

{return vi + v2:
}

void test010

{

| MyAdd myAdd:

cout << myAdd(10, 10) << endl:
```

```
//2. 相 比 函数 的 |
jelass MyPrint
{

可 以 有 自己 的 成 员 属性 ， 但 相 比 普通 的 成 员 |

iblic:
‘void operator () (string test)
{

cout << test < endl:

count++:

}
int count-0:// 记 录 调 用 的 次 数

void test020

MyPrint myPrint;
ayPrint (‘Hello world”);
ayPrint (‘Hello world”) ;
ayPrint (‘Hello world”);
ayPrint (‘Hello world”)
cout 《《“ 调 用 次 数 为 : ”< myPrint. count << endl:
```

一个应用案例

```
1. 仿 函 数 既 能 起 苦 通 函 数 一 样 传 入 给 定数 量 的 参数 ， 还 能 存储 或 者 处 理 更 多 我 们 需要 的 有 用 信息 。 我 们 可 以 举 个 例子 :
假设 有 一 个 vector<string>， 你 的 任务 是 统计 长 度 小 于 5 的 string 的 个 数 ， 如 果 使 用 count_i 邓 数 的 话 ， 你 的 代码 可 能 长 成 这 样 :

bool LengthIsLessThanFive(const string& str) [
return str. length()<5;

}

int res=count_if (vec. begin(), vec.end(), LengthIsLessThanFive) ;

'pcount_ifasnS= Sev —NSACEH, JRE ooksHie, RN, WREBSSENMEKE HIS MIS, RTS R SRK:

bool LenthIsLessThan(const string& str, int len) {
return str. length()<Len;

}
IX NESIERLATE NEAERS RE, (BITRE Ecount_fABNSHESK: count_fkAVBunary function ( 仅 带 有 一 个 参数 ) (PATCHES. WRC, SRSRETRTIE:

class ShorterThan {
public:
explicit ShorterThan(int mazLength) : length(maxLength) 0}
bool operator () (const string& str) const {
return str. length() < length;
}
private:

const int length;
```

```
/3. 最 重要 的 作用 ， 不 能 作为 参数 传递
void doPrint QFPrint& mp, string test)

mp (test) :

roid test030
(

MyPrint myPrint;
doPrint (ayPrint, “hello c++”):

7
```

## 适配器

bind1st bind2nd绑定另一个参数

not1 not2 取反适配

ptr\_fun普通函数适配

mem\_fun mem\_fun\_ref成员函数适配

|  |
| --- |
| [//函数适配器bind1st bind2nd](STL示例代码/15 函数对象适配器)  [//现在我有这个需求 在遍历容器的时候，我希望将容器中的值全部加上100之后显示出来，怎么做哇？](STL示例代码/15 函数对象适配器)  [struct myprint](STL示例代码/15 函数对象适配器) **[:](STL示例代码/15 函数对象适配器)**[public binary\_function](STL示例代码/15 函数对象适配器)**[<](STL示例代码/15 函数对象适配器)**[int](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[int](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[void](STL示例代码/15 函数对象适配器)**[>{](STL示例代码/15 函数对象适配器)**[//二元函数对象 所以需要继承 binary\_fucntion<参数类型,参数类型,返回值类型>](STL示例代码/15 函数对象适配器)  [void](STL示例代码/15 函数对象适配器)**[operator()(](STL示例代码/15 函数对象适配器)**[int v1](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[int v2](STL示例代码/15 函数对象适配器)**[)](STL示例代码/15 函数对象适配器)**[const](STL示例代码/15 函数对象适配器)**[{](STL示例代码/15 函数对象适配器)**  [cout](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)** [v1](STL示例代码/15 函数对象适配器) **[+](STL示例代码/15 函数对象适配器)** [v2](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)**[" "](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  **[}](STL示例代码/15 函数对象适配器)**  **[};](STL示例代码/15 函数对象适配器)**  [void test02](STL示例代码/15 函数对象适配器)**[(){](STL示例代码/15 函数对象适配器)**  [vector](STL示例代码/15 函数对象适配器)**[<](STL示例代码/15 函数对象适配器)**[int](STL示例代码/15 函数对象适配器)**[>](STL示例代码/15 函数对象适配器)** [v](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[1](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[2](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[3](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[4](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [//我们直接给函数对象绑定参数 编译阶段就会报错](STL示例代码/15 函数对象适配器)  [//for\_each(v.begin(), v.end(), bind2nd(myprint(),100));](STL示例代码/15 函数对象适配器)  [//如果我们想使用绑定适配器,需要我们自己的函数对象继承binary\_function 或者 unary\_function](STL示例代码/15 函数对象适配器)  [//根据我们函数对象是一元函数对象 还是二元函数对象](STL示例代码/15 函数对象适配器)  [for\_each](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[begin](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[end](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [bind2nd](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[myprint](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)**[100](STL示例代码/15 函数对象适配器)**[));](STL示例代码/15 函数对象适配器)**  [cout](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)** [endl](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  [//总结： bind1st和bind2nd区别?](STL示例代码/15 函数对象适配器)  [//bind1st ： 将参数绑定为函数对象的第一个参数](STL示例代码/15 函数对象适配器)  [//bind2nd ： 将参数绑定为函数对象的第二个参数](STL示例代码/15 函数对象适配器)  [//bind1st ,bind2nd将二元函数对象转为一元函数对象](STL示例代码/15 函数对象适配器)  **[}](STL示例代码/15 函数对象适配器)**  [//函数对象适配器 not1 not2](STL示例代码/15 函数对象适配器)  [struct myprint02](STL示例代码/15 函数对象适配器) **[{](STL示例代码/15 函数对象适配器)**  [void](STL示例代码/15 函数对象适配器)**[operator()(](STL示例代码/15 函数对象适配器)**[int v1](STL示例代码/15 函数对象适配器)**[)](STL示例代码/15 函数对象适配器)**[const](STL示例代码/15 函数对象适配器)**[{](STL示例代码/15 函数对象适配器)**  [cout](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)** [v1](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)**[" "](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  **[}](STL示例代码/15 函数对象适配器)**  **[};](STL示例代码/15 函数对象适配器)**  [void test03](STL示例代码/15 函数对象适配器)**[(){](STL示例代码/15 函数对象适配器)**  [vector](STL示例代码/15 函数对象适配器)**[<](STL示例代码/15 函数对象适配器)**[int](STL示例代码/15 函数对象适配器)**[>](STL示例代码/15 函数对象适配器)** [v](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[2](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[1](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[5](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[4](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [vector](STL示例代码/15 函数对象适配器)**[<](STL示例代码/15 函数对象适配器)**[int](STL示例代码/15 函数对象适配器)**[>::](STL示例代码/15 函数对象适配器)**[iterator it](STL示例代码/15 函数对象适配器) **[=](STL示例代码/15 函数对象适配器)** [find\_if](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[begin](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[end](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [not1](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[bind2nd](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[less\_equal](STL示例代码/15 函数对象适配器)**[<](STL示例代码/15 函数对象适配器)**[int](STL示例代码/15 函数对象适配器)**[>(),](STL示例代码/15 函数对象适配器)**[2](STL示例代码/15 函数对象适配器)**[)));](STL示例代码/15 函数对象适配器)**  [cout](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)**["it:"](STL示例代码/15 函数对象适配器)**[<<\*](STL示例代码/15 函数对象适配器)**[it](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)** [endl](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  [sort](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[begin](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[end](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [not2](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[greater](STL示例代码/15 函数对象适配器)**[<](STL示例代码/15 函数对象适配器)**[int](STL示例代码/15 函数对象适配器)**[>()));//debug模式下报错，release没事](STL示例代码/15 函数对象适配器)**  [for\_each](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[begin](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[end](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [myprint02](STL示例代码/15 函数对象适配器)**[());](STL示例代码/15 函数对象适配器)**  [cout](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)** [endl](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  [//not1 对一元函数对象取反](STL示例代码/15 函数对象适配器)  [//not2 对二元函数对象取反](STL示例代码/15 函数对象适配器)  **[}](STL示例代码/15 函数对象适配器)**  [//如何给一个普通函数使用绑定适配器(bind1st bind2nd)绑定一个参数？(拓展)](STL示例代码/15 函数对象适配器)  [//ptr\_fun](STL示例代码/15 函数对象适配器)  [void myprint04](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[int v1](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[int v2](STL示例代码/15 函数对象适配器)**[){](STL示例代码/15 函数对象适配器)**  [cout](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)** [v1](STL示例代码/15 函数对象适配器) **[+](STL示例代码/15 函数对象适配器)** [v2](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)**[" "](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  **[}](STL示例代码/15 函数对象适配器)**  [void test04](STL示例代码/15 函数对象适配器)**[(){](STL示例代码/15 函数对象适配器)**  [vector](STL示例代码/15 函数对象适配器)**[<](STL示例代码/15 函数对象适配器)**[int](STL示例代码/15 函数对象适配器)**[>](STL示例代码/15 函数对象适配器)** [v](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[2](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[1](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[5](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[4](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [//1 将普通函数适配成函数对象](STL示例代码/15 函数对象适配器)  [//2 然后通过绑定器绑定参数](STL示例代码/15 函数对象适配器)  [for\_each](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[begin](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[end](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [bind2nd](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[ptr\_fun](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[myprint04](STL示例代码/15 函数对象适配器)**[),](STL示例代码/15 函数对象适配器)**[100](STL示例代码/15 函数对象适配器)**[));](STL示例代码/15 函数对象适配器)**  [cout](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)** [endl](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  [//总结: ptr\_fun 将普通函数转变为函数对象](STL示例代码/15 函数对象适配器)  **[}](STL示例代码/15 函数对象适配器)**  [//mem\_fun mem\_fun\_ref](STL示例代码/15 函数对象适配器)  [//如果我们容器中存储的是对象或者对象指针，如果能指定某个成员函数处理成员数据。](STL示例代码/15 函数对象适配器)  [class student](STL示例代码/15 函数对象适配器)**[{](STL示例代码/15 函数对象适配器)**  [public](STL示例代码/15 函数对象适配器)**[:](STL示例代码/15 函数对象适配器)**  [student](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[string name](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[int age](STL示例代码/15 函数对象适配器)**[):](STL示例代码/15 函数对象适配器)**[name](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[name](STL示例代码/15 函数对象适配器)**[),](STL示例代码/15 函数对象适配器)** [age](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[age](STL示例代码/15 函数对象适配器)**[){}](STL示例代码/15 函数对象适配器)**  [void print](STL示例代码/15 函数对象适配器)**[(){](STL示例代码/15 函数对象适配器)**  [cout](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)**["name:"](STL示例代码/15 函数对象适配器)**[<<](STL示例代码/15 函数对象适配器)** [name](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)**[" age:"](STL示例代码/15 函数对象适配器)**[<<](STL示例代码/15 函数对象适配器)** [age](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)** [endl](STL示例代码/15 函数对象适配器)**[;;](STL示例代码/15 函数对象适配器)**  **[}](STL示例代码/15 函数对象适配器)**  [void print2](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[int a](STL示例代码/15 函数对象适配器)**[){](STL示例代码/15 函数对象适配器)**  [cout](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)**["name:"](STL示例代码/15 函数对象适配器)**[<<](STL示例代码/15 函数对象适配器)** [name](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)**[" age:"](STL示例代码/15 函数对象适配器)**[<<](STL示例代码/15 函数对象适配器)** [age](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)**[" a:"](STL示例代码/15 函数对象适配器)**[<<](STL示例代码/15 函数对象适配器)** [a](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)** [endl](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  **[}](STL示例代码/15 函数对象适配器)**  [int age](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  [string name](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  **[};](STL示例代码/15 函数对象适配器)**  [void test05](STL示例代码/15 函数对象适配器)**[(){](STL示例代码/15 函数对象适配器)**  [//mem\_fun : 如果存储的是对象指针，需要使用mem\_fun](STL示例代码/15 函数对象适配器)  [vector](STL示例代码/15 函数对象适配器)**[<](STL示例代码/15 函数对象适配器)**[student](STL示例代码/15 函数对象适配器)**[\*>](STL示例代码/15 函数对象适配器)** [v](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  [student](STL示例代码/15 函数对象适配器)**[\*](STL示例代码/15 函数对象适配器)** [s1](STL示例代码/15 函数对象适配器) **[=new](STL示例代码/15 函数对象适配器)** [student](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**["zhaosi"](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[10](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [student](STL示例代码/15 函数对象适配器)**[\*](STL示例代码/15 函数对象适配器)** [s2](STL示例代码/15 函数对象适配器) **[=new](STL示例代码/15 函数对象适配器)** [student](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**["liuneng"](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[20](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [student](STL示例代码/15 函数对象适配器)**[\*](STL示例代码/15 函数对象适配器)** [s3](STL示例代码/15 函数对象适配器) **[=new](STL示例代码/15 函数对象适配器)** [student](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**["shenyang"](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[30](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [student](STL示例代码/15 函数对象适配器)**[\*](STL示例代码/15 函数对象适配器)** [s4](STL示例代码/15 函数对象适配器) **[=new](STL示例代码/15 函数对象适配器)** [student](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**["xiaobao"](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[40](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[s1](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[s2](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[s3](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[s4](STL示例代码/15 函数对象适配器)**[);](STL示例代码/15 函数对象适配器)**  [for\_each](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[begin](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [v](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[end](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [mem\_fun](STL示例代码/15 函数对象适配器)**[(&](STL示例代码/15 函数对象适配器)**[student](STL示例代码/15 函数对象适配器)**[::](STL示例代码/15 函数对象适配器)**[print](STL示例代码/15 函数对象适配器)**[));](STL示例代码/15 函数对象适配器)**  [cout](STL示例代码/15 函数对象适配器) **[<<](STL示例代码/15 函数对象适配器)**["-----------------------------"](STL示例代码/15 函数对象适配器)**[<<](STL示例代码/15 函数对象适配器)** [endl](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  [//mem\_fun\_ref : 如果存储的是对象，需要使用mem\_fun\_ref](STL示例代码/15 函数对象适配器)  [vector](STL示例代码/15 函数对象适配器)**[<](STL示例代码/15 函数对象适配器)**[student](STL示例代码/15 函数对象适配器)**[>](STL示例代码/15 函数对象适配器)** [v2](STL示例代码/15 函数对象适配器)**[;](STL示例代码/15 函数对象适配器)**  [v2](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[student](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**["zhaosi"](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[50](STL示例代码/15 函数对象适配器)**[));](STL示例代码/15 函数对象适配器)**  [v2](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[student](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**["liuneng"](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[60](STL示例代码/15 函数对象适配器)**[));](STL示例代码/15 函数对象适配器)**  [v2](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[student](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**["shenyang"](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[70](STL示例代码/15 函数对象适配器)**[));](STL示例代码/15 函数对象适配器)**  [v2](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[push\_back](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[student](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**["xiaobao"](STL示例代码/15 函数对象适配器)**[,](STL示例代码/15 函数对象适配器)**[80](STL示例代码/15 函数对象适配器)**[));](STL示例代码/15 函数对象适配器)**  [for\_each](STL示例代码/15 函数对象适配器)**[(](STL示例代码/15 函数对象适配器)**[v2](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[begin](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [v2](STL示例代码/15 函数对象适配器)**[.](STL示例代码/15 函数对象适配器)**[end](STL示例代码/15 函数对象适配器)**[(),](STL示例代码/15 函数对象适配器)** [mem\_fun\_ref](STL示例代码/15 函数对象适配器)**[(&](STL示例代码/15 函数对象适配器)**[student](STL示例代码/15 函数对象适配器)**[::](STL示例代码/15 函数对象适配器)**[print](STL示例代码/15 函数对象适配器)**[));](STL示例代码/15 函数对象适配器)**  **[}](STL示例代码/15 函数对象适配器)** |

### std::bind

std::bind的头文件是 <functional>，它是一个函数适配器，接受一个可调用对象（callable object），生成一个新的可调用对象来“适应”原对象的参数列表

```
std:: bind2° APA RAURE, ESP:

m 上 mwN PP

template< class F, class... Args >
/*unspecified*/ bind( F&& f, Args&&... args );

template< class R, class F, class... Args >
/*unspecified*/ bind( F&& f, Args&&... args );
```

返回一个基于f的函数对象，其参数被绑定到args上。

f的参数要么被绑定到值，要么被绑定到placeholders（占位符，如\_1, \_2, ..., \_n）。

std::bind将可调用对象与其参数一起进行绑定，绑定后的结果可以使用std::function保存。

作用：

将可调用对象和其参数绑定成一个防函数；

只绑定部分参数，减少可调用对象传入的参数。

用法：

1.绑定普通函数

```
1 double callableFunc (double x, double y) {return x/y;}
2 auto NewCallable = std::bind (callableFunc, std::placeholders::_1,2);
3 | std::cout << NewCallable (10) << '\n';

。bind 的 第 一 个 参数 是 函数 名 ， 普 通 函 数 做 实 参 时 ， 会 隐 式 转换 成 函数 指针 。 因 此
std::bind(callableFunc，1,2) 等 价 于 std::bind (&callableFunc，1,2);

。_ 1 表示 占 位 符 ， 位 于 <functional> 中 ，std::placeholders:: 1;

。 第 一 个 参数 被 占 位 符 占用 ， 表 示 这 个 参数 以 调用 时 传 入 的 参数 为 准 ， 在 这 里 调用 NewCallable 时 ， 给 它 传
入 了 10， 其 实 就 想到 于 调用 callableFunc(10,2);
```

2.绑定成员函数

```
class Base

1

aif

3 public:

4 void display _sum(int al, int a2)

5 {

6 std::cout << al + a2 << NMn'

7 }

8

9 int m_data = 30;

10 }5

11°) int main()

12 {

13 Base base;

14 auto newiFunc = std::bind(&Base::display_sum, &base, 100, std::placeholders::_1);
15 newiFunc(2@); // should out put 120.
16 }

。bind 绑 定 类 成 员 函 数 时 ， 第 一 个 参数 表示 对 象 的 成 员 函 数 的 指针 ， 第 二 个 参数 表示 对 象 的 地 址 。

。 必须 显 式 地 指定 &Base::diplay_sum， 因 为 编译 器 不 会 将 对 象 的 成 员 函 数 隐 式 转换 成 函数 指针 ， 所 以 必须
在 Base::display_sum 前 添加 &;

。 使 用 对 象 成 员 函 数 的 指针 时 ， 必 须要 知道 该 指针 属于 哪个 对 象 ， 因 此 第 二 个 参数 为 对 象 的 地 址 &base;
```

3.绑定引用参数

默认情况下，bind的那些不是占位符的参数被拷贝到bind返回的可调用对象中。

但是，与lambda类似，有时对有些绑定的参数希望以引用的方式传递，或是要绑定参数的类型无法拷贝。

```
ow ON DUM BF whN RB

ee
G2wouonaoa nr anuPF WHR DOD WO WAN DU FPWNH RP @

#include <iostream>

#include <functional>

#include <vector>

#include <algorithm>

#include <sstream>

using namespace std::placeholders;

using namespace std;

ostream & printInfo(ostream &0s, const string& s, char c)

{

int

os << Ss << ci

return os;

main()

vector<string> words{"welcome", "to", "C++11"};
ostringstream os;
char c = ' ‘3
for_each(words.begin(), words.end(),
[&os, c](const string & s){os << s << c3} )3

cout << os.str() << endl;

ostringstream os1;

// ostream fe7g, Fi Bea fbind —PiYR,

// WAIRR EC, BUTEA ESE HI ef HEC

for_each(words.begin(), words.end(),
bind(printInfo, ref(os1), _1, c))3

cout << osl.str() << endl;
```

### std::function

std::function对象是对C++中现有的可调用实体的一种类型安全的包裹（我们知道像函数指针这类可调用实体，是类型不安全的）。

目标实体包括普通函数、[Lambda](https://so.csdn.net/so/search?q=Lambda&spm=1001.2101.3001.7020)表达式、函数指针、以及其它函数对象等。

#### 直接用法

```
// 声 明 一 个 模板

typedef std::function<int(int)> Functional;

//normal function
int TestFunc(int a)

{
】}

//l\ambda expression
auto lambda = [](int a)->int{return a;};

return a;

//functor 仿 函数

class Functor

{

public:
int operator() (int a)

return a;

// 类 的 成 员 函 数 和 类 的 静态 成 员 函 数

class CTest

{
public:
int Func(int a)
{
return a;

static int SFunc(int a)

{
t

return a;
```

```
int main(int argc, char* argv[])

// 封 装 普通 函数

Functional obj = TestFunc;
int res = obj(@);

cout << "normal function :

<< res << endl;

obj lambda;
res = obj(1);
cout << "lambda expression :

// 封 装 仿 函 数
Functor functor0bj;
obj = functorObj;
res = obj(2);

cout << "functor :

// 封 装 1ambda 表 达 式

<< res << endl;

<< res << endl;

// 封 装 类 的 成 员 函 数 和 static 成 员 函 数

CTest 七 ;

obj = std::bind(&CTest::Func, &t, std::placeholders::_1);
res = obj(3);

cout << "member function :

<< res << endl;

obj = CTest::SFunc;
res = obj(4);
cout << "static member function :

<< res << endl;

return Q@;
```

std::function对象最大的用处就是在实现函数回调

使用者需要注意，它不能被用来检查相等或者不相等，但是可以与NULL或者nullptr进行比较。

#### 作为参数用法（回调）

std::function对象直接值传递即可，类似智能指针，，只是管着一个指针

```
class ProgramA {
public:
void FunA1() { printf("I'am ProgramA.FunA1() and be called..\n"); }

void FunA2() { printf("I'am ProgramA.FunA2() and be called..\n"); }

static void FunA3() { printf("I'am ProgramA.FunA3() and be called..\n"); }
33

class ProgramB {
typedef std::function<void ()> CallbackFun;
public:
void FunB1(CallbackFun callback) {
printf("I'am ProgramB.FunB2() and be called..\n");
callback();

void normFun() { printf("I'am normFun() and be called..\n"); }

int main(int argc, char **argv) {
ProgramA PA;
PA.FunA1();

printf("\n");

ProgramB PB;

PB.FunB1(normFun) ;

printf("\n");

PB.FunB1(ProgramA: : FunA3) ;

printf("\n");

PB.FunB1(std: :bind(&ProgramA: :FunA2, &PA));
```

## 算法

算法分为:**质变算法**和**非质变算法**。

质变算法：是指运算过程中会更改区间内的元素的内容。例如拷贝，替换，删除等等

非质变算法：是指运算过程中不会更改区间内的元素内容，例如查找、计数、遍历、寻找极值等等

|  |
| --- |
| **再好的编编程技巧，也无法让一个笨拙的算法起死回生。** |

用来操作容器中的数据的模板函数。例如，STL用sort()来对一个vector中的数据进行排序，用find()来搜索一个list中的对象， 函数本身与他们操作的数据的结构和类型无关，因此他们可以用于从简单数组到高度复杂容器的任何数据结构上。

![](test_assets/image_422.png)

### 遍历

![](test_assets/image_423.png)

### 查找替换统计

![](test_assets/image_424.png)

#### find值查找

```
Unik:
。 SURE, RELROETRIRR, HTRLRAREA(tmend)

BUR:
© Find(iterator beg, iterator end, value);
UREERTR, TAO, HTS CR
1 beg FRR
/end SFE
H value 查找 的 元 素
```

```
// 查找 内 置 数据 类 型
void test010

{
vector<int? v;
for (int i= 0; i < 10; i+)
{
|v. push back (i) ;
}

vector<int): :iterator it-find(v. begin(), v.end0, 5):
if (it = vend)
{

cout << “未 找到 5” << endl:

cout << “找到 67 << endl:
```

```
// 查 找 自 定义 数据 类 型

class Person

{
public:
Person(string name, int age)
{
mAge =
| name = nase
+
88

bool operator 一 (const Personk p)
{

if (@ Age == p.m Age Gi m Name = p.m Name)
{

{return true:
}
else
{
1 return false;
tot
}
string m Name:
```

```
void test020

{

‘vector@Person> p:
Person pl ("aaa”, 10):

Person p4Caadr 40):

// 旋 入 到 窒 器 中

vectordPersony: :iterator it = find(p. begin), p.endQ, p2):
if (it = pend)
{

cout << “未 找到 <« endl:

cout 《《“ 找 到 。 姓名: ” Cit Dm Namecc"\t 年 龄 : “<Cit->m_Age << endl:
```

进阶：

find\_first\_of

find\_lase\_of

#### find\_if条件查找

查找满足条件的元素。

```
find_if(iterator beg, iterator eng, _Pred);
/ SRST, AMSAT ER, PNR
/ beg 开始 迁 代 器

I end SRBC

|) Pred 函数 或 者 谓词 (返回 bool 类 型 的 仿 另 数 )
```

```
// 音 抄 病 下 条 件 的 元 素 一 一 内 站 数据 关 型

class GreaterFive

{
public:
| bool operator Q (int val)

{
{return val > 5:
}

void test010

{

| vector<int> v:

for (int i= 0; i < 10; i+)
{

v. push_back (i) ;
}

vector<int): :iterator it-find_if(v. begin(), v.end0, GreaterFive():

if Gt = v.endO)
{
cout << “AERA « endl:

cout 《《“ 找 到 ， 第 一 个 满足 条 件 的 为 : “< 人 kit 《< endl:
```

```
// 查 找 蒲 足 条 件 的 元 素 一 一 自 定义 数据 类 型
class Person

{
public:
| Person(string name, int age)

{

mAge = age:
m Name = name:

}

string m Name:
‘int mAge:

class Greater20
{

public:

‘bool operator () (const Personk p)

return p.m Age > 20:
```

```
void test02()
{
fieetaikPerson> p:

Person pl ("aaa”, 10):

Person p4Caadr 40):

// 旋 入 到 窒 器 中

end0)
```

#### any\_of

```
bool any of ( InputIterator start, InputIterator end, UnaryPredicate callback ) ;
```

里面用lamb，有一个为真就返回真

#### all\_of

```
bool all of (<Start of Range>, <End of Range>, UnaryPredicate pred);
```

里面用lamb，全部为真才返回真

#### binary\_search二分查找

![](test_assets/image_435.png)

用二分法查找很高效，但是必须已经是升序，因为第四个参数默认是内建函数对象less

如果是降序排序，第四个参数要加上，内建函数对象greater

此外，如果是自定义的数据类型，根据第四个参数，less重载<号，greater重载>号

#### lower/upper\_bound查找下上限

该函数内部使用的查找算法是二分查找，故仅适用于有序数据

一、lower\_bound()返回值是一个迭代器,返回指向大于等于key的第一个值，如果没有，返回end()。

对于set等容器，格式为：set. lower\_bound(key)

对于自排序数组，格式为：

```
a 数 组

lower_bound(a, atn, 3)-—a

1, 2, 3, 3, 3, 4]

(1, 2, 2, 4]

[4, 5, 6, 7, 8]

(1, 1, 2, 2, 2]

w | 口 | mw
```

二、upper\_bound()函数，返回大于key的第一个元素，注意lower\_bound是“大于等于”，upper\_bound是“大于”

对于set等容器，格式为：set. upper\_bound(key)

对于自排序数组，格式为：

```
a 数 组

upper_bound(a, atm 3)-a

[1, 2, 3, 3, 3, 4]

(1, 2, 2, 4]

[4, 5, 6, 7, 8]

(1, 1, 2, 2, 2]

wm | 口 |mw |m
```

三、对于递减数组：

```
递减 数列

lower_bound(begin,end,num,greater<type>()

从 数组 的 begin 位 置 到 end-1 位 置 二 分 查找 第 一 个 小 于 等 于 num 的 数字 ， 找 到 则 返回 该 数字 的 地 址 ， 找 不 到 则 返回 end。
upper_bound(begin,end,num,greater<type>())

从 数组 的 begin 位 置 到 end-1 位 置 二 分 查找 第 一 个 小 于 num 的 数字 ， 找 到 则 返回 该 数字 的 地 址 ， 找 不 到 则 返回 end。
```

#### adjacent\_find相邻重复元素查找

```
功能 摘 述 :
。 SRR OT

URAL:
© adjacent _Find(iterator beg, iterator end);
/查找 相 邻 更 揽 元 素 LAGOA — MOR
1/ beg FISHES
Mend SFiS
```

如果是自定义数据类型，函数第三个参数提供一个函数、仿函数，告诉编译器怎么才算相等

#### replace替换

```
replace(iterator beg, iteratorJend, oldvalue, newalue);
RAGE SB STH

beg 开始 法 代 器

1 end 结束 选 代 器

WoldvalueIB 元 素

1 newvalue 新 元 素
```

替换所有而不是一个

```
void print (int v)
{
cout << v <<

}

void test010
{
vector<int? v1:
for (int i= 0; i < 10; i+)
{
vi. push_back (i) :
}

for_each(vi. begin, vi.end(), print):
cout << endl;

NBR
replace(v1.beginQ, vi.end0, 5, 2000);
for_each(vl. begin), vi.end(), print):
```

#### replace\_if条件替换

```
函数 原型:
«© [replace_if(iterator beg, iterator end, _pred, newalue);
// 按 条 件 苦 换 元 素 ， 汪 足 条 件 的 若 换 成 指定 元 素
1/ beg FEE
Mend 结束 迁 代 器
11 pred Bi)
J newalue ERATE
```

```
void print (int v)

{
| cout << v «77
}
class Greater}
{
public:
bool operator () (int v)
{
{return v > 3;
}

void test010

{
vector<int? v1:
for (int i= 0; i < 10; i+)
{

v1. push_back (i) :
}

for_each(vi. begin, vi.end(), print):
cout << endl;

LPB AIV
replace_if (v1. begin(), vi. end(), Greater3(), 999) :
for_each (v1. begin, vi.end(), print):
```

#### minmax查最值

std::pair std::minmax(list);

std::min(list);

std::max(list);

list可以直接初始化，只要类型相同能被模板函数识别即可

```
long long x=nums[i];//%# filong 1
long long tmp = mins;
minS=min({minS,x,x°minS,x*maxS})5/
maxS=nax({maxS,x,x°tmp, x*maxS}) 5
```

### 排序乱序反转

![](test_assets/image_445.png)

#### sort排序

![](test_assets/image_446.png)

对于可以随机访问的容器,容器数据类型非自定义,从小到大排序

sort(开头,结尾);

对于不可以随机访问的容器(这种容器一般自带算法),容器数据类型非自定义,从小到大排序

list1.sort( );

自定义排序规则

```
void print(int v)

{
j

cout GT

void test010
{

HBUAR

sort (v. begin, v.end0):
for_each(v. begin), v.endQ, print):
cout << endl;

BARE

sort(v.begin(), v.end(), greater<int>0) :// 使 用 内 置信 图 数
for each(v.begin0，vend0，print)

cout << endl:
```

```
mylist. sort (myfunc2) ;
```

list只有谓词一个参数

对于其他数据类型

```
// 指 定 排序 规则
‘bool comparePerson (Person &pl,Person &p2)
{

// 按 照 年 龄 升序
| if (pl.m_ Age == p2.m Age)

// 年 龄 相同 ”按照 身高 降序
return pl.mHeight > p2.m Height;
iF

| else

return pl.m _Agey< p2.m_Age;

}
```

，普通函数和仿函数都可以 。

在类中的话，最好用lamb表达式，参数列表最好直接auto（static函数也可以）

```
sort (envelopes .begin(),envelopes.end(),[](const auto& v1,const auto& v2){
return v1[@]!=v2[@]?v1[@]<v2[@]:v1[1]>v2[1];
})5
```

#### random\_shuffle洗牌

![](test_assets/image_451.png)

```
void print (int v)
{

cout GT
}

void test010
{

vector<int? v;

for (int i= 0; i < 10; i+)
{

|v. push_back (i) ;

}

random shuffle(v.begin0，v.end0O) :// 的 随机 打 乱

for_each(v. begin, v.endQ, print):

| cout < endl:
}

int min0

{

‘srand((unsigned int) time (NULL)) :/7 AF Si 2 Meo.
test010
```

#### reverse反转

```
ea:
+ SSeaTRORE

BUR:
© ‘reverse(iterator beg, Iterator end);
// BIT
1 beg 开始 法 代 器
Wend SRR
```

和拷贝类似，后面迭代器指向的元素不参与反转

注意返回值为void

### 拷贝交换合并填充

![](test_assets/image_454.png)

#### copy拷贝

```
copy(iterator begy iterator end, iterator dest);
(REBT, RRA, HE
beg FREER

Mend 结束 迁 代 器

J dest 目标 起 始 迁 代 器
```

```
void print (int v)
{

cout GT
}

void test010
{

vector<int? v1:
for (int i= 0; i < 10; i+)

copy (v1. begin, vi.endQ, v2. begin()):
for_each(vl. begin, vi.end(), print):
cout << endl;
for_each(v2. begin), v2.end(), print):
cout << endl;
```

#### swap交换

```
功能 手 述 :
+ Sen (Sante

Ba:

‘© swap(container c1, container ¢2);
1 BFS TR
Ac1 容 器 1
VC2 容 器 2
```

得是同种类型的容器

```
voua prant\ine vy
{
cout GT

}

void test010

vector<int> v1:
vector<int> v2:
for (int i= 0; i < 10; i+)
{
vi. push_back (i) :
| v2. push_back (+100) :
}

cout << “交换 前 ” << endl:
for_each(vi. begin, vi.end(),
cout << endl;

for_each(v2. begin), v2.end(),
cout << endl:

NEB

swap (vl, v2):

cout << “交换 后 ” << endl:
for_each(vi. begin, vi.end(),
cout << endl.

for_each(v2. begin), v2.end(),
cout << endl;

print):

print):

print):

print):
```

#### merge合并

![](test_assets/image_459.png)

两个升序序列，合并后还是升序的，最后一个隐藏参数默认是less

```
void print (int v)
{

cout GT
j

void test010
{

vector<int> v1:
vector<int> v2:

for (int i= 0; i < 10; i+)
{

v1. push_back (i) :
| v2.push_back(i + 1):

/目标 容 器

vectarkint》wTarget:

vlarget. resize(vl. size() + v2.size0)

merge (vl. begin, vi.end(), v2.beginQ, v2.end0, vTarget. begin() :
for_each(vTarget.begin(), vlarget. end(), print):

cout << endl:
```

同样不开辟空间，要resize

若要合并两个降序序列，最后加上一个参数greater

```
merge(vl. begin(), vl.end(), v2. begin(), v2.end(), v3. begin(), greater<int>());
```

#### fill填充

```
功能 描述

向 容器 中 填充 指定 的 元 素

函数 原型 :

fill(iterator beg, iterator end, value);
// 向 容器 中 填充 元 素

// beg FREE

// end 结束 迭代 器

value 填充 的 值
```

```
void print (int val)

{

cout << val<<
}

void test01Q)

{
vector<int>vl
vi. resize (10)

fill(vi.begin(), vi.end(), 100)
for_each(vi.begin(), vi.end(), print)
```

不resize，就还是空的

## 迭代器

迭代器(iterator)是一种抽象的设计概念，现实程序语言中并没有直接对应于这个概念的实物。在<<Design Patterns>>一书中提供了23中设计模式的完整描述，其中iterator模式定义如下：提供一种方法，使之能够依序寻访某个容器所含的各个元素，而又无需暴露该容器的内部表示方式。

迭代器的设计思维-STL的关键所在，STL的中心思想在于将数据容器(container)和算法(algorithms)分开，彼此独立设计，最后再一贴胶着剂将他们撮合在一起。从技术角度来看，容器和算法的泛型化并不困难，c++的class template和function template可分别达到目标，如果设计出两这个之间的良好的胶着剂，才是大难题。

迭代器的种类:

|  |  |  |
| --- | --- | --- |
| 输入迭代器 | 提供对数据的只读访问 | 只读，支持++、==、！= |
| 输出迭代器 | 提供对数据的只写访问 | 只写，支持++ |
| 前向迭代器 | 提供读写操作，并能向前推进迭代器 | 读写，支持++、==、！= |
| 双向迭代器 | 提供读写操作，并能向前和向后操作 | 读写，支持++、--， |
| 随机访问迭代器 | 提供读写操作，并能在数据中随机移动 | 读写，支持++、--、[n]、-n、<、<=、>、>= |

![](test_assets/image_464.png)

### 定义与使用语法

容器名<类型名>::iterator 迭代器变量名，见下例

各个容器都有begin（）和end（）函数，用来给迭代器赋值

```
// 新 建 选 代 器

vector<int>: :iterator itBegin = Y.begin() ;// 起 始 选 代 器 ， 指 向 容器 中 第 一 个 元 素
vector<int>::iterator itEnd = v.end() ;// 结 束 选 代 器 ， 指 向 容器 中 最 后 一 个 元 素 的 下 一 个 位 置
while (itBegin != itEnd)

{

cout << #itBegin << endl;
itBegint+;
```

注意：

1.end()迭代器不是最后一个元素，而是最后一个元素后，故直接输出是报错的

2.可以通过v.end()[-1]获得最后一个元素

```
vector<int> arr={l, 2, 3, 4, 5};
auto @tdlivecterGneiviterater it = arr. begin();
cout << *it<<endl;

it = arr. begin()+1;

cout << *it << endl;

it = arr.begin() + 2;

cout << *it << endl;

it = arr.begin() + 3;

cout << *it << endl;

it = arr.begin() + 4;

cout << *it << endl;

it = arr. end();

cout << *it << endl;
```

```
Microsoft Visual C++ Runtime Library

Y) Debug Assertion Failed!

Program: D:\vsproject\test\x64\Debug\test exe
File: D:\Microsoft Visual
‘Studio\2022\Communit\VC\Tools\MSVC\14.33.31629\include\vector
Line: 50

Expression: can't dereference out of range vector iterator

For information on how your program can cause an assertion
failure, see the Visual C++ documentation on asserts.

(Press Retry to debug the application)

=e) 0)
```

还有反向迭代器，注意还是++it

```
// 反 向 遍历
for (string: mi = s.rbegin(); it != s.rend(); ++it)
{

}

cout << endl;

cout << *it <<” ”;
```

const容器要使用const迭代器

```
void pri ctor (const vector<int> &vec)
{
for Wector<int>::const_iterator it = vec. begin(); it != vec.end(); ++it)

{
}

cout << endl |

cout << *it << ” ”;
```

迭代器当作指向元素的指针一样使用即可，有三种用途

![](test_assets/image_470.png) Iterator类的访问方式就是把不同集合类的访问逻辑抽象出来，使得不用暴露集合内部的结构而达到循环遍历集合的效果。

### 种类

```
迭代 器 种 类 :

种 类 功能 支持 运算
ARSE 对 数据 的 只 读 访问 只 读 ， 支 持 ++、
输出 迭代 器 TI， 对 数据 的 只 写 访问 只 写 ， 支 持 ++
前 向 迭代 器 读 写 操作 ， 并 能 向 前 推进 迭代 器 读 写 ， 支 持 ++、
双向 迭代 器 读 写 操作 ， 并 能 向 前 和 向 后 操作 读 写 ， 支 持 ++、--

随机 访问 迁 。。 读 写 操作 ， 可 以 以 跳跃 的 方式 访问 任意 数据 ， 功 能 读 写 ， 支 持 ++、 一 、

代 器 最 强 的 迭代 器 <=, > OF

常用 的 容器 中 和 迭代 器 种 类 为 双向 迭代 器 ， 和 随机 访问 迭代 器
```

![](test_assets/image_472.png)string是随机访问迭代器

注意map.begin()+1是不行的，因为只有随机访问迭代器可以这么加

而双重循环时内部变量往往为外部变量+1，对于随机访问迭代器是可以的，map等双向迭代器则如图操作

```
auto it2 = map. begin() ;

for (auto itl = map. begin(); itl != map.end(); it1++) {
| for (it2=itl, it2++; it2 != map.end(); it2++) {

| | ret += diffs(itl>first, it2—first) * it1—secc
i}

1
```

### 与指针的区别

```
2 迭代 器 和 指针 的 区 别

迁 代 器 不 是 指针 ， 是 类 模板 ， 胡 现 的 像 指针 。 他 只 是 模拟 了 指针 的 一 些 功能 ， 重 载 了 指针 的 一 些 操作 符 ，-->、++、-- 等 。 和 迭代 器 封装 了 指针 ， 是 一 个 可 和 遍历 STL (
Standard Template Library) 容器 内 全 部 或 部 分 元 素 的 对 象 ， 本 质 是 封装 了 原生 指针 ， 是 指针 概念 的 一 种 提升 ， 提 供 了 比 指针 更 高 级 的 行为 ， 相 当 于 一 种 智能 指针 ， 他
可 以 根据 不 同类 型 的 数据 结构 来 实现 不 同 的 ++，-- 等 操作 。

迁 代 器 返回 的 是 对 象 引用 而 不 是 对 象 的 值 ， 所 以 cout 只 能 输出 迭代 器 使 用 取 值 后 的 值 而 不 能 直接 答 出 其 自身 。
```

### 失效情形

迭代器失效是一种现象，由特定操作引发，这些特定操作对容器进行操作，使得迭代器不指向容器内的任何元素，或者使得迭代器指向的容器元素发生了改变（后者取决于编译器，部分编译器会将此种情况也视为迭代器失效，部分编译器并不视为失效）

![](test_assets/image_475.png)

1.对于内存连续容器vector：插入/删除某元素后，后边的每个元素的迭代器都会失效，后边每个元素都往后/前移动一位；插入超出容量的数据，将导致重新分配内存，迭代器也会失效。失效后要更新迭代器。

2.对于关联容器map，set来说，使用了erase后，当前元素的迭代器失效，但是其结构是红黑树，删除当前元素，不会影响下一个元素的迭代器，所以在调用erase之前，记录下一个元素的迭代器即可。

3.对于list来说，删除元素的迭代器失效，后面不受影响，两个erase函数都是返回后继数据的迭代器

### std::back\_inserter

常用于copy，如

std::vector<int> vec1;

std::copy(vec2.begin(), vec2.end(), std::back\_inserter(vec1));

## 空间配置器

一般情况下,一个程序包括数据结构和相应的算法，而数据结构作为存储数据的组织形式，与内存空间有着密切的联系。在C++ STL中，空间配置器便是用来实现内存空间(一般是内存，也可以是硬盘等空间)分配的工具，他与容器联系紧密，每一种容器的空间分配都是通过空间分配器alloctor实现的。

为了最大化提升效率，分开空间配置和对象构造两部分。内存配置操作:通过alloc::allocate()实现；内存释放操作:通过alloc::deallocate()实现；对象构造操作:通过::construct()实现；对象释放操作:通过::destroy()实现

STL空间配置器产生的缘由：

　　在软件开发，程序设计中，我们不免因为程序需求，使用很多的小块内存（基本类型以及小内存的自定义类型）。在程序中动态申请，释放。

这个过程过程并不是一定能够控制好的，于是乎，

问题1：就出现了内存碎片问题。

问题2：一直在因为小块内存而进行内存申请，调用malloc，系统调用产生性能问题。

策略：如果申请的内存大小超过128，那么空间配置器就自动调用一级空间配置器。反之调用二级空间配置器。

**一级空间配置器，STL源码中的一级空间配置器命名为class \_\_malloc\_alloc\_template ，它很简单，就是对malloc，free，realloc等系统分配函数的一层封装。**

**二级空间配置器，由一个内存池和自由链表配合实现的。**

关于内存空间的配置与释放，采用两级配置器：一级配置器主要是考虑大块内存空间，利用malloc和free实现；二级配置器主要是考虑小块内存空间而设计的（为了最大化解决内存碎片问题，进而提升效率），采用链表free\_list来维护内存池（memory pool），free\_list通过union结构实现，空闲的内存块互相挂接在一块，内存块一旦被使用，则被从链表中剔除，易于维护。

# BOOST

## ASIO

Boost的ASIO是一个异步IO库，封装了对Socket的常用操作，简化了基于socket程序的开发。支持跨平台。

底层是OS的适配层，上一层一些模板类，再上一层模板类的参数化(TCP/UDP)，再上一层是服务，它只有一种框架为io\_service。

<https://blog.csdn.net/qq_44918090/article/details/126575034>

https://blog.csdn.net/smilejiasmile/article/details/114330843

# C11特性

![](test_assets/image_476.png)

## （1）统一的初始化方法

初始化列表{ }现在不仅仅能初始化数组和struct，还能初始化任意基本数据类型变量和类对象

```
C++98/03 可 以 使 用 初始 化 列表 (initializer list) 进行 初始 化 :

int i_arr[3] = { 1, 2, 3}; long Larr[] = { 1, 3, 2, 4}; struct A { int x; int y; }a={1, 2};
但 是 这 种 初始 化 方式 的 适用 性 非常 狭 容 ， 只 有 上 面 提 到 的 这 两 种 数据 类 型 可 以 使 用 初始 化 列表 。 在 C++11 中 ， 初 始 化 列表 的 适用 性 被 大 大 增加 了 。 它 现在 可 以 用 于 任何 类 型 对 象 的 初始 化 ， 实 例如 下 :

| int main(void) { Foo al (123) ; Foo a2 = 123; //error: ’Foo::Foo(const Foo &)’ is private Foo a3 = { 123}; Foo a4 { 123 }; int a = {3}; int a6 {3}; return 0; }
在 上 例 中 ，a3、a4 使 用 了 新 的 初始 化 方式 来 初始 化 对 象 ， 效 果 如 同 al 的 直接 初始 化 。a5、a6 则 是 基本 数据 类 型 的 列表 初始 化 方式 。 可 以 看 到 ， 它 们 的 形式 都 是 统一 的 。 这 里 需要 注意 的 是 ，a3 虽然 使 用 了 等 于 号 ， 但 它 仍然 是 列表 初始 化 ， 因

此 ， 私 有 的 拷贝 构造 并 不 会 影响 到 它 。a4 和 a6 的 写法 ， 是 C++98/03 所 不 具备 的 。 在 C++11 中 ， 可 以 直接 在 变量 名 后 面 跟 上 初始 化 列表 ， 来 进行 对 象 的 初始 化 。
```

## （2）成员变量默认初始化

```
ER SESE WIRY,

/7/ 程 序 实例 #include<iostream using namespace std; class B { public: int m= 1234; /成 员 变量 有 一 个 初始 值 int n; }; int minQ { Bb; cout < b.m< endl; return 0; }
```

在类定义时也可以指定默认值了，C11以前是不行的

## （3）auto

见基础，关键字

## （4）decltype

见基础，关键字

## （5）智能指针

见基础，指针。三种

## （6）nullptr

解决NULL的遗留问题

## （7）基于for的循环

见基础-选择与循环

## （8）右值引用和move语义

面向对象，类封装，构造，移动构造函数中也有提及

```
1. 右 值 引用

C++98/03 标准 中 就 有 引用 ， 使 用 "&" 表示 。 但 此 种 引用 方式 有 一 个 缺陷 ， 即 正常 情况 下 只 能 操作 C++ 中 的 左 值 ， 无 法 对 右 值 添加 引用 。 举 个 例子 :

int num = 10;
int 好 = num; /正确
int & = 10; // 错 误

int num = 10;
const int &b = num;

const int &c = 10;

Pal, C++11 HERS TS S/S, BRAGS, "88" 表示 。
需要 注意 的 ， 和 声明 左 值 引用 一 样 ， 右 值 引用 也 必须 立即 进行 初始 化 操作 ， 且 只 能 使 用 右 值 进 行 初始 化 ， 比 如 :

int num = 10;
/fint @& a = num 7/ 右 值 引用 不 能 初始 化 为 左 值
int && a = 10;

和 常量 左 值 引用 不 同 的 是 ， 右 值 引用 还 可 以 对 右 值 进行 修改 。 例 如 :

int && a = 10;

a = 100;

cout <<a << endl;

BARTER:
100

ay

另外 值得 一 提 的 是 ，C++ 语法 上 是 支持 定义 常量 右 值 引用 的 ， 例 如

const int8& a = 10;// 编 译 器 不 会 报错

但 这 种 定义 出 来 的 右 值 引用 并 无 实际 用 处 。 一 方面 ， 右 值 引用 主要 用 于 移动 语义 先 美 转发 ， 其 中 前 者 需要 有 修改 右 值 的 权限 ;

如 上 所 示 ， 编 译 器 允许 我 们 为 num 左 值 建立 一 个 引用 ， 但 不 可 以 为 10 这 个 右 值 建立 引用 。 因 此 ，C++98/03 标准 中 的 引用 又 称 为 左 值 引用 。
注意 ， 虽 然 C++98/03 标准 不 支持 为 右 值 建立 非常 星 左 值 引用 ， 但 允许 使 用 常量 左 值 引用 操作 右 值 。 也 就 是 说 ， 常 星 左 值 引用 既 可 以 操作 左 值 ， 也 可 以 操作 右 值 ， 例 如 :

我 们 知道 ， 右 值 往往 是 没有 名 称 的 ， 因 此 要 使 用 它 只 能 借助 引用 的 方式 。 这 就 产生 一 个 问题 ， 实 际 开发 中 我 们 可 能 需要 对 右 值 进行 修改 (实现 移动 语义 时 就 需要 ) ， 显 然 左 值 引用 的 方式 是 行 不 通 的 。

其 次 ， 常 量 右 值 引用 的 作用 就 是 引用 一 个 不 可 修改 的 右 值 ， 这 项 工作 完全 可 以 交 给 常 星 左 值 引用 完成 。
```

```
move 语 义

move 本 意 为 "移动 '， 但 该 函数 并 不 能 移动 任何 数据 ， 它 的 功能 很 简单 ， 就 是 将 某 个 左 值 混 制 转化 为 右 值 。 基 于 move() 函数 特殊 的 功能 ， 其 常用 于 实现 移动 语义 。move() 函数 的 用 法 也 很 简单 ， 其 语法 格式 如 下 :

move( arg) // 其 中 ，arg 表示 指定 的 左 值 对 象 。 该 函数 会 返回 are 对 象 的 右 值 形式 。
// 程 序 实例
Hinclude <iostream>
using namespace std;
class first {
public:
first() imum(new int(0)) {

cout << “construct!” << endl;

}

/ ASTER

first (first 8d) :num(d.num) {
d.num = NULL;

cout << “first move construct!” << endl;
3
publi

7/ 这 里 应 该 是 private， 使 用 public 是 为 了 更 方便 说 明 问 题
int #num;
Ds
class second [
public:
second() :firQ 0
HR first 类 的 移动 构造 函数 初始 化 fir
second(second && sec) :fir(move(sec.fir)) [

cout << “second move construct” << endl,

}
public: 。 // 这 里 也 应 该 是 private, A public 是 为 了 更 方便 说 明 问 题
first fir;

qh
int minQ {
second oth;
second oth2 = move (oth);
/foout << oth. fir.num << endl; 7/ 程 序 报 运行 时 错误

return 0;
}
fe
程序 运行 结果 ，
construct!

first move construct!

second move construct

ay
```

move(a)可以初步理解为static\_cast<class A&&>(a)

## （9）完美转发

std::forward()

当我们将一个右值引用传入函数时，他在实参中有了命名，所以继续往下传或者调用其他函数时，根据C++ 标准的定义，这个参数变成了一个左值，并不是他原来的类型。那么他永远不会调用接下来函数的右值版本，这可能在一些情况下造成拷贝。

我们需要一种方法能够按照参数原来的类型转发到另一个函数，为了解决这个问题 C++ 11引入了完美转发，根据右值判断的推倒，调用forward 传出的值，若原来是一个右值，那么他转出来就是一个右值，否则为一个左值。

这样的处理就完美的转发了原有参数的左右值属性，不会造成一些不必要的拷贝。代码如下：

```
#include <iostream>

#include <vector>

#include <string>

using namespace std;

int main()

{

string A("abc");

string&& Rval = std::move(A);

string B(Rval); // this is a copy , not move.
cout << A << endl; // output "abc"

string C(std::forward<string>(Rval)); // move.
cout << A << endl; /* output "" */

return @;
```

小测试：

```
template<typename T>
void print(T& t){
cout << “lvalue" << endl;
}
template<typename T>
void print(T&& t){
cout << "rvalue" << endl;

template<typename T>

void TestForward(T && v){
print(v);
print (std: : forward<T>(v));
print(std: :move(v));

int main(){
TestForward(1);
int x = 1;
TestForward(x) ;
TestForward(std: :forward<int>(x));

return 9;
```

结果为![](test_assets/image_483.png)

## （10）无序容器，哈希表

```
用 法 和 功能 同 map 一 模 一 样 ， 区 别 在 于 哈 希 表 的 效率 更 高 。
(1) 无 序 容器 具有 以 下 2 个 特点 :
a 无 序 容器 内 部 存储 的 键 值 对 是 无 序 的 ， 各 键 值 对 的 存储 位 置 取决 于 该 键 值 对 中 的 键 ，
b. 和 关联 式 容器 相 比 ， 无 序 容器 擅长 通过 指定 键 查找 对 应 的 值 (平均 时 间 复杂 度 为 0(1)) ; 但 对 于 使 用 迭代 器 遍历 容器 中 存储 的 元 素 ， 无 序 容 吉 的 执行 效率 则 不 如 关联 式 容器 。
(2) 和 关联 式 容器 一样 ， 无 序 容器 只 是 一 类 容器 的 统称 ， 其 包含 有 4 个 具体 容器 ， 分 别 为 unordered_map、unordered_multimap、unordered_set 以 及 unordered_multiset。 功 能 如 下 表 :
无 序 容器 功能
unordered_ map 存储 键 值 对 <key, value> 类 型 的 元 素 ， 其 中 各 个 键 值 对 键 的 值 不 允许 重复 ， 且 该 容器 中 存储 的 键 值 对 是 无 序 的 。
unordered_multimap ”和 unordered_map 唯一 的 区 别 在 于 ， 该 容器 允许 存储 多 个 键 相同 的 键 值 对 。
unordered_set 不 再 以 键 值 对 的 形式 存储 数据 ， 而 是 直接 存 储 数 据 元 素 本 身 (当然 也 可 以 理解 为 ， 该 容器 存储 的 全 部 都 是 键 key 和 值 value 相等 的 键 值 对 ， 正 因为 它们 相等 ， 因 此 只 存储 value 即 可 ) 。 另 外 ， 该 容器 存储 的 元 素 不 能 重复 ， 且 容器 内 部 存储 的 元 素 也 是 无 序 的 。
unordered_multiset #2 unordered_set 唯一 的 区 别 在 于 ， 该 容器 允许 存储 值 相同 的 元 素 。
```

```
(3) 程序 实例 (LA unordered_map 容器 为 例 )

Hinclude <iostream>
Hinclude <string>
Hinclude <umordered_map>
using namespace std;
int main@
{
// 创 建 并 初始 化 一 个 unordered_map 容器 ， 其 存储 的 “string, string> 类 型 的 键 值 对
std:tunordered_map<std::string, std::string> my_ullap {
【教程 1 “wore. 123. com’},
【教程 2 “wore. 234. com’},
(°BUEES”, “wore. 345. com”) }
// 查 找 指定 键 对 应 的 值 ， 效 率 比 关联 式 容器 高
string str = my_ullapat(“C 语 言 教程 ) ; 这 里 应 是 “教程 1 或 ,教程 2 或 ,教程 3”
cout << "str =” str endl;
// 使 用 选 代 器 遍历 哈 希 容器 ， 效 率 不 如 关联 式 容器

for (auto iter = my_ullap.begin(), iter != my_ullap.end(); ++iter)

{
7/pair 类 型 键 值 对 分 为 2 部 分
cout << iter->first <<” ” << iter->second << endl;
}
return 0;
}
ie

程序 运行 结果 ，
教程 1 wmw. 123. com
教程 2 wmw. 234 com
PASS wow. 345. com

ay
```

## （10）正则

### 三个主要函数

#include<regex>

![](test_assets/image_486.png)

### 正则表达式写法

regex是一个类，函数里匿名对象就好

```
定义 方法 如 下

regex pattern( "规则 ") ;
```

```
{n}
{n}

{n,m}

意义

匹配 行 的 开头
匹配 行 的 结尾

匹配 任意 单个 字符
匹配 [中 的 任意 一 个 字符
设 定 分 组

转 义 字符

匹配 数字 [0-9]

\d BUR

匹配 字母 |a-z]， 数 字 ， 下 划 线
W 取 反

匹配 空格

\s BUR

前 面 的 元 素 重 复 1 次 或 多 次
前 面 的 元 素 重 复 任意 次
前 面 的 元 素 重 复 0 次 或 1 次
前 面 的 元 素 重 复 n 次

前 面 的 元 素 重 复 至 少 n 次

前 面 的 元 素 重复 至 少 n 次 ， 至 多 m 次
逻辑 或
```

^，非

```
^ 的 用 法
例 [^abc] 表 示 除 abc 外 ， 其 他 字符 都 可 以 。

#include<regex>
#include<iostream> GN 选择 Mi
using namespace std;
Sjint main() {
string n= "w’;
bool res = regex_match(n, regex(”[-wel]”))
cout << res << endl;
| return 0;

-口上 性

© oo
```

.，匹配任意字符

```
-的 用 法
这 是 一 个 小 数 点 ， 表 示 除 了 m 和 Y 以 外 的 任何 字符 。

日 #include<regex>
| #include<iostream>
using namespace std;

Flint main() {
string n = “abel”;
bool res = regex_match(n, regex(”....”));
cout << res << endl;
return 0;

CONIA RWMYH

四 个 小 数 点 表示 四 个 任意 字符 ， 所 以 结果 为 1。
```

[]，匹配任意一个

```
0] 的 用 法
例如 [ab 表示 只 要 是 abc 中 的 一 个 就 可 以 。

1 日 #include<regex>

2 | #include<iostream>

3 using namespace std;

4 int mainQ {

5 string n = "Ww";

6 bool res = regex_match(n, regex(”[wel]”));
7 cout << res << endl;

8 return 0;

9 }

结果 为 1， 因 为 w 在 we1 中 。 CSDN
```

{}，匹配前面的表达式

```
妖 的 用 法
例 交 0{n} 表 示 匹 配 前 面 的 表达 式 n 次 。

1 FiFinclude<regex>
| #include<iostream>
using namespace std;

日 int main() {
string n = "66";
bool res = regex_match(n, regex(6{2}”));
cout << res << endl;
return 0;

COIBMH KWH

CSDN
```

```
全 的 用 法
例 %n{a.b} 雪 示 匹 配 前 面 的 表达 式 最 少 a 次 ， 最 多 b 次 。

1 日 #include<regex>
| #include<iostream>
using namespace std;

Elint main() {
string n = "6";
bool res = regex_match(n, regex("6{1, 2}”));
cout << res << endl;
return 0;

COIBRH HWY

}

结果 为 1， 匹 配 1 次 。 CSDN
```

\*的用法

匹配前面的表达式任意次

-，表示范围

```
-的 用 法
例如 [1-9] 代表 从 1 到 9 的 任意 一 个 字符 。

日 #include<regex>
| #include<iostream>
using namespace std;

日 int main() {
string n= "4";
bool res = regex_match(n, regex(”[1-9]”));
cout << res << endl;
return 0;

CONIMRHhRWNHYH

结果 为 1。 CSDN
```

\\d，匹配数字

```
Gostream> mn
using nanespace std:
int main0 {

srving n= “abed
bool ree = repex match (a, reve
cout << see << en

return 0;

“abe\\a"))
```

一个 \ 代表的是字符串转义，正则表达式转义要两个 \ ，如例子匹配数字是[\\d](file:///\\d)

\\D，匹配非数字

```
CoVounsone

#include<regex>
#include<iostream>
using namespace std;
int main()

{

string n = “abc3";
bool res = regex_match(n, regex("abc\\D"
cout << res <« endl;

return 0;

最 后 运行 结果 为 0， 因 为 3 不 是 非 数字 。
```

\\w，匹配大小写字母、数字、下划线

```
\w 用 法
它 代 表 任 意 一 个 大 写 或 小 写字 母 、 数 字 或 下 划 线 。

日 #include<regex>
#include<iostream>
“using namespace std;
日 int main) {
string n

“abcd” ;

cout << res << endl;
return 0;

CHONMR YH RWMH

}

六 段 代码 结果 是 1， 因 为 3 是 数字 。

日 #include<regex>

| #include<iostream>
using namespace std;

Sint main() {
string n = “abc_”

cout << res << endl;
return 0;

COIMBRA RWMH

六 段 代码 的 运行 结果 也 是 1。

bool res = regex_match(n, regex("abc\\w”));

bool res = regex_match(n, regex(“abe\\w”));
```

\\s，匹配空格或tab

```
\s 的 用 法
它 代 表 匹 配 一 个 肉眼 无 法 看 见 的 符号 ， 比 如 空格 或 Tab。

Fitinclude<regex>
| #include<iostream>
using namespace std;

Sint main() {
string n = “abel”;
bool res = regex_match(n, regex(“abc\\s”));
cout << res << endl;
return 0;

CONIMRHRHWMH

}

因为 我 在 abc 后 面 加 了 1， 所 以 结果 为 0。 CSDN
```

|，或

```
| 的 用 法
表示 或 ， 表 示 满 足 任 意 一 个 条 件 即 可

1 Eitinclude<regex>
| #include<iostream>
using namespace std;

Hint main() {
string n = “abl2cd”;
bool res = regex_match(n, regex("abl2cd/ab23er”));
cout << res << endl;
return 0;

CHOIR RwWH

注意 ， 如 果 前 后 都 有 其 他 字符 ， 要 用 小 括号 ( ) 把 | BUORIEE. CSDI
```

## （11）lambda表达式

见基础，函数

## （12）线程类

本来用Linux的<pthread.h>，windows的<windows.h>。C++11提供了语言层面上的多线程，包含在头文件<thread>中。它解决了跨平台的问题，提供了管理线程、保护共享数据、线程间同步操作、原子操作等类。主要有5个头文件，如图：

![https://img-blog.csdnimg.cn/20210428113430200.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1FMZWVscQ==,size_16,color_FFFFFF,t_70#pic_center](test_assets/image_500.png)

### thread

#### thread

主要包括创建和销毁

```
ww IN

IN PP

std: :thread myThread ( thread_fun);
myThread ) ;

std: :thread myThread ( 100)
myThread ) ;

std: :thread (thread_fun,1) 3
```

![](test_assets/image_502.png)

#### this\_thread

4个函数

```
1.5 this thread

this_thread 是 一 它 有 4 个 :
函数 使 用 说 明
get_id std:this_thread::get_id() 获取 线程 id
yield stdthis_thread:-yield() 线程 执行 ， 回 到 就 绪 ;
sleep_for std:this_thread::sleep_for(sta::chrono::seconds(1)) 暂停 1 秒
Sleep_until 如 下 一 分 钟 后 执行 吗 ， 如 下

td: :chrono: :system_clock;
time_t tt m_Clock: :to_time_t(s

struct std::tm * ptm Localtime (att
cout

ptm->tm_min

ptm->tm_sec

this_thread: :sleep_until (system from_time_t (mktime(ptm
```

### mutex

#### mutex

```
mutex 头 文件 主要 声明 了 与 马帮 量 (mutex) 相 关 的 关 。mutex 提 供 了 4 神 瑟 斥 闪 型， 如 下 表 所 不。

类 型 说 明
std::mutex 最 基本 的 Mutex 类 -
std-recursive_mutex 递 月 Mutex 类 。
std-time_mutex 定时 Mutex 类 。
std::recursive_timed_mutex 定时 递 明 Mutex 36,

std:mutex 是 C++11 中 最 基本 的 互 斥 量 ，std--mutex 对 象 提供 了 独占 所 有 权 的 特性 一 一 即 不 支持 递归 地 对 std::mutex 对 象 上 锁 ， 而
std::recursive_lock 则 可 以 递归 地 对 互 斥 量 对 象 上 锁 。
```

```
2.1 lockSunlock

mutex 常 用 操作 |

#include
#include
#include
std: :mutex mtx;
void print_block (int n, char c
mtx.
for
std
mtx.

int main (

thread th1 (print_bl
thread th2 (print

return 9
```

#### lock\_guard（优先用）

```
的 互 斥 锁 的 所 有 权 。 当 控制 d 对 象 的 作用 域 时 ，lock_guard 析 构 并 释 训

#include

std: :mutex g_i_mutex;

1

2

4

5| int gi-0
6

7

8 | void

9

9 const std
11 g_i;
12 std::cout << std: :this_thread ) gi

rd<std: :mutex: i_mutex!

16 | int )

this_thread
```

#### unique\_lock

![](test_assets/image_507.png)

```
#include
#include
#include
struct Box {

explicit Box(int num

int num_things

std: :mutex m;
void Box &from, Box &to
std: :unique_lock<std: :mutex
std: :unique_lock<std: :mutex
std lock1, Lock2
from num
num:
int )
std: :thread ti(transfer, std
std: :thread t2(transfer, std
tl
t2
cout

num_things {num}

int num)

from.m,

to.m,

(accl),
(acc2),

accl

std
std

defer_lock)
defer_lock)

ace2), 1

num_things
num_things
```

### condition\_variable

![](test_assets/image_509.png)

#### wait（搭配unique\_lock）

![](test_assets/image_510.png)

```
#include
#include
#include
#include

std: :mutex mtx;
std: :condition_variable cv;

int cargo = 0;
bool shipment_available() {return cargo!=0;}

void consume (int n) {

for (int i-0; in; ++i) {
std: :unique_lock<std: :mutex> Uck(mtx) ;
cv.wait(1ck, shipment_available) ;
std::cout << cargo << ‘\n';
cargo=0;
+
+
int main ()
{
std: :thread consumer_thread (consume, 10) ;
for (int i-0; i<19; ++i) {
while (shipment_available()) std: :this_thread: :yield();
std: :unique_lock<std: :mutex> Uck(mtx) ;
cargo = i+1;
cv.notify_one();
+
consumer_thread.join();,

return 0;
```

#### wait\_for

```
'5std::condition_variable:.wait() 类 似 ， 不 过 wait_for 可 以 指定 一 个 时 间 段 ， 在 当前 线程 收 到 通知 或 者 指定 的 时 间 rel_time 超时 之 前 ， 该
线程 都 会 处 于 阻塞 状态 。 而 一 旦 超时 或 者 收 到 了 其 他 通知 ，wait_for 返 回 ， 剩 下 的 处 理 步骤 和 wait() 类 似 。

eriod>s rel_time

测 | 条件 ， 只 有 当 pred 条 件 为 false 时 调用 wait(

ENB RA pred true Sz

template <class
```

```
CaAYVAMAWNHE

10

12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30

#include
#include
#include
#include
#include

std: :condition_variable cv;

int value;

void read_value() {

std::cin >> value;
cv.notify_one();

+

int main ()

{

std::cout << “Please, en
std::thread th (read_value);

rinting dots): \n";

std::mutex mtx;
std: :unique Lock<std: :mutex> Ick(mtx) ;
while (cv.wait_for(1ck, std: :chrono: :seconds(1))==std: :cv_status: :timeout) {

std::cout << std::endl;
+
std::cout " << value << '\n';
th. join();
return 0;
```

### 线程池

见vsproject的thread poll
