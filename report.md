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
    (q_0) edge              node {0} (q_1)
          edge [loop above] node {1} ()
    (q_1) edge              node {1} (q_2)
          edge [loop above] node {0} ()
    (q_2) edge [loop above] node {0} ();
\end{tikzpicture}
\caption{Caption of the FSM}
\label{fig:my_label}
\end{figure}

## 10. Draw a state diagram for a finite automaton corresponding to the following regular expressions.

(a) $010^*1$
少なくとも０１１が必要である。
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
    \caption{Caption of the FSM}
    \label{fig:my_label}
    \end{figure}
(a) $(010^*1)^*$
ここでわざわざ${q\prime}_0$を想定する理由ですが、
恐らく$q_0$に$1^*$が合った時に$111$の様な入力を受け入れ続けてしまうからかと。
ループの処理を開始点aと終点bをスコープに取るとして、
aの頭に新しい開始点a\prime を加えてeで開始点に移動し、
終点bから開始点aへeで移動するのが副作用が０なのだと思われます。
ということは17-11と17-12の対比で説明されていました。
副作用を抑えるために、こうした設計が美しいのですね。
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
    \caption{Caption of the FSM}
    \label{fig:my_label}
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
        (q_0) edge              node {0} (q_1)
              edge [bend left, above] node {$e$} (q_3)
        (q_1) edge              node {1} (q_2)
        (q_2) edge              node {1} (q_3)
              edge [loop right] node {0} ()
        (q_3) edge [bend left, below] node {$e$} (q_0)
              edge                    node {1} (q_4);
    \end{tikzpicture}
    \caption{Caption of the FSM}
    \label{fig:my_label}
    \end{figure}
この図も可能だが不愉快。確かにノードの数は減るが、
1の後ろに繰り返し処理がつく場合とで分けなくてはならない。
定式化したほうが美しいと思います。
あと、恐らく後者は移動回数が１回増えてしまいそう。
    \usetikzlibrary{automata,positioning}
    \begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
    \centering % centers the figure
    \begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
       \node[state,initial]           (q_00)                  {$q\prime_0$}; 
       \node[state]                   (q_0) [right = of q_00] {$q_0$}; 
       \node[state]                   (q_1) [right = of q_0] {$q_1$}; 
       \node[state]                   (q_2) [right = of q_1] {$q_2$}; 
       \node[state]                   (q_3) [right = of q_2] {$q_3$}; 
       \node[state,accepting]         (q_4) [above = of q_0] {$q_4$}; 
        \path[->] 
        (q_00)edge              node {$e$} (q_0)
        (q_0) edge              node {0} (q_1)
              edge              node {1} (q_4)
        (q_1) edge              node {1} (q_2)
        (q_2) edge              node {1} (q_3)
              edge [loop above] node {0} ()
        (q_3) edge [bend left, below] node {$e$} (q_0);
    \end{tikzpicture}
    \caption{Caption of the FSM}
    \label{fig:my_label}
    \end{figure}
ループ後のルートも気になる。
多分、案２の方が紙面は取らないけど、
もし最初の１つが１だった場合、
行き先が２こできてしまう。その意味では前者が好ましい？
$(010^*1)$の処理に割り込む形の記述は嬉しくない。
冗長になるが、一貫性を保つ方が美しい。

また、０と３を同じノードにできそうな気もするが、
その場合はｑ３で
一つのモジュールとして考えたい。
最後のノードに繰り返しがついた時と付かない時で
形が変わってしまい不愉快。
確かにノードの数は一つ減るが。

多分、ループ処理の際にわざわざeを頭に足すのと同じ理屈。
(a) $(010^*1)^*1(0 \cup 1)^*$
    \usetikzlibrary{automata,positioning}
    \begin{figure}[ht] % ’ht’ tells LaTeX to place the figure ’here’ or at the top of the page
    \centering % centers the figure
    \begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto,thick] 
       \node[state,initial]           (q_00)                  {$q\prime_0$}; 
       \node[state]                   (q_0) [right = of q_00] {$q_0$}; 
       \node[state]                   (q_1) [right = of q_0] {$q_1$}; 
       \node[state]                   (q_2) [right = of q_1] {$q_2$}; 
       \node[state]                   (q_3) [right = of q_2] {$q_3$}; 
       \node[state,accepting]         (q_4) [above = of q_0] {$q_4$}; 
        \path[->] 
        (q_00)edge              node {$e$} (q_0)
        (q_0) edge              node {0} (q_1)
              edge              node {1} (q_4)
        (q_1) edge              node {1} (q_2)
        (q_2) edge              node {1} (q_3)
              edge [loop above] node {0} ()
        (q_3) edge [bend left, below] node {$e$} (q_0);
    \end{tikzpicture}
    \caption{Caption of the FSM}
    \label{fig:my_label}
    \end{figure}

<!--
なぜM1のループがM1プライムになるのか。
単にQ0をFinalにするだけではだめなのか。
M2がエラーになるけど。
一般化としてEを横に置いてあるだけなのか、
（そちらのほうが美しい）
それとも他の理由があるのか。
-->
