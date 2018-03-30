



# 简介

nodejs的模板引擎有EJS、Jade、Swig等。theme-next采用的swig



参考 - http://yangxiaofu.com/swig/



# Swig

## 示例

安装 Swig
```sh
$ npm install swig --save
```


创建模板
```html
<h1>{{ pagename|title }}</h1>
<ul>
{% for author in authors %}
  <li{% if loop.first %} class="first"{% endif %}>
    {{ author }}
  </li>
{% endfor %}
</ul>
```

渲染模板

```js
var swig  = require('swig');
swig.renderFile('/path/to/template.html', {
    pagename: 'awesome people',
    authors: ['Paul', 'Jim', 'Jane']
});

```

渲染结果

```html
<h1>Awesome People</h1>
<ul>
  <li class="first">Paul</li>
  <li>Jim</li>
  <li>Jane</li>
</ul>
```

## 模板使用文档

http://yangxiaofu.com/swig/docs/

### Variables 变量

```js
{{ foo.bar }}
// is equivalent to
{{ foo['bar'] }}
```

### Logic Tags  逻辑标签

```js
{% if foo %}bar{% endif %}

// Create a list of people, only if there are items in the people array
{% for person in people %}
  {% if loop.first %}<ol>{% endif %}
  <li>{{ person.name }}</li>
  {% if loop.last %}</ol>{% endif %}
{% endfor %}
```

模板`{% %}`语句与javascript的区别。

- 模板引擎  .swig -> .html   `{% %}`中的语句在后台执行。node后台可否用jquery？
- javascript是动态改变的html。`<script>`在浏览器端执行。


### Comments 注释
```js
{#
This is a comment.
It will be fully stripped and ignored during parsing.
#}

```
