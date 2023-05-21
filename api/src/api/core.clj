(ns api.core
  (:require [ring.middleware.params :refer [wrap-params]]
            [api.service :as service])
  (:gen-class))

(def handler
  (-> service/myroutes
      wrap-params))
