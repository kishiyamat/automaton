---
documentclass: ltjsarticle
title: 言語情報解析演習I課題
author: 岸山健
id: 31-187002
date: July 2, 2018
header-includes:
    \usepackage{tikz}
---
<!--
https://www3.nd.edu/~kogge/courses/cse30151-fa17/Public/other/tikz_tutorial.pdf
https://tex.stackexchange.com/questions/20784/which-package-can-be-used-to-draw-automata
矢印が出ないと思っていたら解像度の問題でした。
-->
# Exercises

## 1. Construct context sensitive grammars for each of the following languages:

a. CBの繋がりをBCに書き換えます。

$$
R = \left\{
\begin{aligned}
S &\rightarrow AN \\
N &\rightarrow bC \\
S &\rightarrow ASN \\
\epsilon A &\rightarrow \epsilon a \\
aA &\rightarrow aa \\
C \epsilon &\rightarrow c \epsilon \\
Cc &\rightarrow cc \\
aB &\rightarrow ab \\
CB &\rightarrow CC^\prime \\
CC^\prime &\rightarrow BC^\prime \\
BC^\prime &\rightarrow BC \\
bB &\rightarrow bb \\
\end{aligned}
\right\}
$$

b. 上の入れ替え規則をA--B間、A--C間にもつくれば自由に入れ替えられ、abcが同数の文字列を生成できます。しかし終端器号まで派生させられた場合の書き換え規則を思いつきませんでした。

$$
R = \left\{
\begin{aligned}
S &\rightarrow AN \\
N &\rightarrow bC \\
S &\rightarrow ASN \\
\epsilon A &\rightarrow \epsilon a \\
aA &\rightarrow aa \\
C \epsilon &\rightarrow c \epsilon \\
Cc &\rightarrow cc \\
aB &\rightarrow ab \\
CB &\rightarrow CC^\prime \\
CC^\prime &\rightarrow BC^\prime \\
BC^\prime &\rightarrow BC \\
bB &\rightarrow bb \\
AB &\rightarrow A^\prime B \\
A^\prime B &\rightarrow B^\prime A \\
B^\prime A &\rightarrow BA \\
AC &\rightarrow A^\prime C \\
A^\prime C &\rightarrow C^\prime C \\
C^\prime C &\rightarrow CA \\
\end{aligned}
\right\}
$$

c. 未回答
