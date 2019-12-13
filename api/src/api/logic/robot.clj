(ns api.logic.robot
  (:require
    (api.logic
      [utils :as u])))

(defrecord Robot [id type position direction])


(defn create-robot
  "Create a robot"
  [id position orientation]
  (map->Robot
    {:id id
     :type :robot
     :position position
     :direction (u/direction-with-4-sides orientation)}))


