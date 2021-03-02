COCO_to_OI_dict = {'Baseball glove' : 'Baseball glove',
'Parking meter' : 'Parking meter', 
'Skateboard' : 'Skateboard',
'Car' : 'Car', 
'Cup' : ['coffee cup', 'Measuring cup'],
'Toilet' : 'Toilet',
'bicycle' : 'bicycle',
'sink' : 'sink',
'cow': ['Cattle', 'Bull'],
'cat': 'cat',
'Motorcycle' : 'Motorcycle',
'Bed' : 'Bed',  #(also infant bed; does not match tho)',
'boat' : 'boat',
'Cake' : 'Cake',
'refrigerator' : 'refrigerator',
'Airplane' : 'Airplane',
'Carrot' : 'Carrot',
'Stop sign' : 'Stop sign',
'Zebra' : 'Zebra',
'Tie' : 'Tie',
'Pizza' : 'Pizza',
'Banana' : 'Banana',
'Traffic light' : 'Traffic light',
'Tennis racket' : 'Tennis racket',
'Microwave' : 'Microwave oven',
'Apple': 'Apple',
'donut': 'Doughnut', 
'Bear': ['Bear', 'Brown bear', 'Polar bear'], # [Teddy bear; discard]',
'Teddy bear' : 'Teddy bear', #    (has its own class)',
'clock': ['Alarm clock', 'Clock', 'Digital clock'], # double check',
'sports ball' : ['Ball', 'Football', 'Volleyball' , 'Tennis Ball', 'Rugby ball', 'golf ball',  'Cricket ball'], #,   [See which one matches better]',
'horse': 'horse',
'Hair drier': 'Hair dryer',  #+  [Hand dryer!! Not related]',
'Fire hydrant': 'Fire hydrant',
'Bus': 'Bus',
'Dining Table' : ['Table', 'Kitchen & dining room table'], #  Table!!!. (Types of tables in OpenImages: Billiard table, coffee table, kitchen and dining, Table, )',
'Couch': ['Couch', 'Studio couch'], # +  (maybe also Sofa bed and sofa)',
'mouse': 'computer mouse',
'Remote': 'Remote control',
'Bench': 'Bench',
'Scissors': 'Scissors',
'Truck': 'Truck',
'Wine glass': 'Wine glass',
'Oven': 'Oven',
'Backpack': 'Backpack',
'Bird': 'Bird',
'Handbag': 'Handbag',
'Sheep': 'Sheep',
'Spoon': 'Spoon',
'Tv':'Television',
'Frisbee' : 'Flying disc',
'Keyboard' : 'computer Keyboard',
'Sandwich' : ['Sandwich', 'Submarine sandwich'],
'Cell phone' : 'Mobile phone',
'Giraffe' : 'Giraffe',
'Chair' : 'Chair',
'Bottle' : 'Bottle',
'Potted plant' : 'Houseplant', #,  (open images has also plant but does not seem related much)',
'Broccoli' : 'Broccoli',
'Umbrella' : 'Umbrella',
'Orange' : 'Orange',
'Hot dog' : 'Hot dog',
'Knife' : 'kitchen knife', # (OI also has knife but that is way different; sort of street knife)',
'Vase' : 'Vase',
'Surfboard' : 'Surfboard',
'Toaster' : 'Toaster',
'Bowl' : ['bowl', 'Mixing bowl'],
'Suitcase' : 'Suitcase',
'Fork' : 'Fork',
'Skis' : 'Ski',
'Book' : 'Book',
'Kite' : 'Kite',
'Person' : 'Person',
'Dog' : 'Dog',
'Laptop' : 'Laptop',
'Elephant' : 'Elephant',
'Toothbrush' : 'Toothbrush',
'Baseball bat' : 'Baseball bat',
'Snowboard' : 'Snowboard',
'Train' : 'Train',
}