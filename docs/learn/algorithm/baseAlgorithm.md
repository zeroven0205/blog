### 常见算法问题
#### fibonacci数列
～～～ javascript
/**
 *@desc: fibonacci
 *@param: count {Number}
 *@return: result {Number} 第count个fibonacci值，计数从0开始
  fibonacci数列为：[1, 1, 2, 3, 5, 8, 13, 21, 34 …]
  则getNthFibonacci(0)返回值为1
  则getNthFibonacci(4)返回值为5
 */
function getNthFibonacci(count){
    let _num = parseInt(count);
    
    if (isNaN(_num) || _num < 0) {
        return 0;
    }
    
    if(_num < 2){
        return 1;
    }
    return getNthFibonacci(_num - 2) + getNthFibonacci(_num - 1);
}

function fib(count) {

    // if(count <= 0) return 0;
    // if(count < 2) return 1;
    // var pre = 1;
    // var cur = 1;
    // for(var i = 2; i < count; i++){
    //  var after = pre + cur;
    //  pre = cur;
    //  cur = after;
    // }
    // return after // TODO 有问题
    
    //参数判断
    var count = parseInt(count);
    if (isNaN(count) || count < 0) {
        return 0;
    }
     
    function f(count) {
        if (count <= 1)
            return 1;
        return arguments.callee(count - 1) + arguments.callee(count - 2);    //callee是装逼用的，直接用f也行
    }
    return f(count);
}

let showStr = '';
let max = 10;
for (var i=0; i<max; i++){
    showStr = showStr + fib(i) + ((i == max-1) ? ' ...' : ', ')
}
console.log(showStr)
～～～
