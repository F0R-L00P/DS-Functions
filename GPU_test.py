# =============================================================================
# Assigning tensors to GPU
# =============================================================================
import torch

# check cuda availability
torch.cuda.is_available()

# get device location
torch.cuda.current_device()

# get device name
torch.cuda.get_device_name(0)

# check memory allocation
# will be zero if nothing is running
torch.cuda.memory_allocated()

# test - CPU
test_var1 = torch.FloatTensor([1.0, 2.0, 3.0])
print(test_var1)

# check device --> execution is with cpu
test_var1.device

# test - GPU
test_var1 = torch.FloatTensor([1.0, 2.0, 3.0]).cuda()
print(test_var1)

# check device --> execution is with cpu
test_var1.device