#coding:utf-8
import warnings
class DefaultConfig(object):
    env = 'ATAE-LSTM' 
    model = 'ATAE-LSTM' 
    
    base_root = 'C:/Users/SEONGGYUN/ATAE-LSTM/ATAE-LSTM/'
    #base_root = '/content/drive/MyDrive/2팀/ATAE-LSTM/ATAE-LSTM/'
    embedding_root = base_root + 'data/glove/glove.840B.300d.txt' 
    train_data_root = base_root + 'data/restaurants-train.xml'
    test_data_root = base_root + 'data/restaurants-trial.xml' 
    load_model_path = None 
    
    use_cuda = True
    
    word_independence = 3
    # how many times an un-pretrained word have to appear for to be independent
    # this allow out-of-vocabulary words to have an independent embedding instead of <UNKNOWN>
    word_max_input = 100000
    # the Stanford-GloVe file may contains too many pretrained word embeddings and most of them are not needed in this task
    # so I can limit the number of words loaded to save memory
    
    max_seq_len = 128
    # the sequence of tokens should not be more than max_seq_len in length
    # the empty positions will be filled by token <PADDING>
    max_terms_len = 32
    
    use_layerNorm = True
    
    rescaling = False
    
    use_myAttentionMechanism = True
    
    classes = 3 # how many classes
    
    batch_size = 64
    
    hidden_size = 300 # the dimension of word vectors, aspect embeddings and the size of hidden layers
    
    print_freq = 40 # how many steps as an interval between two prints
    
    max_epoch = 10 ################ 조절해야됨, 원래 500 ############3
    
    lr = 1e-4
    lr_decay = 0.9
    lr_min = 5e-6
    weight_decay = 0.001 # L2-regularization
    epsilon = 0.1 # unknown parameters are randomly initialized from U(−ϵ,ϵ)
    
    
    def parse(self, kwargs):
        
        for k, v in kwargs.items():
            if not hasattr(self, k):
                warnings.warn("Warning : opt has not attribute named %s" %k)
            setattr(self, k, v)
        
        print('user config:')
        for k, v in self.__class__.__dict__.items():
            if not k.startswith('__'):
                print(k, getattr(self, k))
        return

opt = DefaultConfig()