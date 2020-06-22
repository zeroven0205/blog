## 闭包项目实战应用
这是项目中味了保证JS的性能（堆栈内存的性能优化），应该尽可能的减少必报的使用（不销毁的堆栈内存耗性能）

### 闭包具有保护作用：保护私有变量不受外界的干扰
> 在项目中，团队协作开发时候，尽可能的减少全局变量的使用，以防止相互之间的冲突（全局变量污染），要把各自的代码封装在一个闭包中，让全局变量转化为私有变量；

```
(function () {
	var n =1;
	function fn() {

	}
	// ...
})();
```
> 封装类库插件时候，也要把自己的程序存放到闭包中保护起来，防止和用户的程序冲突，但需要暴露方法，该如何处理？
#### 常用的处理方式：
1、jQuery的方式：把需要暴露的方法抛到全局

```
(function () {
	function jQuery() {
		//...
	}
	//...
	// 把需要公外面使用的方法，通过给WIN设置属性的方式暴露出去
	window.jQuery = window.$ = jQuery;
})();
jQuery();
$();
```
2、Zepto方式：给予RETURN把需要供外部使用的方法暴露出来(单例模式)
```
var Zepto = (function () {
	// ...
	return {
		xxx: function () {

		},
		yyy: function () {

		}
	}
})();
Zepto.xxx();
```

### 闭包具有保存作用：形成不销毁的栈内存，把一些值保存下来，方便后面的调取使用
```
var oTab = document.getElementById('tab'),
	tabList = oTab.getElementBytagName('li'),
	divList = oTab.getElementBytagName('div');
function changeTab(curIndex) {
	for (var i=0; i < tabList.length; i++) {
		tabList[i].className = divList[i].className = '';
	}
	// curIndex:记录的是当前点击LI的索引
	tabList[curIndex].className = 'active';
	divList[curIndex].className = 'active';
}

// changeTab(x);
// tab的事件点击绑定，what's wrong! Why?
for (var i=0; i < tabList.length; i++) {
	tabList[i].onclick = function () {
		changeTab(i);
		// =>执行方法，形成一个私有的栈内存，遇到变量I，I不是私有变量，向上一级作用域查找（上级作用域WINDOW）
		// =>当我们点击时候，外层循环已经结束（能点击时，页面加载完成——预示着页面内的JS代码已经执行完毕，也就是FOR循环已经执行结束），外层循环结束时全局下的I等于LI的总长度等于3
	}
}
```
所有的事件绑定都是异步编程

