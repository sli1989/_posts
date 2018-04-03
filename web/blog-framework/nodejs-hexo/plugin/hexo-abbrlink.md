---
title: 【Hexo插件系列】permalink 永久链接 - hexo链接持久化解决方案
abbrlink: 2cc9ead
tags:
  - permalink
  - hexo
  - plugin
  - hexo-abbrlink
categories:
  - web
  - blog-framework
  - nodejs-hexo
  - plugin
date: 2018-03-28 00:00:00
---


# 背景

hexo默认的链接是`http://example.com/2013/07/14/path/hello-world/` 这种类型的，这源于站点目录下的配置`_config.yml`里的配置: `permalink: :year/:month/:day/:title/`.

这种默认配置的缺点
- 文件名是中文，导致url链接里有中文出现
- 年月日都会有分隔符，目录层次较深
- 后台路径`path`变化，会导致链接批量变化。非常影响SEO

# Hexo 默认配置

https://hexo.io/zh-cn/docs/permalinks.html

`_config.yml`

`permalink: :year/:month/:day/:title/`


## Hexo实现permalink的源码

https://github.com/hexojs/hexo/search?utf8=%E2%9C%93&q=permalink&type=



```js
// https://github.com/hexojs/hexo/blob/master/lib/plugins/filter/post_permalink.js
const _ = require('lodash');
const util = require('hexo-util');
const pathFn = require('path');
const Permalink = util.Permalink;
let permalink;

function postPermalinkFilter(data) {
  /*
  1. data变量
  data.slug是path+文件名
  data.title是post中的title

  2. meta变量
  post_title
  */

  const config = this.config;
  const meta = {
    id: data.id || data._id,
    title: data.slug,
    name: typeof data.slug === 'string' ? pathFn.basename(data.slug) : '', // 这里把path当做了basename
    post_title: util.slugize(data.title, {transform: 1}),
    year: data.date.format('YYYY'),
    month: data.date.format('MM'),
    day: data.date.format('DD'),
    i_month: data.date.format('M'),
    i_day: data.date.format('D')
  };

  if (!permalink || permalink.rule !== config.permalink) {
    permalink = new Permalink(config.permalink);
  }
  /*
  默认配置：permalink: :year/:month/:day/:title/
  对应这里的permalink变量，具体如下：
  permalink Permalink {
    rule: ':year/:month/:day/:title/',
    regex: /^(.+?)\/(.+?)\/(.+?)\/(.+?)\/$/,
    params: [ 'year', 'month', 'day', 'title' ] }

  即把meta中的这几个变量作为param，通过rule和regex转为永久链接。
  */
  const categories = data.categories;

  if (categories.length) {
    meta.category = categories.last().slug;
  } else {
    meta.category = config.default_category;
  }

  const keys = Object.keys(data);
  let key = '';

  for (let i = 0, len = keys.length; i < len; i++) {
    key = keys[i];
    if (meta.hasOwnProperty(key)) continue;

    // Use Object.getOwnPropertyDescriptor to copy getters to avoid "Maximum call
    // stack size exceeded" error
    Object.defineProperty(meta, key, Object.getOwnPropertyDescriptor(data, key));
  }

  return permalink.stringify(_.defaults(meta, config.permalink_defaults)); // 核心代码，把meta的变量，传入到
}

module.exports = postPermalinkFilter; // 重点是这个exports

```

# hexo-abbrlink插件 源码

原理：
- 注册before_post_render钩子，
- 取出来abbrlink这个属性看是否存在，存在的就不管了，
- 否则就生成连接
- 新链接写入post源文件。


入口：

```js
var hexo = hexo || {};
// 注册before_post_render钩子
hexo.extend.filter.register('before_post_render', require('./lib/logic'), 15);
```


https://github.com/rozbo/hexo-abbrlink/blob/master/lib/logic.js



```js
var crc16 = require('./crc16');
var crc32 = require('./crc32');
var model = require('./model');
var front = require('hexo-front-matter');
var fs = require('hexo-fs');

function org_get_abbrlink(data) {
    var r = data.content.match(/#\+ABBRLINK:.*\n/);
    if (r) {
        data.abbrlink = r[0].split(':')[1].trim();
    }
    else
    {
        data.abbrlink = ''
    }
        return data
}

let logic = function(data) {
    var log = this.log;
    if (data.layout == 'post') {
        let abbrlink
        if (!/.*\.org/.test(data.source)){
            abbrlink = data.abbrlink
        }
        else
        {
            abbrlink = org_get_abbrlink(data).abbrlink
        }
        if (!abbrlink) {
			var opt_alg = ((this.config.abbrlink && this.config.abbrlink.alg) ? this.config.abbrlink.alg : 'crc16');
			var opt_rep = ((this.config.abbrlink && this.config.abbrlink.rep) ? this.config.abbrlink.rep : 'dec')

      // 注意，这里采用的data.title进行的hash。
      // 很好，正合我意。可以做到path无关hash了。
			let res = (opt_alg == 'crc32' ? crc32.str(data.title) >>> 0 : crc16(data.title) >>> 0);
			//check this abbrlink is already exist then get a different one
			abbrlink = model.check(res);
			//set abbrlink to hex or dec
			abbrlink = opt_rep == 'hex' ? abbrlink.toString(16) : abbrlink;
            data.abbrlink = abbrlink;
            let postStr;
            if (!/.*\.org/.test(data.source)){
            //re parse front matter
            var tmpPost = front.parse(data.raw);
            //add new generated link
            tmpPost.abbrlink = abbrlink;
            //process post  这里要重写post，不建议这样做。有误改原文件的风险。
                postStr = front.stringify(tmpPost);
            postStr = '---\n' + postStr;
            fs.writeFileSync(data.full_source, postStr, 'utf-8');
            }
            else
            {
                postStr = data.raw.split("\n")
                postStr.splice(2,0,'#+ABBRLINK: ' + abbrlink)
                fs.writeFileSync(data.full_source, postStr.join('\n'), 'utf-8');
            }
            log.i("Generate link %s for post [%s]", abbrlink, data.title);
        }
        model.add(abbrlink);
    }
    return data
}

module.exports = logic;
```


TODO:

- 提供hash配置。比如采用date、path做hash
    - 一般用不到，我觉得
- 不局限hex，可以采用所有数字+字母。容量更大。
- link写入到了.md文件中
    - 优势：1. hexo读取方便  2. link复用，减少link的变动，利于SEO  3. 加速，不用每次重新hash
    - 缺陷：需要重写md文件，强行插入abbrlink属性。
    - 建议：与hexo动态交互，而不是把link写入到md静态文件。link的复用可以采用独立的数据文件

# 参考
