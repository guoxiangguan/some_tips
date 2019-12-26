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
* set cursorcolumn: 设置高亮列
* set cursorline: 设置高亮行
* highlight CursorLine   cterm=NONE ctermbg=black ctermfg=green guibg=NONE guifg=NONE: 设置高亮行的颜色配置
* highlight CursorColumn cterm=NONE ctermbg=black ctermfg=green guibg=NONE guifg=NONE: 设置高亮列的颜色配置
```
# 个人配置
set nu                                                                                                                                   
set ruler
set showcmd
set incsearch
set autoindent
filetype plugin indent on
set cursorcolumn "设置高亮列"
set cursorline "设置高亮行"
"美化vim配色"
highlight CursorLine   cterm=NONE ctermbg=black ctermfg=green guibg=NONE guifg=NONE
highlight CursorColumn cterm=NONE ctermbg=black ctermfg=green guibg=NONE guifg=NONE
```

## 对比差异修改
* vimdiff file1,file2 [file3 \[file4\]]: 进入比较模式, 使用垂直分割, 若要水平分割, 则加上 -o 参数
* :\[range\]diffg\[et\] \[bufspec\]: 用另一个缓冲区来修改当前缓冲区, 消除不同之处
* :\[range\]diffp\[ut\] \[bufspec\]: 用当前缓冲区来修改另一个缓冲区, 消除不同之处
* \[count\]do: 同 :diffget, 但没有范围, 给出的 \[count\] 用作 :diffget 的 \[bufspec\] 参数
* dp: 同 :diffput, 但没有范围
* 注意: 当没有给定 \[range\] 时, 受影响的仅是当前光标所处位置或其仅上方的差异文本
* zo: 展开折叠的部分
* [c: 反向跳转至上一处更改的开始, 计数前缀使之重复执行相应次
* ]c: 正向跳转至下一个更改的开始, 计数前缀使之重复执行相应次

## 跳转
