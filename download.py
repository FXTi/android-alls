#!/bin/sh/python
import os

API2JAR = {
    31: "org:robolectric:android-all:12-robolectric-7732740",
    30: "org:robolectric:android-all:11-robolectric-6757853",
    29: "org:robolectric:android-all:10-robolectric-5803371",
    28: "org:robolectric:android-all:9-robolectric-4913185-2",
    27: "org:robolectric:android-all:8.1.0-robolectric-4611349",
    26: "org:robolectric:android-all:8.0.0_r4-robolectric-r1",
    25: "org:robolectric:android-all:7.1.0_r7-robolectric-r1",
    24: "org:robolectric:android-all:7.0.0_r1-robolectric-r1",
    23: "org:robolectric:android-all:6.0.1_r3-robolectric-r1",
    22: "org:robolectric:android-all:5.1.1_r9-robolectric-r2",
    21: "org:robolectric:android-all:5.0.2_r3-robolectric-r0",
    19: "org:robolectric:android-all:4.4_r1-robolectric-r2",
    18: "org:robolectric:android-all:4.3_r2-robolectric-r1",
    17: "org:robolectric:android-all:4.2.2_r1.2-robolectric-r1",
    16: "org:robolectric:android-all:4.1.2_r1-robolectric-r1",
}

MIRROR_URL = 'https://maven.aliyun.com/repository/central/'

for api in API2JAR.keys():
    try:
        os.mkdir('android-{}'.format(api))
    except FileExistsError:
        continue
    artifacts = API2JAR[api].split(':')
    cmd = 'wget ' + MIRROR_URL + '/'.join(artifacts) + '/' + '-'.join(artifacts[-2:]) + ".jar -O " + 'android-{}'.format(api) + "/android-all.jar"
    print(cmd)
    os.system(cmd)
