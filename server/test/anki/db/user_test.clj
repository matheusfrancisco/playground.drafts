(ns anki.db.user-test
  (:require [clojure.test :refer [is deftest testing use-fixtures]]
            [datomic.api :as d]
            [anki.db.user :as SUT]
            [clojure.test.check.generators :as gen]
            [clojure.spec.alpha :as s]
            [anki.db.with-db :refer [with-db *conn*]]
            ))

(use-fixtures :each with-db)

(deftest user
  (testing "create!"
     (let [user-params {:user/email    (gen/generate (s/gen :user/email))
                        :user/password (gen/generate (s/gen :user/password))}
           user-parameters (gen/generate (s/gen ::SUT/user))
           uid (SUT/create! *conn* user-parameters)]
        (is (not (nil? uid)))
        (is (= true (uuid? uid))))))