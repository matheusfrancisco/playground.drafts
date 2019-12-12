(ns api.logic.dinosaurs)

(defrecord Position [x y])
(defrecord Dinosaur [id type position])

(defn create-dinosaur
  [id position]
  (map->Dinosaur
    {:id id
     :type :dinosaur
     :position position}))
