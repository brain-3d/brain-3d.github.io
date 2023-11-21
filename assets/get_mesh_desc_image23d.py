import os

scenes = sorted([f[:-4] for f in os.listdir('glb')])
image_to_3D_scenes = [f[:-4] for f in os.listdir('../../dreammaker-results/fine_0711/image_to_3D_glb') if f.endswith('.glb')]
scenes = [s for s in scenes if s in image_to_3D_scenes]
total_s = ''
titles = []

for scene in scenes:
    name = scene[:-1].replace('_', ' ')
    name = name.replace(',', '')
    i = 1
    while '_'.join(name.split()[-i:]) in titles:
        i += 1
    title = '_'.join(name.split()[-i:])
    title = title.replace(',', '')
    titles.append(title)
    src = "/assets/glb/{}.glb".format(scene)
    poster = "/assets/poster/{}.png".format(scene)
    caption = name
    shortCaption = name.replace('a DSLR photo of', '[...]')
    s = f"""{title}: {{
    src: "{src}",
    poster: "{poster}",
    "environment-image": "https://modelviewer.dev/shared-assets/environments/spruit_sunrise_1k_HDR.hdr",
    caption: "{caption}",
    shortCaption: "{shortCaption}"
}},\n"""
    total_s += s
with open('mesh_desc_image23d.txt', 'w') as f:
    f.write(total_s)
print(total_s)
print(len(titles), len(set(titles)))

titles_ = titles[:-1]
title_s = ""
for i in range(0, len(titles_), 2):
    s = "[\'{}\', \'{}\'],\n".format(titles[i], titles[i + 1])
    title_s += s
if len(titles) % 2 == 1:
    title_s += "[\'{}\'],\n".format(titles[-1])
print(title_s)
with open('mesh_title_image23d.txt', 'w') as f:
    f.write(title_s)
print(titles)
print(scenes)