(ns clj-algos.graph)


(defn new-graph [edges]
  (let [graph (map (fn [[u v]]
                     (prn u v)) edges)]
    graph))


(comment 
  (new-graph [[1, 0], [1, 2], [2, 3]])

  )
