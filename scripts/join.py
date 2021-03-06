

import numpy as np


ids_path = "/mnt/data/part12/afhuertass/home/instacart-data/test_ids.txt"
pred_path = "/mnt/data/part12/afhuertass/home/instacart-data/preds/predictions3.txt"

out_string = "order_id,products\n"
with open(ids_path) as ids_file , open( pred_path) as pred_file:

    for x , y in zip(ids_file, pred_file):
        x = x.strip()
        y = y.strip()
        out_string += "{},{}\n".format(x,y)


out = open("sub.txt", "w" )
out.write(out_string)

out.close()



