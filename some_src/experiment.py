from neptune import ChannelType
import os
from some_utils.neptune_utils import get_configuration
# To debug this locally (which is highly recommended) you run this script with
# python some_src/experiment.py --


if __name__ == '__main__':
  ctx, exp_dir_path = get_configuration()
  debug_info = ctx.create_channel('debug info', channel_type=ChannelType.TEXT)
  channel = ctx.create_channel('I wish this was test error',
                               channel_type=ChannelType.NUMERIC)

  os.environ['MRUNNER_UNDER_NEPTUNE'] = '1'
  debug_info.send('experiment path {}'.format(exp_dir_path))
  print('got delta', ctx.params['delta'], type(ctx.params['delta']))
  for i in range(1, 100):
    # more examples can be found in neptune documentation
    channel.send(x=i, y=1/i)