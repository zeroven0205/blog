#### Nuxt 开发那些事儿
> 使用nuxt-link或者router.push实现的页面跳转，需在destroy方法内销毁掉页面挂载到window上的方法，否则新页面中仍然会执行这个全局的方法