import matplotlib.pyplot as plt

def compare_plots_(train,val,metric):
    epochs = range(1,len(train)+1)
    plt.plot(epochs,train,'bo',label='Training %s'%(metric))
    plt.plot(epochs,val,'ro',label='Validation %s'%(metric))
    plt.title('Training and Validation %s'%(metric))
    plt.legend()
    plt.show()
    
if __name__ == '__main__':
    compare_plots()