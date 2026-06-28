# Week 6: Autoencoder for Image Denoising using MNIST

## 📖 Project Overview

This project implements a **Convolutional Denoising Autoencoder** using the **MNIST handwritten digit dataset**. The objective is to train the model to reconstruct clean images from noisy input images.

To achieve this, Gaussian noise is artificially added to the original MNIST images. The autoencoder learns to remove the noise and generate images that closely resemble the original handwritten digits.

---

## 🎯 Objective

- Load and preprocess the MNIST dataset.
- Normalize image pixel values.
- Add Gaussian noise to create noisy images.
- Build a Convolutional Autoencoder.
- Train the model using noisy images as input and clean images as target.
- Reconstruct denoised images.
- Compare Original, Noisy, and Reconstructed images.

---

## 📂 Dataset

**Dataset:** MNIST Handwritten Digits

- Training Images: **60,000**
- Testing Images: **10,000**
- Image Size: **28 × 28**
- Color Format: **Grayscale**

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- OpenCV (for loading PNG images)

---

## 🧠 Model Architecture

### Encoder
- Conv2D (32 filters, ReLU)
- MaxPooling2D
- Conv2D (16 filters, ReLU)
- MaxPooling2D

### Decoder
- Conv2D (16 filters, ReLU)
- UpSampling2D
- Conv2D (32 filters, ReLU)
- UpSampling2D
- Conv2D (1 filter, Sigmoid)

---

## ⚙️ Workflow

1. Load the MNIST dataset.
2. Normalize pixel values to the range [0,1].
3. Add Gaussian noise to the images.
4. Build the Convolutional Autoencoder.
5. Train the model using noisy images as input.
6. Predict denoised images.
7. Visualize the Original, Noisy, and Denoised images.
8. Plot the training and validation loss.

---

## 📊 Results

The autoencoder successfully learns to remove noise from handwritten digit images. As training progresses, both the training loss and validation loss decrease, indicating that the model effectively reconstructs clean images from noisy inputs.

The notebook includes:
- Original Images
- Noisy Images
- Denoised Images
- Training Loss Curve
- Validation Loss Curve

---

## 📈 Future Improvements

- Train for more epochs to improve reconstruction quality.
- Experiment with deeper encoder-decoder architectures.
- Test different types of image noise.
- Apply the model to real-world image denoising datasets.

---

## 📁 Repository Structure

```
Week6/
│── Week6_AkshitaSharma.ipynb
│── README.md
```

---

## 👩‍💻 Author

**Akshita Sharma**

Data Science Internship Assignment – Week 6

Celebal Technologies
