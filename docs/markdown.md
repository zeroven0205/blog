
## fed组件库的规范、规划
- 规范：命名、export、import的方式
- 规划：职能划分 
-  hbh-pc 专用于PC端
-  eslint、ES6的语法，杜绝ES5、ES6共存的方式，抽象的能力，设计模式的问题
-  
-  

hbh-widget



#### Markdown语法
* **这是加粗的文字**
* *这是倾斜的文字*
* ***这是斜体加粗的文字***
* ~~这是加删除线的文字~~
>这是引用的内容
>>这是引用的内容
>>>>>这是引用的内容
---
----
***
*****



#### 标题
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题

#### 斜体和粗体
*斜体*或_斜体_
**粗体**
***加粗斜体***
~~删除线~~

#### 超链接
欢迎来到[梵居闹市](http://blog.leanote.com/freewalk "梵居闹市")
我经常去的几个网站[Google][1]、[Leanote][2]以及[自己的博客][3]
[Leanote 笔记][2]是一个不错的[网站][]。
[1]:http://www.google.com "Google"
[2]:http://www.leanote.com "Leanote"
[3]:http://http://blog.leanote.com/freewalk "梵居闹市"
[网站]:http://http://blog.leanote.com/freewalk

#### 列表
- 无序列表项 一
- 无序列表项 二
- 无序列表项 三
- 使用 *，+，- 表示无序列表
- 


#### 引用
*   阅读的方法:
    > 打开书本。
    > 打开电灯。
> 1.   这是第一行列表项。
> 2.   这是第二行列表项。
> 
> 给出一些例子代码：
> 
>     return shell_exec("echo $input | $markdown_script");

>>> 请问 Markdwon 怎么用？ - 小白
>> 自己看教程！ - 愤青
> 教程在哪？ - 小白

#### 插入图像
美丽花儿：
![美丽花儿][flower]
[flower]:http://ww2.sinaimg.cn/large/56d258bdjw1eugeubg8ujj21kw16odn6.jpg  "美丽花儿"
* * *
使用 Markdown[^1]可以效率的书写文档, 直接转换成 HTML[^2], 你可以使用 Leanote[^Le] 编辑器进行书写。
[^1]:Markdown是一种纯文本标记语言
[^2]:HyperText Markup Language 超文本标记语言
[^Le]:开源笔记平台，支持Markdown和笔记直接发为博文
***
$$\sum_{i=1}^n a_i=0$$
$$f(x_1,x_x,\ldots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2 $$
$$\sum^{j-1}_{k=0}{\widehat{\gamma}_{kj} z_k}$$
*****
flow
st=>start: Start:>https://www.zybuluo.com
io=>inputoutput: verification
op=>operation: Your Operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end
st->io->op->cond
cond(yes)->e
cond(no)->sub->io
- - -
|学号|姓名|分数|
|-|-|-|
|小明|男|75|
|小红|女|79|
|小陆|男|92|
---------------------------------------


```
#include <stdio.h>
int main(void)
{
    printf("Hello world\n");
}
、、、
