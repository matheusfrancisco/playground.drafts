(ns api.logic.utils)

(defrecord Point [x y])

(defn create-point
  "Create a new point"
  [position-x position-y]
  (->Point position-x position-y))

(defonce orientation-sides
  {:up    (create-point  0 -1)
   :right (create-point  1 0)
   :down  (create-point  0 1)
   :left  (create-point -1 0)})

(defrecord Direction [orientation position])

(defn create-direction-oriented
  "Create a  new direction"
  [orientation directions]
  (map->Direction
    {:orientation orientation
     :position (orientation directions)}))

(defn direction-with-4-sides
  "Create a direction with 4 sides"
  [orientation]
  (create-direction-oriented orientation orientation-sides))



