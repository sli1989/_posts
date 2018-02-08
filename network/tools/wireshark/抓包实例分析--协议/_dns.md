


抓之前最好先清一下dns缓存

```bash
# windows
$ ipconfig /displaydns  #查看本地缓存的DNS信息
$ ipconfig /flushdns  #清除本地缓存的DNS信息

# linux
$ /etc/rc.d/init.d/nscd restar
```
