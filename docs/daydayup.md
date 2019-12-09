### 异步请求数据顺序保障
请教大家一个问题，在ant design oro项目中，有这样一种场景，用户频繁点击翻页，多次dispatch同一个effect来获取列表数据，由于不能保证异步请求返回数据的顺序，所以如何保证页面接收到的props数据和当前的page是匹配的呢？
1. 防抖
2. 取消上次请求
3. redux-saga里有takeLatest

### 

