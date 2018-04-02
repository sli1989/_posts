

## 加密

https://github.com/MikeCoder/hexo-blog-encrypt/blob/master/index.js#L81

```js
data.content = CryptoJS.AES.encrypt(data.content, String(data.password)).toString();
```

## 解密


https://github.com/MikeCoder/hexo-blog-encrypt/blob/master/lib/blog-encrypt.js#L8

```js
var content = CryptoJS.AES.decrypt(document.getElementById("encrypt-blog").innerHTML.trim(), pass);  // 加密
content = decodeBase64(content);
```
