(defproject api "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "EPL-2.0 OR GPL-2.0-or-later WITH Classpath-exception-2.0"
            :url "https://www.eclipse.org/legal/epl-2.0/"}
  :plugins [[lein-ring "0.12.5"]
            [lein-midje "3.2.1"]]
  :ring {:handler api.core/handler
         :auto-reload? true
         :auto-refresh? false}
  :dependencies [[org.clojure/clojure "1.10.0"]
                 [ring/ring "1.8.0"]
                 [compojure "1.6.1"]
                 [midje "1.9.9"]
                 [ring/ring-jetty-adapter "1.8.0"]
                 [ring/ring-devel "1.8.0"]
                 [ring/ring-core "1.8.0"]])
