# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:23:53 2022

@author: agiokap
"""

import json
import matplotlib.pyplot as plt

def load_history(path):
    with open(path) as history_json:
        history = json.load(history_json)
    return history

def acc_val_plots(history, from_json = False, augmentation = False, transfer_learning = False):
    
    if from_json:
        history = load_history(history)
    else:
        acc, val_acc = history["accuracy"], history["val_accuracy"]
        loss, val_loss = history["loss"], history["val_loss"]
        
        num_epochs = range(len(acc))
        
        fig, (ax_acc, ax_loss) = plt.subplots(2, 1)
        fig.suptitle("Accuracy and Loss ({} Augmentation/{} Transfer Learning)".format(("with" if augmentation == True else "without"),
                                                                                       ("with" if transfer_learning == True else "without")))
        
        ax_acc.plot(num_epochs, acc)
        ax_acc.plot(num_epochs, val_acc)
        plt.legend(["Training", "Validation"])
        ax_acc.set_ylabel("Accuracy")
        
        ax_loss.plot(num_epochs, loss)
        ax_loss.plot(num_epochs, val_loss)
        plt.legend(["Training", "Validation"])
        ax_loss.set_ylabel("Loss")
        ax_loss.set_xlabel("Epoch")