---
title:
---



## 入口

```js
'use strict';

var assign = require('object-assign');

hexo.config.category_generator = assign({
  per_page: typeof hexo.config.per_page === 'undefined' ? 10 : hexo.config.per_page
}, hexo.config.category_generator);

// 注册category钩子
hexo.extend.generator.register('category', require('./lib/generator'));
```


# 其他

`.travis.yml`

```yml
language: node_js
node_js:
- '0.10'
- '0.11'
- '0.12'
- iojs
script:
- npm test
after_script:
- cat ./coverage/lcov.info | ./node_modules/coveralls/bin/coveralls.js
deploy:
  provider: npm
  email: dev@adrianhaasler.com
  api_key:
    secure: OK0bKCkTZmTiexyO58dv0MqIn+WyYA/iJtnt0uhSICBT+69225UOhDJjai0kFRyBZ1ELQ0kEDaQAdyzNHavofjbp/wzXdKJMdiHJGjH0rshvsJqm4oGHJryH/LAIJ/XCFeLcte+RCfY466JJk2yqK6rh2SwiKG7RrmkL2BuCAzItW7Y7v1MaaFA2A9cX7ymPpB4qlFAgMtrVBtirUNgJEKJJA2wXTld1tceEi/TwziSVdALZA03ou7ljtW/wgmPi+1jS0+yh7Fak78TcfUc7M8Hb/Cfr1IKbXl2Z9xOAfQ1WoFcTCoXRPqo0Um9QOIaEBQlUl/oegW1rvuhPyWmU+GEUhVpZr4CcbKbsn4Nkl08OisNYUfIwoxExxaHIzvExTLKo+Mmh2x4M7ywsmS1xnWBmUSurQrCLEp3p2eXTvIVYmpsl0RZaZLU9UHBxVZ/OVfk85Leefg5k7vlbaCOM0s8Qpxq8PAUoZTN+o+uBxtcPQvNRst+Qz+xhcroSNWboc9G2hRyfKXsm7Y0K+Cg5LAvXE44n/iyHc4mZhKP0Rumxpjtk/9BhokqWAERSxe1OBjKGA5VanO5DeEHiEHcXP3+2TVtYLgvp4evYasD+VQhchZJnFhM89n9NMgpF6y88lQkLc2VPuxIroBDx1AaAZ1fnhLN8ao2qJjRe88JQ43Q=
  on:
    tags: true
    repo: ahaasler/hexo-generator-multilingual-category
    node: '0.12'
```
