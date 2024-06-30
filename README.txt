main.exe的同一目录下必须要有"key.txt"文件，和documents文件夹。

"key.txt"文件中，每一行代表一个属性/标签。
documents文件夹中的每一个文件夹代表一件文物。

每个文件中需要有key中的属性的txt文件。

例，如果对文物A和文物B进行归类，并附加abc……n等若干个标签，以下为操作步骤：

1.在documents文件夹下创立一个文件夹。

2.该文件夹中保存文物A的所有内容。例如关于A文物的图片，关于A文物的描述pdf文件等任意内容。

3.在A文物中创建txt文档，文档名称为“key.txt”中的一个标签。文档内容为A对应该标签的内容。

4.重复1-3步骤对文物B进行操作。

5.点击main.exe文件，将documents中的所有文件的标签信息读取并储存到excel中。

6.对excel进行查找操作（或者叫筛选）。找到目标文件的标签及其地址。

7.将地址复制到资源管理器（或者我的电脑）的搜索栏中，然后点击回车/搜索。



以下为初始的文件结构：
---文档1
  |-main.exe （重要，必须存在）
  |-key.txt （重要，必须存在）
  |-documents index.xlsx （可以被覆盖，也可以删除后自动重新创立）
  |-documents （重要，必须存在）


以下为运行exe文件后的文件结构：
---文档1
  |-main.exe
  |-key.txt
  |-documents index.xlsx
  |-documents
     |-A文件夹
        |-标签a.txt
        |-标签b.txt
	……
        |-标签n.txt
        |-关于文物A的文档.pdf/png/jpg/word
     |-B文件夹
        |-标签a.txt
        |-标签b.txt
	……
        |-标签n.txt
        |-关于文物B的文档.pdf/png/jpg/word