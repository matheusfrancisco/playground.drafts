(ns api.logic.utils-test
  (:require [clojure.test :refer :all]
            [midje.sweet :refer :all]
            [api.logic.utils :as u]))


(facts "Be able to create new point"
       (fact "create a new point"
             (u/create-point 1 1) => {:x 1 :y 1}))

(facts "Be able to create direction"
       (fact "create a new up direction"
             (u/create-direction-oriented :up u/orientation-sides)
             => {:orientation :up :position {:x 0 :y -1}})

       (fact "create a direction with 4 sides")
             (u/direction-with-4-sides :up) =>
             {:orientation :up :position {:x 0 :y -1}})


