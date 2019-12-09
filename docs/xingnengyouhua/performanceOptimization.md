### 可测的23条规则

1.Minimize HTTP Requests 减少HTTP请求

图片、css、script、flash等等这些都会增加http请求数，减少这些元素的数量就能减少响应时间。把多个JS、CSS在可能的情况下写进一个文件，页面里直接写入图片也是不好的做法，应该写进CSS里，利用 CSS sprites 将小图拼合后利用background来定位。
2.Use a Content Delivery Network 利用CDN技术
CDN 确实是好东西，8过服务器提供商的这项服务一般是要收费的，我以前买的国内空间是有这个的但是我当时根本不知道啥用，现在没了。。。
3.Avoid CSS Expressions 避免CSS Expressions
CSS表达式很可怕，这个只被IE支持的东西执行时候的运算量非常大，你移动一下鼠标它都要进行重计算的，但有时候为了做浏览器的兼容必须要用到这个
4.Add an Expires or a Cache-Control Header 设置头文件过期或者静态缓存
浏览器会用缓存来减少http请求数来加快页面加载的时间，如果页面头部加一个很长的过期时间，浏览器就会一直缓存页面里的元素。不过这样如果 页面里的东西变动的话就要改名字了，否则用户端不会主动刷新，看自己衡量了~ 这项可以通过修改.htaccess文件来实现。
5.Gzip Components Gzip压缩
Gzip格式是一种很普遍的压缩技术，几乎所有的浏览器都有解压Gzip格式的能力，而且它可以压缩的比例非常大，一般压缩率为85%。压缩没压缩，可以到 这里 做下测试。
6.Put Stylesheets at the Top 把CSS放顶部
让浏览者能尽早的看到网站的完整样式。
7.Put Scripts at the Bottom 把JS放底部
网站呈现完毕后再进行功能设置，当然这些JS要在你的加载过程中不影响内容表现。
8.避免使用CSS表达式
9.Make JavaScript and CSS External 将JS和CSS外链
前面讲到了缓存这个事情，一些较为公用的JS和CSS，我们可以使用外链的形式，譬如我就是从Google外链来的jQuery文件，如果我的浏览者在浏览别的使用了这个外链文件的网站时已经下载并缓存了这个文件，那么他在浏览我的网站的时候就不需要再进行下载了！~
10.Reduce DNS Lookups 减少DNS查找
貌似是要减少网站从外部调用资源，我的Google分析和picasa的外链图片都算在里面了。
11.Minify JavaScript and CSS 减小JS和CSS的体积
写JS和CSS都是有技巧的，用最少的代码实现同样的功能，减少空白，增强逻辑性，用缩写方式等等，当然也有不少工具也能够帮你实现这一点。
12. Avoid Redirects 避免重定向
再写入链接时，虽然”http://www. today-s-ooxx. com”和”http://www. today-s-ooxx. com/” 仅有一个最后的”/”只差，但是结果是不同的，服务器需要花时间把前者重定向为后者然后进行跳转，这个要自己注意，也可以在Apache里用Alias 或者mod_rewrite或者DirectorySlash解决。
13. Remove Duplicate Scripts 删除重复脚本
重复调用的代码浏览器并不会识别忽略，而是会再次运算一遍，这当然是大大的浪费。
14. Configure ETags 配置ETags
搞不清楚咋回事，总之我是在. htaccess里把它删除了。
15. Make Ajax Cacheable 缓存Ajax
Ajax是实时响应的，在浏览器接收到新的数据前，旧的数据被缓存，这样能够更好的提高效率。
16. Use GET for AJAX Requests 用GET方式进行AJAX请求
Get 方法和服务器只有一次交互（发送数据），而 Post 要两次（发送头部再发送数据）。
17. Reduce the Number of DOM Elements 减少DOM元素数量
复杂的页面结构意味着更长的下载及响应时间，更合理更高效的使用标签来架构页面，是好的前端的必备条件。
18. No 404s 不要出现404页面
站点本身里（非搜索结果）出现404页面，无意义的404页面会影响用户体验并且会消耗服务器资源。
19. Reduce Cookie Size 减小Cookie
Cookie在服务器及浏览器之间的通过文件头进行交换，尽可能减小Cookie体积，设置合理的过期时间，能够很好的提高效率。
20. Use Cookie-free Domains for Components 对组件使用无Cookie的域名
对静态组件的Cookie读取是一种浪费，使用另一个无Cookie的域名来存放你的静态组件式一个好方法，或者也可以在Cookie中只存放带www的域名。
21. Avoid Filters 避免过滤器的使用
如果需要Alpha透明，不要使用AlphaImageLoader，它效率低下而且只对IE6及以下的版本适用，用PNG8图片。如果你非要使用，加上_filter以免影响IE7+用户。
22. Don’t Scale Images in HTML 不要在HTML中缩放图片
图片要用多大的就用多大的，1000X1000的图片被width=”100″ height=”100″以后，本身的KB数是不会减少的。
23. Make favicon. ico Small and Cacheable 缩小favicon. ico的大小并缓存它
站点的浏览器ICO应该不是经常换吧，那就长时间的缓存它，并且最好控制在1K以下。


### 不可测试的一些规则

Flush the Buffer Early 尽早的释放缓冲

当用户进行页面请求时，服务器端需要花费200到500毫秒时间来拼合HTML，将写在head与body之间，释放缓冲，这样可以将文件头先发送出去，然后再发送文件内容，提高效率。

Post-load Components 延迟加载组件

最先加载必须的组件进行页面初始化，然后再加载其他，YUI Image Loader 是很好的例子。

Preload components 预加载组件

提前加载以后可能用到的东西，和延迟加载并不冲突，它的目的是为后续请求提供更快的响应，参见Google首页上的CSS sprites应用。

Split Components Across Domains 跨域分离组件

页面组件多个来源可以增大你的平行下载量，但注意不要过多，超过2-4个域名会引起上面说到的DNS查找浪费。

Minimize the Number of iframes 减少iframe数量

需要更有效的利用 ifames。
iframe 优点：有利于下载缓慢的广告等第三方内容，安全沙箱，并行下载脚本
iframe 缺点：即使为空也会有较大资源消耗，会阻止页面的onload，非语义

Minimize DOM Access 减少DOM的访问次数

JS访问DOM是很慢的，尽量不要用JS来设置页面布局。

Develop Smart Event Handlers 开发灵活的事件处理句柄

DOM树上过多的元素被加入事件句柄的话，反应效率肯定会低，YUI事件工具有一个 onAvailable 方法可以帮助你灵活的设置DOM事件句柄

Choose < link >over @import 使用< link >而非 @import

在IE中使用@import就和在页面底部用< link >一样，我们前面说要把< link >放顶部的。

Optimize Images 优化图片、CSS Sprites 优化CSS Sprites

将你的GIF转为PNG8会是个减小体积的好办法，另外有很多方法处理你的JPG及PNG图片以达到优化效果。

Optimize CSS Spirite

在CSS Sprites中竖直并尽量紧凑的排列图片，尽量将颜色相似的图片排在一起，会减小图片本身的大小及提高页面图片显示速度。

Keep Components under 25K 保证组件在25K以下

iPhone不能缓存25K以上的组件，并且这还是要在被压缩前。

Pack Components into a Multipart Document 将组件打包进一个多部分的文档中

就好像在邮件中加入附件一样，一个HTTP请求就够了，但是这一技术需要确保你的代理支持，iPhone就不支持。

作者：全栈弄潮儿
链接：https://www.jianshu.com/p/486f88018543
来源：简书 ---- 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。