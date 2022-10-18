

def read_dataset(path):
    train_reviews = open(path+"train_reviews.txt", encoding="utf-8").read().split('\n')
    train_labels = open(path+"train_labels.txt", encoding="utf-8").read().split('\n')
    
    test_reviews = open(path+"test_reviews.txt", encoding="utf-8").read().split('\n')
    test_labels = open(path+"test_labels.txt", encoding="utf-8").read().split('\n')
    return train_reviews, train_labels, test_reviews, test_labels 
    
    
train_reviews, train_labels, test_reviews, test_labels = read_dataset("../dataset/")

import random
import time
for _ in range(20):
    s = random.randint(0, len(test_reviews))
    print(test_reviews[s], test_labels[s])
    time.sleep(5)
