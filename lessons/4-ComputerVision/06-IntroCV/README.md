# Introduction to Computer Vision

[Computer Vision](https://en.wikipedia.org/wiki/Computer_vision) is a discipline whose aim is to allow computers to gain high-level understanding of digital images. This is quite broad definition, because *understanding* can mean many different things, including finding object on the picture (**object detection**), understanding what is happening (**event detection**), describing picture in text, or 3D reconstruction of the scene. There are also special tasks related to human images: age/emotion estimation, face detection and identification, and 3D pose estimation, to name a few.

## [Pre-lecture quiz](https://black-ground-0cc93280f.1.azurestaticapps.net/quiz/106)

One of the simplest tasks of computer vision is **image classification**. 

Computer vision is often considered to be a branch of AI. Nowadays, most of computer vision tasks are solved using neural networks. We will learn more about special type of neural networks for computer vision, [convolutional neural networks](../07-ConvNets/README.md), throughout this section.

However, before you pass the image to a neural network, in many cases it makes sense to use some algorithmic techniques to enhance the image.

There are several Python libraries available for image processing:
* **[imageio](https://imageio.readthedocs.io/en/stable/)** can be used for reading/writing different image formats. It also support video manipulation with ffmpeg.
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** (also known as PIL) is a bit more powerful, and also supports some image manipulations, such as morphing, pallette adjustments, etc.
* **[OpenCV](https://opencv.org/)** is a powerful image processing library written in C++, which became *de facto* standard for image processing. It has convenient Python interface.
* **[dlib](http://dlib.net/)** is a C++ library that implements many machine learning algorithms, including some of the Computer Vision algorithms. It also has Python interface, and can be used for challenging tasks such as face and facial landmark detection.

## OpenCV

[OpenCV](https://opencv.org/) is considered to be *de facto* standard for image processing. It contains a lot of useful algorithms, implemented in C++. You can call OpenCV from Python as well.

A good place to learn OpenCV is [this Learn OpenCV course](https://learnopencv.com/getting-started-with-opencv/). In our curriculum, our goal is not to learn OpenCV, but show you some examples when it can be used, and how. 

### Loading Images

Images in Python can be conveniently represented by Numpy arrays. For example, grayscale image with size of 320x200 pixels would be stored in 200x320 array, and color image of the same dimension would have shape of 200x320x3 (for 3 color channels). To load an image, you can use the following code:

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

Traditionally, OpenCV uses BGR (Blue-Green-Red) encoding for color images, while the rest of Python tools use more traditional RGB. For the image to look right, you need to convert it to RGB color space, either by swapping dimensions in numpy array, or by calling OpenCV function:

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

The same `cvtColor` function can be used to perform other color space transformations, eg. convert image to grayscale, or to HSV (Hue-Saturation-Value) color space.

You can also use OpenCV to load video frame-by-frame - an example is given in the exercise [OpenCV Notebook](OpenCV.ipynb).

### Image Processing

Before feeding an image to a neural network, you may want to apply several pre-processing steps. OpenCV can do many things, including:
* **Resizing** the image using `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`
* **Blurring** the image using `im = cv2.medianBlur(im,3)` or `im = cv2.GaussianBlur(im, (3,3), 0)`
* Changing **brightness and contrast** of the image can be done by numpy array manipulations, as described [here](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv).
* Instead of adjusting brightness/contrast, it is often better to use [thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) by calling `cv2.threshold`/`cv2.adaptiveThreshold` functions. 
* Applying different [transformations](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html) to the image:
    - **[Affine transformations](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)** can be useful if you need to combine rotation, resizing and skewing to the image, and you know source and destination location of three points in the image. Affine transformations keep parallel lines parallel.
    - **[Perspective transformations](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)** can use useful when you known source and destination positions of 4 points in the image. For example, if you take a picture of a rectangular document via smartphone camera from some angle, and you want to make a rectangular image of the document itself.
* Understanding movement inside the image by using **[optical flow](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)**.
## Examples of using Computer Vision

In our [OpenCV Notebook](OpenCV.ipynb), we give some examples of when computer vision can be used to perform specific tasks:

* **Pre-processing a photograph of Braille book**. We focus on how we can use thresholding, feature detection, perspective transformation and numpy manipulations to separate individual Braille symbols for further classification by a neural network.

![Braille Image](data/braille.jpeg) | ![Braille Image Pre-processed](images/braille-result.png) | ![Braille Symbols](images/braille-symbols.png) 

> *Image from [OpenCV.ipynb](OpenCV.ipynb)*
 
* **Detecting motion in video using frame difference**. If the camera is fixed, then frames from the camera should be pretty similar to each other. Since frames are represented as arrays, just by subtracting those arrays for two subsequent frames we will get the pixel difference, which should be low for static frames, and become higher once there is substantial motion in the image.

![Image of video frames and frame differences](images/frame-difference.png)

> *Image from [OpenCV.ipynb](OpenCV.ipynb)*

* **Detecting motion using Optical Flow**. [Optical flow](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) allows us to understand how individual pixels on video frames move. There are two types of optical flow:
   - **Dense Optical Flow** computes the vector field that shows for each pixel where is it moving
   - **Sparse Optical Flow** is based on taking some distinctive features in the image (eg. edges), and building their trajectory from frame to frame.

![Image of Optical Flow](images/optical.png)

> *Image from [OpenCV.ipynb](OpenCV.ipynb)*

Read more on optical flow [in this great tutorial](https://learnopencv.com/optical-flow-in-opencv/).

## ✍️ Exercises: try OpenCV in Action

Let's do some experiments with OpenCV by exploring [OpenCV Notebook](OpenCV.ipynb)

## [Post-lecture quiz](https://black-ground-0cc93280f.1.azurestaticapps.net/quiz/206)

## [Assignment](lab/README.md)

In this lab, you will take a video with simple gestures, and your goal would be to extract up/down/left/right movements using optical flow.

<img src="images/palm-movement.png" width="30%" alt="Palm Movement Frame"/>

## Takeaway

Sometimes, relatively complex tasks such as movement detection or fingertip detection can be solved purely by computer vision. Thus, it is very helpful to know basic techniques of computer vision, and what libraries like OpenCV can do.

