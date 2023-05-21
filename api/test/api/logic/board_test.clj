(ns api.logic.board-test
  (:require [clojure.test :refer :all]
            [midje.sweet :refer :all]
            [api.logic.board :as board]))


(facts "Be able to create an empty simulation space -an empty 50 x 50 grid"
       (fact "Must be a 50x50 grid"
             (board/new-board 50 50) => {:size 50 :units 50}))


