# Vue学习记录

## 1、Vue介绍

​    Vue是一套用于构建用户界面的渐进式框架。与其它大型框架不同的是，Vue被设计为可以自底向上逐层应用。Vue的核心库只关注视图层，不仅易于上手，还便于和第三方库或既有项目整合。另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue也完全能够为复杂的单页应用（SPA）提供驱动。

## 2、Vue常用指令

- v-bind：操作元素的 class 列表和内联样式是数据绑定的一个常见需求。因为它们都是属性，所以我们可以用 v-bind 处理它们：只需要通过表达式计算出字符串结果即可。可以简写为“：“。
- v-if和v-show：用于实现条件渲染，Vue会根据表达式的值的真假条件来渲染元素。
- v-for：用v-for指令根据遍历数组来进行渲染，需要以site in sites形式的特殊语法，sites是数组名，site的数组元素迭代的别名。
- v-on：可以用 v-on 指令监听 DOM 事件，并在触发时运行一些 JavaScript 代码。可以简写为”@“
- v-model：用 v-model 指令在表单\<input>、\<textarea> 及 \<select> 元素上创建双向数据绑定。它会根据控件类型自动选取正确的方法来更新元素。
- v-html指令用于输出html代码，数据绑定最常见的形式就是使用往双重花括号里插入的文本插值。

## 3、Vue全家桶

- Vue-cli为现代前端工作流提供了batteries-included的构建设置，只需要几分钟的时间就可以运行起来并带有热重载、保存时lint校验，以及生产环境可用的构建版本。

- Vue router是vue.js官方的路由管理器，它和vue.js的核心深度集成，让构建单页面应用变得易如反掌。使用vue.js,我们可用通过组合组件来组成应用程序，当你要把vue router添加进来，我们需要做的是，将组件（components）映射到路由（routes），然后告诉vue router在哪里渲染它们。

  \<router-link>是一个组件，该组件用于设置一个导航链接，切换不同的HTML内容，to属性是目标地址，即要显示的内容。

  replace属性，当点击的时候会调用router.replace()而不是router.push(),导航后不会留下history记录。

  append属性，则在当前（相对）路径前添加基路径。例如，我们从/a导航到一个相对路径b，如果没有配置append，则路径为/b，如果配置了，则为/a/b

  ```
  <router-link :to="{path: 'relative/path'}"append></router-link>
  ```

  tag属性，如果想要渲染某种标签，例如\<li>，于是使用tag prop类指定何种标签，同样它还是会监听点击，触发导航。

  ```
  <router-link :to="/foo" tag="li">foo</router-link>
  ```

- Vuex是一个专为vue.js应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。

- Axios是一个基于promise的http库，可以用在浏览器和node.js中。简单来说就是前端最火最简单的一种http请求解决方案。

  ```
  post方法
  new Vue({
    el: '#app',
    data () {
      return {
        info: null
      }
    },
    mounted () {
      axios
        .post('abc.php')
        .then(response => (this.info = response))
        .catch(function (error) { // 请求失败处理
          console.log(error);
        });
    }
  })
  
  ```

  ```
  get方法
  <div id="app">
    <h1>网站列表</h1>
    <div
      v-for="site in info"
    >
      {{ site.name }}
    </div>
  </div>
  <script type = "text/javascript">
  new Vue({
    el: '#app',
    data () {
      return {
        info: null
      }
    },
    mounted () {
      axios
        .get('demo.json')
        .then(response => (this.info = response.data.sites))
        .catch(function (error) { // 请求失败处理
          console.log(error);
        });
    }
  })
  </script>
  ```

  ```
  执行并发请求
  function getUserAccount() {
    return axios.get('/user/12345');
  }

  function getUserPermissions() {
    return axios.get('/user/12345/permissions');
  }
  axios.all([getUserAccount(), getUserPermissions()])
    .then(axios.spread(function (acct, perms) {
      // 两个请求现在都执行完成
    }));
  ```

## 4、Vue项目开发流程

1. 利用vue-cli脚手架构建模板框架
2. 使用html、js、css还有element-ui或者iview-ui组件库还原页面
3. 配置vue-router
4. Vuex进行状态管理
5. 用Axios获取接口，将数据正确渲染到页面上

## 5、Vue与React比较

- 开发模式不同：

  Vue采用MVVM模式的一种方式实现，没有完全遵循MVVM模型

  React是MVC模式

- 渲染方式不同：

  Vue可以更快地计算出virtual DOM的差异，这是由于它在渲染的过程中，会跟踪每一个组件的依赖关系，不需要重新渲染整个组件树。而对react而言，每当应用的状态被改变时，全部子组件都会重新渲染。当然，这可以通过shouldComponentUpdate这个生命周期方法来进行控制，但Vue将次视为默认的优化。

- 写法不同：

  Vue可以使用单文件组件，就是把html、css、js写到一个文件中。Vue使用了基于HTML的模板语法。

  在React中，一切都是javaScript。

- 使用场景不同：

  React适用于大型应用，Vue适用于小型应用。

## 6、Vue.js目录结构

| 目录/文件    | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| build        | 项目构建（webpack）相关代码                                  |
| config       | 配置目录、包括端口号等                                       |
| node_modules | npm加载的项目依赖模块                                        |
| src          | 开发目录，所做的事情都在这个目录里。其包含了以下目录和文件：assets:放置一些图片；components:目录里面放了一个组件文件；App.vue：项目入口文件；main.js：项目的核心文件 |
| static       | 静态资源目录，存放图片字体等                                 |
| test         | 初始测试目录                                                 |
| .xxxx文件    | 这些都是一些配置文件，包括语法配置，git配置等                |
| index.html   | 首页入口文件                                                 |
| package.json | 项目配置文件                                                 |
| README.md    | 项目的说明文档                                               |

## 7、Vue构造器

  ```
  var vm=new Vue({
    el: '#vue_de',
    data:{
      site:"baidu",
      url:"www.baidu.com",
      alexa:"1000"
      //等等其他属性
    }，
    methods：{
      datail：function（）{
        return this.site+“123456”;
    }，
    computed：{

    }，
    watch：{

    }

  })
  ```

el参数是DOM元素中的id。

**data** 用于定义属性，实例中有三个属性分别为：site、url、alexa。

**methods** 用于定义的函数，可以通过 return 来返回函数值。

**{{ }}** 用于输出对象属性和函数返回值。

当一个Vue实例被创建的时候，它向Vue的响应式系统中加入了其data对象中能找到的所有属性，当这些属性的值发生改变的时候，html视图将也会产生相应的变化。

除了数据属性，Vue实例还提供了一些有用的实例属性与方法，它们都有前缀$,以便与用户定义的属性区分开来。

计算属性关键词：computed，

我们可以使用methods来替代computed，从效果上来说，两个是一样的，但是computed是基于它的依赖缓存，只有相关依赖发生改变时才会重新取值。而是用methods时，在重新渲染的时候，函数总是会重新调用执行。

监听属性watch，可以通过watch来相应数据的变化。

## 8、Vue中相关知识

- 双向绑定：

  所谓双向绑定，指的是Vue实例中的data与其渲染的DOM元素的内容保持一致，无论谁被改变，另一方会相应的更改为相同的数据。

  双向绑定是在同一个组件内，将数据和视图绑定起来，和父子组件之间的通信并无关联。

- 组件系统：

  组件系统是Vue的另一个重要概念，因为它是一种抽象，允许我们使用小型、独立和通常可复用的组件构建大型应用。组件（component）是Vue最强大的功能之一，组件可以帮助你扩展基本的HTML元素，以封装可重用代码。组件中，data必须是一个函数。

  注册一个全局组件语法格式如下：

  ```
  Vue.component(tagName,options)
  ```

  tagName为组件名，options为配置选项。注册后，我们可以使用以下方式来调用组件：

  ```
  <tagName></tagName>
  ```

  prop是父组件用来传递数据的一个自定义属性，父组件的数据需要通过props把数据传给子组件，子组件需要显示地用props选项声明“prop”：

  ```
  <div id="app">
      <child message="hello!"></child>
  </div>
  <script>
  // 注册
  Vue.component('child', {
    // 声明 props
    props: ['message'],
    // 同样也可以在 vm 实例中像 "this.message" 这样使用
    template: '<span>{{ message }}</span>'
  })
  // 创建根实例
  new Vue({
    el: '#app'
  })
  </script>
  
  ```

  如果子组件要把数据传递回去，就需要使用自定义事件！

  我们可以使用 v-on 绑定自定义事件, 每个 Vue 实例都实现了事件接口(Events interface)，即：

  - 使用 `$on(eventName)` 监听事件
  - 使用 `$emit(eventName)` 触发事件

  另外，父组件可以在使用子组件的地方直接用 v-on 来监听子组件触发的事件。

- Vue常用的三种传值方式：

  1、父传子

  2、子传父

  3、非父子传值
