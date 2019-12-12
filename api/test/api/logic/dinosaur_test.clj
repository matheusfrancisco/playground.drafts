(ns api.logic.dinosaur-test
  (:require [clojure.test :refer :all]
            [midje.sweet :refer :all]
            [api.logic.dinosaurs :as dino]))


(facts "Be able to create a dinosaur"
       (fact "create a dinosaur"
             (dino/create-dinosaur 1 {:x 2 :y 1}) => {:id 1 :type :dinosaur :position {:x 2 :y 1}}))


