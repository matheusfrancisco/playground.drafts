(ns api.logic.robot)

(defrecord Robot [id type position direction])


(defn create-robot
  "Create a robot"
  [id position orientation]
  (map->Robot
    {:id id
     :type :robot
     :position position
     :direction orientation}))
