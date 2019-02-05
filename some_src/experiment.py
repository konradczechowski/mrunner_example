from neptune import ChannelType
import os
from some_utils.neptune_utils import get_configuration
from some_utils.neptune_utils import neptune_logger

if __name__ == '__main__':
  ctx, exp_dir_path = get_configuration()
  debug_info = ctx.create_channel('debug info', channel_type=ChannelType.TEXT)

  os.environ['MRUNNER_UNDER_NEPTUNE'] = '1'
  debug_info.send('experiment path {}'.format(exp_dir_path))
  print('got delta', ctx.params['delta'], type(ctx.params['delta']))
  for i in range(1, 100):
    # more examples can be found in neptune documentation
    neptune_logger('some numeric logs', 1/i)
