
import math
carrying_weight_percentage = 1/3
coconut_weight = 1450
macaw_weight = 900
macaw_limit = macaw_weight * carrying_weight_percentage
number_macaws = coconut_weight/macaw_limit
print(math.ceil(number_macaws))