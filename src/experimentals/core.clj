(ns experimentals.core
  (:require
   [clj-http.client :as http]
   [clojure.data.json :as json]
   [clojure.walk :as walk]
   [clojure.java.io :as io]))

(def access-token "")

(defn generate-img-variations-with-prompt
  [{:keys [api-key n prompt file]}]
  (let [url "https://api.openai.com/v1/images/edits"
        headers {"Authorization" (str "Bearer " api-key)}
        image-data (-> file io/input-stream)
        multipart [{:name "image"
                    :content-type "image/png"
                    :content image-data}
                   {:name "prompt" :content prompt}
                   {:name "n" :content (str n)}
                   {:name "size" :content "1024x1024"}]]
    (-> (http/post url {:headers headers
                        :multipart multipart})
        :body
        (json/read-str)
        (walk/keywordize-keys))))

(defn create-image-edits
  [{:keys [api-key n prompt file]}]
  (let [url "https://api.openai.com/v1/images/edits"
        headers {"Authorization" (str "Bearer " api-key)}
        image-data (-> file io/input-stream)
        multipart [{:name "image"
                    :content-type "image/png"
                    :content image-data}
                   {:name "prompt" :content prompt}
                   {:name "n" :content (str n)}
                   {:name "size" :content "1024x1024"}]]
    (-> (http/post url {:headers headers
                        :multipart multipart})
        :body
        (json/read-str)
        (walk/keywordize-keys))))

(defn generate-img-variations [{:keys [api-key n file]}]
  (let [url "https://api.openai.com/v1/images/variations"
        headers {"Authorization" (str "Bearer " api-key)}
        image-data (-> file io/input-stream)
        multipart [{:name "image"
                    :content-type "image/png"
                    :content image-data}
                   {:name "n" :content (str n)}
                   {:name "size" :content "1024x1024"}]]
    (-> (http/post url {:headers headers
                        :multipart multipart})
        :body
        (json/read-str)
        (walk/keywordize-keys))))

(defn generate-image-from-prompt [api-key prompt n]
  (let [url "https://api.openai.com/v1/images/generations"
        headers {"Authorization" (str "Bearer " api-key)}
        params {:prompt prompt
                :n n
                :size "1024x1024"}]
    (-> (http/post url {:headers headers
                        :content-type :json
                        :body (json/write-str params)})
        :body
        (json/read-str)
        (walk/keywordize-keys))))

(comment

  (require '[image-resizer.core :refer :all])
  (require '[image-resizer.format :as format])

  (format/as-file
   (-> (io/file "p2.png")
       (resize 400 400))
   "p3.png"
   :verbatim)

  (generate-image-from-prompt access-token "A white siamese cat" 1)

  (generate-img-variations {:api-key access-token
                            :n 6
                            :prompt "Create a world cup brazil player"
                            :file "profile.png"})

  (generate-img-variations-with-prompt {:api-key access-token
                                        :n 6
                                        :prompt "Imagine the original image as a backdrop for a World Cup celebration. Add elements such as flags, banners, and other decorations to create a lively and festive atmosphere. Use your creativity and artistic skills to make the image look vibrant and exciting, as if the World Cup is happening right there in the scene. Try to capture the energy and excitement of a World Cup event, and create a beautiful and memorable image that celebrates the beauty of the game and its global significance."
                                        :file "profile.png"})
  (create-image-edits {:api-key access-token
                       :n 6
                       :prompt "Use your creativity and artistic skills to transform the face in the original image into a series of superhero characters and beautiful scenes. Experiment with different styles, colors, and techniques to create images that are both visually striking and emotionally evocative. Try to capture the essence of each superhero character and beautiful scene, and create a collection of images that showcases your unique perspective and vision. Use your imagination and artistic flair to create a series of images that are truly one-of-a-kind."
                       :file "p3.png"})

  #_(generate-and-save-avatars (io/file "profile.jpg") "create an avatar image"))
