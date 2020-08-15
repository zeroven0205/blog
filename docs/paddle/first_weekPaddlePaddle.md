## PaddlePaddle 飞桨开源深度学习平台尝鲜
* description: first note for paddlePaddle platform, it will be much more rich and varied, stay tuned!

### Local本地环境的搭建配置
* 确保patyon的版本正确, 2.7.x ～ 3.7.x，3.8.0+不支持
* Mac 下安装Python[mac python2.7.10 升级到 3.6](https://www.cnblogs.com/liang1101/p/7049948.html)
* 安装pyenv [解决pyenv无法切换python版本问题](https://blog.csdn.net/dqchouyang/article/details/105965546)
~~~ shell
export HOMEBREW_NO_AUTO_UPDATE=true
brew install pyenv
pyenv install 3.6.10
pyenv rehash
pyenv versions
pyenv global 3.6.10
~~~

### 学习过程
* 学习熟悉Python基本语法
* 熟悉熟练操作aistudio Notebook执行器，掌握学习平台的基本操作、包括不限于快捷键等的掌握，会提升学习、练习、作业编码等效率
* 对照notebook中关于pdb代码调试的文档实践，调试并体验pdb代码调试
* 波士顿房价暨手写数字识别等视频看过一遍后，再次对照note笔记自上而下copy代码，运行测试调试

### 代码实践暨学习案例
* [波士顿房价预测模型](./bostonhouse.py)
* [手写数字识别](./hnwr.py)
* [手写数字识别测试用例](./hnwrtest.py)
* [数字倒转函数](./reverse.py)
* [pdb断点调试案例](./pdbDemo.py)

### 总结于体会
* 需要仔细认真对待前面介绍平台及环境，Notebook及执行器等，【工欲善其事，必先利其器】
* 仔细阅读文档比看视频更重要，推荐自上而下从前到后照着Notebook的文档copy代码，逐模块运行调试，方可理解其中的关键点
* 感慨下：强大的Notebook网页版代码执行器，超级强大便捷，无需切换终端，无需ssh，无需关注环境等等问题，帅呆屌爆了 ：）