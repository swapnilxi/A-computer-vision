import React from 'react'

function ImageClassifier() {
  return (
    <div>ImageClassifier
     <h2>Image Classifier steps</h2>
     <li>
        <h3>1. Data Collection</h3>
        <p>Collect a dataset of images for training and testing the model. You can use publicly available datasets or create your own.</p>
        <h3>2. Data Preprocessing- Train test split </h3>
        <p>Preprocess the images by resizing, normalizing, and augmenting them. Split the dataset into training and testing sets.</p>
        <h3>3. Train Classifier</h3>
        <p>Choose a machine learning model (e.g., CNN) and train it on the training dataset. Use techniques like transfer learning if needed.</p>
        <h3>4. Evaluate Model and test performance</h3>
        <p>Evaluate the model's performance on the testing dataset. Use metrics like accuracy, precision, recall, and F1-score.</p>
     </li>





    </div>
  )
}

export default ImageClassifier