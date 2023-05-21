(ns api.logic.dinosaurs)


(defn create-dinosaur
  [id position]
  {:id id
   :type :dinosaur
   :position position})
