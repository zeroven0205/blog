# 微信小程序开发实战 #
>

之后的迭代或者更新开发，都可以采用 **featrue/develop/x.x.x** 的分支形式，方便管理和查看迭代和更新版本


## 全局配置app.json ##
> 链接：[https://developers.weixin.qq.com/miniprogram/dev/framework/config.html#%E5%85%A8%E5%B1%80%E9%85%8D%E7%BD%AE](https://developers.weixin.qq.com/miniprogram/dev/framework/config.html#%E5%85%A8%E5%B1%80%E9%85%8D%E7%BD%AE "app.json")

- pages：页面路由（在小程序工具里面创建时，会自动生成到app.json的pages属性里面）
- usingComponents：全局组件注册（目前里面就注册了login-form组件，在login.wxml和campaign.wxml页面用到）
- window：全局页面配置，定义小程序所有页面的顶部背景颜色，文字颜色定义等
- tabBar：架子采用tabBar布局
- networkTimeout：各类网络请求的超时时间，单位均为毫秒（超时弹窗提示）
- debug：可以在开发者工具中开启 debug 模式，在开发者工具的控制台面板，调试信息以 info 的形式给出，其信息有Page的注册，页面路由，数据更新，事件触发等。可以帮助开发者快速定位一些常见的问题


## app.wxss ##
全局样式配置，包含：

- 清除浮动：clearfix
- 单行省略号：ellipsis
- 多行省略号：mult_line_ellipsis2（两行省略，其他行数，可自行添加）
- 轮播广告位指示点的样式：swiper-box


## app.js ##
小程序初始化完成时触发，全局只触发一次。

- 小程序强制更新（function）：toUpdate
- 查看改城市大礼包是否开启，修改模块名称(module)：footNav
- 用户是否选择了城市(string)：perCity
- 城市字段返回(function)：switchCity
- 获取用户信息(function)：getUserInfo（新版小程序不可用，需要用户主动触发）
- 判断是否登录了(function)：isLogin(依赖openLogin函数)


## project.config.json ##
通常大家在使用一个工具的时候，都会针对各自喜好做一些个性化配置，例如界面颜色、编译配置等等，当你换了另外一台电脑重新安装工具的时候，你还要重新配置。

考虑到这点，小程序开发者工具在每个项目的根目录都会生成一个 project.config.json，你在工具上做的任何配置都会写入到这个文件，当你重新安装工具或者换电脑工作时，你只要载入同一个项目的代码包，开发者工具就自动会帮你恢复到当时你开发项目时的个性化配置，其中会包括编辑器的颜色、代码上传时自动压缩等等一系列选项。

其他配置项细节可以参考文档 开发者工具的配置：[https://developers.weixin.qq.com/miniprogram/dev/devtools/projectconfig.html](https://developers.weixin.qq.com/miniprogram/dev/devtools/projectconfig.html "工具配置") 


## assets字体图标配置 ##
采用iconfont字体图标


## common全局公共函数配置（其实放在官方提供的 utils.js 文件目录下面也可以） ##
- api.js：wx.request请求统一配置，以及环境域名配置、强制更新版本号配置
- init.js：用户登陆设置缓存（高额返现campaign页面有用到）
- remove.js：数组去重
- tip.js：大量文字信息（login页面最下面的协议信息）
- toast.js：wx.showToast、wx.showModal弹窗的封装（cash页面有用到）


## components全局组件 ##
全局组件封装，包含弹窗、swiper轮播图、无数据模块显示、webview跳转等


## images全局图片 ##
大一点的图片，都用专题系统转换成线上的地址，很小的图标把它们保存在这里。


----------

# 各路由页面注意事项 #


## 我的 ##

**头部用户微信登录**

1. 用户没有登录的情况下，显示默认图片和默认姓名及会员等级
2. 用户登录情况下，显示后台返回姓名及会员等级
3. 用户微信登录情况下，显示用户微信头像 + 姓名 + 后台返回会员等级

**导航栏**
点击 我的签到礼、录单、邀请函、高额返现的业务逻辑（执行 directClick 函数），除了高额返现外，其他导航都采用 web-view 跳转

1. 先判断登录情况
2. 判断url里面是否有sp字段（sp=0：不需要索票）
3. 如果sp没有值或者值大于3，就和sp=0是一样的
4. sp=1：判断 ticket1 是否为 true
5. sp=2：判断 ticket2 是否为 true
6. sp=3：判断 wx.getStorageSync('ticket') 是否为 true
7. 索票来源字符拼接（某些模块需要索票，而且需要传入src索票来源参数）
8. 判断是高额返现卡、还是其他 （高额返现跳内置页面，其他页面跳内置h5页面）

**内容模块**

- 我的现金劵/大礼包、我的收藏、我的订单，点击进入子页面都需要判定用户是否登录小程序（不是微信登录,是后台登录）
- 我的客服采用微信内置功能 ``` <button class="kefu" open-type="contact"></button>``` 
- 切换账号：跳转登录页面 /pages/login/login

## 导航栏高额返现 ##
> 因为这块内容和逻辑处理比较多，如果这块内容需要改的的话，可以找叶丹同学


## 精选商品 ##

- 头图都是配置的，需要配置图片和图片webview跳转连接，如果头图一张都没配置，就采用默认图片；如果配置了图片但对应图片的连接没有配置，则不可点击跳转，否则可点击跳转
- 商品分类：上海有10个分类,其他城市隐藏设计师分类
- 热销品牌：采用 scroll-view 布局，而且点击模块要居中显示（封装了navbar组件）


## 现金劵/大礼包 ##
这个模块是两个模块的合体，需要通过接口判断该城市下面的“大礼包”是否开启，如果没有开启就显示现金劵模块，开启了就显示大礼包模块；通过数据 status 判断（1是现金劵，2是装修大礼包）


## 家博会 ##

- 头图：头图都是配置的，需要配置图片和图片webview跳转连接，如果头图一张都没配置，就采用默认图片；如果配置了图片但对应图片的连接没有配置，则不可点击跳转，否则可点击跳转
- 索票导语：后台返回，如果没有返回则显示默认文字
- 手机号码：用户输入正确的手机号码后，失去焦点时，会进行后端交互，把手机号码传入到后台数据中，也就是用户填了手机号码，但没继续下去的话，运营也可以拿到用户填的手机号，然后去做后续跟进
- 展会特色：运营配置的数据，不过需要注意的是，配置的数量如果是偶数，则图片都是左右均等分的，但如果是奇数，那最后一张图是全登分的长图（实现原理是采用flex布局）；并且图片如果配置了跳转连接，是可以跳转webview页面的


## 家装攻略 ##

- 头图：头图都是配置的，需要配置图片和图片webview跳转连接，如果头图一张都没配置，就采用默认图片；如果配置了图片但对应图片的连接没有配置，则不可点击跳转，否则可点击跳转
- 攻略详情页面（内容）：里面的内容是富文本，并且采用的是【 dmp运营管理后台--攻略--攻略管理--攻略列表--新增】 里面的第三套模板作为页面布局用的，前端通过返回的 type 去判断该渲染什么结构
- 攻略详情页面（全部推荐）：全部推荐里面的预约模块，其实就是筛选详情内容返回的 type='product' 商品类型添加的。
- 攻略详情页面分享：采用 自定义分享配置 onShareAppMessage
- 攻略详情页面客服：采用 button 属性配置进入客服界面发送消息模板



# 关于页面下拉刷新 #
> 没有采用 onPullDownRefresh（这个是下拉刷新执行函数，需要提前配置好下拉刷新功能，具体配置看官网文档） 加载局部模块，采用的是直接重载页面，注意 tabBar 页面采用 wx.reLaunch 重载，下面就以 tabBar 路由页面为例：

``` javascript
onPullDownRefresh: function () {
  setTimeout(() =&gt; {
    wx.reLaunch({
      url: &#x27;页面路径 + 参数（有参数的前提下）&#x27;
    })
  }, 500)
}
```


# 关于小程序登录问题 #
小程序登录，采用的是用户进入登录页面，填写手机号码获取验证码的方式，前后端流程是这样的：

1. 用户点击确认登录，前端执行 wx.login 获取微信返回的 code 值
2. 后端通过用户填写的 手机号码 + 验证码 + code，在后台服务那里去跟微信服务换取用户的 oppenid（后端服务在解码code 的时候需要 iv 和 encryptedData 这两个用户的编码值去解码，这两个值通过 wx.getUserInfo 去获取）
3. 通过这个 oppenid 后端可以得到 _wxspcsessionid_，这个id就可以作为小程序的登录凭证，它是会过期的，并且由于服务端语言不同的问题，后端会把这个id值在转换成一个通用的id值，叫做 jhu（它是不过期的） ，但由于公司后端业务等问题，后端并没有在h5页面里面通过接口直接转换成 jhu，所以前端不能直接传人这个 _wxspcsessionid_ 值，因为h5页面没做任何处理，需要前端直接传人那个通用的 jhu 作为用户h5页面的登陆凭证
4. 所以前端在微信小程序内部发起请求时，后端会把 _wxspcsessionid_ 转换成 jhu 后，直接返回给前端，前端在打开h5页面时，再直接传人就可以了


# 关于数据打点 #
小程序数据打点采用的是微信后台提供的“数据分析--自定义分析”这个功能，页面内没有做打点。
链接地址：[https://developers.weixin.qq.com/miniprogram/analysis/custom/#%E4%BA%8B%E4%BB%B6%E7%9A%84%E7%BC%96%E8%BE%91%E4%B8%8E%E5%8F%91%E5%B8%83](https://developers.weixin.qq.com/miniprogram/analysis/custom/#%E4%BA%8B%E4%BB%B6%E7%9A%84%E7%BC%96%E8%BE%91%E4%B8%8E%E5%8F%91%E5%B8%83 "数据分析")


