(ns api.service
  (:require [compojure.route :as route]
            [compojure.core :refer [defroutes GET]]
            [ring.middleware.params :refer [wrap-params]]
            [ring.adapter.jetty :refer [run-jetty]])
  (:gen-class))


(defroutes myroutes
  (GET "/" [] "Hello World")
  (GET "/test" [] "Testanto"))


