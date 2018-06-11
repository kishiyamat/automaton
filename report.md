---
documentclass: ltjsarticle
title: 言語情報解析演習I課題
author: 岸山健
id: 31-187002
date: June 11, 2018
header-includes:
    \usepackage{tikz}
---
<!--
https://www3.nd.edu/~kogge/courses/cse30151-fa17/Public/other/tikz_tutorial.pdf
https://tex.stackexchange.com/questions/20784/which-package-can-be-used-to-draw-automata
矢印が出ないと思っていたら解像度の問題でした。
-->
# Exercises

## 1. Construct a Turing machine that accepts any tape written on the vocabulary {0,1} and converts every contiguous string of two or more 1's to 0's. Everything else is left unchanged.

1が出てきたら0が出てくるまで進み、0が出てきたら左に戻り1を$q_2$状態の0に戻し、
左に戻り1を0に戻す、という過程を0が出てくるまで繰り返す。0にあたったら状態を$q_0$に戻す。
この方法だと$ (q_2, 0|\#) &\rightarrow (q_3, L)$ とするか{0,#}で別の遷移を定義するかしなくてはならない。

$$
\delta = \left\{
\begin{aligned}
(q_0, 0) &\rightarrow (q_0, R)\\
(q_0, 1) &\rightarrow (q_1, R)\\
(q_1, 0) &\rightarrow (q_0, R)\\
(q_1, 1) &\rightarrow (q_2, R)\\
(q_2, 1) &\rightarrow (q_2, R)\\
(q_2, 0|\#) &\rightarrow (q_3, L)\\
(q_3, 1) &\rightarrow (q_2, 0)\\
(q_3, 0) &\rightarrow (q_0, 0)
\end{aligned}
\right\}
$$

## 2. Construct a Turing machine with three states {$q_0,q_1,q_2$},initial state,$q_0$, that begins with an input tape consisting entirely of blanks and halts with exactly three contiguous 1's on the tape.

初期状態を$q_0$とする3つの状態を持ち、入力は#のみのテープ。これを3つの1に書き換えて止まる様なTuring machineを作る、という解釈をしました。
最初から3つ#を1に変えて初期状態に戻して動かなくなります。

$$
\delta = \left\{
\begin{aligned}
(q_0, \#) &\rightarrow (q_1, 1)\\
(q_1, 1) &\rightarrow (q_1, R)\\
(q_1, \#) &\rightarrow (q_2, 1)\\
(q_2, 1) &\rightarrow (q_2, R)\\
(q_2, \#) &\rightarrow (q_0, 1)
\end{aligned}
\right\}
$$

