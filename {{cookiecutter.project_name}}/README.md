## {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description}}



### 说明

本项目结构改自：

* [cookiecutter-flask : A Flask template with Bootstrap 3, starter templates, and working user registration.](https://github.com/sloria/cookiecutter-flask)
* [cookiecutter-flask-2: A heavier weight fork of cookiecutter-flask, with more boilerplate including forgotten password and Heroku integration](https://github.com/wdm0006/cookiecutter-flask)

感谢前人栽树。



### 快速安装

执行以下命令:

```

cd {{cookiecutter.project_name}}
pip install -r requirements/dev.txt
python manage.py server

```

然后访问: http://localhost:5000 你将会看到HelloWorld的输出



启动的时候绑定端口和主机可以参考一下命令

```

# -h 绑定主机，默认绑定为127.0.0.1,如果允许所有主机访问可以使用-h 0.0.0.0
# -p 绑定端口，默认绑定端口为5000,如果需要更改为其它端口比如8000，可以使用 -p 8000
python manage.py server -h 127.0.0.1 -p 6000

```

### 初始化数据库

你可以使用以下命令，

```

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

```

注意：默认情况使用的sqlite3数据库，如果你希望更改成mysql或postgresql，请在{{cookiecutter.project_name}}/{{cookiecutter.app_name}}/lib/settings.py设置修改



<font color='red'>备注：建议只在测试环境使用该命令，生成环境需要非常谨慎或不建议使用</font>



### 执行单元测试

你可以执行以下命令执行单元测试

```

python manage.py test

```



单元测试的文件存放在{{cookiecutter.project_name}}/tests下面



### 关于项目目录介绍

* {{ cookiecutter.project_name }}
  * requirements
    * dev.txt : 这个是开发环境的依赖配置
    * prod.txt：这个是生产环境的依赖配置
  * tests
    * conftest.py : pytest的fixture定义类
    * factories.py: 定义一些注入对象
    * test_config.py : config的单元测试类
    * test_models.py : models的单元测试类
    * test_views.py : views的单元测试类
  * {{ cookiecutter.app_name }}
    * lib
      * commands : 一些命令
      * database.py : 一些数据库常用定义
      * extensions.py : 插件
      * settings.py : 系统配置
      * utils.py : 公共方法
    * app.py ： 系统初始化配置
    * models.py ： 存放模型的类
    * services.py ：存放业务逻辑的类
    * views.py : 存放路由以及视图代码的类
  * manage.py : 服务启动文件，入口类
  * requirements.txt : 链接到生产环境的依赖配置



