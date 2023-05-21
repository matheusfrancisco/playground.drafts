(ns api.logic.board)


(defn new-board
  "Return a board of to-array-2d "
  ([size units]
   {:size size
     :units units})
  ([size]
   (new-board size #{}))
  ([]
   (new-board [50 50])))

