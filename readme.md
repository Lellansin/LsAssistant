LsAssistant
===========

编程学习助手。sublime text 编辑器插件。

配置
-----------

【Tools】-> 【LsAssistant 编程助手】 -> 【功能 默认设置】，接着出来的文件中将 gcc 启动脚本目录填上，如下：
<pre>
{
	// 输入编译器启动脚本路径 (注意 '\' 字符需要转义成 '\\' 或者换成 '/')
	"compiler_path" : "D:\\gcc\\MinGW\\open_distro_window.bat"
}
</pre>
填好之后 Ctrl+S 保存接着就可以开始编写程序了。


编写
-------------
我们可以 Ctrl+N 新建一个 .c 文件，也可以跑到你要放代码的目录下 右键新建【文本文件】然后将文本文件改成 .c 文件再用 sublime 来编辑。内容输入我们的第一个程序：

hello.c
<pre>
#include <stdio.h>
int main()
{
    printf("你好, 世界");
}
</pre>

输入完毕之后，按下 【F5】 或者 【ctrl+alt+o】 就可以调用我们的 gcc 运行脚本启动并切换到 【当前工作目录】 下。

<pre>
# 查看当前目录下的文件
dir
# 编译我们刚写的 hello.c 并生成可执行文件 exe
gcc hello.c
# 可以查看到新生成的 a.exe
dir
# 回车运行我们刚刚写的程序
a.exe
</pre>


CMD下如何显示UTF8编码
-------------

1、打开CMD.exe命令行窗口

2、通过 chcp命令改变代码页，UTF-8的代码页为65001
<pre>chcp 65001 </pre>
执行该操作后，代码页就被变成UTF-8了。但是，在窗口中仍旧不能正确显示UTF-8字符。

3、修改窗口属性，改变字体
在命令行标题栏上点击右键，选择"属性"->"字体"，将字体修改为True Type字体"Lucida Console"，然后点击确定将属性应用到当前窗口。