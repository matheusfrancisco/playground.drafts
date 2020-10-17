(ns anki.db.user
  (:require [datomic.api :as d]
            [clojure.string :as str]
            [clojure.spec.alpha :as s]))

;pattern #"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
(defn validate-email [email]
  (let [email-regex #".+\@.+\..+"]
     (re-matches email-regex email)))

(s/def :user/password (s/and string? #(>= (count %) 6)))
(s/def :user/username string?)
(s/def :user/email (s/and string? validate-email))
(s/def :user/token string?)

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
           tx-data (merge {:user/id user-id} user-params)]
        (d/transact conn [tx-data])
        user-id)
     (throw (ex-info "User is invalid"
                     {:anki/error-id :validation
                      :error "Invalid email or password provided"}))))

(comment
  (def sample-user {:user/email "matheusmachadoufsc@gmail.com"
                    :user/username "xico"
                    :user/password "123123"})

  (s/valid? ::user sample-user))