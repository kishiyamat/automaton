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
          edge [loop below] node {0} ()
    (q_1) edge              node {1} (q_2)
          edge [loop above] node {0} ()
    (q_2) edge              node {1} (q_0)
          edge [loop below] node {0} ();
\end{tikzpicture}
\end{figure}

(b) The set of all strings containing a total of exactly two 1's.[^no-one]

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
\end{figure}

[^no-one]:最後に１を与えないと状態の遷移ができないが、
最後に１を与えた場合はacceptしてはならない状態となるので放置で問題なく、
むしろ状態が一つ増えてしまうので放置した。

(c) The set of all strings which contain a block of at least three consecutive 1's.

\usetikzlibrary{automata,positioning}
\begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
\centering % centers the figure
\begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
   \node[state,initial]     (q_0)                  {$q_0$}; 
   \node[state]             (q_1) [right = of q_0] {$q_1$}; 
   \node[state]             (q_2) [right = of q_1] {$q_2$}; 
   \node[state,accepting]   (q_3) [right = of q_2] {$q_3$}; 
    \path[->] 
    (q_0) edge              node {1} (q_1)
          edge [loop above] node {0} ()
    (q_1) edge              node {1} (q_2)
          edge [bend left, below] node {0} (q_0)
    (q_2) edge              node {1} (q_3)
          edge [bend right, above] node {0} (q_0)
    (q_3) edge [loop above] node {0,1} ();
\end{tikzpicture}
\end{figure}

\newpage

(d) The set of all strings which contain no block of more than one consecutive 0 nor any block of more than one consecutive 1.
The set of all strrings.

\usetikzlibrary{automata,positioning}
\begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
\centering % centers the figure
\begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
   \node[state,initial,accepting] (q_0)                  {$q_0$}; 
   \node[state,accepting]         (q_1) [above right = of q_0] {$q_1$}; 
   \node[state,accepting]         (q_2) [below right = of q_0] {$q_2$}; 
   \node[state]                   (q_3) [above right = of q_2] {$q_3$}; 
    \path[->] 
    (q_0) edge [above=0.3]                   node {$e$} (q_1)
          edge [below=0.3]            node {$e$} (q_2)
    (q_1) edge                    node {1} (q_3)
          edge [above, bend right, right=0.3] node {0} (q_2)
    (q_2) edge [right]            node {0} (q_3)
          edge [above, bend right, left=0.3] node {1} (q_1)
    (q_3) edge [loop right]       node {0,1} ();
\end{tikzpicture}
\end{figure}

## 10. Draw a state diagram for a finite automaton corresponding to the following regular expressions.

(a) $010^*1$
    \usetikzlibrary{automata,positioning}
    \begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
    \centering % centers the figure
    \begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
       \node[state,initial]           (q_0)                  {$q_0$}; 
       \node[state]                   (q_1) [below = of q_0] {$q_1$}; 
       \node[state]                   (q_2) [right = of q_1] {$q_2$}; 
       \node[state,accepting]         (q_3) [above = of q_2] {$q_3$}; 
        \path[->] 
        (q_0) edge              node {0} (q_1)
        (q_1) edge              node {1} (q_2)
        (q_2) edge              node {1} (q_3)
              edge [loop right] node {0} ();
    \end{tikzpicture}
    \end{figure}

(a) $(010^*1)^*$
    \usetikzlibrary{automata,positioning}
    \begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
    \centering % centers the figure
    \begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
       \node[state,initial,accepting] (q_00)                 {$q\prime_0$}; 
       \node[state]                   (q_0) [right = of q_00] {$q_0$}; 
       \node[state]                   (q_1) [below = of q_0] {$q_1$}; 
       \node[state]                   (q_2) [right = of q_1] {$q_2$}; 
       \node[state,accepting]         (q_3) [above = of q_2] {$q_3$}; 
        \path[->] 
        (q_00)edge              node {$e$} (q_0)
        (q_0) edge              node {0}   (q_1)
        (q_1) edge              node {1}   (q_2)
        (q_2) edge              node {1}   (q_3)
              edge [loop right] node {0}   ()
        (q_3) edge [bend left, below] node {$e$} (q_0);
    \end{tikzpicture}
    \end{figure}

(a) $(010^*1)^*1$
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
              edge                    node {1} (q_4);
    \end{tikzpicture}
    \end{figure}

\newpage

(a) $(010^*1)^*1(0 \cup 1)^*$
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
       \node[state]         (q_5) [right = of q_4]{$q_5$}; 
       \node[state]         (q_6) [below right = of q_5] {$q_6$}; 
       \node[state]         (q_7) [below left = of q_5] {$q_7$}; 
       \node[state,accepting]         (q_8) [below right = of q_7] {$q_8$}; 
        \path[->] 
        (q_00)edge              node {$e$} (q_0)
              edge [bend left, above] node {$e$} (q_3)
        (q_0) edge              node {0} (q_1)
        (q_1) edge              node {1} (q_2)
        (q_2) edge              node {1} (q_3)
              edge [loop right] node {0} ()
        (q_3) edge [bend left, below] node {$e$} (q_0)
              edge                    node {1} (q_4)
        (q_4) edge              node {$e$} (q_5)
        (q_5) edge              node {$e$} (q_6)
              edge              node {$e$} (q_7)
        (q_6) edge  [left]            node {0} (q_8)
        (q_7) edge   [above]    node {1} (q_8)
        (q_8) edge [right] node {$e$} (q_5);
    \end{tikzpicture}
    \end{figure}

$(0 \cup 1)^*$に以下の遷移図を与えた場合が上となる。

\usetikzlibrary{automata,positioning}
\begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
\centering % centers the figure
\begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
   \node[state,initial,accepting]         (q_55) {$q_5\prime$}; 
   \node[state]         (q_5) [right = of q_55]{$q_5$}; 
   \node[state]         (q_6) [below right = of q_5] {$q_6$}; 
   \node[state]         (q_7) [below left = of q_5] {$q_7$}; 
   \node[state,accepting]         (q_8) [below right = of q_7] {$q_8$}; 
    \path[->] 
    (q_55) edge              node {$e$} (q_5)
    (q_5) edge              node {$e$} (q_6)
          edge              node {$e$} (q_7)
    (q_6) edge  [left]            node {0} (q_8)
    (q_7) edge   [above]    node {1} (q_8)
    (q_8) edge [right] node {$e$} (q_5);
\end{tikzpicture}
\end{figure}

もっと$(0 \cup 1)^*$を単純にすれば以下の図も可能である。

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

<!--
なぜM1のループがM1プライムになるのか。
単にQ0をFinalにするだけではだめなのか。
M2がエラーになるけど。
一般化としてEを横に置いてあるだけなのか、
（そちらのほうが美しい）
それとも他の理由があるのか。
-->
