# latex 教程

## latex源文件的基本框架
    \documentclass{article} % 指定文档类型
    % 导言区: 全局设置, 宏包调用等
    \begin{document} % 正文开始

    Hi, this is my first \Latex{} file.

    \end{document} % 结束
* 反斜杠开头的字符串: 排版命令
* 注解符: 百分号 %

## 源文件的基本组成
* latex 源文件: 正文 + 命令 + 注解
* latex 命令: 反斜杠开头的字符串(只含字母, 区分大小写), 可带参数  
    >\command  
    >
    >\command[option][arguments]
    * 方括号中的参数是**可选的**, 花括号中的参数是**必需的**
    * 参数可以是一个, 也可以有多个, 若有多个, 用逗号隔开
    * 部分不带参数的命令有时也称为**声明**
## 选择文档类
`\doucumentclass[选项]{文档类}`
* 必须出现在最前面, 用于指定文档的全局版式.
    * 常用的文档类有: `article`, `book`, `beamer`, `ctexart`, `ctexbook`
    * 常用的选项有:
        * 10pt(缺省值), 11pt, 12pt -> 指定基本字体的大小
        * letterpaper(缺省值), a4paper, a5paper, ...: 指定纸张的大小
        * 选项可以组合使用, 如: (相互排斥的除外)
            >\documentclass[a4paper]{article}
            >\documentclass[11pt,a4paper]{book}

## 定义新命令 
`\newcommand{新命令}{命令内容}`
* 用户也可以修改已有的命令

    `\renewcommand{已有命令}{命令内容}`

## 两个重要概念: 分组和环境
### 分组
* 有些命令只对其参数或紧跟其后的一个字符起作用
* 有些命令对后面所有的文本都起作用, 这些名称通常也称为声明
* 可以利用大括号 (即分组) 来扩展或限制命令的作用范围 
```
    1 This is \textbf bold face style.\\
    2 This is \textbf{bold face} style.\\
    3 This is \bfseries bold face style.\\
    4 This is {\bfseries bold face} style.
```
**输出结果**:
```
    This is bold face style. → \textbf 只对后面一个字符起作用
    This is bold face style. → 用分组扩展 \textbf 的作用
    This is bold face style. → \bfseries 对后面所有的文本起作用
    This is bold face style. → 用分组限制 \bfseries 的作用
```

### 环境
* 在 LATEX 中, 为了排版某些具有特定格式的文本, 需要把它们放在相应的环 境中, 如表格, 列表, 数学公式等. 基本语法为:
```
    \begin{环境名}
    .
    .
    .
    \end{环境名}
```
* 开始和结束的环境名必须一致
* 环境可以嵌套，但不能交叉
* 环境中可包含其它命令，通常这些命令只在该环境中其作用
* document 环境是 LATEX 的一个最基本的环境, 一篇文档有且只能有一个 document 环境, 正文的所有内容都必须放在 document 环境中

## 导言区
* 导言区: \documentclass 和 \begin{document} 之间的区域
* 导言区用于放置全局控制命令, 如: 调用宏包, 设置页面大小, ...
* 放在导言区的命令对整个文档都起作用
* 有些命令只能放在导言区, 如: 调用宏包, 设置页面大小
* 有些命令不能放在导言区, 如: 章节命令
* 有些命令既可以放在导言区, 也可以放在正文中, 如: 定义新命令
```
    \documentclass[11pt,a4paper]{article}
    \usepackage{amsmath} % AMS 数学公式宏包
    \usepackage{amssymb} % AMS 数学符号
    \usepackage{amsfonts} % AMS 数学字体
    \begin{document}
    The Euler equation is given by
    $$ e^{ix} \triangleq \cos(x) + i\sin(x). $$
    \end{document}
```

## 宏包
* 宏包 是对 LATEX 功能的扩展
* 宏包调用方法 (只能出现在导言区)
    * `\usepackage[选项]{宏包名}`
* 如果宏包不带选项, 则可以多个一起调用, 如:
    * \usepackage{amsmath,amssymb}
* 常用宏包:
    > ctex, geometry, fancyhdr, natbib, float, caption
    > amsmath, amssymb, amsfonts, amsthm, ntheorem, bm
    > xcolor, graphicx, subfigure, epstopdf
    > longtable, colortbl, tcolorbox, mdframed
    > algorithm, algpseudocode, listings

## 长度
* 长度 由十进制数和长度单位表示, 如: 0.5cm, 11pt, ...
* 常用长度单位
    |mm 毫米 | pt 点 / 磅|
    |----|----|
    |cm 厘米 em | 大约为大写字母 M 的宽度|   
    |in 英寸 ex | 大约为小写字母 x 的高度|
     1 in = 2.54cm = 72pt, em 和 ex 与当前字体尺寸有关  
* 弹性长度 \fill → 表示充满, 正常值为零, 但可以伸展到任何长度
* 长度设置与修改  
`\setlength{长度数据命令}{长度}`  
`\addtolength{长度数据命令}{长度}`
* 常用长度数据命令 (变量)
    ```
    \textwidth, \textheight
    \parindent, \parskip
    \hoffset, \voffset
    \baselineskip
    ```
* 长度有时也可以是负值, 如:  
 `\setlength{\hoffset}{-5mm}`

## 换行, 分段, 分页
* 换行: LATEX 会自动换行, 若需 强制换行, 可使用 \\ 或 \newline
* \\ 后面可以带 长度, 以增加当前行与新行之间的距离,
参数可正可负, 如: \\[3mm], \\[-5pt]
    > 一般情况下, 不建议使用强制换行.
* 分段: 两个连续回车 (即一个空行) 或 \par
    > 建议使用空行进行分段
* 分页: LATEX 会自动分页
* 若需 强制分页, 可用命令 \newpage 或 \clearpage
    > 一般情况下, 不建议使用强制分页.

## 行间距
* 行间距 (可以用 \setlength 修改)
* \baselineskip → 相邻两行 基线 之间的距离
* 行间距伸展因子: \baselinestretch
* 行间距伸展命令: \linespread
    ```
    1 \renewcommand{\baselinestretch}{1.2}
    2 \linespread{1.2}
    ```
* 建议用伸展因子或伸展命令来修改行间距
* 如果上述命令放在导言区时, 则直接对整篇文档起作用
* 若放在正文中, 则只有当字体尺寸发生改变时才会起作用
* 若需要立即起作用, 可在其后面加上 \selectfont

## 段间距与段落缩进
* 修改段落间距: \parskip
    >\setlength{\parskip}{长度}
* 段落缩进
* 段落首行缩进的长度 → \parindent
* 每一节的第一段首行不会自动缩进 (英文习惯)
* 解决方法: 调用 indentfirst 宏包: \usepackage{indentfirst}
* 两个相关命令
* \indent → 强制缩进
* \noindent → 不允许缩进

## 水平间距
* 强制空格: \␣
* \quad → 产生一段宽度为 1em 的水平空白
* \qquad → \quad 的两倍
* \\, → 大约为 \quad 的 3/18
* \hspace{宽度} → 产生指定宽度的水平空白
* \hspace*{宽度} → 若要在行首产生一定的空白, 则需使用此命令
* \hfill → \hspace{\fill}, 根据排版需要插入空白, 撑满整行
* \hphantom{文本内容}: 水平空白的宽度等于文本内容的总宽度

## 垂直间距
* \smallskip → 垂直空白高度为 3pt plus 1pt minus 1pt
* \medskip → \smallskip 的两倍
* \bigskip → \smallskip 的四倍
* \vspace{高度} → 产生指定高度的垂直空白
* \vspace*{高度}→ 同 \vspace, 主要同在页面的顶部
* \vfill → \vspace{\fill}
* \vphantom{文本内容} → 垂直空白的高度等于文本内容的总高度

## 特殊字符
* 有 10 个字符被赋予了特殊用途, 需要使用相应的命令才能输出  

| 字符 | # | $ | %  | { | } | ˜ | _ | ˆ | & | \ |
|-|-|-|-|-|-|-|-|-|-|-|
| 命令 | \\# | \\$ | \\% |\\{| \\} | \\˜{} | \\_{} | \\ˆ{} |\\& | \\textbackslash |

* 符号 “>”, “<”, “|” 被定义成数学符号, 只能用在数学模式中, 若要在普通文本中输出, 也需使用相应的命令

|字符 |\||< |>|
|-|-|-|-|
命令 |\textbar |\textless |\textgreater

* 引号与连字号

字符 |‘| ’| “ |” |`| -| –| —
|-|-|-|-|-|-|-|-|-|
|命令| \` (倒引号) |\'| ``| " 或'' |\ˋ{}| - |- -| - - -|

## 书写源文件时注意事项
* 中文和英文之间, 中文与数学公式之间建议留空格
* 各种环境的开始和结束命令最好独占一行
* 分段: 建议使用一个空行
* 单个回车编译时被看成是一个空格
* 多个连续的空格编译时被看成是一个空格
* 数学公式中的标点必须用英文标点

## 中文排版
* ctex 文档类: ctexart, ctexbook, ctexrep
    ```
    1 \documentclass[a4paper]{ctexart}
    2 \usepackage{amsmath,amssymb,amsfonts}
    3 \begin{document}
    4 欧拉公式是
    5 $$ e^{ix} = \cos(x) + i\sin(x).$$
    6 \end{document}
    ```

## 数学公式
* 分式: \frac{}{}
* 大写的希腊字母lambda: \varLambda
* 字母上加一个波浪: \tilde{}
* 根式: \sqrt[n]{...}
    * 例: $\sqrt[n]{a+b}$
- $\le$: \le \leq
- $\ge$: \ge \geq
- $\lfloor$: \lfloor
- $\rfloor$: \rfloor

