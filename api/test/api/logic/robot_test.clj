(ns api.logic.robot-test
  (:require [clojure.test :refer :all]
            [midje.sweet :refer :all]
            [api.logic.robot :as robot]
            [api.logic.utils :as u]))


(facts "Be able to create and check position to robot"
       (fact "Create a robot with id 1 position-x 1, position-y 2 in map anda direction up"
             (robot/create-robot 1 {:x 1 :y 2} :up)
             => {:id 1
                 :type :robot
                 :position {:x 1 :y 2}
                 :direction (u/direction-with-4-sides :up)}))


