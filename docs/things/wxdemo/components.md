# 小程序常用功能 & 组件封装 #

## 获取用户信息 ##
> 最新版本的获取用户信息，不可以直接在打开小程序时直接获取，而是需要用户点击 button 按钮，点击允许获取后才能获取到用户信息，比如头像、用户名等（用户绑定的电话号码不在其中，需要单独调用API接口）。

``` 
// wxml
&lt;button open-type=&quot;getUserInfo&quot; bindgetuserinfo=&quot;getUserInfo&quot;&gt;点击获取用户信息&lt;/button&gt;


// js
getUserInfo: function(e) {
    console.log(e)
}
``` 


## 获取用户绑定微信手机号码 ##
> 需先调用 wx.login 接口。需要将 button 组件 open-type 的值设置为 getPhoneNumber，当用户点击并同意之后，可以通过 bindgetphonenumber 事件回调获取到微信服务器返回的加密数据， 然后在第三方服务端结合 session_key 以及 app_id 进行解密获取手机号。

``` 
// wxml
&lt;button open-type=&quot;getPhoneNumber&quot; bindgetphonenumber=&quot;getPhoneNumber&quot;&gt;获取用户手机号码&lt;/button&gt; 


// js
getPhoneNumber(e) {
  console.log(e)
}
``` 


## 微信客服 ##
> 点击button按钮跳转微信客服，并且还需要在客服回话框内显示一个卡片，用户点击该卡片可以向客服系统发送用户预留的卡片消息，点击卡片消息可以跳转到该卡片对应的小程序页面。

``` 
// wxml
&lt;button 
  open-type=&quot;contact&quot;
  show-message-card=&quot;true&quot;
  send-message-title=&quot;会话内消息卡片标题&quot;
  send-message-img=&quot;会话内消息卡片图片&quot;
  send-message-path=&quot;会话内消息卡片点击跳转小程序路径&quot;
&gt;微信客服&lt;/button&gt;



## 监听页面上下滚动 ##
onPageScroll: function (ev) {
  var _this = this;
  // 当滚动的top值最大或最小时，为什么要做这一步是因为在手机实测小程序的时候会发生滚动条回弹，所以为了处理回弹，设置默认最大最小值
  if (ev.scrollTop &lt;= 0) {
    ev.scrollTop = 0;
  } else if (ev.scrollTop &gt; wx.getSystemInfoSync().windowHeight) {
    ev.scrollTop = wx.getSystemInfoSync().windowHeight;
  }
  // 判断浏览器滚动条上下滚动
  if (ev.scrollTop &gt; this.data.scrollTop || ev.scrollTop == wx.getSystemInfoSync().windowHeight) {
    // 向下滚动
    console.log(&#x27;向下滚动&#x27;)
  } else {
    // 向上滚动
    console.log(&#x27;向上滚动&#x27;)
  }
  // 可以给scrollTop重新赋值
  setTimeout(function () {
    _this.setData({
      scrollTop: ev.scrollTop
    })
  }, 0)
}
``` 


## 常用页面头图轮播 ##
> 在很多业务中，关于头图那块是这样的需求；头图是由后台运营配置的，运营可以配置一张到多张，而且可以配置头图的链接，如果有配置链接就可以点击跳转到配置页面，如果没有就点击不跳转；如果运营一张头图都没有配置，就显示默认头图。具体需求，按公司需求而定。

**注意事项**

1. 在pages目录同级的地方创建 components 目录，用来存放公用组件
2. 头图点击跳转链接，需要web-view的配合，所以需要在pages目录下面创建webview目录
3. 关于数据的key值，需要根据后台返回，所以需要改动的地方就是组件里面的这个key值
4. 假设你在components目录下有一个swiper组件

**components swiper组件**
``` 
// wxml
&lt;view class=&quot;header-swiper-wrap&quot; hidden=&quot;{{show}}&quot;&gt;
  &lt;swiper class=&quot;swiper-wrap&quot; wx:if=&quot;{{swiperData.datas.length}}&quot;&gt;
    &lt;block wx:for=&quot;{{swiperData.datas}}&quot; wx:key=&quot;{{index}}&quot;&gt;
      &lt;swiper-item wx:if=&quot;{{item.img_link}}&quot;&gt;
        &lt;navigator url=&quot;/pages/webview/webview?url={{item.img_link}}&quot; class=&quot;swiper_navigator&quot;&gt;
          &lt;image src=&quot;{{item.img_url}}&quot; mode=&quot;aspectFill&quot;&gt;&lt;/image&gt;
        &lt;/navigator&gt;
      &lt;/swiper-item&gt;
      &lt;swiper-item wx:else&gt;
        &lt;image src=&quot;{{item.img_url}}&quot; mode=&quot;aspectFill&quot;&gt;&lt;/image&gt;
      &lt;/swiper-item&gt;
    &lt;/block&gt;
  &lt;/swiper&gt;
  &lt;view class=&quot;swiper-wrap&quot; wx:else&gt;
    &lt;image src=&quot;{{swiperData.defaults}}&quot; mode=&quot;aspectFill&quot;&gt;&lt;/image&gt;
  &lt;/view&gt;
&lt;/view&gt;


// wxss
.header-swiper-wrap .swiper-wrap {
  position: relative;
  display: block;
  height: 100%;
}
.header-swiper-wrap .swiper_navigator {
  display: block;
  height: 100%;
}
.header-swiper-wrap .swiper-wrap image {
  width: 100%;
  height: 100%;
}


// js
Component({
  properties: {
    swiperData: {
      type: Object,
      value: {}
    }
  },
  data: {
    show: false
  },
  ready: function() {
    // 如果传人的数据既没有默认头图，也没有轮播数据，那么swiper组件不显示
    var isShow = !this.properties.swiperData.defaults &amp;&amp; !this.properties.swiperData.datas.length
    if (isShow) {
      this.setData({
        show: true
      })
    }
  },
  methods: {}
})
``` 


**需要引入组件的pages页面**
``` 
// .json 文件配置
{
  "component": true,
  "usingComponents": {
    "header-swiper": "/components/swiper/swiper"
  }
}

// wxml
&lt;header-swiper swiper-data=&quot;{{swiper_data}}&quot;&gt;&lt;/header-swiper&gt;

// js
data: {
  swiper_data: {
    height: &#x27;400rpx&#x27;, 		// 头图高度
    defaults: &#x27;默认头图地址&#x27;,	// 默认头图
    datas: [			// 轮播图数据，这个数据是请求过来的，这里只是模拟
      {
        img_url: &#x27;图片地址&#x27;,
        img_link: &#x27;webview跳转地址&#x27;
      }
    ]
  }
}
``` 

## 可滚动视图区域 scroll-view （横向居中滚动） ##
> scroll-view 的默认功能可以满足日常需求，但一些额外的需求就需要手动开发，比如“横向居中滚动”：可以设置初始 scroll 滚动条位置，便于定位到具体模块；点击模块的时候，需要模块滚动到居中位置


**注意事项**

1. 在pages目录同级的地方创建 components 目录，用来存放公用组件
2. 假设你在components目录下有一个scroll组件

**components scroll组件**
``` 
// wxml
&lt;view class=&quot;scroll-view-wrap&quot;&gt;
  &lt;scroll-view
    style=&quot;background: #dfdfdf;&quot;
    scroll-x
    scroll-left=&quot;{{scrollLeft}}&quot;
    scroll-with-animation=&quot;true&quot;
  &gt;
    &lt;view class=&quot;item-box&quot; style=&quot;width: {{scrollWidth}};&quot;&gt;
      &lt;text 
        id=&quot;scroll{{index}}&quot;
        class=&quot;text {{index == itemIndex?&#x27;active&#x27;:&#x27;&#x27;}}&quot;
        wx:for=&quot;{{scrollViewData.datas}}&quot;
        wx:key=&quot;{{index}}&quot;
        data-index=&quot;{{index}}&quot;
        bindtap=&quot;changeItem&quot;
      &gt;{{item.name}}&lt;/text&gt;
    &lt;/view&gt;
  &lt;/scroll-view&gt;
&lt;/view&gt;

&lt;view&gt;{{scrollViewData.datas[itemIndex].content}}&lt;/view&gt;


// wxss，样式可以自行更改
.scroll-view-wrap {
  position: relative;
  font-size: 0;
}
.scroll-view-wrap .item-box {
  display: flex;
  justify-content:space-around;
}
.scroll-view-wrap .text {
  flex: 1;
  text-align:center;
  display: inline-block;
  height: 80rpx;
  line-height: 80rpx;
  font-size: 30rpx;
  padding: 0 10rpx;
}
.scroll-view-wrap .active {
  color: #fff;
  background-color: #333;
}


// js
Component({
  properties: {
    scrollViewData: {
      type: Object,
      value: {}
    }
  },
  data: {
    isShow: true,
    itemIndex: 0,       // 选中第几个模块
    scrollLeft: 0,      // 滚动条偏移量
    deviationWidth: 0,  // 滚动时的偏移差值
    elementWidth: 0,    // 页面元素宽度
    scrollWidth: &#x27;&#x27;,    // scroll 内外框元素宽度
  },
  lifetimes: {
    ready: function () {
      let that = this
      let scrollViewData = that.properties.scrollViewData
      let index = scrollViewData.index
      let viewWidth = wx.getSystemInfoSync().windowWidth
      let num = 750 / viewWidth

      let query = wx.createSelectorQuery().in(this)

      query.select(&#x27;.text&#x27;).fields({
        size: true
      }, function (res) {
		// scroll-left 偏移量，每个定位到的模块，如果要居中的话，都需要用他们的 offsetLeft 去减掉这个值
        let deviationWidth = res.width + (res.width / 2)

		// 每个模块的宽度
        let elementWidth = res.width

        // 在这个换算中不使用 elementWidth * num 而是使用 elementWidth * 2
        // 是因为在ipad端，num的值小于1，所以会出现宽度问题，就粗略的用2来解决
        let scrollWidth = scrollViewData.datas.length * (elementWidth * 2) + &#x27;px&#x27;

        // 设置传人index对应的scroll偏移量
        let scrollLeft = (that.properties.scrollViewData.index * elementWidth) * 2 - (deviationWidth * 2)
		
		// 改变初始scroll偏移量
        that.changeWidth(scrollWidth)

        that.setData({
          elementWidth: elementWidth,
          deviationWidth: deviationWidth,
          scrollLeft: scrollLeft,
          itemIndex: index
        })
      }).exec()
    }
  },
  methods: {
    // 点击模块改变scroll偏移量
    changeItem: function(e) {
      let index = e.currentTarget.dataset.index
      let viewWidth = wx.getSystemInfoSync().windowWidth
      let width = this.data.deviationWidth * 2
      let left = e.target.offsetLeft - width
      this.setData({
        scrollLeft: left,
        itemIndex: index
      })
    },
    // 改变初始scroll偏移量
    changeWidth: function (scrollWidth) {
      this.setData({
        scrollWidth: scrollWidth
      })
    }
  }
})
``` 


**需要引入组件的pages页面**
``` 
// wxml
&lt;scroll-view-mode scroll-view-data=&quot;{{scrollViewData}}&quot;&gt;&lt;/scroll-view-mode&gt;


// .json 文件配置
{
  "component": true,
  "usingComponents": {
    "scroll-view-mode": "/components/scroll/scroll"
  }
}


// js
data: {
  scrollViewData: {
    index: 0,     // 初始定位到scroll第几个模块
    datas: [      // scroll数据
      { id: 1010, name: "我是数据", content: '我是内容' }
    ]
  }
}
``` 