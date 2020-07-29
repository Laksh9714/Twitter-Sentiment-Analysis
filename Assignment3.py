# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:42:42 2020

@author: Laksh
"""

from threading import Thread
import StreamConsumer as sc
import StreamProducer as sp
import sys
    
if __name__ == "__main__":
    
    def producer(hashtag): 
    
        # import your script A
        sp.main(hashtag)
    
    def consumer():
        
        sc.main()
        
        
    hashtag = []
    count = len(sys.argv)
    for i in range(1,count):
        hashtag.append(sys.argv[i])
    
    
    Thread(target = producer,args=[hashtag]).start()
    Thread(target = consumer).start()
    
    
    
    



