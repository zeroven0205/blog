### H5 performance optimization
#### 网络网关层
1. 静态资源分多域名的解析，不同服务器机房部署（就近原则）——图片资源、js、css资源域名拆分
2. 服务器静态资源nginx容器部署，cdn加速，cdn缓存等
3. dns、域名的预解析

#### 客户端渲染层资源加载的优化
1. 图片资源的优化：
   1. 雪碧图、资源压缩、渲染通道png与jpg
   2. 新特性webp
   3. 图片按需懒加载
   4. 阿里云图片服务器图片裁切
1. 关于preload和prefetch https://www.cnblogs.com/xiaohuochai/p/9183874.html 
1. 首屏渲染：css、JS资源位置，是否必须最前面
1. 首屏完全没必要加载请求全球旅拍的内容
1. 重绘和重排  style="display:none;"与visibility

#### 代码实现层
1. 
1. 
1. 
1. 
1. 