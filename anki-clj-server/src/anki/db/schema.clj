(ns anki.db.schema)
;; - 3 define schema schema
;; Mandatory
;; - ident => ex: user/full-name
;; - value type ex: string/long/uuid
;; - cardinality ex: one or many
;; Optional
;; - doc
;; - identity
;; - index
(def schema
  [{:db/ident       :user/id
    :db/valueType   :db.type/uuid
    :db/cardinality :db.cardinality/one
    :db/unique      :db.unique/identity
    :db/doc "Id of the User"}
   {:db/ident       :user/email
    :db/valueType   :db.type/string
    :db/cardinality :db.cardinality/one
    :db/unique      :db.unique/identity
    :db/doc "Email of the User"}
   {:db/ident       :user/username
    :db/valueType   :db.type/string
    :db/cardinality :db.cardinality/one
    :db/unique      :db.unique/identity
    :db/doc "Username of the User"}
   {:db/ident       :user/password
    :db/valueType   :db.type/string
    :db/cardinality :db.cardinality/one
    :db/unique      :db.unique/identity
    :db/doc "Hashed Password of the User"}
   {:db/ident       :user/token
    :db/valueType   :db.type/string
    :db/cardinality :db.cardinality/one
    :db/unique      :db.unique/identity
    :db/doc "Token of the User"}])

;## User
;    - id           (uuid)
;- full-name    (string)
;- username     (string)
;- email        (string => unique)
;- password     (string => unique)
;- token        (string)
;
;
;## Topics
;    - id              (uuid)
;- author       (Ref)
;- title        (string)
;- tags         (vector of strings)
;
;
;## Cards
;    - id              (uuid)
;- topic           (Ref)
;- front           (string)
;- back            (string)
;- progress        (long)
;- next-study-date (date|instant)