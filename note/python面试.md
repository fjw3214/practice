# 测试开发

[toc]

### 自我介绍

* 面试官你好，我是西安邮电大学计算机学院软件工程专业2021届的冯军伟。我在校期间成绩良好，并加入了我校信息中心直属的智邮普创工作室，为数字化校园服务。毕业后曾工作于杭州杏林信息科技有限公司，从事系统部署调试维护等工作，在此期间极大的增强了我对Oracle数据库的熟练度，以及排查问题解决问题的能力。性格特点脾气好，做事认真专注，积极向上。有责任心。。

### 测试知识

#### 黑盒测试

在黑盒测试中主要关注被测软件的功能实现，而不是内部逻辑。在黑盒测试中，被测对象的内部结构，运作情况对测试人员是不可见的，测试人员对被测产品的验证主要是根据其规格，验证其与规格的一致性。在绝大多数没有用户参与的黑盒测试中，最常见的测试有：功能性测试、容量测试、安全性测试、负载测试、恢复性测试、标杆测试、稳定性测试、可靠性测试等

##### 黑盒测试方法

* 等价类划分，边界值测试，因果分析法，错误推测法，判定表法，场景分析法

  划分等价类的标准：

* 1)完备测试、避免冗余;       （2）划分等价类重要的是：集合的划分，划分为互不相交的一组子集，而子集的并是整个集合;    3)并是整个集合：完备性;         4)子集互不相交：保证一种形式的无冗余性;        5)同一类中标识（选择）一个测试用例，同一等价类中，往往处理相同，相同处理映射到"相同的执行路径

### python

###### 多继承

多继承是一个子类可以有多个直接父类时，该子类会继承得到所有父类的方法，但是如果其中有多个父类包含同名方法，此时排在前面的父类中的方法会“遮蔽”后面父类中的方法。

在 Python 中有一个列表叫 MRO，它的全称是 Method Resolution Order，即方法解析顺序列表。对于我们定义的每个类，它都会根据一种特定的算法(C3线性算法，拓扑排序的算法）来得到一个列表，这个列表代表了类继承的顺序。我们可以通过 mro() 方法来查看某个类的 MRO 列表。

Python2.3之前是基于深度优先的算法，之后的是采用C3算法。C3算法的本质就是Merge(融合），不断地把`mro`()函数返回的序列进行Merge，规则如下：

- 如果第一个序列的第一个元素，是后续序列的第一个元素，或者不在后续序列中再次出现，则将这个元素合并到最终的方法解析顺序序列中，并从当前操作的全部序列中删除。
- 如果不符合，则跳过此元素，查找下一个列表的第一个元素，重复1的判断规则

**为什么会有这种算法？**

Python 中，是多继承的，如果父类中存在同名函数的时候，是会产生二义性的，MRO 就是用来处理这种问题的。

MRO原则：

1. 子类一定在父类前面
2. 如果存在多个父类，它会根据 MRO 列表顺序来执行
3. 如果多个父类存在相同方法，会根据 MRO 列表选择第一个符合的类

###### 如何实现多线程

如何在Python中实现多线程？

Python有一个多线程库，但是用多线程来加速代码的效果并不是那么的好，

Python有一个名为Global Interpreter Lock（GIL）的结构。GIL确保每次只能执行一个“线程”。一个线程获取GIL执行相关操作，然后将GIL传递到下一个线程。

虽然看起来程序被多线程并行执行，但它们实际上只是轮流使用相同的CPU核心。

###### 迭代器和生成器

迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一 个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

生成器本质上就是一个函数，它记住了上一次返回时在函数体中的位置。
对生成器函数的第二次（或第n次）调用，跳转到函数上一次挂起的位置。
而且记录了程序执行的上下文。

可迭代对象：

一类是集合数据类型，如 list 、 tuple 、 dict 、 set 、 str 等；
一类是 generator ，包括生成器和带 yield 的generator function。

isinstance() 判断一个对象是否是 ***\*Iterable\**** 对象：

（3）区别：
①生成器是生成元素的，迭代器是访问集合元素的一中方式
②迭代输出生成器的内容
③迭代器是一种支持next()操作的对象
④迭代器（iterator）：其中iterator对象表示的是一个数据流，可以把它看做一个有序序列，但我们不能提前知道序列的长度，只有通过nex()函数实现需要计算的下一个数据。可以看做生成器的一个子集。

###### `*args和**args`

> *args是发送一个非键值类型的可变参数列表给函数
>
> **kargs是发送多个键值对作为参数传递给函数，也叫字典参数

###### 内存管理

* Python的内存管理机制： 引用计数，垃圾回收，内存池机制

python的变量其实是C语言的指针一样，指向数据存在的内存区，变量存放的地方和数据存放的地方是不同的。

Python缓存了[-5, 256]的整数和短字符串，因此每个对象在内存中只存有一份，引用所指对象就是相同的，即使使用赋值语句，也只是创造新的引用，而不是对象本身；Python没有缓存长字符串、列表及其他对象，可以由多个相同的对象，可以使用赋值语句创建出新的对象。

对于任意对象，系统会维护一个计数器时刻记录该对象被引用的次数。每次有新的对象引用该对象，其计数器加1，每次使用del释放一个引用，其计数器减1，如果垃圾回收机制发现某对象的引用次数为0，则将其删除。

* 垃圾回收机制：

  * 引用计数
  * 标记清除

  > 标记清除（Mark—Sweep）』算法是一种基于追踪回收（tracing GC）技术实现的垃圾回收算法。它分为两个阶段：第一阶段是标记阶段，GC会把所有的『活动对象』打上标记，第二阶段是把那些没有标记的对象『非活动对象』进行回收。那么GC又是如何判断哪些是活动对象哪些是非活动对象的呢？
  >
  > 对象之间通过引用（指针）连在一起，构成一个有向图，对象构成这个有向图的节点，而引用关系构成这个有向图的边。从根对象（root object）出发，沿着有向边遍历对象，可达的（reachable）对象标记为活动对象，不可达的对象就是要被清除的非活动对象。根对象就是全局变量、调用栈、寄存器。
  >
  > 标记清除算法作为Python的辅助垃圾收集技术主要处理的是一些容器对象，比如list、dict、tuple，instance等，因为对于字符串、数值对象是不可能造成循环引用问题。Python使用一个双向链表将这些容器对象组织起来。不过，这种简单粗暴的标记清除算法也有明显的缺点：清除非活动的对象前它必须顺序扫描整个堆内存，哪怕只剩下小部分活动对象也要扫描所有对象。

  * 分代回收

  > 分配内存
  > -> 发现超过阈值了
  > -> 触发垃圾回收
  > -> 将所有可收集对象链表放到一起
  > -> 遍历, 计算有效引用计数
  > -> 分成 有效引用计数=0 和 有效引用计数 > 0 两个集合
  > -> 大于0的, 放入到更老一代
  > -> =0的, 执行回收
  > -> 回收遍历容器内的各个元素, 减掉对应元素引用计数(破掉循环引用)
  > -> 执行-1的逻辑, 若发现对象引用计数=0, 触发内存回收
  > -> python底层内存管理机制回收内存

* 内存池机制

Python中有分为大内存和小内存：（256K为界限分大小内存）

1、大内存使用malloc进行分配

2、小内存使用内存池进行分配

3、Python的内存池(金字塔)

　　第3层：最上层，用户对Python对象的直接操作

　　第1层和第2层：内存池，有Python的接口函数PyMem_Malloc实现-----若请求分配的内存在1~256字节之间就使用内存池管理系统进行分配，调用malloc函数分配内存，但是每次只会分配一块大小为256K的大块内存，不会调用free函数释放内存，将该内存块留在内存池中以便下次使用。

　　第0层：大内存-----若请求分配的内存大于256K，malloc函数分配内存，free函数释放内存。

###### 深拷贝和浅拷贝

在创建新实例类型时使用浅拷贝，并保留在新实例中复制的值。浅拷贝用于复制引用指针，就像复制值一样。这些引用指向原始对象，并且在类的任何成员中所做的更改也将影响它的原始副本。浅拷贝允许更快地执行程序，它取决于所使用的数据的大小。

深拷贝用于存储已复制的值。深拷贝不会将引用指针复制到对象。它引用一个对象，并存储一些其他对象指向的新对象。原始副本中所做的更改不会影响使用该对象的任何其他副本。由于为每个被调用的对象创建了某些副本，因此深拷贝会使程序的执行速度变慢。


###### 闭包

* python中的闭包需要满足三个条件：

1. 必须是一个嵌套的函数。
2. 闭包必须返回嵌套函数。
3. 嵌套函数必须引用一个外部的非全局的局部自由变量

> python3中，可以用nonlocal 关键字声明 一个变量， 表示这个变量不是局部变量空间的变量，需要向上一层变量空间找这个变量。
>
> 在python2中，没有nonlocal这个关键字，可以把闭包变量改成可变类型数据进行修改，比如列表。

* 闭包的用处：

1. 可做装饰器使用。比如计算某个函数运行时间
2. 面向对象编程，可以使用闭包实现实现面向对象
3. 闭包就是父函数给子函数传值，解决作用域问题
4. 防止函数内部的变量执行完城后，被销毁，使其一直保存在内存中。

优点：

* python闭包的优点：

  * 避免使用全局变量
  * 可以提供部分数据的隐藏
  * 可以提供更优雅的面向对象实现

  ###### 包和模块和库

  ```css
  用来包裹一个或者多个模块（py文件）的目录（文件夹）
  __init__.py 用来申明该文件夹是一个包
  __init__.py文件有个__all__属性，用来描述该包下的所有py文件
  只有被它描述的文件，才可以使用from xxx import *
  ```

  ###### 什么是模块（module）？

  

  ```css
      一个  .py文件就是一个模块
  包含大量类或者方法的py文件，模块一般是包含包下面的
  ```

  

  库是具有相关功能模块的集合。

### 数据库知识

###### 事务

所谓事务，事务就是针对数据库的一组操作，它可以由一条或多条SQL语句组成，同一个
事务的操作具备同步的特点，如果其中有一条语句不能执行的话，那么所有的语句都不
会执行，也就是说，事务中的语句要么都执行，要么都不执行。

- 在 MySQL 中只有使用了 Innodb 数据库引擎的数据库或表才支持事务。
- 事务处理可以用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行。
- 事务用来管理 insert,update,delete 语句

**四大特性：**

原子性：一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。

一致性：在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。

隔离性：数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。

持久性：事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。

**隔离级别**

MySQL定义了四种隔离级别，包括一些具体规则，用于限定事务内外哪些改变是可见的，哪些改变是不可见的。低级别的隔离一般支持更高的并发处理，并且拥有更低的系统开销。

1. REPEATABLE READ `Repeatable Read` 可重复读

MySQL数据库默认的隔离级别。该级别解决了READ UNCOMMITTED隔离级别导致的问题。它保证同一事务的多个实例在并发读取事务时，会“看到同样的”数据行。不过，这会导致另外一个棘手问题“幻读”。InnoDB和Falcon存储引擎通过多版本并发控制机制解决了幻读问题。

2. READ COMMITTED `Read Committed` 读取提交内容

大多数数据库系统的默认隔离级别（但是不是MySQL的默认隔离级别），满足了隔离的早先简单定义：一个事务开始时，只能“看见”已经提交事务所做的改变，一个事务从开始到提交前，所做的任何数据改变都是不可见的，除非已经提交。这种隔离级别也支持所谓的“不可重复读”。这意味着用户运行同一个语句两次，看到的结果是不同的。

3. READ UNCOMMITTED `Read UnCommitted` 读取未提交内容

在这个隔离级别，所有事务都可以“看到”未提交事务的执行结果。在这种级别上，可能会产生很多问题，除非用户真的知道自己在做什么，并有很好的理由选择这样做。本隔离级别很少用于实际应用，因为它的性能也不必其他性能好多少，而别的级别还有其他更多的优点。读取未提交数据，也被称为“脏读”

4. SERIALIZABLE `Serializable` 可串行化

该级别是最高级别的隔离级。它通过强制事务排序，使之不可能相互冲突，从而解决幻读问题。简而言之，SERIALIZABLE是在每个读的数据行上加锁。在这个级别，可能导致大量的超时`Timeout`和锁竞争`Lock Contention`现象，实际应用中很少使用到这个级别，但如果用户的应用为了数据的稳定性，需要强制减少并发的话，也可以选择这种隔离级

下面的表格总结了各种隔离级别和各自的缺点

| 隔离级别         | 脏读可能性 | 不可重复读可能性 | 幻读可能性 | 加锁读 |
| :--------------- | :--------: | :--------------: | :--------: | :----: |
| READ UNCOMMITTED |     是     |        是        |     是     |   否   |
| READ COMMITTED   |     否     |        是        |     是     |   否   |
| REPEATABLE READ  |     否     |        否        |     是     |   否   |
| SERIALIZABLE     |     否     |        否        |     否     |   是   |

修改隔离级别的方法

全局修改

全局修改需要修改MySql的全局文件mysql.ini，修改内容如下

```
1 #可选参数有：READ-UNCOMMITTED, READ-COMMITTED, REPEATABLE-READ, SERIALIZABLE.
2 [mysqld]
3 transaction-isolation = REPEATABLE-READ
```

语句修改

在命令行模式下连上MySql后，可以使用下列语句查看MySql当前隔离级别

```ruby
mysql> select @@tx_isolation;
+-----------------+
| @@tx_isolation  |
+-----------------+
| REPEATABLE-READ |
+-----------------+

1 row in set (0.00 sec)
```

可以使用下面的命令修改当前会话Session的隔离级

```mysql
mysql> set session transaction isolation level read committed;
```



###### 增删改查语句大全

```mysql
 mysql增删改查语句大全

#登录数据库
mysql -hlocalhost -uroot -p;
#修改密码
mysqladmin -uroot -pold password new;


#显示数据库
show databases;
#显示数据表
show tables;
#选择数据库
use examples;
#创建数据库并设置编码utf-8 多语言
create database `examples` default character set utf8 collate utf8_general_ci;
#删除数据库
drop database examples;
#创建表
create table test(
    id int(10) unsigned zerofill not null auto_increment,
    email varchar(40) not null,
    ip varchar(15) not null,
    state int(10) not null default '-1',
primary key (id)
)engine=InnoDB;
#显示表结构
describe 
#删除表
drop table test；
#重命名表
alter table test_old rename test_new;
#添加列
alter table test add cn int(4) not null;
#修改列
alter table test change id id1 varchar(10) not null;
#删除列 
alter table test drop cn;
#创建索引
alter table test add index (cn,id);
#删除索引
alter table test drop index cn
#插入数据
insert into test (id,email,ip,state) values(2,'qq@qq.com','127.0.0.1','0');
#删除数据 
delete from test where id = 1;
#修改数据
update test set id='1',email='q@qq.com' where id=1;
#查数据
select * from test;  #取所有数据
select * from test limit 0,2;  #取前两条数据 
select * from test email like '%qq%' #查含有qq字符 _表示一个 %表示多个
select * from test order by id asc;#降序desc
select * from test id not in('2','3');#id不含2,3或者去掉not表示含有
select * from test timer between 1 and 10;#数据在1,10之间

#---------------------------表连接知识------------------------------
#等值连接又叫内链接 inner join 只返回两个表中连接字段相等的行
select * from A inner join B on A.id = B.id; #写法1
select * from A,B where A.id = B.id; #写法2
select a.id,a.title from A a inner join B b on a.id=b.id and a.id=1;#写法3 表的临时名称
select a.id as ID,a.title as 标题 from A inner join B on A.id=B.id;#添加as字句

#左连接又叫外连接 left join 返回左表中所有记录和右表中连接字段相等的记录
select * from A left join B on A.id = B.id;

select * from A left join (B,C,D) on (B.i1=A.i1 and C.i2=A.i2 and D.i3 = A.i3);#复杂连接

#右连接又叫外连接 right join 返回右表中所有记录和左表中连接字段相等的记录
select * from A right join B on A.id = B.id;

#完整外部链接 full join 返回左右表中所有数据
select * from A full join B on A.id = B.id;

#交叉连接 没有where字句 返回卡迪尔积
select * from A cross join B;
-------------------------表连接结束------------------------------------------------------------
-----------------索引创建------------------------------------------------
show index from A #查看索引
alter table A add primary key(id) #主键索引
alter table A add unique(name) #唯一索引
alter table A add index name(name) #普通索引
alter table A add fulltext(name) #全文索引
alter table A add index name(id,name) #多列索引

#常用函数
abs(-1)#绝对值
pi()#pi值
sqrt(2)#平方根
mod(-5,3)#取余-2
ceil(10.6)#进位+1 结果11 ceil(10.0)结果10
floor(10.6)#取整 10
round(2.5)#四舍五入到整数 结果3
round(2.5,2)#保留两位小数 结果2.50
truncate(2.5234,3)#取小数后3位不四舍五入 2.523
sign(-2);#符号函数 返回-1 0还是0 正数返回1
pow(2,3),exp(2);#2的3次幂 或e的2次幂
log(2),log10(2);#求对数
radians(180),degrees(0.618);#角度弧度转换
sin(0.5),asin(0.5)#正弦和反正弦 类似cos acos tan atan
length('hi')#计算字符长度
concat('1',1,'hi')#合并字符串
insert('12345',1,0,'7890');#从开头第1个字符开始到0个结束，替换成后边字符串，0表示在最前边插入
ucase('a'),lcase('A')#转成大写和小写
left('abcd',2),right('abcd',2);#返回前两个字符和后两个字符
ltrim('  0  '),rtrim(' 0 '),trim('  0  ')#删除空格
replace('1234567890','345678','0');#替换输出12090
substring('12345',1,2)#取字符 输出12 1是位置 2是长度
instr('1234','234');#取得234位置是2
reverse('1234');#反序输出4321
current()#返回日期
curtime()#返回时间
now()#返回日期时间
month(now())#当前月份 monthname 英文月份
dayname(now())#星期英文 dayofweek()1是星期天 weekday()1是星期二
week(now())#本年第多少周
dayofyear(now()),dayofmonth(now())#今天是本年第多少天 今天是本月第多少天
year(now()),month(now()),day(now()),hour(now()),minute(now()),second(now())#返回年月日 时分秒
time_to_sec(now()),sec_to_time(3600*8);#转换时间为秒和还原
version()#mysql版本
database()#当前连接的数据库 没有为null
user()#获取用户名
md5('a')#加密字符串
ascii('a')#ascii值97
bin(100),hex(100),oct(100)#返回二进制 十六进制 八进制
conv(10001,2,8);#各种进制相互转换
rand()#生成0到1之间随机数
sleep(0.02)#暂停秒数
---------------------------------

    1. MySQL 为日期增加一个时间间隔：date_add()

    set @dt = now();

    select date_add(@dt, interval 1 day);   - 加1天

    select date_add(@dt, interval 1 hour);   -加1小时

    select date_add(@dt, interval 1 minute);    - 加1分钟

    select date_add(@dt, interval 1 second); -加1秒

    select date_add(@dt, interval 1 microsecond);-加1毫秒

    select date_add(@dt, interval 1 week);-加1周

    select date_add(@dt, interval 1 month);-加1月

    select date_add(@dt, interval 1 quarter);-加1季

    select date_add(@dt, interval 1 year);-加1年

    MySQL adddate(), addtime()函数，可以用date_add() 来替代。下面是date_add() 实现addtime() 功能示例：

    mysql> set @dt = '2009-09-09 12:12:33';

    mysql>

    mysql> select date_add(@dt, interval '01:15:30' hour_second);-加上1小时15分30秒

     date_add(@dt, interval '01:15:30' hour_second)

     

    结果:2009-09-09 13:28:03

     

    mysql> select date_add(@dt, interval '1 01:15:30' day_second);-加1天1小时15分30秒

     date_add(@dt, interval '1 01:15:30' day_second)

     2008-08-10 13:28:03

    date_add() 函数，分别为@dt 增加了“1小时15分30秒” 和 “1天1小时15分30秒”

    2. MySQL 为日期减去一个时间间隔：date_sub()

    mysql> select date_sub('1998-01-01 00:00:00', interval '1 1:1:1' day_second);

     date_sub('1998-01-01 00:00:00', interval '1 1:1:1' day_second)

     www.2cto.com

    MySQL date_sub() 日期时间函数 和date_add() 用法一致，不再赘述。另外，MySQL 中还有两个函数subdate(), subtime()，建议，用date_sub() 来替代。

    3. MySQL 另类日期函数：period_add(P,N), period_diff(P1,P2)

    函数参数“P” 的格式为“YYYYMM” 或者 “YYMM”，第二个参数“N” 表示增加或减去N month（月）。

    MySQL period_add(P,N)：日期加/减去N月。

    mysql> select period_add(200808,2), period_add(20080808,-2)

    | period_add(200808,2) | period_add(20080808,-2) |

    结果|               200810 |                20080806 |

    MySQL period_diff(P1,P2)：日期P1-P2，返回N 个月。

    mysql> select period_diff(200808, 200801);

     period_diff(200808, 200801)

      结果:7

     MySQL 中，这两个日期函数，一般情况下很少用到。

    4. MySQL 日期、时间相减函数：datediff(date1,date2), timediff(time1,time2)

    MySQL datediff(date1,date2)：两个日期相减date1 date2，返回天数。网站制作学习网整理

    select datediff('2008-08-08', '2008-08-01'); - 7

    select datediff('2008-08-01', '2008-08-08'); -7

    MySQL timediff(time1,time2)：两个日期相减time1 time2，返回time 差值。

    select timediff('2008-08-08 08:08:08', '2008-08-08 00:00:00');- 08:08:08

    select timediff('08:08:08', '00:00:00');                      - 08:08:08

    注意：timediff(time1,time2) 函数的两个参数类型必须相同。

---------------------------------
数据库优化
1.开启缓存，尽量使用php函数而不是mysql
2. explain select 语句可以知道性能
3.一行数据使用 limit 1；
4.为搜索字段重建索引 比如关键字 标签
5.表连接join保证字段类型相同并且有其索引
6.随机查询使用php $r = mysql_query("SELECT count(*) FROM user");
                    $d = mysql_fetch_row($r);
                    $rand = mt_rand(0,$d[0] - 1);
                    $r = mysql_query("SELECT username FROM user LIMIT $rand, 1");
7.避免使用select * 应该使用具体字段
8.每张表都是用id主键，并且是unsigned int
9.对于取值有限而固定使用enum类型，如性别 国家 名族 部门 状态
10.尽可能使用not null ip存储使用int(4),使用ip 转化函数ip2long()相互long2ip()
11.delete和insert语句会锁表，所以可以采用分拆语句操作
while(1){操作语句;usleep(2000);}
12.选择正确的存储引擎；MyISAM适合大量查询 写操作多用InnoDB支持事务

#存储过程
#存储程序
delimiter #定义存储程序
create procedure getversion(out params varchar(20)) #params是传出参数 in传进 out传出 inout传回
begin
select version() into params; #版本信息赋值params
end
call getversion(@a); #调用存储过程
select @a;
delimiter #定义存储函数
create function display(w varchar(20)) returns varchar(20)
begin
return concat('hello',w);
end
select display('world');

drop procedure if exists spName; #删除一个存储过程
alter function spName [];#修改一个存储过程
show create procedure spName;#显示存储过程信息
declare varName type default value;#声明局部变量
#if语句
if 条件 then 语句
elseif 条件 then 语句
else 语句
end if
#case语句
case 条件
when 条件 then 语句
when 条件 then 语句
else 语句
end case
#loop语句
fn:loop
语句
end loop fn;
leave fn #退出循环
#while语句
fn：while 条件 do
语句
end while fn


#mysql使用帮助资料
? contents; #列出帮助类型
? data types;#列出数据类型
？ int;#列出具体类型
? show;#show语句
? create table;#
#常见表的比较
                    Myisam   BDB    Memory    InnoDB    Archive
存储限制        no           no      yes                64T        no
事物安全                      支持                         支持                         
锁机制         表锁           页锁    表锁             行锁          行锁
全文索引       支持
外键支持                                                        支持
myisam  frm存储表定义 MYD存储数据 MYI存储索引
InnoDB 用于事务处理
char 和 varchar保存和索引都不相同
浮点数float(10,2) 定点数decimal(10,2)
长度一定下，浮点数表示更大数据范围，缺点是引起精度丢失，货币等使用定点数存储
        索引适合于where字句或者连接字句列
        对于唯一值使用唯一索引

添加新用户 grant select,insert,update,delete on *.* to Yoby@localhost identified by 'mysql'; 
#           *.* 数据库名.表名，限制登录某一个数据库 test.*                           localhost是本地主机 网络可以使用 '%'代替所有主机        'mysql'是密码 Yoby是用户名  所有权限可以用 all代替
查看用户权限 show grants for 'root'@'localhost';
移除权限  revoke all on *.* from root@localhost;
group by id 分组
having 限制字句
select1 union select2 联合查询有重复去掉保留一行
select2 union all select2 所有行合并到结果集中去

--------------------------------------------------------------------

修改MYSQL参数
show variables like '%Func%';
set global log_bin_trust_function_creators=1;
show variables like '%Func%';

实用的insert select语句：

INSERT INTO KM_MEMBER_RELA_FULLCUT (
	SELECT
		a.MB_ID,
		b.MPFC_ID,
		1
	FROM
		KM_MEMBER a,
		KM_MEMBER_PREF_FULLCUT b
	WHERE
		b.MPFC_STATUS = 0
	AND NOT EXISTS (
		SELECT
			1
		FROM
			KM_MEMBER_RELA_FULLCUT
		WHERE
			MB_ID = a.MB_ID
		AND MPFC_ID = b.MPFC_ID
	)

)
```





### 算法知识

### 网络知识

##### 从输入url到页面加载

* 输入URL（协议名，域名。端口号（隐藏））
* 判断浏览器缓存是否过期
* DNS域名解析：首先浏览器先检查本地hosts文件是否有这个网址映射关系，如果有就调用这个IP地址映射，完成域名解析。如果没找到则会查找本地DNS解析器缓存，如果找到则返回。如果还是没有找到则会查找本地DNS服务器，如果找到则返回。否则递归或迭代访问顶级域服务器，根服务器
* TCP连接
* HTTP请求
* 处理请求并返回HTTP响应
* 页面渲染
* 关闭TCP连接

##### tcp和udp的区别
TCP面向连接（如打电话要先拨号建立连接）；UDP是无连接的，即发送数据之前不需要建立连接

TCP要求的系统资源较多，UDP较少

TCP提供可靠的服务。也就是说，通过TCP连接传送的数据，无差错，不丢失，不重复，且按序到达；UDP尽最大努力交付，即不保证可靠交付

TCP面向字节流，实际上是TCP把数据看成一连串无结构的字节流；UDP是面向报文的UDP没有拥塞控制，因此网络出现拥塞不会使源主机的发送速率降低（对实时应用很有用，如IP电话，实时视频会议等）

每一条TCP连接只能是点到点的；UDP支持一对一，一对多，多对一和多对多的交互通信

TCP首部开销20字节；UDP的首部开销小，只有8个字节

TCP的逻辑通信信道是全双工的可靠信道；UDP则是不可靠信道
