# Optimization Analysis of Universal and Cover-Dependent Deep Hiding for Visual Data
Embedding


### Datasets 
#### ImageNet
 1. Follow the common setup to make ImageNet compatible with pytorch as described in [here](https://github.com/pytorch/examples/tree/master/imagenet).
 2. Set the path to the pytorch ImageNet dataset folder in the main file.

## Experiments
### Train
To train the main UDH model, run the script `bash ./scripts/train_main_udh.sh`.
To train the main DDH model, run the script `bash ./scripts/train_main_ddh.sh`.
To train the UDH model for watermarking, run the script `bash ./scripts/train_watermarking.sh`.
To train the UDH model for LFM, run the script `bash ./scripts/train_lfm.sh`.

Weights and other details of the training instances are saved into the `./training/` folder.

### Test
To get the main qualitative and quantitative results, run the script `bash ./scripts/test_main.sh`.
To get the results for watermarking, run the script `bash ./scripts/test_watermarking.sh`.

#
Reference [UDH: Universal Deep Hiding for Steganography, Watermarking, and Light Field Messaging](https://papers.nips.cc/paper/2020/file/73d02e4344f71a0b0d51a925246990e7-Paper.pdf).

