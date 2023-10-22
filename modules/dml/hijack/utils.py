import torch
from typing import Callable
from installer import log

def catch_nan(func: Callable[[], torch.Tensor]):
    tries = 0
    tensor = func()
    while tensor.isnan().sum() != 0 and tries < 10:
        if tries == 0:
            log.warning("NaN is produced. Retry with same values...")
        tries += 1
        tensor = func()
    if tensor.isnan().sum() != 0:
        log.error("Failed to cover NaN.")
    return tensor
