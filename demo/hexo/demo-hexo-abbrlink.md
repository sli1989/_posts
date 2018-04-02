---
categories:
  - demo
  - hexo
date: 2000-01-01 00:00:00
tags:
  - hexo
  - plugin
  - hexo-auto-category
---


# Demo for No-Title


This is a post, which has no title.


Typically, we can locate this file by URL with default hexo settings.

```yml
permalink: :year/:month/:day/:title/
```

e.g. URL is as follows:
```
https://blog.eson.org/2000/01/01/demo/hexo/no-title/
```
It shows the full path of this post `_post/demo/hexo/no-title.md`.

# Trouble in hexo-abbrlink

`hexo-abbrlink` is a great plugin for hexo users. I setup `hexo-abbrlink` in my post.

In this case, url becomes
```
https://blog.eson.org/pub/0/
```

God, I want to locate this post and add a title. But, how can I locate my error-post?

# Solution

## with hexo-abbrlink log

It would be better if `hexo-abbrlink` log the post with no title. Give me a warning.

## with hexo-auto-category

In this post, you may notice that the category is `demo`, `hexo`.
Actually, the full path of this post is `_post/demo/hexo/no-title.md`. It really helps.

`hexo-auto-category` binds folder structure to category. It is also a good way to locate your post.


# Summary

`hexo-abbrlink` and `hexo-auto-category`
