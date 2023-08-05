from ...statistics import ThresholdOptimization
from ..gradient_boosting import GradientBoosting
from ..model import Model
from .util import FEATURES, format_info, pickle_and_unpickle, train_test


def test_gradient_boosting():
    to = ThresholdOptimization.from_string("maximum recall @ precision >= 0.9")
    model = GradientBoosting(FEATURES, max_thresholds=5,
                             threshold_optimizations=[to])
    format_info(model)
    train_test(model)
    pickle_and_unpickle(model)
    format_info(model)

    config = {
        'scorer_models': {
            'test': {
                'class': "revscoring.scoring.models.GradientBoosting",
                'features': [1, 2, 3]
            }
        }
    }
    model = Model.from_config(config, 'test')
    assert isinstance(model, GradientBoosting)
    assert False
