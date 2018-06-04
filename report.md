---
documentclass: ltjsarticle
title: 言語情報解析演習I課題
author: 岸山健
id: 31-187002
date: June 4, 2018
header-includes:
    \usepackage{tikz}
---
<!--
https://www3.nd.edu/~kogge/courses/cse30151-fa17/Public/other/tikz_tutorial.pdf
https://tex.stackexchange.com/questions/20784/which-package-can-be-used-to-draw-automata
矢印が出ないと思っていたら解像度の問題でした。
-->
# Exercises

## 1. Construct context free grammars generating each of the following languages:

(a) $L_1 = a^nb^ma^n(n,m \geq 1)$

> $S \rightarrow aSa$

> $S \rightarrow bS$

> $S \rightarrow b$

(b) $L_2 = a^nb^na^mb^m(n,m \geq 1)$

> $S \rightarrow AA$

> $S \rightarrow ab$

> $S \rightarrow aAb$

(c) $L_3 = \{ x \mbox{ | } x \in \{a,b\}^* \mbox{and }x\mbox{ contains twice as many } b \mbox{'s as }a \mbox{'s}\}$

> $S \rightarrow e$

> $S \rightarrow aBB$

> $S \rightarrow bAB$

> $S \rightarrow bBA$

> $A \rightarrow aS$

> $B \rightarrow bS$

(d) $L_4 = \{xx^R \mbox{ | } x \in \{a,b\}^* \}$

> $S \rightarrow e$

> $S \rightarrow aSa$

> $S \rightarrow bSb$

(e) $L_5 = \{x \in \{a,b\}^* \mbox{ | } x = x^R \}$

> $S \rightarrow e$

> $S \rightarrow a$

> $S \rightarrow b$

> $S \rightarrow aSa$

> $S \rightarrow bSb$

## 4

CFGが生成する$L$があり、$L^R$はCFGの右辺にreverseの操作を行なった結果の右辺で生成できると仮定するならば、
CFGはreverseされてもCFGであるためreverseに対してclosedである。
