# For the "test" argument input the UDH trained folder path, 
# for the "test_diff" argument input the DDH trained folder path. 
python3 main.py \
  --imageSize 128 \
  --bs_secret 40 \
  --num_training 1 \
  --num_secret 1 \
  --num_cover 1 \
  --channel_cover 3 \
  --channel_secret 3 \
  --norm 'batch' \
  --loss 'l2' \
  --beta 0.75 \
  --remark 'main' \
  --test 'autodl-container-32de4894e4-392808a3_2025-12-06_H17-45-51_128_1_1_44_1_batch_l2_0.75_1colorIn1color_main_udh' \
  --test_diff 'autodl-container-32de4894e4-392808a3_2025-12-06_H23-06-58_128_1_1_44_1_batch_l2_0.75_1colorIn1color_main_ddh' \