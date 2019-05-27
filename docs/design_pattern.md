### 前端开发模式
* 单例模式
* 观察者模式
* 命令模式
* 职责链模式

#### 单例模式
单例模式的定义是保证一个类只有一个实例，并且提供一个访问它的全局访问点。有些时候一些对象我们往往只需要一个，比如线程池、全局缓存、浏览器中的window对象等。单例模式的优点是：

> 可以用来划分命名空间，减少全局变量的数量
> 使用单例模式可以使代码组织的更为一致，使代码容易阅读和维护
> 可以被实例化，且实例化一次

要实现一个标准的单例模式并不复杂，无非是用一个变量标识当前是否已经为某个类创建过对象，如果是，则在下一次获取这个类的实例时，直接返回之前创建的对象。下面是单例模式的基本结构：
~~~ 
// 单例模式
var Singleton = function(name){
    this.name = name;
    this.instance = null;
};
Singleton.prototype.getName = function(){
    return this.name;
};
// 获取实例对象
Singleton.getInstance = function(name) {
    if(!this.instance) {
        this.instance = new Singleton(name);
    }
    return this.instance;
};
// 测试单例模式的实例
var a = Singleton.getInstance("aa");
var b = Singleton.getInstance("bb");
~~~ 

实际上因为单例模式是只实例化一次，所以a和b其实是相等的。也即是说下面语句的值为true。
~~~ 
console.log(a===b)
~~~ 

由于单例模式只实例化一次，因此第一次调用，返回的是a实例的对象，继续调用的时候，b的实例也就是a的实例，因此下面打印的都是aa：
~~~ 
console.log(a.getName());// aa

console.log(b.getName());// aa  
~~~ 
