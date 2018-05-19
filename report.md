---
documentclass: ltjsarticle
title: 言語情報解析演習I課題
author: 岸山健
id: 31-187002
date: May 14, 2018
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
> $V_N$ を $\{S,A,B,F\}$ とする。

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

(b) $L_2 = \{x|x \mbox{contains any number of occurence of }a\mbox{ and }b\mbox{ in any order}\}$

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
$$
R = \left\{
\begin{aligned}
S &\rightarrow bS\\
S &\rightarrow aA\\
A &\rightarrow bA\\
A &\rightarrow aF\\
F &\rightarrow bF\\
F &\rightarrow \epsilon
\end{aligned}
\right\}
$$

\usetikzlibrary{automata,positioning}
\begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
\centering % centers the figure
\begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
   \node[state,initial]     (S)                  {$S$}; 
   \node[state]             (A) [right = of S] {$A$}; 
   \node[state,accepting]   (F) [right = of A] {$F$}; 
    \path[->] 
    (S) edge              node {a} (A)
          edge [loop above] node {b} ()
    (A) edge              node {a} (F)
          edge [loop above] node {b} ()
    (F) edge [loop above] node {b} ();
\end{tikzpicture}
\end{figure}

(a) $L_4 = \{\}$

$$
\left\{
\begin{aligned}
S &\rightarrow aS\\
S &\rightarrow bS\\
S &\rightarrow F
\end{aligned}
\right\}
$$

(a) $L_5 = \{\}$

($$
\left\{
\begin{aligned}
S &\rightarrow aS\\
S &\rightarrow bS\\
S &\rightarrow F
\end{aligned}
\right\}
$$

a) $L_6 = \{\}$

$$
\left\{
\begin{aligned}
S &\rightarrow aS\\
S &\rightarrow bS\\
S &\rightarrow F
\end{aligned}
\right\}
$$

\usetikzlibrary{automata,positioning}
\begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
\centering % centers the figure
\begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
   \node[state,initial]           (q_00)                 {$q\prime_0$}; 
   \node[state]                   (q_0) [right = of q_00]{$q_0$}; 
   \node[state]                   (q_1) [below = of q_0] {$q_1$}; 
   \node[state]                   (q_2) [right = of q_1] {$q_2$}; 
   \node[state]                   (q_3) [above = of q_2] {$q_3$}; 
   \node[state,accepting]         (q_4) [right = of q_3] {$q_4$}; 
    \path[->] 
    (q_00)edge              node {$e$} (q_0)
          edge [bend left, above] node {$e$} (q_3)
    (q_0) edge              node {0} (q_1)
    (q_1) edge              node {1} (q_2)
    (q_2) edge              node {1} (q_3)
          edge [loop right] node {0} ()
    (q_3) edge [bend left, below] node {$e$} (q_0)
          edge                    node {1} (q_4)
    (q_4) edge [loop right] node {0,1} ();
\end{tikzpicture}
\end{figure}
