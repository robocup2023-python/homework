## 1. 介绍

### 1.1. 为什么要做类型注解

随着项目越来越大，代码也就会越来越多，在这种情况下，如果没有类型注解，我们很容易不记得某一个方法的入参类型是什么，一旦传入了错误类型的参数，再加上python是解释性语言，只有运行时候才能发现问题， 这对大型项目来说是一个巨大的灾难。

### 1.2. typing模块的作用

自python3.5开始，PEP484为python引入了**类型注解(type hints)** 机制。 主要作用如下：

- **类型检查**，防止运行时出现参数和返回值类型、变量类型不符合。
- 作为开发文档附加说明，方便使用者调用时传入和返回参数类型。
- 该模块加入后并不会影响程序的运行，不会报正式的错误，只有提醒。pycharm目前支持typing检查，参数类型错误会黄色提示

**官网typing详细说明**： [typing类型标注](https://link.zhihu.com/?target=https%3A//docs.python.org/zh-cn/3/library/typing.html%23module-typing)

### 1.3. 在IDE里面使用类型注解

因为类型注释的检查是IDE来完成的，所以不同的IDE有不同的方式。PyCharm已经做的很智能了，我们基本上不用操作什么。但是如果使用VSCode，我们需要自己来处理一些事情。

在VSCode中 类型注解是通过mypy库来实现的，所以首先要安装mypy库：

```bash
python -m pip install mypy
```

安装完成后，可以在命令行通过使用mypy来进行类型注解检查，但这样比较麻烦，很少有人这么做。  
通常，我们会将这个功能配置在VSCode里面， 由VSCode在我们编写代码的时候自动进行检查。

方法是在VSCode的配置文件中增加下面的键值对：

```json
"python.linting.mypyEnabled": true,
```

## 2. 对常用类型的类型注解分别进行介绍

### 2.1. int, str等基础类型的类型注解

最简单的使用方式：

<figure data-size="normal"><div><img src="https://pic3.zhimg.com/80/v2-cbca86d9bc331821611fd1f46822748a_1440w.webp" data-size="normal" data-rawwidth="710" data-rawheight="316" class="origin_image zh-lightbox-thumb lazy" width="710" data-original="https://pic3.zhimg.com/v2-cbca86d9bc331821611fd1f46822748a_r.jpg" data-actualsrc="https://pic3.zhimg.com/v2-cbca86d9bc331821611fd1f46822748a_b.jpg" data-original-token="v2-7d6d11d87fa768469f34152dc7faaad7" height="316" data-lazy-status="ok"></div><figcaption>示例代码2-1</figcaption></figure>

类型注解就是在参数后面通过冒号的方式加入了类型的说明， 代码简单解释：

- `a: int`: 指定了输入参数a为int类型，
- `b: str`: 指定了输入参数b为str类型，
- `-> str`: 指定了test函数的返回值为srt类型

可以看到上面一共有两处有告警（有背景色的算告警，波浪线的是因为中间应该有两个空行，但是我只写了一个）:

- 在test函数定义中， 我们最终返回了一个`int`，此时pycharm就会有警告（因为我们定义了返回值为str）；
- 在test函数调用时， 参数 `a` 我们输入的是字符串，此时也会有警告(因为我们定义了`a`的类型为int)；

> 但非常重要的一点是，pycharm只是提出了警告，但实际上运行是不会报错。这其实是python这种语言在工程实践中的一种非常优雅的处理方式：  
> - 新的功能（Type Hints）不会影响原来的代码（如果变为强制报错，那原来写的代码就都不能运行了）  
> - 即使不适用新的功能（Type Hints）代码也可以正常运行

### 2.2. list、tuple等简单复合类型的类型注解的介绍