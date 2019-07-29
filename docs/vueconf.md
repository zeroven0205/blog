### [尤雨溪](https://github.com/yyx990803)
* CromeDevTools
* state of chiana
* 蒋豪群（@sodatea）cli
*
#### Vue 3.0进展
* 设计目标
* 更快：最小化操作
Object.defineProperty -> Proxy 对象结构的改变
virtual DOM ———— 抽象层：核心价值，纯JS描述界面渲染成什么样的表达力，代价是几乎整个都要重新创建，每个组件内部便利整个数
JSX，时间分片
SVELTE：极致的编译路线，最大的限制，只能用模版；放弃virtual DOM

为什么不能抛弃Virtual DOM
Vue所特有的：
动静结合
Block tree ===“区块树”
更新性能由与模版整体大小相关提升为与动态内容的数量相关
benchmark


TypeScript
Class API： CANCELED  Web UI层面几乎用不上CLASS的最大优势继承，更多的是聚合

Function-based API
对比CLASS API
> 
> 更友好的逻辑复用（eg：鼠标位置侦听）
> tree shaking更友好
> 代码更容易压缩

Vue尺寸包动态依赖于所使用的内容
Mixins：当大量使用时候
高阶组件：大量使用时候 props命名空间...
作用域插槽 v-slot：
没有命名空间冲突；数据来源清晰；但额外的组件实例性能消耗
With new API

value mapper

### 吴俊杰 ———— 汇丰 Jay Lu 
https://github.com/jaylu
Vue + Jest
Vue.js单元测试之旅
E2E Tests
Snapshot Tests
Unit Tests
@vue/test-utils { shallowMount }

* [vueconf2019-unit-test](https://github.com/jaylu/vueconf2019-unit-test)
从零开始写一个单元测试：

如何合理的设计一个组件
** 参考资料

### 韩东老师 使用Vue实现0代码交互 声明式编程的牛逼地方
Vue声明式编程的几个案例
基本的双向绑定
components、data、template、{{}}、v-model ———— 声明式
method、on:event ———— 命令式
零命令式的编码
双向绑定，多个输入修改同一个data时候的数据同步性便利
eg：
1、调色器R、G、B  无JS的逻辑
2、随时间变化的色块。hsl($(Math.floor(t/10)x360))
3、视差滚动 slot 插槽
4、SVG编辑器：
pointer-input 手势的基本实现
dragable 容器整个拖动
5、webgl绘制流动的效果————输出
webgl-render：attribute、uniform1l
可以组合任意的输入和输出
更多的构想(Vue组件的一些畅想)：
Device orientation
Device motion
Vibration 震动
Data Fetcher 键鼠、ajax异步请求等
... ... 

React社区 版主React China老师
composer:respo-mvc.org
fetch ==>  前端实现

### [蒋豪群](https://github.com/sodatea)

Vue loader
In-DOM Template
MarkupLanguage
Hyper Script
预编译（使用Vue loader）
自己动手
@vue/component-compiler-utils
JSX -- Directives & Modifiers
Template Strings
vue-html
类型安全 Vue TypeScript
Vue 2。vue-property
Decorators的问题:
Stage2标准，未来变动；TypeScript的实现已经与最新的标准脱节很久；Babel的实现与TypeScript的是实现

使用TypeScript：组件库中推荐；特别复杂的表达式等
webcomponent库
cli基于webpack，

### 袁源 百度 codepen.io 二维码
Vue 开发Echarts踩坑指南
FPS meter
动画分辨率，视网膜屏 10==> 13/14
cavas动画优化：动与静的内容分层，zlevel ==> 20
Echarts的实力instance放在了data中
实时更新，setoption
内存和崩溃的问题：
Memory。Allocation instument
Distance 为1时不释放；context
setTimeout 0的方式来处理特别耗资源的
vue-echarts 

### 天翔 Skyline 快手架构师 快手游戏直播
小程序的定位————提升开发效率，再影响外部
一个月搭建起来快手小程序
探索Web编程的另一种形态
vue-mark-display 

入口劫持 - Webview
入口劫持 - JSCore

Methods劫持 - Webview

Vue 源码
JS组件：
原生组件
小程序比较Web的优势：转场、loading动画
Web Worker！ 线程隔离，有限的API调用
Vue.js 数据驱动、组件化
Web中可否引入Virtual DOM？

微前端：
以前iframe
现在：可以考虑使用web worker（可以做业务隔离）

Hybird + 极限下发
提升开发效率，强化Webview的能力

快应用与小程序
“标准如何制定” 快应用————手机厂商

跨线程的数据通信 == 性能

### 张文韬 百度前端技术部 
H5的业务需要做到 小程序中去
一套代码，多端使用
@allen-zh

小程序与H5端同构开发的需求 Mars


### [真山](https://github.com/ulivz) vuePress 1.x
vicbergquist
vuesax
静态网站生成器
在markdown中使用Vue
plugins-pwa：Service-Worker
plugins-search：如何实现开箱即用的搜索？
plugins-blog 让开发博客主题更简单
vuePress-plugins-yuque 创造了纯动态数据源的可能性
Page Management
如何写一个VuePress插件
Front Matter



### [](https://github.com/xxx) Dcloud 崔红保
Vue开发小程序之性能优化
小程序开发生态 ———— 17年小程序

wepy，组件开发及npm支持等，模拟实现 ==> mpvue
uni-app、Megalo、mpx、Chameleon

Taro nanachi


uni-app
继承自Vue.js，跨平台多终端
编译器 + 运行时 
uni-app runtime： 事件代理机制，数据同步机制
性能优化：
1、启动加载
改写Vue的patch，删除vnode
2、页面渲染
减少调用setData频次，减少调用setData数据量
自定义组件实现局部数据刷新
通用建议：onPageScroll滚动；避免后台页面执行JS逻辑（settimeout等）

分包，渲染滚动等