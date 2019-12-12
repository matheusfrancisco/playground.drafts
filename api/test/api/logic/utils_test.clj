(ns api.logic.utils-test
  (:require [clojure.test :refer :all]
            [midje.sweet :refer :all]
            [api.logic.utils :as utils]))


(facts "Be able to create a point"
       (fact "create a new point"
             (utils/create-point 1 1) => {:x 1 :y 1}))


