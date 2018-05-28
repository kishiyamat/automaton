---
documentclass: ltjsarticle
title: 言語情報解析演習I課題
author: 岸山健
id: 31-187002
date: May 28, 2018
header-includes:
    \usepackage{tikz}
---
<!--
https://www3.nd.edu/~kogge/courses/cse30151-fa17/Public/other/tikz_tutorial.pdf
https://tex.stackexchange.com/questions/20784/which-package-can-be-used-to-draw-automata
矢印が出ないと思っていたら解像度の問題でした。
-->
# Exercises

## 7. Construct a non-deterministic pda which accepts every string which of the form $a^nb^n$ or of the form $a^{2n}b^n$ for all *n* $geq$ 1.

初期状態に対するaの入力でAをスタックし、bを超えた後で受理する言語を分岐させる。
分岐させる先はaでAを消費する$q_1$と
aaでAを消費する$q_2$とする。
前者は $a^nb^n$ を受理し、
後者は $a^{2n}b^n$ を受理する。
aabaaaなどは前者の場合スタックが足りず、
後者の場合は遷移する先がないため拒否される。

$K = \{q^0, q^1\}$, 

$\Sigma = \{a, b\}$, 

$\Gamma = \{A\}$, 

Initial state =  $q_0$, 
$F             =  \{q_1, q_2\}$, 

$$
\Delta              =  \left\{
                        \begin{aligned}
                        &(q_0,a,e) &\rightarrow (q_0,A)\\
                        &(q_0,b,e) &\rightarrow (q_1,e)\\
                        &(q_0,b,e) &\rightarrow (q_2,e)\\
                        &(q_1,a,A) &\rightarrow (q_1,e)\\
                        &(q_2,aa,A) &\rightarrow (q_2,e)
                        \end{aligned}
                        \right\}
$$
