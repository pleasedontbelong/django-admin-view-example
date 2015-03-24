from socket import gethostname

hostname = gethostname()

try:
    from .local import *
except ImportError:
    from .prod import *

try:
    from .temp import *
except ImportError:
    pass
