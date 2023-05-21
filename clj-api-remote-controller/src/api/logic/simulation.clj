(ns api.logic.simulation
  (:require [api.logic.board :as b]))


(defn create-simulation
  "Create a new simulation"
  ([id title board]
  {:id id
   :title title
   :board board})
  ([id title]
   (create-simulation id title b/new-board)))
