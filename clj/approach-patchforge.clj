;https://gist.github.com/lsmag/03de73af220bc16480b73b2bdb7d071e
(ns patchforge.domain.logic.accounts
  (:require [patchforge.domain.entities.accounts :as entities]
            [patchforge.types.core :as types]
            [samps.match-with :refer [with]]
            [schema.core :as s]))

(s/defn ->user :- (types/result entities/User s/Str)
  [{:keys [user-id
           email
           organization
           password-hash
           created-at]}]
  (if (types/valid? entities/Email email)
    {:ok #:accounts.user{:id user-id
                         :email email
                         :password-hash password-hash
                         :created-at created-at
                         :active? false
                         :organization organization
                         :permissions #{}}}
    {:error "E-mail is not valid"}))

(s/defn conj-permission :- entities/User
  [user :- entities/User
   permission :- entities/Permission]
  (update user :accounts.user/permissions conj permission))

;; organization name must be a string that begins with
;; a letter and only has numbers, _-
(s/defn ->organization- :- entities/Organization
  [organization-id :- s/Uuid
   organization-name :- s/Str
   owner :- entities/User
   created-at :- java.time.Instant]
  #:accounts.organization{:id organization-id
                          :name organization-name
                          :created-at created-at
                          :owner #:accounts.user{:id owner-id}})

(comment
;; in the use-case
(with [user-id uuid
       organization-id organization-id
       {:ok organization} (->organization ... organization-id user-id)  ;; org-name might be invalid.
       {:ok user} (-> (->user ... ... ...)
                     (conj-permission :superuser)
                     ->active)

      ;; this function can be created later. When creating an organization,
      ;; we create it and the user at the same time.
      {:ok organization} (change-owner organization user)  ;; needs to assert that user belongs to this organization. Useless here, but still

      {:ok _} (db.accounts/add-organization db organization)  ;; it will simply not write updated-at
      {:ok _} (db.accounts/add-user db user)  ;; it will not write updated-at
      {:ok _} (db/accounts/update-organization-owner db organization)] ;; this is needed because the ownership is a separate table
    {:ok ...}
  ))


;test framework
;https://github.com/clojure-expectations/clojure-test
