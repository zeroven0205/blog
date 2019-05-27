# dmp运营中心后台 #
> 运营管理平台，负责所有运营日常工作需要；包含订单、现金劵、客资、电话营销等很多模块

# dmp测试登陆地址 #
[http://sso.test.tthunbohui.com/login](http://sso.test.tthunbohui.com/login "login")

# 开发过程 #
> 整个项目采用前端配合后端开发，对于某些页面由前端编写页面结构和样式提供给后台人员（单页面形式即可），如果有个别交互复杂一点的页面，后端不好处理的，可由前端去编写那些交互。

# 技术桟 #
1. jquery（3.1.1版本）
2. layui（页面主要组件）
3. bootstrap
4. select2（select下拉插件）
4. adminLTE(项目布局用的这个)

# 静态资源 #
> 在gitLab里面的common目录develop分支下面放置所有该项目用到的静态资源文件，如果有新增的资源，上传分支后，可以让刘伟发布出去

域名地址：http://s6.tthunbohui.cn/compont/
已有资源文件：bootstrap，jquery，layui，tree(Jquery文件树形菜单插件)，select2

## CDN示例： ##
- http://s6.tthunbohui.cn/compont/layui/layui.js
- http://s6.tthunbohui.cn/compont/layui/css/layui.css
- 对照资源文件夹路径即可获取文件资源


## 关于table元素的适配问题 ##
> 由于原页面布局在容器的宽度定义上用的是百分比，所以在页面容器变小的情况下，table布局会自动缩放，导致table最右边的区域显示不全，而且父级元素也没有添加overflow处理，所以全局定义了一个 @media 类去做处理。

``` css
@media screen and (max-width: 1200px) {
  .screen-table-wrap {
    overflow: auto;
  }
  .screen-table-box {
    width: 1200px;
  }
}
```

## 高频率触发ajax问题 ##
> 对于高频率触发ajax请求导致页面请求过多、过快的问题，都统一采用函数节流的方式去处理。

``` html
function throttle(fn,context){    
   clearTimeout(fn.timer)
   fn.timer = setTimeout(function(){
     fn.call(context);
   },1000)
}
```
 
