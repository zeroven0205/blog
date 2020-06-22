### 初始化一个ts项目
* 初始化package.json ‘npm init -y’
* 如果出现 ‘command not found: tsc’，则表示没有全局安装或者全局安装了没有
* 全局安装typescript ‘npm install typescript -g’，‘tsc --version’检查版本
* 执行‘tsc --init’初始化 created a tsconfig.json file.
* 编译ts文件：命令行执行tsc ts文件名
* ‘mkdir src’
* ‘touch main.ts’

#### TypeScript数据类型
数据类型|书写格式|数据说明
---|:--:|---:
undefined |   let a: undefined = undefined | 默认可以赋值给任何类型，strictNullChecks标记除外，只能赋值给自身或者void
null |    let b: null = null  | 默认可以赋值给任何类型，strictNullChecks标记，除外，只能赋值给自身或者void
string |  let c: string = '123' | 只能赋值字符串类型
number |  let d: number = 123 | 只能赋值数字类型
boolean | let e: boolean = true | 只能赋值布尔类型
Array |   let f: number[] = [1,2] let f: Array = [1,2 | 根据数组的数据类型，数组里面的数据只能是对应的类型，如：number，则数组里面只能是数字，不能有字符串
Tuple |   let g: [string, number] = ['1', 2]  | 元祖类型用来声明一个已知数量和数据类型的数组，不必统一，但顺序类型必须一致
enum |    enum color {red, green, blue} | 使用枚举类型可以为一组数值赋予友好的名字
any | let h: any = 1 | any类型是十分有用的，可以让你操作任意类型
void |    let void = undefined | void类型像是与any类型相反，它表示没有任何类型，只能为它赋予undefined和null
Object |  let Object = {a: 1} | 赋值除了基础类型之外的一些复合数据，如对象，函数

> 在TypeScrip中有几种特殊的Number类型 我们需要额外注意一下
*NaN：它是Not a Number 的简写，意思就是不是一个数值。如果一个计算结果或者函数的返回值本应该是数值，但是由于种种原因，他不是数字。出现这种状况不会报错，而是把它的结果看成了NaN。（这就好比我们去泰国外，找了一个大长腿、瓜子脸、水蛇腰的女神。房也开好了，澡也洗完了，发现跟我们的性别统一，我们只能吃个哑巴亏，你绝不会声张）
*Infinity :正无穷大
*-Infinity：负无穷大

2、类型断言
类型断言好比其它语言里的类型转换，但是不进行特殊的数据检查和解构。

1.标准
let someValue: any = "this is a string";
let strLength: number = (<string>someValue).length;
2.简介
let someValue: any = "this is a string";
let strLength: number = (someValue as string).length;