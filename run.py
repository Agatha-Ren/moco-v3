import os
str=('python main_moco.py -a vit_small -b 1024 --optimizer=adamw --lr=1.5e-4 --weight-decay=.1 epochs=30 --warmup-epochs=40 --stop-grad-conv1 --moco-m-cos --moco-t=.2 --dist-url \'tcp://localhost:10001\' --gpu=1 -b=128 --multiprocessing-distributed --world-size 1 --rank 0 /mnt/Data/Datasets/yren_data/dataset')
p=os.system(str)
print(p)