

# 简介


# 为什么要用HTTPS？



HTTPS 会为您的网站建立加密的信息安全通道，保证数据传输的安全，防止传输内容被第三方冒充或篡改。

劫持

## 分类

SSL证书没有所谓的“品质”和“等级”之分，只有三种不同的类型。SSL证书需要向国际公认的证书证书认证机构（简称CA，Certificate Authority）申请。CA机构颁发的证书有3种类型：
- 域名型SSL证书（DV SSL）：信任等级普通，只需验证网站的真实性便可颁发证书保护网站；  
- 企业型SSL证书（OV SSL）：信任等级强，须要验证企业的身份，审核严格，安全性更高；
- 增强型SSL证书（EV SSL）：信任等级最高，一般用于银行证券等金融机构，审核严格，安全性最高，同时可以激活绿色网址栏。

链接：https://www.zhihu.com/question/19578422/answer/114210307



## 免费服务

[SSL 证书服务，大家用哪家的？](https://www.zhihu.com/question/19578422)


- Let's Encrypt：免费，快捷，支持多域名，三条命令即时签署+导出证书。缺点是暂时只有三个月有效期，到期需续签。  

- 又拍云免费提供 Let’s Encrypt 和 Symantec 签发的两款 DV SSL 证书，也是业内唯一一家提供两种免费证书的服务商。在又拍云平台上直接申请和管理证书。立即签署颁发，并实现了Let's Encrypt 自动续期功能。

- 腾讯的就是方便，不过时间只有一年。

- cloudflare 免费版并不是很快。而且他强制你 nameserver 指过去。反正我不想用


## coding pages提供的SSL证书

<img src="/images/raw/建站 - HTTPS - CodingPages.png">

> 注意：申请 SSL/TLS 证书需要通过 Let's Encrypt 的 HTTP 方式验证域名所有权。如果您的域名在境外无法访问 Coding Pages 的服务器，将导致 SSL/TLS 证书申请失败。

采用的`Let’s Encrypt`免费证书，有效期也是三个月。但是coding pages会自动给证书续期。

```yml
网站: blog.eson.org
验证者: Let's Encrypt
起始时间: 2018年3月1日
过期时间: 2018年5月30日
```



github pages不能直接设置https，但可以通过cdn来设置ssl，如cloudflare。

gitpage + 又拍云cdn + 又拍云https (需要自己的域名备案)


## cloudflare

### 配置CDN流程
1. 进入万网控制台
1. [修改dns服务器](https://help.aliyun.com/knowledge_detail/39845.html)，默认dns服务器 dns1.hichina.com,dns2.hichina.com，修改成cloudflare的dns服务器

> To use Cloudflare, you need to change your domain's authoritative DNS servers, which are also referred to as nameservers.

用 cloudflare,但是他要我更换 dns 服务器，更换后貌似导致域名访问不了 coding pages 的服务器了。原因是cloudflare接管DNS解析后，不支持双线部署。

### 设置https
- 在CF的Crypto页中，SSL设置为Flexible。这将允许CDN到github pages之间的访问为http。
- 现在，通过https://你的域名已经可以访问站点首页了。

### 强制https

CF提供Page Rules功能，可设置路由规则。通过规则中的`Always use https`选项，可以将用户强制跳转到https

参考 https://blog.chionlab.moe/2016/01/28/github-pages-with-https/


### 证书截图


```yml
网站: blog.eson.org
颁发给: sni90514.cloudflaressl.com  # 这个是
颁发者: COMODO ECC Domain Validation Secure Server CA 2
颁发者组织: COMODO CA Limited  # 也叫验证者
起始时间: 2018年3月9日
过期时间: 2018年9月16日
```


提供PV UV统计，

### 原理

它的原理是当访客使用 HTTPS 访问站点的时候，从访客到 Cloudflare 这段是加密的，然后从 Cloudflare 到站点这段是明文的。虽然不是全程加密，但是也能很大程度上解决中间人，如果从 Cloudflare 到站点的信道相对可靠的话


- 更改DNS服务器。这样万网域名`eson.org`中的所有配置失效，转由cloudflare提供DNS解析服务。
  - 但是cloudflare没有线路配置，也就没必要双线部署了
- DNS导向到github page之前，进行了缓存。
