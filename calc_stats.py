
# from collections import defaultdict

val_stat = {'suitcase': 26, 'elephant': 46, 'spoon': 68, 'bowl': 92, 'carrot': 111, 'handbag': 63, 'pizza': 89, 'cup': 175, 'baseball glove': 27, 'baseball bat': 14, 'bear': 72, 'wine glass': 75, 'sandwich': 120, 'sports ball': 196, 'cake': 356, 'fork': 44, 'truck': 134, 'fire hydrant': 12, 'laptop': 42, 'clock': 39, 'orange': 170, 'refrigerator': 24, 'broccoli': 49, 'sink': 47, 'knife': 32, 'oven': 33, 'toilet': 36, 'vase': 64, 'stop sign': 10, 'hot dog': 17, 'giraffe': 25, 'apple': 126, 'zebra': 45, 'surfboard': 14, 'book': 329, 'tie': 99, 'cell phone': 114, 'skateboard': 30, 'keyboard': 51, 'donut': 80, 'kite': 15, 'bed': 59, 'snowboard': 5, 'skis': 5, 'tennis racket': 23, 'mouse': 22, 'microwave': 23, 'backpack': 30, 'umbrella': 18, 'traffic light': 19, 'toothbrush': 14, 'banana': 26, 'scissors': 1, 'teddy bear': 16, 'remote': 9, 'parking meter': 3, 'toaster': 1, 'bench': 2}
test_stat = {'truck': 435, 'orange': 903, 'apple': 382, 'cake': 1008, 'umbrella': 117, 'toilet': 65, 'banana': 155, 'cell phone': 364, 'vase': 144, 'cup': 567, 'donut': 212, 'wine glass': 218, 'bear': 255, 'sink': 114, 'zebra': 126, 'spoon': 199, 'tennis racket': 84, 'traffic light': 52, 'bed': 195, 'carrot': 198, 'oven': 67, 'refrigerator': 104, 'microwave': 63, 'fire hydrant': 56, 'pizza': 202, 'sports ball': 800, 'fork': 152, 'handbag': 191, 'book': 1521, 'clock': 137, 'tie': 319, 'teddy bear': 97, 'keyboard': 180, 'elephant': 149, 'laptop': 144, 'knife': 103, 'giraffe': 69, 'bowl': 252, 'broccoli': 215, 'scissors': 6, 'skateboard': 75, 'baseball glove': 60, 'stop sign': 31, 'sandwich': 330, 'suitcase': 60, 'remote': 28, 'hot dog': 49, 'kite': 61, 'surfboard': 61, 'mouse': 86, 'parking meter': 4, 'baseball bat': 24, 'backpack': 63, 'toaster': 4, 'skis': 32, 'toothbrush': 19, 'bench': 1, 'frisbee': 1, 'hair dryer': 2}
train_stat = {'sports ball': 8957, 'tie': 9636, 'book': 25444, 'cup': 4192, 'wine glass': 6831, 'backpack': 953, 'carrot': 1419, 'cell phone': 5534, 'clock': 1456, 'spoon': 1515, 'cake': 5041, 'refrigerator': 508, 'bowl': 4524, 'baseball bat': 1097, 'orange': 5937, 'baseball glove': 2345, 'laptop': 5581, 'truck': 6523, 'keyboard': 3272, 'bench': 4857, 'traffic light': 4672, 'surfboard': 1463, 'umbrella': 4896, 'tennis racket': 876, 'sink': 1409, 'fork': 1372, 'skis': 1013, 'toilet': 1051, 'bed': 2155, 'giraffe': 1378, 'teddy bear': 1324, 'skateboard': 1054, 'elephant': 2858, 'handbag': 2127, 'pizza': 1834, 'apple': 3626, 'oven': 571, 'broccoli': 1120, 'fire hydrant': 416, 'suitcase': 524, 'microwave': 408, 'mouse': 660, 'vase': 1574, 'hot dog': 446, 'sandwich': 1375, 'kite': 1495, 'snowboard': 397, 'scissors': 384, 'zebra': 1090, 'banana': 1489, 'bear': 1660, 'knife': 333, 'toaster': 70, 'toothbrush': 213, 'frisbee': 210, 'donut': 902, 'stop sign': 347, 'remote': 219, 'parking meter': 184, 'hair dryer': 22}

merge_dict = {}

sum_val = 0
for x in val_stat.keys():
	merge_dict[x] = val_stat[x] 
	sum_val += val_stat[x] 

sum_test = 0
for x in test_stat.keys():
	merge_dict[x] = merge_dict.get(x,0) + test_stat[x] 
	sum_test += test_stat[x] 


sum_train = 0
for x in train_stat.keys():
	merge_dict[x] = merge_dict.get(x,0) + train_stat[x] 
	sum_train += train_stat[x] 


print(merge_dict)
print(f'sum val = {sum_val}')
print(f'sum test = {sum_test}')
print(f'sum test = {sum_train}')




# train_stat = 