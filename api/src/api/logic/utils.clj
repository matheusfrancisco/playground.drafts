(ns api.logic.utils)

(defrecord Point [x y])

(defn create-point
  "Create a new point"
  [position-x position-y]
  (->Point position-x position-y))
