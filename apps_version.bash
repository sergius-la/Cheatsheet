echo "------------------------"
echo "    Douyin" 
adb shell dumpsys package com.ss.android.ugc.aweme | grep versionName
echo "------------------------"

echo "------------------------"
echo "    Kuaishou" 
adb shell dumpsys package com.smile.giftmaker | grep versionName
echo "------------------------"

echo "------------------------"
echo "    Wechat" 
adb shell dumpsys package com.tencent.mm | grep versionName
echo "------------------------"

echo "------------------------"
echo "    Toutiao" 
adb shell dumpsys package com.ss.android.article.news | grep versionName
echo "------------------------"

echo "------------------------"
echo "    Netease News" 
adb shell dumpsys package com.netase.newsreader.activity | grep versionName
echo "------------------------"

echo "------------------------"
echo "    Tencent News" 
adb shell dumpsys package com.tencent.news | grep versionName
echo "------------------------"

echo "------------------------"
echo "    Xigua" 
adb shell dumpsys package com.ss.android.article.video | grep versionName
echo "------------------------"

echo "------------------------"
echo "    Houshan" 
adb shell dumpsys package com.ss.android.ugc.live | grep versionName
echo "------------------------"