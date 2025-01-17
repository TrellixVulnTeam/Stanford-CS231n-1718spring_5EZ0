import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  
  num_train = X.shape[0]
  num_class = W.shape[1]

  score = X.dot(W)
  # 这是笔记中提到的一个技巧，为了防止计算指数和的时候发生数据过大溢出，
  # 在这里加一步均值归一化
  score -= np.max(score, axis=1).reshape(-1,1)
  
  for i in range(num_train):
    loss += -score[i, y[i]] + np.log(np.sum(np.exp(score[i,:])))
    for j in range(num_class):
      temp = np.exp(score[i, j]) / np.sum(np.exp(score[i,:]))
      if j==y[i] :
        temp -= 1
      dW[:,j] += temp * X[i]
  loss /= num_train
  loss += reg * np.sum(W * W)
  dW = dW / num_train + 2 * reg * W
  
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]
  num_class = W.shape[1]
  score = X.dot(W)
  score -= np.max(score, axis=1).reshape(-1,1)
  poss = np.exp(score) / np.sum(np.exp(score), axis=1).reshape(-1,1)

  loss = -np.sum(np.log(poss[range(num_train), list(y)]))
  loss = loss / num_train + reg * np.sum(W * W)
  
  poss[range(num_train), list(y)] -= 1
  dW = X.T.dot(poss)
  dW = dW / num_train + 2 * reg * W

  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

