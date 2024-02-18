# Machine Learning on Raspberry Pi Zero/Zero-W
## This repo provides a comprehensive guide and required tool to do machine learning task on Pi-Zero/Zero-W. <br>
An older version of Keras is used. Currently tensorflow adapted Keras as front-end API. 
Keras always needs a backend tensor based package for running ML algorithms. Earlier Version V1.0.0 of Keras supports 
***theano*** as backend but latest version uses Tensorflow. Officially tensorflow is not supported on Pi-Zero armV6 architecture. However, you can run inference using pre-trained TFLITE model. Here  *theano* as tensor provider which works as a backend support for Keras.<br>

1. Installing Theano using *pip* package manager<br>

```
pip3 install Theano==1.0.5
```
2. Then clone this repo and move to the parent directory and install required dependencies for Keras

```
pip install requirements.txt
```

3. Build Keras from source<br>

     Move to *keras-1.0* directory and run the following <br>

```
sudo python setup.py install
```
The setup.py script will build and install Keras. During build process you may encounter error regarding scipy and pyml but they will not hamper the operation of Keras.<br>

4. To verify the installation, open a python terminal by typing *python* and then in Python console, import keras <br>

```
import keras
keras.__version__
```
   ![image](https://github.com/charlie2951/mL_Rpi_ZeroW/assets/90516512/0982b6b8-0ade-4b60-b4ab-a6b24fe54be5)

   <br>

   Now move to the parent git directory and run the test script called *test_keras.py*. This file contain one fully connected neural network (Dense layers). It will take approx 106sec to train the network and predict. <br>

   **Note: Model training on Pi-Zero is challenging due to lower compuattional resources such as RAM size, speed etc. However, if you want to explore for fun then just go through it.** <br>
   *It is always advisable that train the model in PC/in google Colab-> convert it to Tensor flow LITE format (.tflite) and then run classification on Pi-Zero using TFLITE runtime.* 
 <br>  
Disclaimer: Source code of Keras-1.0 taken from [Keras-1 repo](https://github.com/keras-team/keras/tree/keras-1)
<br>
# Tensorflow Lite Runtime for Running model trained on Tensorflow (tested on Pi-Zero only) <br>

**Navigate to the tflite_micro_rpi0 sub-directory for detailed instruction and installation**
