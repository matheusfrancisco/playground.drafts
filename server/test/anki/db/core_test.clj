(ns anki.db.core-test
  (:require [clojure.test :refer [is deftest testing use-fixtures]]
            [anki.db.with-db :refer [with-db *conn*]]
            [anki.db.core :as SUT]))

(use-fixtures :each with-db)

(deftest conn
  (testing "create-conn"
      (is (not (nil? *conn*)))))
