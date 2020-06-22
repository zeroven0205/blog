Vue 的父组件和子组件生命周期钩子执行顺序是什么?
vue的生命周期：beforeCreate created beforeMount mounted beforeDestory destoryed beforeUpdate updated

父组件和子组件钩子执行顺序

1. 加载渲染过程：
父beforeCreate->父created->父beforeMount->子beforeCreate->子created->子beforeMount->子mounted->父mounted
父组件挂载完毕肯定是等里面的子组件都挂载完毕后才算父组件挂载完毕了，所以父组件的mounted在最后。
2. 子组件更新过程(子组件更新影响到父组件的情况)：
父beforeUpdate -> 子beforeUpdate->子updated -> 父updted
子组件更新过程(子组件更新不影响父组件的情况)：
子beforeUpdate -> 子updated
3. 父组件更新过程(父组件影响子组件的情况)：
父beforeUpdate -> 子beforeUpdate->子updated -> 父updted
父组件更新过程(父组件不影响子组件的情况)：
父beforeUpdate -> 父updated
4. 销毁过程：
父beforeDestroy->子beforeDestroy->子destroyed->父destroyed


> @luchx 谢谢你的回答，我对2，3不太理解。如果一个页面 app组件-> main组件 ->footer组件-> btn组件 > ，当btn组件更新的时候，是这样的更新过程吗？
> footer组件beforeUpdate -> btn组件beforeUpdate -> btn组件updated -> footer组件updated
> 如果是的话，当footer组件beforeUpdate、updated的时候，main组件和app组件是也会走这样的更新过程吗。

如果只是btn组件更新是只会触发btn组件的生命周期，也就是btn组件: beforeUpdate -> updated
父子组件的更新依赖执行顺序是在于全局状态的更新，比如通过props传递，或者vuex等存在数据流向触发的更新，那么更新顺序就是父beforeUpdate->子beforeUpdate->子updated->父updated