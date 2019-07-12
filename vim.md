# vim 教程

## 修改
* 连接下一行: J
* 大范围替换:
    `:[range]substitute/from/to/[flags]`
    * 例子:
        * `:%s/a/b/`:
            * % 表示作用于全部行
            * :s 命令只作用在当前行
        * `:%s/a/b/g`:
            * 对行中所有匹配点起作用, 添加 g 标记
        * `:%s/a/b/c`:
            * 每次替换前向你询问是否需要替换
        * 标志 p 用于打印出最后一个修改的行
        * `:s+one/two+one or two+`
            * 防止歧义, 用加号代替正斜杠
    * 最简单的范围表达式是 `{number}, {number}`
        * `:1,5s/this/that/g`
            * 会在 1 到 5 行执行替换命令
        * `:54s/president/fool/`
            * 如果只用一个数值, 表示某个指定的行
        * `:.,$/yes/no/`
            * 表示修改当前行到文件末的全部内容
## 标签操作集合
* :tabnew 建立对指定文件的新 tab
* :tabc 关闭当前 tab
* :tabo 关闭所有其它 tab
- :tabp 前一个
- :tabn 后一个
- 标准模式下:
    - gt, gT 可以直接在 tab 之间切换

## 配置
* set ruler: 在右下角显示当前光标的位置
* set showcmd: 在右下角显示未完成的命令
* set showmode: 在左下角显示编辑模式
* set incsearch: 在输入部分查找模式时显示相应的匹配点
* map Q gq: 定义一个键映射
* filetype plugin indent on: 1. 文件类型探测 2. 使用文件类型相关的插件 3. 使用缩进文件
* autocmd FileType text setlocal textwidth=78: 当文件类型被设置为 text 的时候, 后面的命令自动执行, 在一行长于 78 个字符的时候自动换行