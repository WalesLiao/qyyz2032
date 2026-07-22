################################################################################
## AnimeStyle 背景轮播（自动扫描 + 每次启动随机新增 wipe 序列）
################################################################################

# 自动扫描 game/images/AnimeStyle/ 目录下的图片文件
# 按文件名排序后存入列表，供主菜单轮播使用
# 每次启动都会重新生成 ATL 文件，wipe 序列随机更新

init python:
    import random, os

    anime_bg_list = [ ]

    for f in renpy.list_files():
        if f.startswith("images/AnimeStyle/"):
            if f.lower().endswith((".png", ".jpg", ".jpeg")):
                anime_bg_list.append(f)

    anime_bg_list.sort()

    if anime_bg_list:
        wipe_names = [
            "w1","w2","w3","w4","w5","w6","w7","w8","w9","w10",
            "w11","w12","w13","w14",
            "dots","edges","flips","fur","glasswool",
            "letter","maze","radio","wet"
        ]

        gen_file = os.path.join(config.gamedir, "_carousel_atl.rpy")

        with open(gen_file, "w", encoding="utf-8") as f:
            f.write("## 自动生成 - 每次启动随机新增\n\n")
            f.write("image carousel_anim:\n")
            for i, img in enumerate(anime_bg_list):
                w = random.choice(wipe_names)
                f.write(f'    Transform("{img}", size=(1920, 1080), fit="cover", align=(0.5, 0.5)) with {w}\n')
                f.write("    pause 1.92\n")
            f.write("    repeat\n")

