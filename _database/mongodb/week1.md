## M101J: MongoDB for Java Developers 笔记

### class1
what count for final grade? homework & final exam

### class2
- non-relational: store data not in table like relational.   json hireachi
- schemaless: 
- mongodb is document oriented
- not support joins between collectionos, not support sql
- has dynamic shcema
- 

## 3 0 MongoDB Relative to Relational  没看懂
what features did mongodb omit inorder to retain scalability?
joins & transactions across multiple collections
not index, not secondary index


## Overview of building an app with mongodb

- spark java (a micro web framework inspired by sinatra)
- freemaker to create html views
- mongo java driver (connect to mongodb)

## install mongodb
  bin/mongod - The database process.
  bin/mongos - Sharding controller.
  bin/mongo  - The database shell (uses interactive javascript).



    $ ./mongod --help

  To run a single server database:

    $ mkdir /data/db
    $ ./mongod
    $
    $ # The mongo javascript shell connects to localhost and test database by default:
    $ ./mongo
    > help

## BSON
mondodb stores data as BSON or binary JSON  （格式转换由mongo java driver来完成）
- lightweight
- traversable 可通过的 穿越的
- efficient


## CRUD
create
read
update
delete
video.movies   movies collection in the video database

findOne m101.hw1

同一个collection中的所有doc必须有unique id
- the heart of the query language for mongodb is a query by example strategy

##
spark java embeds jetty inside of it

视频中依赖java7  sparkjava 0.9.9.4
sparkjava2必须要java8

## hw1

wget hw1....zip
unzip
mongorestore dump
mongo  # mongo shell
use m101 # swith to database m101
db.hw1.findOne()  # list all the docs in m101.hw1, 也可以db.hw1.find() 


## hw2

## hw3