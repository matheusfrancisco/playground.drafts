(ns clj-algos.graph)

(defn dfs [g]
  [])

(defn make-graph-adj [n]
  (let [graph ()]
    graph))

(defn find-word [matrix word]
  (let [m (count matrix)
        n (count (first matrix))
        found? (atom false)]
    (defn search [row col index]
      (when (and (< row m) (< col n) (< index (count word))
                 (not @found?)
                 (= (str (get-in matrix [row col])) (str (get word index))))
        (if (= index (dec (count word)))
          (reset! found? true)
          (do (search (inc row) col (inc index))
              (search row (inc col) (inc index))
              (search (dec row) col (inc index))
              (search row (dec col) (inc index))))))
    (search 0 0 0)
    @found?))

(comment
  (find-word  [["t", "h", "i", "s", "i", "s", "a"],
               ["s", "i", "m", "p", "l", "e", "x"],
               ["b", "x", "x", "x", "x", "e", "b"],
               ["x", "o", "g", "g", "l", "x", "o"],
               ["x", "x", "x", "D", "T", "r", "a"],
               ["R", "E", "P", "E", "A", "d", "x"],
               ["x", "x", "x", "x", "x", "x", "x"],
               ["N", "O", "T", "R", "E", "-", "P"],
               ["x", "x", "D", "E", "T", "A", "E"]] "this")

  (make-graph-adj [[1, 0], [1, 2], [2, 3], [1 4]]))
