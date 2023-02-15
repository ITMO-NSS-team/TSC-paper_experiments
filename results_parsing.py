import os
from typing import Union

import pandas as pd


class ResultsPicker:

    def __init__(self, path: str, launch_type: Union[str, int] = 'max'):
        self.exp_path = path
        self.launch_type = launch_type

    def run(self, get_metrics_df: bool = False, add_info: bool = False):
        """
        Base method for parsing results of experiments.

        Returns:
            Table with results of experiments.

        """

        metric_dict = self.get_metrics()

        if get_metrics_df:
            if add_info:
                metrics_df = self._create_metrics_df(metric_dict)
                datasets_info = self.get_datasets_info()
                return pd.merge(metrics_df, datasets_info, how='left', on='dataset')
            return self._create_metrics_df(metric_dict)

        return metric_dict

    @staticmethod
    def _create_metrics_df(metric_dict):
        columns = ['dataset', 'experiment']
        metrics_df = pd.DataFrame()
        for ds in metric_dict.keys():
            for exp in metric_dict[ds].keys():
                metrics = metric_dict[ds][exp]
                metrics_df = metrics_df.append({'dataset': ds, 'experiment': exp, 'f1': metrics['f1'][0],
                                                'roc_auc': metrics['roc_auc'][0], 'accuracy': metrics['accuracy'][0],
                                                'precision': metrics['precision'][0], 'logloss': metrics['logloss'][0]},
                                               ignore_index=True)

        metrics_df = pd.concat([metrics_df[['dataset', 'experiment']],
                                metrics_df[[col for col in metrics_df.columns if col not in columns]]], axis=1)
        return metrics_df

    def get_metrics(self):
        experiments = self.list_dirs(self.exp_path)
        metric_dict = {}
        for exp in experiments:
            exp_path = os.path.join(self.exp_path, exp)
            ds_list, metrics_list = self.read_exp_folder(exp_path)

            for metric, dataset in zip(metrics_list, ds_list):
                if dataset not in metric_dict.keys():
                    metric_dict[dataset] = {}
                if dataset not in metric_dict.keys():
                    metric_dict[dataset] = {}
                metric_dict[dataset].update({exp: metric})

        return metric_dict

    def read_exp_folder(self, folder):
        datasets_path = os.path.join(self.exp_path, folder)
        datasets = self.list_dirs(datasets_path)
        metrics_list = []
        for ds in datasets:
            ds_path = os.path.join(self.exp_path, folder, ds)
            metrics = self.read_ds_data(ds_path)
            metrics_list.append(metrics)

        return datasets, metrics_list

    def read_ds_data(self, path):
        if self.launch_type == 'max':
            best_launch = self.find_best_launch(path)
        else:
            best_launch = self.launch_type
        metrics_path = os.path.join(path, best_launch, 'test_results', 'metrics.csv')

        metrics = pd.read_csv(metrics_path, index_col=0)
        if 'index' in metrics.columns:
            del metrics['index']
            metrics = metrics.T
            metrics = metrics.rename(columns=metrics.iloc[0])
            metrics = metrics[1:]

        return metrics

    @staticmethod
    def list_dirs(path):
        """Function used instead of ``os.listdir()`` to get list of non-hidden directories.

        Args:
            path (str): Path to the directory.

        Returns:
            list: List of non-hidden directories.

        """
        path_list = []
        for f in os.listdir(path):
            # if not f.startswith('.'):
            if '.' not in f:
                path_list.append(f)
        return path_list

    @staticmethod
    def list_files(path):
        """Function used instead of ``os.listdir()`` to get list of non-hidden files.

        Args:
            path (str): Path to the directory.

        Returns:
            list: List of non-hidden files.

        """
        path_list = []
        for f in os.listdir(path):
            if os.path.isfile(path + '/' + f) and not f.startswith('.'):
                path_list.append(f)

        return path_list

    def find_best_launch(self, launch_folders):
        best_metric = 0
        launch = 1
        for _dir in self.list_dirs(launch_folders):
            if len(_dir) == 1:
                metric_path = os.path.join(launch_folders, str(_dir), 'test_results', 'metrics.csv')
                metrics = pd.read_csv(metric_path, index_col=0)
                if 'index' in metrics.columns:
                    del metrics['index']
                    metrics = metrics.T
                    metrics = metrics.rename(columns=metrics.iloc[0])
                    metrics = metrics[1:]
                metric_sum = metrics['roc_auc'].values[0] + metrics['f1'].values[0]
                if metric_sum > best_metric:
                    best_metric = metric_sum
                    launch = _dir
        return launch

    @staticmethod
    def get_datasets_info():
        table = pd.read_json('./ucr_datasets.json')

        table = table.drop([col for col in table.columns if len(col) == 1] + ['Dataset_id'], axis=1)
        table.columns = list(map(str.lower, table.columns))
        table.type = table.type.str.lower()

        return table


# Example of usage:
if __name__ == '__main__':
    path_to_results = os.path.abspath('./csv_results')
    parser = ResultsPicker(path=path_to_results)
    metrics_dataframe = parser.run(get_metrics_df=True, add_info=True)
