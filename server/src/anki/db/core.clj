(ns anki.db.core
  (:require [datomic.api :as d]
            [anki.db.schema :refer [schema]]))

;; TODO
;; 1 - create a db-uri
(def database-uri "datomic:sql://anki-development?jdbc:postgresql://localhost:5432/datomic?user=datomic&password=datomic")

(defn create-conn [db-uri]
  (d/create-database db-uri)
  (let [conn (d/connect db-uri)]
       conn))

;; - 2. create a connection
(def conn (create-conn database-uri))

(comment
  ;; - 3 . create schema and transact into the database
  (def tx @(d/transact conn schema))

  (keys tx)
  (def db-before (:db-before tx))
  (def db-after (:db-after tx))

  (d/q '[:find ?doc
         :where
         [_ :db/doc ?doc]]
       db-before))
