# sudoku.py
`sudoku.py`は通常の数独を解くためのコードです。
`board` に 問題の数字を入れる(空欄は0)ことで解を出します。

# x.py
`x.py`は対角線ナンプレを解くことができます。`sudoku.py` の`check`関数をこのコードに変更することで変えることができます。

# consecutive.py
`consecutive.py` は1つ違いナンプレを解くことができます。
`board` の後ろに `lines_beside` と `lines_vertical` を入れます。
横に隣接している線が二重線の時は `lines_beside` の該当箇所を0から1に変えます。
同様に縦に横に隣接している線が二重線の時は `lines_vertical` の該当箇所を0から1に変えます。
さらに、 `sudoku.py` の `check` 関数を変えることで解くことができます。
