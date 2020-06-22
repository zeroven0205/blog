JavaScript中如何对一个对象进行深度clone

方法一：

function deepClone(obj){
  var str = JSON.sringify(obj);
  var newobj = JSON.parse(str);
  return newobj;
}
方法二：

//深克隆
function deepClone(obj){
    if (!obj) { return obj; }
    var o = obj instanceof Array ? [] : {};
    for(var k in obj){
        if(obj.hasOwnProperty(k)){
            o[k] = typeof obj[k] === "object" ? deepClone(obj[k]) : obj[k];
        }
    }
    return o;
}