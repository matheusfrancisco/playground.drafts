(ns api.logic.board)

(def rows 50)
(def cols 50)


(defn new-board
  "Return simple board size-x per size-y"
  [size-x size-y]
  {:size-x size-x :size-y size-y})


