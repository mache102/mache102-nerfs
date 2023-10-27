import configargparse

def config_parser():

    parser = configargparse.ArgumentParser()
    parser.add_argument('--config', is_config_file=True,
                        help='config file path')
    parser.add_argument("--embed_config", type=str, default="positional",
                        help="filename of embedders config")
    parser.add_argument('--model_config', type=str, default="vanilla_nerf",
                        help='model config name')
    parser.add_argument("--expname", type=str,
                        help='experiment name')
    parser.add_argument("--basedir", type=str, default='./logs/',
                        help='where to store ckpts and logs')
    parser.add_argument("--datadir", type=str, default='./data/llff/fern',
                        help='input data directory')
    parser.add_argument("--seed", type=int, default=None,
                        help='random seed')

    # training options
    parser.add_argument("--train_iters", type=int, default=200000,
                        help="number of iterations to train")
    parser.add_argument("--train_bsz", type=int, default=32*32*4,
                        help='batch size (number of random rays per gradient step)')
    parser.add_argument("--render_bsz", type=int, default=1024*32,
                        help='number of rays processed in parallel, decrease if running out of memory')
    parser.add_argument("--net_bsz", type=int, default=1024*64,
                        help='number of pts sent through network in parallel, decrease if running out of memory')
    parser.add_argument("--lr", type=float, default=5e-4,
                        help='learning rate')
    parser.add_argument("--lr_decay", type=int, default=250,
                        help='exponential learning rate decay (in 1000 steps)')
    parser.add_argument("--reload", action='store_true',
                        help='reload weights from saved ckpt')
    parser.add_argument("--ft_path", type=str, default=None,
                        help='specific weights npy file to reload for coarse network')

    # rendering options
    parser.add_argument("--N_coarse", type=int, default=64,
                        help='number of coarse samples per ray')
    parser.add_argument("--N_fine", type=int, default=0,
                        help='number of additional fine samples per ray')
    parser.add_argument("--perturb", type=float, default=1.,
                        help='set to 0. for no jitter, 1. for jitter')
    parser.add_argument("--raw_noise_std", type=float, default=0.,
                        help='std dev of noise added to regularize sigma_a output, 1e0 recommended')

    parser.add_argument("--render_only", action='store_true',
                        help='do not optimize, reload weights and render out render_poses path')
    parser.add_argument("--render_test", action='store_true',
                        help='render the test set instead of render_poses path')
    parser.add_argument("--render_factor", type=int, default=1,
                        help='downsampling factor to speed up rendering, set 4 or 8 for fast preview')

    # training options
    parser.add_argument("--precrop_iters", type=int, default=0,
                        help='number of steps to train on central crops')
    parser.add_argument("--precrop_frac", type=float,
                        default=.5, help='fraction of img taken for central crops')

    # dataset options
    parser.add_argument("--testskip", type=int, default=8,
                        help='will load 1/N images from test/val sets, useful for large datasets like deepvoxels')

    parser.add_argument("--use_viewdirs", action='store_true',
                        help='use full 5D input instead of 3D')
    parser.add_argument("--use_depth", action='store_true', 
                        help='use depth to update')
    parser.add_argument("--use_gradient", action='store_true', 
                        help='use gradient to update')
    parser.add_argument("--stage", type=int, default=0,
                        help='use iterative training by defining stage, if 0: don\'t use')


    # logging/saving options
    parser.add_argument("--iter_print",   type=int, default=100,
                        help='frequency of console printout and metric loggin')
    parser.add_argument("--iter_ckpt", type=int, default=10000,
                        help='frequency of weight ckpt saving')
    parser.add_argument("--iter_test", type=int, default=1000,
                        help='frequency of testset saving')
    parser.add_argument("--iter_video", type=int, default=5000,
                        help='frequency of render_poses video saving')

    parser.add_argument("--sparse-loss-weight", type=float, default=1e-10,
                        help='learning rate')
    parser.add_argument("--tv-loss-weight", type=float, default=1e-6,
                        help='learning rate')

    return parser
