# PaintingStyleDetector: AI-based Painting Style Recognition
PaintingStyleDetector is an AI model capable of detecting the artistic style of a painting. Users can upload a painting, and the AI will identify the painting style, such as Baroque, Romanticism, Fauvism, etc. The model utilizes batch normalization to enhance training speed, generalization, and stability of the neural network. The Adadelta algorithm is employed to adapt the learning rate to parameters, improving AI convergence during training.
<br><br>
Built with Python, PyTorch, Django, OpenCV, and VGG16 (CNN, Batch Normalization).

## Table of Contents
[Features](#features) <br>
[Requirement](#requirement)<br>
[Installation](#requirement)<br>
[Usage](#usage)<br>
[Contribution](#contribution)<br>


## Features
* __Painting Style Detection:__ Identify the artistic style of a painting (e.g., Baroque, Romanticism, Fauvism) using AI.
* __Batch Normalization:__ Improve training speed, generalization, and stability of the neural network.
* __Adaptive Learning Rate:__ Use the Adadelta algorithm to adapt the learning rate, enhancing AI convergence during training.

## Requirement
* Python 3.6 or higher
* PyTorch
* Django
* OpenCV
* VGG16


## Installation
```bash
git clone https://github.com/jliu0105/painting_detector_ai.git
```

## Usage
* Open the application in your browser.
* Upload a painting using the "Upload" button.
* Click the "Detect Style" button to analyze the painting.
* The AI will identify the painting style and display the result.
## Contribution
We welcome contributions from the community! If you're interested in contributing to this project, please follow these steps:

1. Fork the repository
2. Create a new branch for your changes
3. Commit your changes and push them to your fork
4. Create a pull request for your changes
