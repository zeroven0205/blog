# 微信小程序（2.0） #

## 产品定位及功能介绍 ##
- 微信小程序是一种全新的连接用户与服务的方式，它可以在微信内被便捷地获取和传播，同时具有出色的使用体验。
- 微信小程序是一种全新的连接用户与服务的方式，它可以在微信内被便捷地获取和传播，同时具有出色的使用体验。
- 小程序内全部采用组件的形式进行编辑，并且融合了MVVM的设计模式，以数据驱动视图的方式开展我们的小程序开发。
- 提供微信内置的很多API供开发者调用（数据请求、获取用户信息、分享等）。
- 微信小程序提供专门的开发工具（微信小程序开发工具），可以很方便的让开发者进行开发和本地以及线上测试调试。
- 总而言之，微信小程序就是运行在微信端的APP。通过它们的组件和提供的API能达到和原生APP一样的用户体验。



## 微信小程序设计指南 ##
这个是小程序设计的一些意见和建议，为方便设计师进行设计，微信提供一套可供Web设计和小程序使用的基础控件库；同时提供方便开发者调用的资源。可以给UI设计师在开发小程序之前看。
[https://developers.weixin.qq.com/miniprogram/design/index.html?t=2018413](https://developers.weixin.qq.com/miniprogram/design/index.html?t=2018413 "微信小程序设计指南")

## 小程序开发流程 ##
1. 注册微信小程序账号以及相关操作：[https://developers.weixin.qq.com/miniprogram/introduction/index.html?t=2018518](https://developers.weixin.qq.com/miniprogram/introduction/index.html?t=2018518 "注册微信小程序账号")
2. 微信小程序开发工具的使用：[https://developers.weixin.qq.com/miniprogram/dev/devtools/devtools.html?t=2018413](https://developers.weixin.qq.com/miniprogram/dev/devtools/devtools.html?t=2018413 "小程序开发工具")
3. 小程序教程、框架、组件、API：[https://developers.weixin.qq.com/miniprogram/dev/index.html?t=2018413](https://developers.weixin.qq.com/miniprogram/dev/index.html?t=2018413 "小程序开发")

## 小程序提供的功能 ##
1. 客服功能：用户可使用小程序客服消息功能，与小程序的客服人员进行沟通。
2. 扫码打开小程序：支持使用微信“扫一扫”或微信内长按识别二维码跳转小程序。
3. 小程序插件：是可被添加到小程序内直接使用的功能组件，插件可以是自己写的，也可以时别人开发好的，不过别人开发好需要像开发者申请，只有开发者同意之后才能使用，所以未来小程序插件将会像npm一样变成一个服务，不在需要去申请。
4. 小程序API：框架提供丰富的微信原生API，可以方便的调起微信提供的能力，如获取用户信息，本地存储，支付功能等。

#### API功能列举 ####
- 发起网络请求
- 上传、下载资源文件
- WebSocket 连接（浏览器与服务器全双工通信：[https://blog.csdn.net/lecepin/article/details/54632749](https://blog.csdn.net/lecepin/article/details/54632749 "websocket")）
- 媒体：图片、录音、音频、视频、数据缓存、地理位置、地图、获取用户系统信息网络状态等、扫码、蓝牙、弹窗、导航、位置信息等

#### 小程序JSSDK ####
> 说明文档：[https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421141115](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421141115 "说明文档")
> 要在网页中使用微信提供的比如：微信扫一扫、定位、图片接口、音频等接口，需要用到它的JSSDK，里面的注意点如下：

1. 配置业务域名（记得把微信提供的校验txt文件放在服务器域名的根目录下，你的h5页面放在同一个服务器域名的目录下）
2. web-view访问域名和h5请求微信签名的域名必须一致，比如都在 xxx.jiehun.com.cn 域名下面才行
3. 在h5当前页面发起后台签名请求，获取“企业号的唯一标识（不是小程序的appID）”、“签名”等信息
4. 请求成功后在去进行 wx.config 配置
5. 这里需要注意一个地方，就是wx.config不要放在事件里面，不然你如果用某个元素的点击事件去触发（比如扫一扫）的话，它要点两次才可以。因为点击的时候，执行wx.config 成功之后，只有再次点击才会触发扫码等微信动作


在此之前记得要先引人 JSSDK的js文件，用到jq的话，jq的访问域名也必须配置进业务域名
小程序以配置的jquery：https://s8.tthunbohui.cn/static/js/hapj.v3.m.min-b2239828.js
总而言之，如果你是小程序web-view导入的h5页面，所有的网络访问都必须配置业务域名

``` javascript
$.ajax({
	url: '获取签名的api?url=' + encodeURIComponent(window.location.href),
	method: 'GET',
	dataType: 'json',
	success: function(res) {
		// 这里面可以获取到后台请求回来的“企业号的唯一标识”、“签名”等信息
		// 把这些信息配置到 wx.config 里面即可调用微信JSSDK提供的功能
		wx.config({
		    debug: true, 
		    appId: appId,				// 必填，企业号的唯一标识，此处填写企业号corpid
		    timestamp: timestamp, 			// 必填，生成签名的时间戳
		    nonceStr: nonceStr, 			// 必填，生成签名的随机串
		    signature: signature,			// 必填，签名
		    jsApiList: ['功能name'] 			// 必填，需要使用的JS接口列表
		})
		wx.ready(function(){
			// wx.config验签通过，可以调用方法了
		})
		wx.error(function(res){
			// 失败了，有可能wx.config验签没通过，所以拿不到“签名”等信息
		})
	}
 )}
```


## 小程序生命周期 ##
> 小程序和vue等常用前端框架一样，都是MVVM的框架，页面也有存在从初始化到卸载的整个过程（生命周期）

1. APP页面注册参考：[https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/app.html](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/app.html "app.js")
2. page生命周期参考：[https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page.html](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page.html "page生命周期")
3. 页面路由时参考：[https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route.html](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route.html "页面路由")

打个比方，你在用 tabBar 做页面布局的时候，在第一次进入该 tabBar 路由时，页面会执行 onLoad、onShow、onReady等生命周期函数，但在下一次切换回 tabBar 路由时，它不会执行 onLoad 生命周期函数，所以，你想要在每一次切换到某个 tabBar 路由时，都希望该页面的某个地方的数据都是重新请求的最新数据的话，那要把那个地方的请求函数应该放在 onShow 生命周期钩子里。


## 监听网络状态变化 ##
[https://developers.weixin.qq.com/miniprogram/dev/api/device.html#wxgetnetworktypeobject](https://developers.weixin.qq.com/miniprogram/dev/api/device.html#wxgetnetworktypeobject "监听网络变化")
这里有个问题：就是如果用户在首次进入tabBar页面的时候，断网了，那么你的初始化程序如果写在比如 onLoad 里面的话，即使用户网络又在次恢复的情况下，用户再次进入该页面的话，它看到的还是问题页面；所以监听网络变化对小程序业务是很有用的，这样在用户网络出问题的时候，就可以利用这个API对小程序进行处理，不至于用户恢复网络的时候，页面是错乱的。至于如何处理.......


## 关于小程序强制更新 ##
[https://developers.weixin.qq.com/miniprogram/dev/framework/operating-mechanism.html](https://developers.weixin.qq.com/miniprogram/dev/framework/operating-mechanism.html "强制更新")
所以，如果你的小程序需要用户不管什么时候进入的时候，都是最新的版本的话，建议在最初的版本上加上强制更新的机制（在app.js里面加入代码即可）；不过微信小程序的强制更新有个体验的问题，就是微信的强制更新需要检测你的版本，同时下载最新的代码包，之后才会出现提示信息，而这个过程要8到10s的时间（具体更具网速而定，以4g测试是这个时间端）。
不过你可以通过在app.js里面通过请求后台版本对比的接口，去做相应处理，如果你觉得那个时间端无所谓的话，就按照文档的代码写就可以。
经过测试，发现在ios系统下和安卓系统下，微信的强制更新还不一样；按照文档上面说的，微信的更新应该是在第二次冷启动后（第一次是下载更新文件），但发布线上的时候发现，ios系统下，假如你现在看的是1.0的版本，在之后你又发布了2.0的版本，当你第一次冷启动之后，应该是下载更新包，但不更新才对，但测试发现，ios系统下，当你发布成功后，你之前预览的1.0版本退出一端时间后再次打开时，它已经更新到最新版本了，而且不是所有ios系统都是这样，而安卓系统倒是保持高度一致


#### 微信小程序-数据综合统计、打点自定义统计 ####
小程序数据分析，是面向小程序开发者、运营者的数据分析工具，提供关键指标统计、实时访问监控、自定义分析等，帮助小程序产品迭代优化和运营。主要功能包括每日例行统计的标准分析，以及满足用户个性化需求的自定义分析。
由于开发工具暂时未支持自定义分析数据上报，所以所有的数据统计上报的实现，都是在线上发布后测试的。了解这一块内容，有利于你在写项目的时候注意页面元素的class或id选择的抒写方式，以及后端数据结构的分配，这样在你抒写页面使用选择器或者后端造数据时，对你后期做数据打点自定义统计时，有很大帮助。
API：[https://developers.weixin.qq.com/miniprogram/analysis/](https://developers.weixin.qq.com/miniprogram/analysis/ "数据统计")
建议在写页面的时候，对以后需要做数据统计的元素身上加上唯一的class或id值，方便后期做数据统计事件用（尤其要注意使用for循环渲染处出来的结构，如果后期需要对渲染出来的模块做打点统计的话，数据里面一定要有模块的唯一标识字段，用这个字段填充模块的class或id）
建议在定义数据统计字段的时候，都加上功能页面名称前缀，比如商品价格 product_pric，建议定义成 xxx_product_pric，这样是为了防止，你在某个统计中用了 product_pric 这个统计字段，但到另一个统计需求中，你不需要这个字段了，然后删除了它，但小程序后台会存有历史数据记录，这样你再次用 product_pric 定义这个数据统计字段时，就要注意该字段的意义跟以前是否一致，如果不一致，建议用新的字段，否则 product_pric 的历史数据跟之后上报的数据含义冲突，对数据分析造成干扰。


> 举一个例子：比如说有一个导航栏，有四个点击按钮，然后你在这个页面需要对这个四个点击按钮分别做数据统计（点击次数统计），
> 但这四个按钮的数据都是后台请求由你 wx:for 循环出来的，而且每个城市返回的数据长度还不一样，有些城市只有一个返回数据，
> 有些可能有多个。那么这个时候做点击统计就不好弄，所以应该提前跟后台商量好，要在每个模块的数据里面去添加一个唯一的标识字符，
> 然后你在微信后台里面通过这个标识字符（你可以把它设置成id值）去做统计事件的设定。



# 关于小程序登录问题(以家芭莎小程序为例) #
家芭莎小程序登录，采用的是用户进入登录页面，填写手机号码获取验证码的方式，前后端流程是这样的：

1. 用户点击确认登录，前端执行 wx.login 获取微信返回的 code 值
2. 后端通过用户填写的 手机号码 + 验证码 + code，在后台服务那里去跟微信服务换取用户的 oppenid
3. 通过这个 oppenid 后端可以得到 _wxspcsessionid_，这个id就可以作为小程序的登录凭证，它是会过期的，并且由于服务端语言不同的问题，后端会把这个id值在转换成一个通用的id值，叫做 jhu（它是不过期的） ，但由于公司后端业务等问题，后端并没有在h5页面里面通过接口直接转换成 jhu，所以前端不能直接传人这个 _wxspcsessionid_ 值，因为h5页面没做任何处理，需要前端直接传人那个通用的 jhu 作为用户h5页面的登陆凭证
4. 所以前端在微信小程序内部发起请求时，后端会把 _wxspcsessionid_ 转换成 jhu 后，直接返回给前端，前端在打开h5页面时，再直接传人就可以了


## 小程序注意点（页面配置方面） ##
#### 关于tabBar动态状态 ####
> 小程序可以统一设置页面底部导航栏（app.json中配置），同时也支持通过 API 的形式在page页面里面动态设置

#### 关于数据的设置 ####
> key和value值不建议设置成一个字段，这样可能会造成不必要的错误（数据设置不上的不明错误），尤其是在自定义组件传递数据的时候，如下：

``` javascript
let datas = xxxxx
this.setData({
    datas: datas
})
```

#### 关于 web-view ####
1. h5页面的小程序标题：小程序页面的标题是由小程序.json文件或者API配置的，但如果是web-view 的h5页面，则是由h5页面的head标签里面的title标签提供的，如果没有提供，那就显示小程序自已的标题（默认小程序标题）
2. web-view 页面在分享时，需要设置 onShareAppMessage（用户点击右上角分享），否则用户打开的分享页面是空白页面。

``` javascript
	onShareAppMessage: function (options) {
  		return {
    		title: '自定义转发标题',
    		path: 'pages/webhref/webhref?url=' + options.webViewUrl
  		}
	}
```


## 小程序注意点（页面样式方面） ##
#### 关于页面背景色 ####
> 小程序可以统一设置窗口背景色（在app.json里面配置），也可以单独设置某个页面的窗口背景色（pages页面的.json文件配置），单独设置的页面背景色按道理应该会覆盖统一设置的窗口背景色，但设置后往往不能如意，所以需要单独设置窗口背景色的话，一般采用css的方式设置（在单独的pages页面的css文件里面设置page样式）

``` css
page{
  background-color: #333333;
}
```

#### 关于一像素问题 ####
> 小程序完美支持1像素，在其他框架中，1像素可能都是1px的写法，但小程序在移动端1px的解决方法就是1rpx
<pre>
border: 1rpx solid #eee;
</pre>

#### 关于swiper显示面板指示点样式的改变  ####
> 文档里面没有明确写明如果改变这个面板指示点的样式，所以要通过自定义 class 的方式改变；给 swiper 标题添加一个 class 比如：swiper-box

``` css
.swiper-box .wx-swiper-dots.wx-swiper-dots-horizontal{
  margin-bottom: 0rpx;
}
.swiper-box .wx-swiper-dot{
  width:20rpx;
  display: inline-flex;
  height: 5rpx;
  margin-left: 8rpx;
  justify-content:space-between;
}
.swiper-box .wx-swiper-dot::before{
  content: &#x27;&#x27;;
  flex-grow: 1; 
  background: #000;
}
.swiper-box .wx-swiper-dot-active::before{
  background:#fff;   
}
```


#### 本地资源图片 ####
> 不能通过url的图片路径来直接获取本地图片，图片路径须使用网络图片，或者 base64，或者使用<image/>标签。

``` css
page{
  background-image: url(线上图片地址);
}
```

#### css ####
- css 不建议使用连号选择 比如： .a, .b {..........}
- 尽量避免id选择器，使用class选择器

#### css适配 ####
注意在使用rpx做计算时，不要忽略不同手机之间的px换算，尤其是在做适配高度的时候
rpx换算px (屏幕宽度/750)	px换算rpx (750/屏幕宽度)

#### 元素居中问题 ####
如果你想让 **子元素块** 水平、垂直居中不会有兼容问题的话，建议使用定位。

``` css
position: absolute;
left: 0;
top: 0;
bottom: 0;
right: 0;
width: 设置宽度;
height: 设置高度;
margin: auto;

```


## 小程序注意点（页面结构方面） ##

#### cover-image ####
- 在安卓机下，使用cover-image加载图片的话，在图片上滑动时，会造成的安卓下无法滑动页面问题
- 所以在显示图片方面，一定要用image组件不要用其他组件


#### 点击按钮 ####
> 点击按钮不要放到**input**元素上面，不然手机键盘弹出时，按钮点击不了

``` css
&lt;div&gt;
	&lt;input type=&quot;text&quot;&gt;
	&lt;button&gt;点击按钮&lt;/button&gt;
&lt;/div&gt;

```

#### 固定定位 ####
> 在改变定位布局的时候，注意页面的占位，不然在小程序里面会出现上下页面抖动的问题
> 在手机端经常出现的底部固定定位按钮，和页面input输入框获得焦点时，手机键盘弹出遮挡问题解决方案：[https://blog.csdn.net/deeplies/article/details/74388061](https://blog.csdn.net/deeplies/article/details/74388061 "wab端键盘弹出问题")


在布局方面，记得给整个父级的底部添加 margin-bottom 一个比较合适的值即可，在input输入框获得焦点时添加如下js代码

元素.scrollIntoView(false);  
元素.scrollIntoViewIfNeeded(true);  
document.body.scrollTop = document.body.scrollHeight;



#### 阻止页面滚动的方法 ####
1. 使用scroll-view组件
2. 在最外层设置catchtouchmove="true"


## 小程序注意点（页面逻辑方面） ##
1. 小程序开发框架的逻辑层由 JavaScript 编写。
2. 每个页面有独立的作用域，并提供模块化能力，通过module.exports导出模块；import引人模块。
3. 由于框架并非运行在浏览器中，所以 JavaScript 在 web 中一些能力都无法使用，如 document，window 等。所以小程序不支持操作DOM元素，视图层的变化都应该采用数据去驱动。


## 微信小程序优化 ##
> 小程序代码包最理想的情况是不超过2M！如果小程序包太大会影响小程序初次打开是的页面速度出现白屏现象。

1. **资源外置：**非核心不紧急的资源文件，特别是图片、音频、视频等体积较大的媒体文件，可以移至cdn服务器，需要时再通过网络载入
2. **数据外置：**非核心不紧急的数据内容，包括城市地区等大段数据，标签映射等大段配置，使用条约、服务说明等大段文案等，可以移至数据服务器或本地storage，需要时再予以载入
3. **页面外置：**对于一些布局或样式比较多的页面，只是用来展示的页面，可以使用web-view组件来引人
4. **清理大文件：**大文件常常存在较大的压缩空间，值得重点排查和处理。查找大文件tip：资源管理器 - 代码目录 - 搜索'*' - 右键 - 排序方式：大小，即可将代码包内所有文件按大小排序展示
5. **分包加载**：[https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages.html](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages.html "分包加载")