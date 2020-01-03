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



