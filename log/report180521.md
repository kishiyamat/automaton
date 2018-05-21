---
documentclass: ltjsarticle
title: 言語情報解析演習I課題
author: 岸山健
id: 31-187002
date: May 21, 2018
header-includes:
    \usepackage{tikz}
---
<!--
https://www3.nd.edu/~kogge/courses/cse30151-fa17/Public/other/tikz_tutorial.pdf
https://tex.stackexchange.com/questions/20784/which-package-can-be-used-to-draw-automata
矢印が出ないと思っていたら解像度の問題でした。
-->
# Exercises

## 11. Construct Type 3 grammars that generate each of the following languages. Assume a fixed terminal vocabulary $V_T=\{a,b\}$.

> 終端記号への遷移 $A \rightarrow x$ を "$A$ から final state $F$ への $x$ を入力とする遷移($A \rightarrow xF$)"とし、
> 入力の無い遷移における入力を \epsilon  とする。
> また、問では終端器号は指定されているが非終端記号は指定されていないため、
> $V_N$ を $\{S,A,B,F\}$ として一部の問に回答した。

(a) $L_1 = \{aa,ab,ba,bb\}$

    $G= \langle V_T, V_N, S, R \rangle$,
    where $V_T =\{a,b\}$; $V_N = \{S,A,B,F\}$; and

$$
R = \left\{
\begin{aligned}
S &\rightarrow aaF\\
S &\rightarrow abF\\
S &\rightarrow baF\\
S &\rightarrow bbF\\
F &\rightarrow \epsilon
\end{aligned}
\right\}
$$

\usetikzlibrary{automata,positioning}
\begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
\centering % centers the figure
\begin{tikzpicture}[shorten >=1pt,node distance=3cm,on grid,auto,thick] 
   \node[state,initial]           (S)                 {$S$}; 
   \node[state,accepting]         (F) [right = of S] {$F$}; 
    \path[->] 
    (S)edge              node {$aa,ab,ab,bb$} (F);
\end{tikzpicture}
\end{figure}

(b) $L_2 = \{x|x \mbox{ contains any number of occurence of }a\mbox{ and }b\mbox{ in any order}\}$

    $G= \langle V_T, V_N, S, R \rangle$,
    where $V_T =\{a,b\}$; $V_N = \{S,A,B,F\}$; and

$$
R = \left\{
\begin{aligned}
S &\rightarrow aS\\
S &\rightarrow bS\\
S &\rightarrow \epsilon
\end{aligned}
\right\}
$$

\usetikzlibrary{automata,positioning}
\begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
\centering % centers the figure
\begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
    \node[state,initial,accepting]           (S)                 {$S$}; 
    \path[->] 
        (S) edge [loop above] node {a,b} ();
\end{tikzpicture}
\end{figure}

<!--
授業の最後のほうでeが必要だって話を確かしてた。
ノートの73行目。
最後が B->b F1 となっている。
-->

\newpage

(c) $L_3 = \{x \mbox{contains exactly two occurrences of a, not necessarily contiguous}\}$

    $G= \langle V_T, V_N, S, R \rangle$,
    where $V_T =\{a,b\}$; $V_N = \{S,A,B,F\}$; and

\newpage

(d) L_4 =

    $G= \langle V_T, V_N, S, R \rangle$,
    where $V_T =\{a,b\}$; $V_N = \{S,A,B,F\}$; and

\newpage

(e) L_5 =

\newpage

(f) L_6 =

