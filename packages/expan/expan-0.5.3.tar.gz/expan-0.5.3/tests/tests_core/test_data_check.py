import unittest
import warnings
from copy import deepcopy

import numpy as np
import pandas as pd

# from time import time
from expan.core.experimentdata import ExperimentData
from expan.core.util import generate_random_data


class DataTestCase(unittest.TestCase):
    def setUp(self):
        """
        Load the needed datasets for all StatisticsTestCases and set the random
        seed so that randomized algorithms show deterministic behaviour.
        """
        # np.random.seed(0)
        self.metrics, self.metadata = generate_random_data()

    def tearDown(self):
        """
        Clean up after the test
        """
        # TODO: find out if we have to remove data manually
        pass

    def test_create_with_insufficient_data(self):
        # should not work:
        with self.assertRaises(ValueError):
            ExperimentData(
                pd.DataFrame(columns=['entity', 'variant']),
                metadata={'experiment': 'test', 'source': 'none'}
            )
        with self.assertRaises(ValueError):
            ExperimentData(
                pd.DataFrame(columns=['entity', 'variant', 'plums']),
                metadata={'experiment': 'test', 'source': 'none', 'primary_KPI': 'plums'}
            )
        with self.assertRaises(ValueError):
            ExperimentData(None)
        # with self.assertRaises(KeyError):
        #	ExperimentData(pd.DataFrame())
        with self.assertRaises(KeyError):
            ExperimentData(
                pd.DataFrame(columns=['entity', 'variant']),
                metadata=None)
        # with self.assertRaises(KeyError):
        # 	ExperimentData(
        # 		pd.DataFrame(columns=['entity', 'treatment_start']),
        # 		metadata={'experiment': 'fesf', 'source': 'random'},
        # 	)
        with self.assertRaises(ValueError):
            ExperimentData(
                pd.DataFrame(columns=['variant', 'treatment_start']),
                metadata={'experiment': 'fesf', 'source': 'random'}
            )
        with self.assertRaises(KeyError):
            ExperimentData(
                pd.DataFrame(columns=['variant', 'entity', 'treatment_start']),
                metadata={
                    'experiment': 'fesf',
                    'source': 'random',
                    'primary_KPI': 'something_not_there'}
            )

    def test_data_generation(self):
        df, md = generate_random_data()
        A = ExperimentData(df, md)
        self.assertIsNotNone(A.kpis)
        self.assertIsNotNone(A.features)
        self.assertIsNotNone(A.metadata)

        # also test incomplete info again
        with self.assertRaises(KeyError):
            ExperimentData(df.drop('entity', axis=1), md)
            # with self.assertRaises(KeyError):
            # 	ExperimentData(df.drop('variant', axis=1), md)

    def test_direct_indexing(self):
        A = ExperimentData(*generate_random_data())
        # this should work
        normal_shifted = A[['normal_shifted', 'feature']]

        # this should not
        with self.assertRaises(KeyError):
            normal_shifted = A[['normal_shifted', 'non_existent_feature']]

    def test_initialize_without_kpi_with_feature(self):
        """Initialize ExperimentData with metrics=None, features=DF"""
        metrics, _ = generate_random_data()
        meta = {
            'source': 'simulated',
            'experiment': 'random_data_generation'
        }
        D = ExperimentData(None, meta, metrics)

    def test_initialize_without_kpi_without_feature(self):
        """Initialize ExperimentData with metrics=None, features=[]/'default'"""
        meta = {
            'source': 'simulated',
            'experiment': 'random_data_generation'
        }

        with self.assertRaises(ValueError):
            D = ExperimentData(None, meta, [])
        with self.assertRaises(ValueError):
            D = ExperimentData(None, meta, 'default')

    def test_initialize_with_metric_with_feature_default(self):
        """Initialize ExperimentData with metrics=DF, features='default'"""
        # metrics,meta = generate_random_data()
        D = ExperimentData(self.metrics, self.metadata, 'default')

    def test_initialize_with_metric_with_feature_list(self):
        """Initialize ExperimentData with metrics=DF, features=list"""
        metrics, meta = generate_random_data()
        D = ExperimentData(metrics, meta, [])
        D = ExperimentData(metrics, meta, [4, 6])

    def test_initialize_with_metric_with_feature_df(self):
        """Initialize ExperimentData with metrics=DF, features=DF"""
        metrics, meta = generate_random_data()
        features = deepcopy(metrics)
        D = ExperimentData(metrics, meta, features)

    def test_init_with_aggregated_kpi(self):
        """Initialize ExperimentData with aggregated KPI data"""
        D = ExperimentData(self.metrics, self.metadata, [4])
        self.assertIsNone(D.kpis_time)

    def test_init_with_time_resolved_kpi(self):
        """Initialize ExperimentData with time-resolved KPI data"""
        n = 5  # replicate raw data and create synthetic time domain
        metrics_time = self.metrics.loc[np.repeat(self.metrics.index.values, n)]
        metrics_time.loc[:, 'time_since_treatment'] = np.tile(list(range(5)), self.metrics.shape[0])

        D = ExperimentData(metrics_time, self.metadata, [4])
        self.assertIsNotNone(D.kpis_time)
        self.assertEqual(D.kpis.shape[0] * n, D.kpis_time.shape[0])

    def test_outlier_filtering(self):
        """Check outlier filtering functionality"""
        # pick 1000 data points and make them outliers
        metrics_outlier = self.metrics
        idx = metrics_outlier.sample(1000).index
        # make sure the values are below than -1 or above 1 then multiply
        metrics_outlier.loc[idx, "normal_shifted_by_feature"] += np.sign(
            metrics_outlier.loc[idx, "normal_shifted_by_feature"])
        metrics_outlier.loc[idx, "normal_shifted_by_feature"] *= 10

        # use 4 rules, one is not implemented and one does not apply, default settings
        D = ExperimentData(metrics=metrics_outlier, metadata=self.metadata)
        D.filter_outliers(rules=[{"metric": "normal_shifted_by_feature",
                                  "type": "threshold",
                                  "value": -10.0,
                                  "kind": "lower"
                                  },
                                 {"metric": "normal_shifted_by_feature",
                                  "type": "threshold",
                                  "value": 10.0,
                                  "kind": "upper"
                                  },
                                 {"metric": "normal_same",
                                  "type": "threshold",  # this does not apply
                                  "value": 10.0,
                                  "kind": "upper"
                                  },
                                 {"metric": "normal_same",
                                  "type": "water",  # this is not implemented
                                  "value": 10.0,
                                  "kind": "both"
                                  }
                                 ])
        self.assertEqual(len(D.metadata['outlier_filter']), 2)  # only are actually applied
        self.assertEqual(len(D.metrics), 9000)
        for i in idx:
            self.assertEqual(D.metrics.ix[i].empty, True)
        self.assertFalse('calc_thresh_value' in D.kpis.columns)

        # use one rule, do not drop NaNs
        D = ExperimentData(metrics=metrics_outlier, metadata=self.metadata)
        temp_D = D
        D.filter_outliers(rules=[{"metric": "normal_shifted_by_feature",
                                  "type": "threshold",
                                  "value": 1.0,
                                  "kind": "lower",
                                  "time_interval": 30758400,
                                  "treatment_stop_time": 30758500}
                                 ])
        self.assertEqual(len(D.metadata['outlier_filter']), 1)
        self.assertFalse('calc_thresh_value' in D.kpis.columns)
        self.assertEqual(len(D.kpis), len(temp_D.kpis))

        # use one rule, do not drop NaNs, do not drop threshold column
        D = ExperimentData(metrics=metrics_outlier, metadata=self.metadata)
        temp_D = D
        D.filter_outliers(rules=[{"metric": "normal_shifted_by_feature",
                                  "type": "threshold",
                                  "value": 1.0,
                                  "kind": "lower",
                                  "time_interval": 30758400,
                                  "treatment_stop_time": 30758500}
                                 ],
                          drop_thresh=False)
        self.assertEqual(len(D.metadata['outlier_filter']), 1)
        self.assertTrue('calc_thresh_value' in D.kpis.columns)
        self.assertEqual(len(D.kpis), len(temp_D.kpis))

    def test_outlier_filtering_no_treatment_start(self):
        """Check if outlier filtering issues a warning when treatment_start_time is not available"""
        # initialize with only the kpi data
        D = ExperimentData(self.metrics[['entity', 'variant', 'normal_shifted']], self.metadata, 'default')
        with warnings.catch_warnings(record=True) as w:
            # Cause all warnings to always be triggered.
            warnings.simplefilter("always")
            # Trigger a warning.
            D.filter_outliers(rules=[{"metric": "normal_shifted",
                                      "type": "threshold",
                                      "value": -1.0,
                                      "kind": "lower",
                                      "time_interval": 30758400,
                                      "treatment_stop_time": 30758500
                                      }
                                     ])
            # Verify warning exists
            assert len(w) == 1

    def test_outlier_filtering_n_filtered(self):
        """Check if the number of filtered entities is persisted in the metadata"""
        D = ExperimentData(self.metrics, self.metadata, 'default')
        D.filter_outliers(rules=[{"metric": "normal_shifted",
                                  "type": "threshold",
                                  "value": -1.0,
                                  "kind": "lower"
                                  }
                                 ])
        self.assertEqual(D.metadata['n_filtered'], [1082])

    def test_outlier_filtering_treatment_exposure(self):
        """Check if scaling of the threshold works when the treatment_exposure is provided"""
        self.metrics['treatment_exposure'] = 1000
        D = ExperimentData(self.metrics[['entity', 'variant', 'normal_shifted', 'treatment_exposure']], self.metadata,
                           features=[3])
        D.filter_outliers(rules=[{"metric": "normal_shifted",
                                  "type": "threshold",
                                  "value": -1.0,
                                  "kind": "lower",
                                  "time_interval": 1000
                                  }
                                 ])
        n_filtered = D.metadata['n_filtered']
        self.assertEqual(n_filtered, [1082])

        # setting a larger long time_interval than the treatment_exposure does not affect the scaling of the threshold
        D = ExperimentData(self.metrics[['entity', 'variant', 'normal_shifted', 'treatment_exposure']], self.metadata,
                           features=[3])
        D.filter_outliers(rules=[{"metric": "normal_shifted",
                                  "type": "threshold",
                                  "value": -1.0,
                                  "kind": "lower",
                                  "time_interval": 10000
                                  }
                                 ])
        self.assertEqual(D.metadata['n_filtered'], D.metadata['n_filtered'])

        # setting a lower time_interval filters less, here so much less that filter will not be applied
        D = ExperimentData(self.metrics[['entity', 'variant', 'normal_shifted', 'treatment_exposure']], self.metadata,
                           features=[3])
        D.filter_outliers(rules=[{"metric": "normal_shifted",
                                  "type": "threshold",
                                  "value": -1.0,
                                  "kind": "lower",
                                  "time_interval": 100
                                  }
                                 ])
        self.assertEqual(len(D.metadata['outlier_filter']), 0)
        self.assertEqual(len(D.metadata['n_filtered']), 0)


if __name__ == '__main__':
    unittest.main()
