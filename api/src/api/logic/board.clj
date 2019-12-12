(ns api.logic.board)


(defrecord Board [size units])

(defn new-board
  "Return a board of to-array-2d "
  ([size units]
  (map->Board
    {:size size
     :units units}))
  ([size]
   (new-board size #{}))
  ([]
   (new-board [50 50])))

