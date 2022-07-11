import os
import yaml
from docopt import docopt

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models.yml')) as f:
    MODELS = yaml.load(f, Loader=yaml.FullLoader)

    # print(MODELS)
    # all_feature_converters = sorted(MODELS['StridedInflatedEfficientNet']['lite'].keys())
    # print(all_feature_converters)
    # args = docopt(__doc__)
    # print(args)
