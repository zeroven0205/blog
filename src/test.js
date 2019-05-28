var name = 'window'
var person1 = {
  name: 'person1',
  show1: function () {
    console.log(this.name)
  },
  show2: () => console.log(this.name),
  show3: function () {
    return function () {
      console.log(this.name)
    }
  },
  show4: function () {
    return () => console.log(this.name)
  }
}
var person2 = { name: 'person2' }

person1.show1()
person1.show1.call(person2)

person1.show2()
person1.show2.call(person2)

person1.show3()()
person1.show3().call(person2)
person1.show3.call(person2)()

person1.show4()()
person1.show4().call(person2)
person1.show4.call(person2)()


var oTab = document.getElementById('tab'),
  tabList = oTab.getElementBytagName('li'),
  divList = oTab.getElementBytagName('div');
function changeTab(curIndex) {
  for (var i=0; i < tabList.length; i++) {
    tabList[i].className = divList[i].className = '';
  }
  // curIndex:记录的是当前点击LI的索引
  tabList[curIndex].className = 'active';
  divList[curIndex].className = 'active';
}

// changeTab(x);
// tab的事件点击绑定，what's wrong! Why?
for (var i=0; i < tabList.length; i++) {
  tabList[i].onclick = function () {
    changeTab(i);
  }
}