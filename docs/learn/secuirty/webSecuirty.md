#### SQL注入
* 就是通过把SQL命令插入到Web表单提交或输入域名或页面请求的查询字符串，最终达到欺骗服务器执行恶意的SQL命令
* [SQL注入是什么？](https://baijiahao.baidu.com/s?id=1629045600845343519&wfr=spider&for=pc)
* 

#### XSS攻击
* 通常指利用网页开发漏洞，注入恶意指令代码到网页，使用户加载并执行攻击者恶意制造的网页程序（标签、
* JS、Java、 VBScript、ActiveX、 Flash等），攻击成功后，攻击者可能得到包括但不限于更高的权限（如执行一些操作）、私密网页内容、会话和cookie等各种内容。
* [XSS攻击百度百科资料](https://baike.baidu.com/item/XSS%E6%94%BB%E5%87%BB/954065?fr=aladdin&ivk_sa=1022817p)
* 

#### CSRF攻击
* CSRF（Cross-site request forgery）跨站请求伪造，也被称为“One Click Attack”或者Session Riding，通常缩写为CSRF或者XSRF，是一种对网站的恶意利用。
* XSS利用站点内的信任用户，而CSRF则通过伪装成受信任用户的请求来利用受信任的网站。与XSS攻击相比，CSRF攻击往往不大流行（因此对其进行防范的资源也相当稀少）但难以防范，所以被认为比XSS更具危险性。
* [CSRF百度百科资料](https://baike.baidu.com/item/CSRF/2735433?fr=aladdin)
* 优质博客链接：[什么是 CSRF 攻击，如何避免？](https://blog.csdn.net/meism5/article/details/90414140)
* 避免方法：
* >>CSRF 漏洞进行检测的工具，如 CSRFTester、CSRF Request Builder...
* >>验证 HTTP Referer 字段
* >>添加并验证 token
* >>添加自定义 http 请求头
* >>敏感操作添加验证码
* >>使用 post 请求

#### DDOS攻击
* [有关DDOS的一切](https://baijiahao.baidu.com/s?id=1626685756082047435&wfr=spider&for=pc)
* 分布式拒绝服务（通常缩写为DDOS）这是一种拒绝任何类型服务的情况
* DOS攻击的基本原理：DOS仅代表拒绝服务。这项服务可以是任何类型的,可以采取以下形式：
* >>劫持网络服务器
* >>使用请求重载端口使其无法使用
* >>拒绝无线认证
* >>拒绝在Internet上提供的任何类型的服务