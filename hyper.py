from chemprop.args import HyperoptArgs
from chemprop.hyperparameter_optimization import hyperopt

args = [
    '--data_path', '../data/QM_137k.csv',
    '--dataset_type', 'regression',
    '--save_dir', 'hyperopt/QM_137k_checkpoints',
    '--config_save_path', 'hyperopt/best_hyperparams.json',
    '--smiles_columns', 'smiles',
    '--target_columns', 'CDD',
    '--is_atom_bond_targets',
    '--epochs', '100',
    '--adding_h',
    '--show_individual_scores',
    '--metric', 'rmse',
    '--extra_metrics', 'mae', 'r2', 'mse',
    '--num_iters', '100',
    '--search_parameter_keywords', 'basic',

]

hyperopt(HyperoptArgs().parse_args(args))