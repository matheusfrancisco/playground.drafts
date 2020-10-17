(ns anki.db.user-test
  (:require [clojure.test :refer [is deftest testing use-fixtures]]
            [datomic.api :as d]
            [anki.db.user :as SUT]
            [anki.db.with-db :refer [with-db *conn*]]))

(use-fixtures :each with-db)

(deftest user
  (testing "create!"
     (let [user-params {:user/email "xico@xicao.com"
                        :user/password "password"}
           uid (SUT/create! *conn* user-params)]
        (is (not (nil? uid)))
        (is (= true (uuid? uid))))))