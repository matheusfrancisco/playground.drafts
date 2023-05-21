(ns api.logic.simulation-test
  (:require [clojure.test :refer :all]
            [midje.sweet :refer :all]
            [api.logic.simulation :as s]
            [api.logic.board :as b]))



(facts "Be able to create a new simulation"
       (fact "Create a simulation")
             (s/create-simulation 1 "board")
             => {:id 1 :title "board" :board b/new-board})

