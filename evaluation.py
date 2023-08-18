# -*- coding: utf-8 -*-
def debugging_function(build_model,test_ds):
  scores=build_model.evaluate(test_ds,batch_size=128,verbose=1)
  print('\nTest result : %.3f loss:%.3f'%(scores[1]*100,scores[0]))