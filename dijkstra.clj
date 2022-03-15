(ns q2
  (:require [clojure.data.priority-map :as pp]
            [clojure.pprint :as pprint]))

"
Considere um grafo dirigido e ponderado G = (V, A, w) representando um mapa com as distancias.
Em G, V e um conjunto de localidades, ´ A o conjunto de arcos e w a funcao de distancia de um arco em
km. Considere a funcao p como o valor cobrado de pedagio em reais em passar por uma
localidade. Deseja-se desenvolver um algoritmo que receba um grafo G, uma funcao p, um vertice de origem s ∈ V, um vertice de destino t ∈ V, preco do combustıvel, a autonomia em km por litro e retorne
a rota de menor custo considerando o valor gasto em viagem. Com base nas informacoes acima, faca:
"

(defn ->graph
  "
  (def v [[\"Sao Paulo\" 1] [\"Floripa\" 2] [\"Jales\" 3] [\"Fernandopolis\" 4] [\"Sao Francisco\" 5]])
  Exemple: (-> graph v)
   => {\"Sao Paulo\" {:w 1 :connections {}},
        \"Fernandopolis\" {:w 2 :connectinos {}},
        \"Floripa \"{:w 3 :connections {}},
        \"Sao Francisco \"{:w 4 :connections {}},
        \"Jales\" {:w 5 :connections {}}}

  w -> it is the pedagio price

  time complexity: O(v)
  "
  [vertices]

  (reduce merge (map (fn [[v w]]
                       (hash-map v {:w w :connections {}}))
                     vertices)))

(defn remove-keys [m pred]
  (select-keys m (filter (complement pred) (keys m))))

(defn map-vals [m f]
  (into {} (for [[k v] m]
             [k (f v)])))

(defn kml-price [km]
  ;; this functions it to calculate the price
  ;; consider 10km/l
  ;; 1l -> 2.5 Reais
  (if (zero? km)
    km
    (let [l (/ km 10)
          p (* 2.5 l)]
      p)))

(defn min-value [v1 v2]
  (if (< (first v1)
         (first v2))
    v1
    v2))

(defn dijkstra
  [graph start]
  (loop [q (pp/priority-map-keyfn first start [0 nil])
         r {}]
    (if-let [[v [d u]] (peek q)]
      (let [e (graph v)
            pedagio-price (e :w)
            connections (e :connections)
            dist-price (-> connections
                           (remove-keys r) ;; remove todo mundo que já foi visto
                           (map-vals (fn [km]
                                       (let [new-cost
                                             ;;new-coas é d o valor do custo anterior + kml-price
                                             (+ d (kml-price km) pedagio-price)]
                                         ;;return new-coast vertice
                                         [new-cost v]))))]
        (recur
          (merge-with
            min-value (pop q) dist-price) ;;; pega com o menor price, que nao foi marcado como visto ainda
          (assoc r v [d u]) ;; add no mapa {vertice [price vertice] ..}
          ))
      r)))

(defn create-edges
  [edges]
  (->> edges
       (map (fn [edge]
              (hash-map (nth edge 0)
                        (hash-map (nth edge 1) (nth edge 2)))))
       (reduce (fn [connections ej]
                 (let [key (-> ej keys first)
                       connection (get connections key)]
                   (if (nil? connection)
                     (merge connections
                            (assoc connections key (get ej key)))
                     (merge connections
                            {key (merge connection
                                        (get ej key))})))) {})))

(defn make-graph
  [vertices edges]
  (let [g (->graph vertices)]
   (reduce-kv (fn [g k v]
                (-> g
                    (assoc-in [k :connections] v)))
              g
              (create-edges edges))))

(defn path-to [goal dik]
  (if (contains? dik goal)
    (reverse (take-while identity
                         (iterate (comp second dik) goal)))
    nil))

(defn cost-to [goal dik]
  (if (contains? dik goal)
    (first (dik goal))
    -1))

(defn -main [_]
  ;; vertices é uma collection [["A, valor-do-pedagio] ... ]
  (let [vertices [["Sao Paulo" 1] ["Floripa" 2]
                  ["Jales" 3] ["Fernandopolis" 4] ["Sao Francisco" 5]]
        ;; edges with weigth [Sao Paulo Floripa 100] Sao Paulo -> 100 -> Floripa
        edges [["Sao Paulo" "Floripa" 100] ["Floripa" "Sao Francisco" 200]
               ["Jales" "Sao Francisco" 20] ["Sao Francisco" "Fernandopolis" 40]
               ["Sao Paulo" "Jales" 82] ["Jales" "Floripa" 230]
               ["Fernandopolis" "Jales" 30]]
        g (make-graph vertices edges)

        ;;Dijkstra with priority heap (fib heap)
        dj (dijkstra g "Sao Paulo")]

    (pprint/pprint g)
    (pprint/pprint "====")
    (pprint/pprint dj)
    (pprint/pprint "====")
    (pprint/pprint (str "Path -> " (path-to "Sao Francisco" dj)))
    (pprint/pprint (str "Custo: " (cost-to "Sao Francisco" dj)))))






(comment

  ;;only to interact with clojure repl in dev mode
  (let [v [["Sao Paulo" 1] ["Floripa" 2]
           ["Jales" 3] ["Fernandopolis" 4] ["Sao Francisco" 5]]

        edges [["Sao Paulo" "Floripa" 100] ["Floripa" "Sao Francisco" 200]
               ["Jales" "Sao Francisco" 20] ["Sao Francisco" "Fernandopolis" 40]
               ["Sao Paulo" "Jales" 82] ["Jales" "Floripa" 230]
               ["Fernandopolis" "Jales" 30]]

        ej (create-edges edges)
        g (->graph v)
        gf (reduce-kv (fn [g k v]
                        (-> g
                            (assoc-in [k :connections] v)))
            g
            (create-edges edges))]
    (pprint/pprint gf))


  (-main nil)

)
