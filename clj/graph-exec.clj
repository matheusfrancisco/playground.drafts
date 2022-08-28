(ns q1
  (:require [clojure.pprint :as pprint]))



"
Considere o seguinte problema: Para uma empresa de entregas, ha uma s ´ erie de centrais que ´
mantem encomendas para entrega em diversas localidades. Alguns pares de localidades trocam enco- ´
mendas e outros nao. Para essa realidade, deseja-se desenvolver um algoritmo que receba uma listagem ˜
com os identificadores das centrais C = {c1, c2, . . . , cn},
 uma listagem com os pares de centrais que trocam encomendas entre si
 L = ({ca, cb}, {cc , cd}, ... (ca, cb , cc , cd ∈ C),
 uma central de origem cs ∈ C e uma central de destino ct ∈ C.
 O algoritmo deve retornar o caminho p = hcx, . . . , cyi no qual uma
encomenda seria enviada de cx para cy, no qual p passe pelo menor numero de centrais poss ´ ´ıvel. Com
base nas informacoes acima, faca:
"

(defrecord Graph [vertices])
(defrecord Vertex
    [key connections parent])

(defn centers
  "Exemple to use:
  (centers 6) => [0, 1, 2, 3, 4, 5, 6]
  time complexity: O(x)

  Since range x is lazy we had to
  consume into a collection vector
  then, it hasnt affect the complexity
  "
  [x]
  (into [] (range x)))

(defn add-vertex
  "Exemple:

  (add-vertex graph \"1\") =>
  {:vertices
    {\"1\" {:key \"1\" :connections #{} :parent nil}}
  }

  (add-vertex graph-with-1 \"2\") =>
  {:vertices
    {\"1\" {:key \"1\" :connections #{} :parent nil}}
    {\"2\" {:key \"2\" :connections #{} :parent nil}}
  }
  "
  [{:keys [vertices] :as graph} key]
  (->Graph (assoc
             vertices
             key
             (->Vertex key #{} nil))))

(defn get-vertex
  "
  time complexity: O(1)
  "
  [{:keys [vertices] :as graph} key]
  (get vertices key))

(defn add-edge-directed
  [u v]
  (assoc u :connections (conj (:connections u) (:key v))))

(defn add-edge
  [{:keys [vertices] :as graph} u v]
  (->Graph
     (-> vertices
         (assoc (:key u) (add-edge-directed u v))
         (assoc (:key v) (add-edge-directed v u)))))


(defn make-graph
  " (make-graph (centers 6)) ;; =>
    {:vertices
        {0 {:key 0, :connections #{}, :parent nil},
         1 {:key 1, :connections #{}, :parent nil},
         2 {:key 2, :connections #{}, :parent nil},
         3 {:key 3, :connections #{}, :parent nil},
         4 {:key 4, :connections #{}, :parent nil},
         5 {:key 5, :connections #{}, :parent nil}}}

  this function returns a representation of the graph withotu the
  connection, I mean without edges

  time complexity : O(centers)
  "
  [centers]
  (reduce (fn [graph center]
             (add-vertex graph center))
          (->Graph {}) centers))

(defn make-edges
  "
  Exemples:
  (let [g (make-graph (centers 6))
        g (make-edges graph [[0 1] [0 2] [1 4] [1 5] [2 3] [3 4] [4 5]])
;; => {:vertices
 {0 {:key 0, :connections #{1 2}, :parent nil},
  1 {:key 1, :connections #{0 4 5}, :parent nil},
  2 {:key 2, :connections #{0 3}, :parent nil},
  3 {:key 3, :connections #{4 2}, :parent nil},
  4 {:key 4, :connections #{1 3 5}, :parent nil},
  5 {:key 5, :connections #{1 4}, :parent nil}}}
  "
  [graph edges]
  (reduce (fn [g [u v]]
            (add-edge g
                      (get-vertex g u)
                      (get-vertex g v)))
          graph edges))

(defn print-vertex [v]
    (println (str
                    "\t" (:key v)
                    "\t- conn: " (:connections v)
                    "\t- parent: " (:parent v))))

(defn print-graph
  "
  output:
  Graph: 0	- conn: #{1 2}	- parent:
         1	- conn: #{0 4 5}	- parent:
         2	- conn: #{0 3}	- parent:
         3	- conn: #{4 2}	- parent:
         4	- conn: #{1 3 5}	- parent:
         5	- conn: #{1 4}	- parent:
  "
  [{:keys [vertices] :as graph}]
    (println "Graph:")
    (doseq [v (map val vertices)]
        (print-vertex v))
  graph)



(defn -graph-complete []
  (let [;;list-of-centers (centers 6)
        edges [[0 1] [0 2] [1 4] [1 5] [2 3] [3 4] [4 5]]
        graph (make-graph (centers 6))
        graph (make-edges graph edges)]
    (pprint/pprint graph)
    (print-graph graph)
    graph))

(defn bfs
  "
    BFS(graph, start-node)
        Marque todos os vertices no grafo como nao descobertos
        Marque o vertice origen como descoberto
        Criar uma queue FIFO (first in first out)  com o vertex de origem
        While queue is not empty::
          Pop o primeiro elemento de queue -> u
          For each vertex v adjacent u
                  Precisa processar edge(u, v)
                  If v nao foi descoberto:
                         Maquer v como descoberto
                         Set v como parent de u
                         Add v na queue
               Marque v como completamente explorado

  time complexity O( V + E )
  "
  [graph start]
  (loop [discovered clojure.lang.PersistentQueue/EMPTY
         discovered-map {(:key start) true} ;; map para marcar os vertices já descobertos
         u start  ;; start
         new-graph graph] ;; novo grafo
     (if (nil? u)
       ;;caso base quando todos os vertices foram explorados
       new-graph
       ;; queue como vizihos que nao foram descobertos
       (let [neighbor-k (filter #(not (contains? discovered-map %))
                                (:connections u)) ;; filter todas as connections já descobertas
             neighbors (map
                         #(assoc (get-vertex graph %) :parent (:key u))
                            neighbor-k) ;; add o parent no viziho
             new-discovered (as-> discovered ds
                              (into clojure.lang.PersistentQueue/EMPTY
                                    (concat ds neighbors))) ;; cria uma nova fila com os novos vizinhos para visitar
             ]
         ;;
         (println (str "Explorando vertex:" (:key u), " vizinho: " (clojure.string/join ", " neighbor-k)))
         ;; recur vai chamar o loop inicial substituindo os parametros
         (recur
           (pop new-discovered) ;; vai ser a nova queue
           (into discovered-map (map
                                  #(hash-map % true)
                                  neighbor-k)) ;;; vai ser o novo mapa de descobertos
           (peek new-discovered) ;; proximo a analisar
           (reduce #(assoc-in %1 [:vertices %2 :parent] (:key u))
                   new-graph
                   neighbor-k)))) ;; novo grafo
     ))

(defn get-path
  "
   get-path (graph, origin, end)
        list de path
        se for nil retorna a lista
            pegar o parent do end
                add na lista
            chama recursivamente para pegar o parent  do parent

  "
  [{:keys [vertices] :as graph} start end]
  (loop [next end
         path [end]]
    (let [p (-> vertices
              (get next)
              :parent)]
      (if (nil? p)
        path
        (recur
          p
          (conj path p))))))

(defn shortest-path
  [{:keys [vertices] :as graph} start end]
  (let [new-graph-with-parents (bfs graph
                                   (-> vertices
                                       (get start)))]
    (get-path new-graph-with-parents start end)))

(defn print-st-path
  [path]
  (println "Caminho: " (reduce (fn [p n]
                     (str p " -> " n))
                   ""
                   (reverse path))))

(defn -main
    []
    (let [graph (-graph-complete)
          shortest-path (shortest-path graph 0 5)]
      (print-st-path shortest-path)))


(-main)

(comment
  (-main))
