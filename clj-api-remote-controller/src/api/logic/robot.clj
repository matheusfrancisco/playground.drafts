(ns api.logic.robot
  (:require
    (api.logic
      [utils :as u])))


(defn create-robot
  "Create a robot"
  [id position orientation]
  {:id id
   :type :robot
   :position position
   :direction (u/direction-with-4-sides orientation)})


