(ns clj-algos.clj-algos-test
  (:require [clojure.test :refer :all]
            [clj-algos.graph :as g]))

(deftest a-test
  (testing "graph dfs algorithm"
    (let [graph (g/new-graph [[1, 0], [1, 2], [2, 3]])]
      (is (= (g/dfs graph 0) [0 1 2 3])))))
