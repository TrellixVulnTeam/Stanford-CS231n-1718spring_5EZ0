---
layout: page
mathjax: true
permalink: /assignments2018/assignment2/
---

In this assignment you will practice writing backpropagation code, and training
Neural Networks and Convolutional Neural Networks. The goals of this assignment
are as follows:

- understand **Neural Networks** and how they are arranged in layered
  architectures
- understand and be able to implement (vectorized) **backpropagation**
- implement various **update rules** used to optimize Neural Networks
- implement **Batch Normalization** and **Layer Normalization** for training deep networks
- implement **Dropout** to regularize networks
- understand the architecture of **Convolutional Neural Networks** and
  get practice with training these models on data
- gain experience with a major deep learning framework, such as **TensorFlow** or **PyTorch**.

You can follow the setup instructions [here](http://cs231n.github.io/setup-instructions/).

### Q1: Fully-connected Neural Network (20 points)
The IPython notebook `FullyConnectedNets.ipynb` will introduce you to our
modular layer design, and then use those layers to implement fully-connected
networks of arbitrary depth. To optimize these models you will implement several
popular update rules.

### Q2: Batch Normalization (30 points)
In the IPython notebook `BatchNormalization.ipynb` you will implement batch
normalization, and use it to train deep fully-connected networks.

### Q3: Dropout (10 points)
The IPython notebook `Dropout.ipynb` will help you implement Dropout and explore
its effects on model generalization.

### Q4: Convolutional Networks (30 points)
In the IPython Notebook ConvolutionalNetworks.ipynb you will implement several new layers that are commonly used in convolutional networks.

### Q5: PyTorch / TensorFlow on CIFAR-10 (10 points)
For this last part, you will be working in either TensorFlow or PyTorch, two popular and powerful deep learning frameworks. **You only need to complete ONE of these two notebooks.** You do NOT need to do both, and we will _not_ be awarding extra credit to those who do. 

Open up either `PyTorch.ipynb` or `TensorFlow.ipynb`. There, you will learn how the framework works, culminating in training a  convolutional network of your own design on CIFAR-10 to get the best performance you can.

**NOTE: Once again, at this time, the PyTorch and TensorFlow notebooks are not finalized. We will update this page with a zip file containing the two notebooks as soon as they are completed!**


### Submitting your work
There are **_two_** steps to submitting your assignment:

**1.** Submit a pdf of the completed iPython notebooks to [Gradescope](https://gradescope.com/courses/17367). If you are enrolled in the course, then you should have already been automatically added to the course on Gradescope. 

To produce a pdf of your work, you can first convert each of the .ipynb files to HTML. To do this, simply run from your assignment directory

```bash
jupyter nbconvert --to html FILE.ipynb
```
for each of the notebooks, where `FILE.ipynb` is the notebook you want to convert. Then you can convert the HTML files to PDFs with your favorite web browser, and then concatenate them all together in your favorite PDF viewer/editor. Submit this final PDF on Gradescope, and be sure to tag the questions correctly!

**Important:** _Please make sure that the submitted notebooks have been run and the cell outputs are visible._


**2.** Submit a zip file of your assignment on AFS. To do this, run the provided `collectSubmission.sh` script, which will produce a file called `assignment2.zip`. You will then need to SCP this file over to Stanford AFS using the following command (entering your Stanford password if requested):

```bash
# Run from the assignment directory where the zip file is located
scp assignment2.zip YOUR_SUNET@myth.stanford.edu:~/DEST_PATH
```

`YOUR_SUNET` should be replaced with your SUNetID (e.g. `jdoe`), and `DEST_PATH` should be a path to an existing directory on AFS where you want the zip file to be copied to (you may want to create a CS231N directory for convenience). Once this is done, run the following:

 ```bash
# SSH into the Stanford Myth machines 
ssh YOUR_SUNET@myth.stanford.edu

# Descend into the directory where the zip file is now located
cd DEST_PATH

# Run the script to actually submit the assignment
/afs/ir/class/cs231n/submit
```
Once you run the submit script, simply follow the on-screen prompts to finish submitting the assignment on AFS. If successful, you should see a "SUBMIT SUCCESS" message output by the script.
