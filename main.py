import os
import shutil
from datetime import datetime

dark_souls_3_save_dir = r'C:\Users\your_user_name\AppData\Roaming\DarkSoulsIII'
back_up_dir = r'C:\Users\your_user_name\Documents\ds3_save_backup'

# find save file
file_paths = [f'{dark_souls_3_save_dir}{os.sep}{fileName}' for fileName in os.listdir(dark_souls_3_save_dir)]
save_dir = ''
for path in file_paths:
    if os.path.isdir(path):
        save_dir = path
        break

save_file_name = [name for name in os.listdir(save_dir) if name.endswith('.sl2')][0]
game_save_path = f'{save_dir}{os.sep}{save_file_name}'

# copy and rename file to back up dir
now = datetime.now()
game_save_new_name = now.strftime('%Y%m%d%H%M%S') + save_file_name
game_save_destination = f'{back_up_dir}{os.sep}{game_save_new_name}'
shutil.copy2(game_save_path, game_save_destination)

# save only the last 10, remove oldest first
back_ups = os.listdir(back_up_dir)
if len(back_ups) > 10:
    back_ups.sort()
    surplus_back_ups = back_ups[:len(back_ups) - 10]
    for file in surplus_back_ups:
        path = f'{back_up_dir}{os.sep}{file}'
        os.remove(path)
