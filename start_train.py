import chemprop

arguments = [
    '--data_path', '../data/QM_100.csv',
    '--dataset_type', 'regression',
    '--save_dir', 'model/QM_137k_checkpoints',
    '--smiles_columns', 'smiles',
    '--target_columns', 'CDD',
    '--is_atom_bond_targets',
    '--epochs', '100',
    '--save_smiles_splits',
    '--adding_h',
    '--show_individual_scores',
    '--metric', 'rmse',
    '--extra_metrics', 'mae', 'r2', 'mse',

]

args = chemprop.args.TrainArgs().parse_args(arguments)
mean_score, std_score = chemprop.train.cross_validate(args=args, train_func=chemprop.train.run_training)