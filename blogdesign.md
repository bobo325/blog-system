
## blog用户表-user

| 列名                  | 类型               |      备注            |
| --------------------| ---------------   |------------------   |
| id                        | int           |  主键自增       |
| username          | varchar(100)| 组织架构ID    |
| password           | varchar(100)| 角色ID             |
| gender               |          int          |性别            |
| tel                        | varchar(100 )|         电话         |
| email                   | varchar(100) |        邮箱         |
| nickname             |     varchar(100)  |    昵称                 |

## blog内容表-article

| 列名                  | 类型               |      备注            |
| :-------------------| ---------------   |------------------   |
| id                        | int         		     |  主键自增       |
| title                     | varchar(100)              |          标题    |
| user_id                    |      int      |     作者id             |
| md_value               |          text          |文章内容            |
| html_value               |          text          |文章html内容           |
| create_time            | datetime|         发布日期        |
| update_time            | datetime|         更新日期        |
| category_name（考虑后期改为ID）  | varchar(100)          |         所属类目名称        |


## blog分类表-category

| 列名                  | 类型               |      备注            |
| --------------------| ---------------   |------------------   |
| id                        | int         		     |  主键自增       |
| name                     | varchar(100)              |          标题    |
| user_id            |       int                |         创建用户id        |
| create_time            |      datetime        |         创建类目日期        |
| update_time            |      datetime        |         修改类目日期        |

## blog标签表-label

| 列名                  | 类型               |      备注            |
| --------------------| ---------------   |------------------   |
| id                        | int         		     |  主键自增       |
| name                     | varchar(100)              |          标签名    |
| user_id            |       int                |         创建用户id        |
| create_time            |      datetime        |         创建类目日期        |
| update_time            |      datetime        |         修改类目日期        |

## blog文章标签中间表-middle

| 列名                  | 类型               |      备注            |
| --------------------| ---------------   |------------------   |
| id                        | int         		     |  主键自增       |
| article_id                     | int              |          文章id    |
| label_id            |       int                |         标签id      |