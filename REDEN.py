import numpy as np
from keras import layers, models, losses, optimizers


n = 10**4
x = np.linspace(0,100,n)
a = 5
b = -5

x_val = np.random.choice(x,int(0.4*n))
x_tre = np.setdiff1d(x,x_val)

y_val = a*x_val +b+ np.random.random(len(x_val))*0.05 +np.sin(x_val)
y_val = a*x_tre +b+ np.random.random(len(x_tre))*0.05 +np.sin(x_tre)


rede = models.Sequential()
rede.add(layers.Dense(32,activation='relu',input_shape=[1]))
rede.add(layers.Dense(32,activation='relu'))
rede.add(layers.Dense(1))
rede.compile(optimizer = optimizers.RMSprop(lr = 0.05), loss = losses.mean_squared_error)

hist = rede.fit(x_tre,y_tre,epochs=180,batch_size=25,validation_data=(x_val,y_val))
