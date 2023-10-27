# CUDA_VISIBLE_DEVICES=0 python run_nerf.py --config configs/chair.txt --finest_res 1024
# CUDA_VISIBLE_DEVICES=1 python run_nerf.py --config configs/chair.txt --finest_res 1024 --i_embed_views 0
# CUDA_VISIBLE_DEVICES=2 python run_nerf.py --config configs/chair.txt --finest_res 1024 --lr 0.01 --lr_decay 100
# CUDA_VISIBLE_DEVICES=3 python run_nerf.py --config configs/chair.txt --finest_res 1024 --log2_hashmap_size 14 

# CUDA_VISIBLE_DEVICES=0 python run_nerf.py --config configs/chair.txt --finest_res 1024 
# CUDA_VISIBLE_DEVICES=1 python run_nerf.py --config configs/chair.txt --finest_res 1024 --lr 0.01 --lr_decay 100
# CUDA_VISIBLE_DEVICES=2 python run_nerf.py --config configs/chair.txt --finest_res 1024 --i_embed 0 --i_embed_views 0
# CUDA_VISIBLE_DEVICES=3 python run_nerf.py --config configs/chair.txt --finest_res 1024 --i_embed 0 --i_embed_views 0 --lr 0.01 --lr_decay 100

# this line
python3 main.py --config configs/gmap_rail1.txt --model_config hash_nerf --embed_config hash_encoding --train_iters 10000 --lr 0.01 --lr_decay 10 --iter_test 100

python run_nerf.py --config configs/chair.txt --finest_res 512 --log2_hashmap_size 19 --lr 0.01 --lr_decay 10

python run_nerf.py --config configs/equirect.txt --finest_res 512 --log2_hashmap_size 19 --lr 0.01 --lr_decay 10

python run_nerf.py --config configs/gmap_rail1.txt --finest_res 512 --log2_hashmap_size 19 --lr 0.01 --lr_decay 10 --train_iters 10000