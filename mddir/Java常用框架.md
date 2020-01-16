Java常用框架

## Docker
首先需要区分容器和虚拟机。
大家可能对虚拟机更了解一点，例如不想装双系统，就下载VMware或者是VisualBox来装另一个系统。传统虚拟机需要模拟整台机器包括硬件，每台虚拟机都要有自己的操作系统，虚拟机一旦被开启，预分配给它的资源将全部被占用，每台虚拟机包括应用、必要的二进制和库、以及一个完整的用户操作系统。而容器技术是和我们的宿主机共享硬件资源及操作系统，可以实现资源的动态分配。容器包含应用和其所有的依赖项，但是与其他容器共享内容。容器在宿主机操作系统中，在用户空间以分离的进程运行。
容器技术是实现操作系统虚拟化的一种途径，可以让您在资源受到隔离的进程中运行应用程序及其依赖关系，通过使用容器，我们可以轻松打包应用的代码、配置和依赖关系，将其变成容易使用的构建块，从而实现环境一致性、运行效率、开发人员生产力和版本控制等诸多目标。容器可以帮助保证应用程序快速、可靠、一致地部署，期间不受部署环境的影响。容器还赋予我们对资源更多的精细化控制能力，让我们的基础设施效率更高。

![image-20191217115640203](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20191217115640203.png)

Docker属于Linux容器的一种封装，提供简单易用的容器使用接口，这是目前最流行的Linux容器解决方案。Linux容器不是模拟一个完整的操作系统，而是对进程进行隔离，相当于是在正常进程的外面套了一个保护层。对于容器里面的进程来说，它接触到的各种资源都是虚拟的，从而实现与底层系统的隔离。
Docker将应用程序与该程序的依赖打包在一个文件里面，运行这个文件，就会生成一个虚拟容器。程序在这个虚拟容器里运行就好像在真实的物理机上运行一样。简单来说，有了docker，就不用担心环境问题了。
总结：Docker的接口相当简单，用户可以方便地创建和使用容器，把自己的应用放入容器。容器还可以进行版本管理、复制、分享、修改，就像管理普通的代码一样。
### Docker的优势
Docker相比于传统虚拟化方式具有更多的优势：
- docker 启动快速属于秒级别。虚拟机通常需要几分钟去启动
- docker 需要的资源更少， docker 在操作系统级别进行虚拟化， docker 容器和内核交互，几乎没有性能损耗，性能优于通过 Hypervisor 层与内核层的虚拟化
- docker 更轻量， docker 的架构可以共用一个内核与共享应用程序库，所占内存极小。同样的硬件环境， Docker 运行的镜像数远多于虚拟机数量，对系统的利用率非常高
- 与虚拟机相比， docker 隔离性更弱， docker 属于进程之间的隔离，虚拟机可实现系统级别隔离
安全性： docker 的安全性也更弱。 Docker 的租户 root 和宿主机 root 等同，一旦容器内的用户从普通用户权限提升为root权限，它就直接具备了宿主机的root权限，进而可进行无限制的操作。虚拟机租户 root 权限和宿主机的 root 虚拟机权限是分离的，并且虚拟机利用如 Intel 的 VT-d 和 VT-x 的 ring-1 硬件隔离技术，这种隔离技术可以防止虚拟机突破和彼此交互，而容器至今还没有任何形式的硬件隔离，这使得容器容易受到攻击
- 可管理性： docker 的集中化管理工具还不算成熟。各种虚拟化技术都有成熟的管理工具，例如 VMware vCenter 提供完备的虚拟机管理能力
- 高可用和可恢复性： docker 对业务的高可用支持是通过快速重新部署实现的。虚拟化具备负载均衡，高可用，容错，迁移和数据保护等经过生产实践检验的成熟保障机制， VMware 可承诺虚拟机 99.999% 高可用，保证业务连续性
- 快速创建、删除：虚拟化创建是分钟级别的， Docker 容器创建是秒级别的， Docker 的快速迭代性，决定了无论是开发、测试、部署都可以节约大量时间
- 交付、部署：虚拟机可以通过镜像实现环境交付的一致性，但镜像分发无法体系化。 Docker 在 Dockerfile 中记录了容器构建过程，可在集群中实现快速分发和快速部署

![image-20191217123614661](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20191217123614661.png)

镜像是 Docker 运行容器的前提，仓库是存放镜像的场所，可见镜像更是 Docker 的核心。
Docker 镜像可以看作是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像不包含任何动态数据，其内容在构建之后也不会被改变。

镜像（Image）就是一堆只读层（read-only layer）的统一视角，也许这个定义有些难以理解，下面的这张图能够帮助读者理解镜像的定义。

![image-20191217123746472](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20191217123746472.png)
从左边我们看到了多个只读层，它们重叠在一起。除了最下面一层，其它层都会有一个指针指向下一层。这些层是Docker 内部的实现细节，并且能够在主机的文件系统上访问到。统一文件系统 (union file system) 技术能够将不同的层整合成一个文件系统，为这些层提供了一个统一的视角，这样就隐藏了多层的存在，在用户的角度看来，只存在一个文件系统。我们可以在图片的右边看到这个视角的形式。

Container (容器)

容器 (container) 的定义和镜像 (image) 几乎一模一样，也是一堆层的统一视角，唯一区别在于容器的最上面那一层是可读可写的。

![image-20191217124015655](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20191217124015655.png)

由于容器的定义并没有提及是否要运行容器，所以实际上，容器 = 镜像 + 读写层。

Repository (仓库)

`Docker` 仓库是集中存放镜像文件的场所。镜像构建完成后，可以很容易的在当前宿主上运行，但是， 如果需要在其它服务器上使用这个镜像，我们就需要一个集中的存储、分发镜像的服务，`Docker Registry` (仓库注册服务器)就是这样的服务。有时候会把仓库 `(Repository)` 和仓库注册服务器 `(Registry)` 混为一谈，并不严格区分。`Docker` 仓库的概念跟 `Git` 类似，注册服务器可以理解为 `GitHub` 这样的托管服务。实际上，一个 `Docker Registry` 中可以包含多个仓库 `(Repository)` ，每个仓库可以包含多个标签 `(Tag)`，每个标签对应着一个镜像。所以说，镜像仓库是 `Docker` 用来集中存放镜像文件的地方类似于我们之前常用的代码仓库。

通常，**一个仓库会包含同一个软件不同版本的镜像**，而**标签就常用于对应该软件的各个版本** 。我们可以通过`<仓库名>:<标签>`的格式来指定具体是这个软件哪个版本的镜像。如果不给出标签，将以 `latest` 作为默认标签.。

仓库又可以分为两种形式：

- `public`(公有仓库)
- `private`(私有仓库)

`Docker Registry` 公有仓库是开放给用户使用、允许用户管理镜像的 `Registry` 服务。一般这类公开服务允许用户免费上传、下载公开的镜像，并可能提供收费服务供用户管理私有镜像。

除了使用公开服务外，用户还可以在本地搭建私有 `Docker Registry` 。`Docker` 官方提供了 `Docker Registry`镜像，可以直接使用做为私有 `Registry` 服务。当用户创建了自己的镜像之后就可以使用 `push` 命令将它上传到公有或者私有仓库，这样下次在另外一台机器上使用这个镜像时候，只需要从仓库上 `pull` 下来就可以了。

我们主要把 `Docker` 的一些常见概念如 `Image` ， `Container` ， `Repository` 做了详细的阐述，也从传统虚拟化方式的角度阐述了 `docker` 的优势，我们从下图可以直观地看到 `Docker` 的架构：

![image-20191217123836348](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20191217123836348.png)

 `Docker` 使用 `C/S` 结构，即**客户端/服务器**体系结构。 `Docker` 客户端与 `Docker` 服务器进行交互，Docker服务端负责构建、运行和分发 `Docker` 镜像。 `Docker` 客户端和服务端可以运行在一台机器上，也可以通过 `RESTful` 、 `stock` 或网络接口与远程 `Docker` 服务端进行通信。 



![image-20191217123848641](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20191217123848641.png)

 这张图展示了 `Docker` 客户端、服务端和 `Docker` 仓库（即 `Docker Hub` 和 `Docker Cloud` ），默认情况下`Docker` 会在 `Docker` 中央仓库寻找镜像文件，这种利用仓库管理镜像的设计理念类似于 `Git` ，当然这个仓库是可以通过修改配置来指定的，甚至我们可以创建我们自己的私有仓库。 

![image-20191217124338239](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20191217124338239.png)



































### MyBatis
MyBatis是一款优秀的持久层框架，它支持定制化SQL、存储过程以及高级映射。MyBatis避免了几乎所有的JDBC代码和手动设置参数以及获取结果集。MyBatis可以使用简单的XML或者注解来配置和映射原生类型、接口和java的POJO（Plain Old Java Objects，普通老式Java对象）为数据库中的记录。
MyBatis的安装非常简单，只需精mybatis-x.x.x.jar文件置于classpath中即可，
如果使用Maven来构建项目，则需要将下面的dependency代码置于pom.xml文件中：
```
<dependency>
  <groupId>org.mybatis</groupId>
  <artifactId>mybatis</artifactId>
  <version>x.x.x</version>
</dependency>
```
#### 从XML中构建SqlSessionFactory
每个基于MyBatis的应用都是以一个SqlSessionFactory的实例为核心的，SqlSessionFactory的实例可以通过SqlSessionFactoryBuilder获得，而SqlSessionFactoryBuilder则可以从XML配置文件或一个预先定制的Configuration的实例构建出SqlSessionFactory的实例。



### 用Spring Boot开发API接口
采用Spring Boot搭建项目，借用Swagger2列出API接口，便于查阅。
#### 返回格式
API接口要求返回的格式是**application/json**,我们知道网页返回的格式一般是**text/html**，因此Spring Boot为写接口，提供了两种实现方式：类注解和方法注解。
- **类注解**@RestController
我们只需要在类是上写上注解@RestController，那么此Controller返回格式就是**text/json**。
```
@RestController
@RequestMapping("/api")
public class APIController {
	@RequestMapping("/get-info")
	public String getInfo() {
		return "";
	}
}
```
- **方法注解**@ResponseBody
我们只需要在某个方法上写上注解@ResponseBody,那么该方法返回格式就是**text/json**。
```
@Controller
@RequestMapping("/api")
public class APIController {
	@RequestMapping("/get-info")
	@ResponseBody
	public String getInfo() {
		return "";
	}
}
```
@RestController的源码：
```
@Controller
@ResponseBody
public @interface RestController{}
```
#### 请求方式
@RequestMapping
在其源码中提到，这种支持任意请求方式，类似自适应。
```
@Mapping
public @interface RequestMapping{}
```
@GetMapping
客户端只能用GET方式请求，适用于查询数据
```
@RequestMapping(method = RequestMethod.GET)
public @interface GetMapping{}
```
@PostMapping
客户端只能用POST方式请求，适用于提交数据
```
@RequestMapping(method = RequestMethod.DELETE)
public @interface DeleteMapping{}
```
@PutMapping
客户端只能用PUT方式请求，使用于修改数据
```
@RequestMapping(method = RequestMethod.PUT)
public @interface PutMapping{}
```
#### 接收参数
@RequestParam
示例：
```
public String getInfo(@RequestParam(name = "param",
									required = false,
									defaultValue = "param default value") String param)
```
name代表提交参数名，
required意思是这个参数是否必需，默认true，没有该参数，无法调用此方法；这里设为false，有无该参数都可以调用。
defaultValue如果该参数值为空，那么就是用默认值
@PathVariable
```
@RequestMapping("/get-info/{param}")
public String getInfo(@PathVariable("param") Object param)
```
我们可以在请求方法后面直接跟值，省去了**？参数名=**。
这种一般配合@DeleteMapping、@PutMapping使用
@RequestHeader
这个使用了获取提交数据的Headers的值，用来接收TOKEN.



## 人生苦短，Let‘s Go
---
Go是一个开源的编程语言，它能让构造简单、可靠且高效的软件变得容易。其用途：Go语言被设计成一门应用于搭载Web服务器，存储集群或类似用途的巨型中央服务器的系统编程语言。对于高性能分布式系统领域而言，Go语言无疑比大多数其它语言有着更高的开发效率。它提供了海量并行的支持，这对于游戏服务端的开发而言是再好不过了。
特点：
1. 简洁、快速、安全
2. 并行、有趣、开源
3. 内存管理、数组安全、编译迅速

Go 语言最主要的特性：
- 自动垃圾回收
- 更丰富的内置类型
- 函数多返回值
- 错误处理
- 匿名函数和闭包
- 类型和接口
- 并发编程
- 反射
- 语言交互性

Go 语言的基础组成有以下几个部分：
- 包声明
- 引入包
- 函数
- 变量
- 语句 & 表达式
- 注释

### 第一个Go程序
hello.go
```
package main
import "fmt"

func main() {
	fmt.Println("hello world!")
}

```
	第一行代码 package main 定义了包名。你必须在源文件中非注释的第一行指明这个文件属于哪个包，如：package main。package main表示一个可独立执行的程序，每个 Go 应用程序都包含一个名为 main 的包。
	下一行 import "fmt" 告诉 Go 编译器这个程序需要使用 fmt 包（的函数，或其他元素），fmt 包实现了格式化 IO（输入/输出）的函数。
	下一行 func main() 是程序开始执行的函数。main 函数是每一个可执行程序所必须包含的，一般来说都是在启动后第一个执行的函数（如果有 init() 函数则会先执行该函数）。
	下一行 /*...*/ 是注释，在程序执行时将被忽略。单行注释是最常见的注释形式，你可以在任何地方使用以 // 开头的单行注释。多行注释也叫块注释，均已以 /* 开头，并以 */ 结尾，且不可以嵌套使用，多行注释一般用于包的文档描述或注释成块的代码片段。
	下一行 fmt.Println(...) 可以将字符串输出到控制台，并在最后自动增加换行字符 \n。
	使用 fmt.Print("hello, world\n") 可以得到相同的结果。
	Print 和 Println 这两个函数也支持使用变量，如：fmt.Println(arr)。如果没有特别指定，它们会以默认的打印格式将变量 arr 输出到控制台。
	当标识符（包括常量、变量、类型、函数名、结构字段等等）以一个大写字母开头，如：Group1，那么使用这种形式的标识符的对象就可以被外部包的代码所使用（客户端程序需要先导入这个包），这被称为导出（像面向对象语言中的 public）；标识符如果以小写字母开头，则对包外是不可见的，但是他们在整个包的内部是可见并且可用的（像面向对象语言中的 protected ）。
运行方式： go run hello.go
也可以使用go build命令来生成二进制。
	注意：不能将**{**单独放在一行
### Go 标记
Go程序可以有多个标记组成，可以是关键字、标识符、常量、字符串、符号。
在Go程序中，一行代表一个语句结束。每个语句不需要想C家族中的其他语言一样以分号；结尾，因为这些工作都将有Go编译器自动完成。
注释不会被编译，每个包都应该有相关注释。
单行注释是最常见的注释方式，也可以使用/**/ 
标识符用来命名变量、类型等程序实体。一个标识符实际上就是一个或者是多个字母（A~Z和a~z）数字（0~9）、下划线（_）组成的序列，但是第一个字符必须是字母或是下划线而不能是数字。
Go语言的字符串可以通过（+）实现
下面列举了 Go 代码中会使用到的 25 个关键字或保留字：

break	default	func	interface	select
case	defer	go	map	struct
chan	else	goto	package	switch
const	fallthrough	if	range	type
continue	for	import	return	var
除了以上介绍的这些关键字，Go 语言还有 36 个预定义标识符：

append	bool	byte	cap	close	complex	complex64	complex128	uint16
copy	false	float32	float64	imag	int	int8	int16	uint32
int32	int64	iota	len	make	new	nil	panic	uint64
print	println	real	recover	string	true	uint	uint8	uintptr

### Go语言数据类型
在Go编程语言中，数据类型用于声明函数的变量。数据类型的出现时为了把数据分成所需内存大小不同的数据，编程的时候需要用大数据的时候才需要申请大内存，就可以充分利用内存了。
数据类型：
1. 布尔型 true或false，例如var b bool = true;
2. 数字类型 整型int和浮点型float32、float64，并且支持复数，其中位的运算采用补码。
3. 字符串类型 字符串可由单个字节连接起来
4. 派生类型 ：
	- 指针类型（Pointer）
	- 数组类型
	- 结构化类型（struct）
	- Channel类型
	- 函数类型
	- 切片类型
	- 接口类型（interface）
	- Map类型

###  Go语言变量与常量
声明变量的一般形式是使用var关键字：
```
var identifier type
var identifier1,identifier2 type
```
实例：
```
package main
import "fmt"
func main() {
	var a string = "Runoob"
	fmt.Println(a)
	var b, c int = 1, 2
	fmt.Println(b, c)
}
```
也可以使用：=来自动判断类型
常量中的数据类型只可以是布尔型、数字型（整数型、浮点型和复数）和字符串型。
常量的定义格式：
```
const identifier [type] = value
```
iota,特殊常量，可以认为是一个可以被编译器修改的常量。
### Go语言运算符
- 算法运算符
- 关系运算符
- 逻辑运算符
- 位运算符
- 赋值运算符
- 其他运算符

条件语句基本与C无异，而循环语句有三种形式，只有其中的一种使用分号。
```
for init; condition; post { }
for condition { }
for { }
```
for循环的range格式可以对slice、map、数组、字符串等进行迭代循环，格式如下：
```
for key, value := range oldMap {
	newMap[key] = value
}
```
### Go语言函数与数组
函数是基本的代码块，用于执行一个任务。
Go语言最少有个main()函数，可以通过函数来划分不同功能，逻辑上每个函数执行的是指定的任务。
函数声明告诉了编译器函数的名称，返回类型和参数。
函数定义格式：
```
func function_name( [parameter list] ) [return_types] {
	函数体
}
```
数组是具有相同唯一类型的一组已编号且长度固定的数据项序列，这种类型可以是任意的原始类型例如整型、字符串或者自定义类型。
语法格式：
```
var variable_name [SIZE] variable_type
```
### Go语言指针与结构体
Go语言的取地址符是&，放到一个变量前使用就会返回相应变量的内存地址。
一个指针变量指向了一个值的内存地址。
类似于变量和创两，在使用变量前你需要声明指针：
```
var var_name *var-type
```
当一个指针被定义后没有分配到任何变量时，他的值为nil。
nil指针也称为空指针，nil在概念上相当于其他语言的null、None、nil、NULL，都指代零值或空值。

Go语言中数组可以存储同一类型的数据，但在结构体中我们可以为不同项定义不同的数据类型。
结构体是由一系列具有相同类型或不同类型的数据构成的数据集合。
结构体表示一项记录，比如保存图书馆的书籍记录，每本书有以下属性：
- Title：标题
- Author：作者
- Subject：学科
- ID：书籍ID
定义结构体需要使用type和struct语句。struct语句定义一个新的数据类型，结构体中有一个或多个成员。type语句设定了结构体的名称。其格式如下：
```
type struct_variable_type struct {
	member definition
	member definition
	...
	member definition
}
```
一旦定义了结构体类型，它就能用于变量的声明，语法格式如下：
```
variable_name := structure_variable_type { value1, value2...valuen}
```
访问结构体成员需要使用点号操作符
### Go语言切片（Slice）
Go语言切片是对数组的抽象，
Go数组的长度不可改变，在特定场景中这样的集合就不适用了，Go中提供了一种灵活、功能强悍的内置类型切片（“动态数组”），与数组相比切片的长度是不固定的，可以追加元素，在追加时可能使切片的容量增大。
**定义切片**：
可以声明一个未指定大小的数组来定义切片：
```
var identifier []type
```
切片不需要说明长度或使用make()函数来创建切片：
```
var slice1 []type = make([]type, len)
也可以简写为
slice1 := make([]type, len)
```
也可以指定容量，其中capacity为可选参数。
```
make([]T, length, capacity)
```
### Go语言类型转换与接口
类型转换用于将一种数据类型的变量转换为另外一种类型的变量。
```
type_name(expression)
```
Go 语言提供了另外一种数据类型即接口，它把所有的具有共性的方法定义在一起，任何其他类型只要实现了这些方法就是实现了这个接口。
```
/* 定义接口 */
type interface_name interface {
   method_name1 [return_type]
   method_name2 [return_type]
   method_name3 [return_type]
   ...
   method_namen [return_type]
}

/* 定义结构体 */
type struct_name struct {
   /* variables */
}

/* 实现接口方法 */
func (struct_name_variable struct_name) method_name1() [return_type] {
   /* 方法实现 */
}
...
func (struct_name_variable struct_name) method_namen() [return_type] {
   /* 方法实现*/
}
```
### Go错误处理与并发
Go 语言通过内置的错误接口提供了非常简单的错误处理机制。
error类型是一个接口类型，这是它的定义：
```
type error interface {
    Error() string
}

func Sqrt(f float64) (float64, error) {
    if f < 0 {
        return 0, errors.New("math: square root of negative number")
    }
    // 实现
}

result, err:= Sqrt(-1)

if err != nil {
   fmt.Println(err)
}
```
Go 语言支持并发，我们只需要通过 go 关键字来开启 goroutine 即可。
goroutine 是轻量级线程，goroutine 的调度是由 Golang 运行时进行管理的。
goroutine 语法格式：
```
go 函数名( 参数列表 )
go f(x, y, z)
//开启一个新的 goroutine:
f(x, y, z)
```
Go 允许使用 go 语句开启一个新的运行期线程， 即 goroutine，以一个不同的、新创建的 goroutine 来执行一个函数。 同一个程序中的所有 goroutine 共享同一个地址空间。

通道（channel）是用来传递数据的一个数据结构。
通道可用于两个 goroutine 之间通过传递一个指定类型的值来同步运行和通讯。操作符 <- 用于指定通道的方向，发送或接收。如果未指定方向，则为双向通道。
示例：
```
package main

import "fmt"

func sum(s []int, c chan int) {
        sum := 0
        for _, v := range s {
                sum += v
        }
        c <- sum // 把 sum 发送到通道 c
}

func main() {
        s := []int{7, 2, 8, -9, 4, 0}

        c := make(chan int)
        go sum(s[:len(s)/2], c)
        go sum(s[len(s)/2:], c)
        x, y := <-c, <-c // 从通道 c 中接收

        fmt.Println(x, y, x+y)
}
```

