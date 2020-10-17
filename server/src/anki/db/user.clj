(ns anki.db.user
  (:require [datomic.api :as d]
            ;[clojure.string :as str]
            [anki.db.core :refer [conn]]
            [clojure.spec.alpha :as s]
            [clojure.test.check.generators :as gen]))

;pattern #"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
(defn validate-email [email]
  (let [email-regex #".+\@.+\..+"]
     (re-matches email-regex email)))

(s/def :user/password
  (s/with-gen
    (s/and string? #(>= (count %) 6))
    #(s/gen #{"123123" "123123123" "1231412444"})))

(s/def :user/username
  (s/with-gen
    string?
    #(s/gen #{"Xico" "Xiquinho"})))

(s/def :user/email
  (s/with-gen
    (s/and string? validate-email)
    #(s/gen #{"xico@gmail.comm" "xicolino@gmail.com"})))

(s/def :user/token
  (s/with-gen
     string?
     #(s/gen #{"sadfasf" "safasfsadfas" "adfsafdafsafs"})))

(s/def :user/id uuid?)

(s/def ::user
  (s/keys :req [:user/email :user/password]
          :opt [:user/id :user/token :user/username]))


;; To create user, the following values are required
;; - email
;; - password
;; Rest are optional values

(defn create! [conn user-params]
   (if (s/valid? ::user user-params)
     (let [user-id (d/squuid)
           tx-data (merge user-params {:user/id user-id})]
        (d/transact conn [tx-data])
        user-id)
     (throw (ex-info "User is invalid"
                     {:anki/error-id :validation
                      :error "Invalid email or password provided"}))))

;; fetch a user by id
(defn fetch
  ([db user-id]
    (fetch db user-id '[*]))
  ([db user-id pattern]
   (d/q '[:find (pull ?uid pattern) .
          :in $ ?user-id pattern
          :where
          [?uid :user/id ?user-id]]
        db user-id pattern)))

;; edit a user by ID
(defn edit!
   [conn user-id user-params]
   (if-let [user (fetch (d/db conn) user-id)]
     (let [tx-data (merge user-params {:user/id user-id})
           db-after (:db-after @(d/transact conn [tx-data]))]
        (fetch db-after user-id))
     (throw (ex-info "Unable to update user"
                     {:anki/error-id :server-error
                      :error "Unable to edit user"}))))


(comment
  (let [user-id (create! conn (gen/generate (s/gen ::user)))
        user (fetch (d/db conn) user-id '[*])]
       (prn user))

  (def sample-user {:user/email    "matheusmachadoufsc@gmail.com"
                    :user/username "xico"
                    :user/password "123123"})


  (s/valid? ::user sample-user)
  ;;generated random data
  ;; with-gen and s/gen

  ;; with-gen accepts two args
  ;; 1/ spec
  ;; 2/ function
  (gen/generate (s/gen :user/email))
  ;;this is powerfull stuf
  (gen/generate (s/gen ::user)))