---
categories:
  - demo
  - hexo
date: 2011-01-01 00:00:00
---


# Demo for No-Title


This is a post, which has no title.


Typically, we can locate this file by URL with default hexo settings.

```yml
permalink: :year/:month/:day/:title/
```

e.g. URL is as follows:
```
https://blog.eson.org/2018/03/08/demo/hexo/no-title/
```

# Trouble in hexo-abbrlink

`hexo-abbrlink` is a great plugin for hexo users. I setup `hexo-abbrlink` in my post.

In this case, url becomes
```
https://blog.eson.org/0/
```

God, I want to locate this file and add a title.
But it is not easy to do so.

# Solution

## with hexo-abbrlink log

It would be better if `hexo-abbrlink` log the post with no title. Give me a warning.

## with hexo-auto-category

In this post, you may notice that the category is `demo`, `hexo`.
`hexo-auto-category` binds folder structure to category. It is also a good way to locate your post.
