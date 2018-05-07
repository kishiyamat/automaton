---
documentclass: ltjsarticle
title: 言語情報解析演習I課題
author: 岸山健
id: 31-187002
date: May 7, 2018
header-includes:
    \usepackage{tikz}
---

# Exercises

## 3. Construct state diagrams for finite automata which accept the following language using as few states as possible:

(a) The set of all strings containing a total of *n* 1's, where *n* is congruent to 1 (modulo 3)
(i,e., the remainder when *n* is divided by 3 is 1)

<!--
https://www3.nd.edu/~kogge/courses/cse30151-fa17/Public/other/tikz_tutorial.pdf
https://tex.stackexchange.com/questions/20784/which-package-can-be-used-to-draw-automata
矢印が出ないと思っていたら解像度の問題でした。
-->

\usetikzlibrary{automata,positioning}
\begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
\centering % centers the figure
\begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
   \node[state,initial]     (q_0)                        {$q_0$}; 
   \node[state]             (q_2) [right = of q_0]       {$q_2$}; 
   \node[state,accepting]   (q_1) [above right = of q_0] {$q_1$}; 
    \path[->] 
    (q_0) edge              node {1} (q_1)
          edge [loop above] node {0} ()
    (q_1) edge              node {1} (q_2)
          edge [loop above] node {0} ()
    (q_2) edge              node {1} (q_0)
          edge [loop right] node {0} ();
\end{tikzpicture}
\caption{Caption of the FSM}
\label{fig:my_label}
\end{figure}

(b) The set of all strings containing a total of exactly two 1's.

\usetikzlibrary{automata,positioning}
\begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
\centering % centers the figure
\begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
   \node[state,initial]     (q_0)                  {$q_0$}; 
   \node[state]             (q_1) [right = of q_0] {$q_1$}; 
   \node[state,accepting]   (q_2) [right = of q_1] {$q_2$}; 
    \path[->] 
    (q_0) edge              node {1} (q_1)
          edge [loop above] node {0} ()
    (q_1) edge              node {1} (q_2)
          edge [loop above] node {0} ()
    (q_2) edge [loop above] node {0} ();
\end{tikzpicture}
\caption{Caption of the FSM}
\label{fig:my_label}
\end{figure}

(c) The set of all strings which contain a block of at least three consecutive 1's.

\usetikzlibrary{automata,positioning}
\begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
\centering % centers the figure
\begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
   \node[state,initial]     (q_0)                  {$q_0$}; 
   \node[state]             (q_1) [right = of q_0] {$q_1$}; 
   \node[state]             (q_2) [right = of q_1] {$q_2$}; 
   \node[state]             (q_3) [right = of q_2] {$q_3$}; 
   \node[state,accepting]   (q_4) [right = of q_3] {$q_4$}; 
    \path[->] 
    (q_0) edge              node {1} (q_1)
          edge [loop above] node {0} ()
          edge [loop below] node {1} ()
    (q_1) edge              node {1} (q_2)
    (q_2) edge              node {1} (q_3)
    (q_3) edge              node {1} (q_4)
          edge [loop above] node {0} ()
    (q_4) edge [loop above] node {0,1} ();
\end{tikzpicture}
\caption{Caption of the FSM}
\label{fig:my_label}
\end{figure}

(d) The set of all strings which contain no block of more than one consecutive 0 nor any block of more than one consecutive 1.

\usetikzlibrary{automata,positioning}
\begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
\centering % centers the figure
\begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
   \node[state,initial,accepting] (q_0)                  {$q_0$}; 
   \node[state,accepting]         (q_1) [right = of q_0] {$q_1$}; 
   \node[state]                   (q_2) [below = of q_0] {$q_2$}; 
   \node[state]                   (q_3) [below = of q_1] {$q_3$}; 
    \path[->] 
    (q_0) edge node {0} (q_1)
          edge node {1} ()
    (q_1) edge node {1} (q_2)
          edge node {0} ()
    (q_2) edge node {0} ();
\end{tikzpicture}
\caption{Caption of the FSM}
\label{fig:my_label}
\end{figure}
