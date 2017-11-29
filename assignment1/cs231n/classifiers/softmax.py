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
  num_train = X.shape[0]
  num_class = W.shape[1]
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for i in xrange(num_train):
    scores = X[i].dot(W)
    shift_scores = scores - max(scores)
    loss += - shift_scores[y[i]] + np.log(sum(np.exp(shift_scores)))
    for j in xrange(num_class):
        softmax_output = np.exp(shift_scores[j])/sum(np.exp(shift_scores))
        if j == y[i]:
            dW[:,j] += (-1 + softmax_output) *X[i] 
        else: 
            dW[:,j] += softmax_output *X[i] 
  loss /= num_train
  dW /= num_train
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################
  loss += reg*np.sum(W*W)
  dW += 2*reg*W

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  num_train = X.shape[0]

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = X.dot(W)
  scores = scores - np.max(scores)
  scores_expo = np.exp(scores)
  log_sum = np.log(np.sum(scores_expo, axis=1))
  softmax = scores_expo / np.sum(scores_expo, axis=1).reshape(-1, 1)
  log_softmax = -scores[np.arange(num_train), y] + log_sum
  loss += np.sum(log_softmax)
  softmax[np.arange(num_train), y] -= 1
  dW = X.T.dot(softmax)
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################
  loss = loss/num_train + reg*np.sum(W*W)
  dW = dW/num_train + 2*reg*W

  return loss, dW

