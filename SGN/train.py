import argparse
import os

import trainer

if __name__ == "__main__":
    # ----------------------------------------
    #        Initialize the parameters
    # ----------------------------------------
    parser = argparse.ArgumentParser()
    # Pre-train, saving, and loading parameters
    parser.add_argument('--pre_train', type = bool, default = True, help = 'pre-train ot not')
    parser.add_argument('--save_mode', type = str, default = 'epoch', help = 'saving mode, and by_epoch saving is recommended')
    parser.add_argument('--save_by_epoch', type = int, default = 100, help = 'interval between model checkpoints (by epochs)')
    parser.add_argument('--save_by_iter', type = int, default = 10000, help = 'interval between model checkpoints (by iterations)')
    parser.add_argument('--save_name_mode', type = bool, default = True, help = 'True for concise name, and False for exhaustive name')
    parser.add_argument('--load_name', type = str, default = '', help = 'load the pre-trained model with certain epoch')
    # GPU parameters
    parser.add_argument('--multi_gpu', type = bool, default = False, help = 'True for more than 1 GPU')
    parser.add_argument('--gpu_ids', type = str, default = '0, 1, 2, 3', help = 'gpu_ids: e.g. 0  0,1  0,1,2  use -1 for CPU')
    parser.add_argument('--cudnn_benchmark', type = bool, default = True, help = 'True for unchanged input data type')
    # Training parameters
    parser.add_argument('--epochs', type = int, default = 1000, help = 'number of epochs of training')
    parser.add_argument('--batch_size', type = int, default = 32, help = 'size of the batches')
    parser.add_argument('--lr', type = float, default = 0.0001, help = 'Adam: learning rate')
    parser.add_argument('--b1', type = float, default = 0.5, help = 'Adam: decay of first order momentum of gradient')
    parser.add_argument('--b2', type = float, default = 0.999, help = 'Adam: decay of second order momentum of gradient')
    parser.add_argument('--weight_decay', type = float, default = 0, help = 'weight decay for optimizer')
    parser.add_argument('--epoch_decreased', type = int, default = 500, help = 'the certain epoch that lr decreased')
    parser.add_argument('--lr_decreased', type = float, default = 0.00001, help = 'decreased learning rate at certain epoch')
    parser.add_argument('--num_workers', type = int, default = 4, help = 'number of cpu threads to use during batch generation')
    # Initialization parameters
    parser.add_argument('--pad', type = str, default = 'reflect', help = 'pad type of networks')
    parser.add_argument('--norm', type = str, default = 'none', help = 'normalization type of networks')
    parser.add_argument('--in_channels', type = int, default = 3, help = 'input channels for generator')
    parser.add_argument('--out_channels', type = int, default = 3, help = 'output channels for generator')
    parser.add_argument('--start_channels', type = int, default = 32, help = 'start channels for generator')
    parser.add_argument('--m_block', type = int, default = 2, help = 'the additional blocks used in mainstream')
    parser.add_argument('--init_type', type = str, default = 'normal', help = 'initialization type of generator')
    parser.add_argument('--init_gain', type = float, default = 0.02, help = 'initialization gain of generator')
    # Dataset parameters
    parser.add_argument('--baseroot', type = str, default = 'C:\\Users\\yzzha\\Desktop\\dataset\\DIV2K\\DIV2K_train_HR', help = 'images baseroot')
    parser.add_argument('--crop_size', type = int, default = 256, help = 'single patch size')
    parser.add_argument('--geometry_aug', type = bool, default = False, help = 'geometry augmentation (scaling)')
    parser.add_argument('--angle_aug', type = bool, default = False, help = 'geometry augmentation (rotation, flipping)')
    parser.add_argument('--scale_min', type = float, default = 1, help = 'min scaling factor')
    parser.add_argument('--scale_max', type = float, default = 1, help = 'max scaling factor')
    parser.add_argument('--mu', type = float, default = 0, help = 'Gaussian noise mean')
    parser.add_argument('--sigma', type = float, default = 30, help = 'Gaussian noise variance')
    opt = parser.parse_args()

    # ----------------------------------------
    #        Choose CUDA visible devices
    # ----------------------------------------
    if opt.multi_gpu == True:
        os.environ["CUDA_VISIBLE_DEVICES"] = opt.gpu_ids
        print('Multi-GPU mode, %s GPUs are used' % (opt.gpu_ids))
    else:
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"
        print('Single-GPU mode')
    
    # ----------------------------------------
    #                 Trainer
    # ----------------------------------------
    trainer.Trainer(opt)