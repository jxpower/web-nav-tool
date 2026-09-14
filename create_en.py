#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create English version of index.html and add language switch buttons to both pages."""

import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ============================================================
# 1. Language switch button HTML
# ============================================================
switch_btn_zh = """<li class="nav-item mr-3 mr-lg-0">
                            <a href="./index-en.html" class="nav-link" style="font-size:14px;padding:6px 12px;border:1px solid #ddd;border-radius:20px;color:inherit;text-decoration:none;">
                                <i class="fas fa-language mr-1"></i>EN
                            </a>
                        </li>"""

switch_btn_en = """<li class="nav-item mr-3 mr-lg-0">
                            <a href="./index.html" class="nav-link" style="font-size:14px;padding:6px 12px;border:1px solid #ddd;border-radius:20px;color:inherit;text-decoration:none;">
                                <i class="fas fa-language mr-1"></i>中文
                            </a>
                        </li>"""

# Insert switch button before the search icon in navbar
nav_search_marker = '<li class="nav-search ml-3 ml-md-4">'
html_zh = html.replace(
    nav_search_marker,
    switch_btn_zh + "\n\n\n                        " + nav_search_marker,
)

# ============================================================
# 2. All translations (Chinese -> English)
# ============================================================
translations = [
    # HTML lang
    ('<html lang="zh-CN">', '<html lang="en">'),
    # Title and meta
    (
        "极限动力工具网 - 实用的资源导航综合网站",
        "JXPower Tools - Practical Resource Navigation Hub",
    ),
    (
        "极限动力工具网,网址导航,开发工具,实用工具,在线工具",
        "JXPower,web directory,dev tools,online tools,utility tools",
    ),
    (
        "极限动力工具网 - 收录各类实用工具网站，包括开发工具、绘图工具、在线编辑器、格式转换等，一站式工具导航平台。",
        "JXPower Tools - A curated collection of practical tool websites including dev tools, design tools, online editors, format converters and more.",
    ),
    # alt/title for logo
    ('alt="极限动力工具网"', 'alt="JXPower Tools"'),
    ('title="极限动力工具网"', 'title="JXPower Tools"'),
    # Sidebar main categories
    ("<span>常用工具</span>", "<span>Popular Tools</span>"),
    ("<span>科研办公</span>", "<span>Research & Office</span>"),
    ("<span>悠闲娱乐</span>", "<span>Entertainment</span>"),
    ("<span>素材资源</span>", "<span>Assets & Resources</span>"),
    ("<span>开发设计</span>", "<span>Dev & Design</span>"),
    ("<span>资讯学习</span>", "<span>News & Learning</span>"),
    # Sidebar subcategories
    ("<span>生物信息</span>", "<span>Bioinformatics</span>"),
    ("<span>云服务器</span>", "<span>Cloud Servers</span>"),
    ("<span>办公学习</span>", "<span>Office & Study</span>"),
    ("<span>影音视频</span>", "<span>Video & Music</span>"),
    ("<span>游戏竞技</span>", "<span>Gaming</span>"),
    ("<span>网盘资源</span>", "<span>Cloud Storage</span>"),
    ("<span>图标素材</span>", "<span>Icon Assets</span>"),
    ("<span>图标设计</span>", "<span>Icon Design</span>"),
    ("<span>平面素材</span>", "<span>Graphic Assets</span>"),
    ("<span>字体资源</span>", "<span>Font Resources</span>"),
    ("<span>PPT资源</span>", "<span>PPT Resources</span>"),
    ("<span>图形创意</span>", "<span>Graphic Design</span>"),
    ("<span>界面设计</span>", "<span>UI Design</span>"),
    ("<span>在线配色</span>", "<span>Color Tools</span>"),
    ("<span>在线工具</span>", "<span>Online Tools</span>"),
    ("<span>谷歌插件</span>", "<span>Chrome Extensions</span>"),
    ("<span>资讯图书</span>", "<span>News & Books</span>"),
    ("<span>博客论坛</span>", "<span>Blog & Forum</span>"),
    ("<span>设计规范</span>", "<span>Design Specs</span>"),
    ("<span>视频教程</span>", "<span>Video Tutorials</span>"),
    # Sidebar bottom
    ("<span>网站提交</span>", "<span>Submit Site</span>"),
    ("<span>友情链接</span>", "<span>Friend Links</span>"),
    ("<span>关于导航</span>", "<span>About</span>"),
    # Top navbar
    ("<span>首页</span>", "<span>Home</span>"),
    ("<span>关于</span>", "<span>About</span>"),
    # Search bar tabs
    ('data-id="group-a"><span>常用</span>', 'data-id="group-a"><span>Popular</span>'),
    ('data-id="group-b"><span>搜索</span>', 'data-id="group-b"><span>Search</span>'),
    ('data-id="group-c"><span>工具</span>', 'data-id="group-c"><span>Tools</span>'),
    ('data-id="group-d"><span>社区</span>', 'data-id="group-d"><span>Community</span>'),
    ('data-id="group-e"><span>生活</span>', 'data-id="group-e"><span>Lifestyle</span>'),
    ('data-id="group-f"><span>求职</span>', 'data-id="group-f"><span>Jobs</span>'),
    # Search placeholder
    ('placeholder="输入关键字搜索"', 'placeholder="Enter keywords to search"'),
    # Search engine labels
    ('<span class="text-muted">百度</span>', '<span class="text-muted">Baidu</span>'),
    ('<span class="text-muted">必应</span>', '<span class="text-muted">Bing</span>'),
    ('<span class="text-muted">谷歌</span>', '<span class="text-muted">Google</span>'),
    (
        '<span class="text-muted">软件</span>',
        '<span class="text-muted">Software</span>',
    ),
    ('<span class="text-muted">文献</span>', '<span class="text-muted">Papers</span>'),
    ('<span class="text-muted">搜狗</span>', '<span class="text-muted">Sogou</span>'),
    ('<span class="text-muted">神马</span>', '<span class="text-muted">Sm</span>'),
    (
        '<span class="text-muted">权重查询</span>',
        '<span class="text-muted">Rank Check</span>',
    ),
    (
        '<span class="text-muted">友链检测</span>',
        '<span class="text-muted">Link Check</span>',
    ),
    (
        '<span class="text-muted">域名信息查询</span>',
        '<span class="text-muted">WHOIS</span>',
    ),
    (
        '<span class="text-muted">PING 检测</span>',
        '<span class="text-muted">PING Test</span>',
    ),
    (
        '<span class="text-muted">死链检测</span>',
        '<span class="text-muted">Dead Link Check</span>',
    ),
    (
        '<span class="text-muted">关键词挖掘</span>',
        '<span class="text-muted">Keyword Tool</span>',
    ),
    ('<span class="text-muted">知乎</span>', '<span class="text-muted">Zhihu</span>'),
    ('<span class="text-muted">微信</span>', '<span class="text-muted">WeChat</span>'),
    ('<span class="text-muted">微博</span>', '<span class="text-muted">Weibo</span>'),
    ('<span class="text-muted">豆瓣</span>', '<span class="text-muted">Douban</span>'),
    ('<span class="text-muted">淘宝</span>', '<span class="text-muted">Taobao</span>'),
    ('<span class="text-muted">京东</span>', '<span class="text-muted">JD</span>'),
    (
        '<span class="text-muted">下厨房</span>',
        '<span class="text-muted">Xiachufang</span>',
    ),
    (
        '<span class="text-muted">香哈菜谱</span>',
        '<span class="text-muted">Xiangha</span>',
    ),
    ('<span class="text-muted">去哪儿</span>', '<span class="text-muted">Qunar</span>'),
    (
        '<span class="text-muted">智联招聘</span>',
        '<span class="text-muted">Zhaopin</span>',
    ),
    (
        '<span class="text-muted">前程无忧</span>',
        '<span class="text-muted">51Job</span>',
    ),
    ('<span class="text-muted">拉钩网</span>', '<span class="text-muted">Lagou</span>'),
    (
        '<span class="text-muted">猎聘网</span>',
        '<span class="text-muted">Liepin</span>',
    ),
    (
        '<span class="text-muted">远程职位</span>',
        '<span class="text-muted">Remote Jobs</span>',
    ),
    # data-placeholder
    ('data-placeholder="百度一下，你就知道"', 'data-placeholder="Baidu Search"'),
    ('data-placeholder="微软 Bing 搜索"', 'data-placeholder="Microsoft Bing Search"'),
    ('data-placeholder="微软必应搜索"', 'data-placeholder="Microsoft Bing Search"'),
    ('data-placeholder="谷歌搜索"', 'data-placeholder="Google Search"'),
    (
        'data-placeholder="Anaconda 软件搜索"',
        'data-placeholder="Anaconda Package Search"',
    ),
    (
        'data-placeholder="PubMed 搜索/文章标题/关键字"',
        'data-placeholder="PubMed Search / Title / Keywords"',
    ),
    ('data-placeholder="360 好搜"', 'data-placeholder="360 Search"'),
    ('data-placeholder="搜狗搜索"', 'data-placeholder="Sogou Search"'),
    ('data-placeholder="UC 移动端搜索"', 'data-placeholder="UC Mobile Search"'),
    (
        'data-placeholder="请输入网址(不带 https://)"',
        'data-placeholder="Enter URL (without https://)"',
    ),
    (
        'data-placeholder="请输入网址(不带https://)"',
        'data-placeholder="Enter URL (without https://)"',
    ),
    ('data-placeholder="请输入关键词"', 'data-placeholder="Enter keywords"'),
    ('data-placeholder="知乎"', 'data-placeholder="Zhihu"'),
    ('data-placeholder="微信"', 'data-placeholder="WeChat"'),
    ('data-placeholder="微博"', 'data-placeholder="Weibo"'),
    ('data-placeholder="豆瓣"', 'data-placeholder="Douban"'),
    ('data-placeholder="淘宝"', 'data-placeholder="Taobao"'),
    ('data-placeholder="京东"', 'data-placeholder="JD.com"'),
    ('data-placeholder="下厨房"', 'data-placeholder="Xiachufang"'),
    ('data-placeholder="香哈菜谱"', 'data-placeholder="Xiangha Recipes"'),
    ('data-placeholder="去哪儿"', 'data-placeholder="Qunar"'),
    ('data-placeholder="智联招聘"', 'data-placeholder="Zhaopin"'),
    ('data-placeholder="前程无忧"', 'data-placeholder="51Job"'),
    ('data-placeholder="拉钩网"', 'data-placeholder="Lagou"'),
    ('data-placeholder="猎聘网"', 'data-placeholder="Liepin"'),
    ('data-placeholder="远程职位"', 'data-placeholder="Remote Jobs"'),
    # Category headers (text after </i>\n)
    (">常用工具\n", ">Popular Tools\n"),
    (">生物信息\n", ">Bioinformatics\n"),
    (">云服务器\n", ">Cloud Servers\n"),
    (">办公学习\n", ">Office & Study\n"),
    (">影音视频\n", ">Video & Music\n"),
    (">游戏竞技\n", ">Gaming\n"),
    (">网盘资源\n", ">Cloud Storage\n"),
    (">图标素材\n", ">Icon Assets\n"),
    (">图标设计\n", ">Icon Design\n"),
    (">平面素材\n", ">Graphic Assets\n"),
    (">字体资源\n", ">Font Resources\n"),
    (">PPT资源\n", ">PPT Resources\n"),
    (">图形创意\n", ">Graphic Design\n"),
    (">界面设计\n", ">UI Design\n"),
    (">在线配色\n", ">Color Tools\n"),
    (">在线工具\n", ">Online Tools\n"),
    (">谷歌插件\n", ">Chrome Extensions\n"),
    (">资讯图书\n", ">News & Books\n"),
    (">博客论坛\n", ">Blog & Forum\n"),
    (">设计规范\n", ">Design Specs\n"),
    (">视频教程\n", ">Video Tutorials\n"),
    # Search modal labels
    (">常用</label>", ">Popular</label>"),
    (">搜索</label>", ">Search</label>"),
    (">工具</label>", ">Tools</label>"),
    (">社区</label>", ">Community</label>"),
    (">生活</label>", ">Lifestyle</label>"),
    (">求职</label>", ">Jobs</label>"),
    # type-text spans in modal
    (
        'class="type-text text-muted">常用</span>',
        'class="type-text text-muted">Popular</span>',
    ),
    (
        'class="type-text text-muted">搜索</span>',
        'class="type-text text-muted">Search</span>',
    ),
    (
        'class="type-text text-muted">工具</span>',
        'class="type-text text-muted">Tools</span>',
    ),
    (
        'class="type-text text-muted">社区</span>',
        'class="type-text text-muted">Community</span>',
    ),
    (
        'class="type-text text-muted">生活</span>',
        'class="type-text text-muted">Lifestyle</span>',
    ),
    (
        'class="type-text text-muted">求职</span>',
        'class="type-text text-muted">Jobs</span>',
    ),
    # Footer
    (
        "本站内容源自互联网，如有内容侵犯了你的权益，请联系删除相关内容。",
        "Site content is sourced from the internet. If any content infringes your rights, please contact us for removal.",
    ),
    ("在线工具导航", "JXPower Tools"),
    ("关于我们", "About Us"),
    # Night mode tooltips
    ('title="日间模式"', 'title="Day Mode"'),
    ('"日间模式"', '"Day Mode"'),
    ('"夜间模式"', '"Night Mode"'),
    # Hitokoto
    ("疏影横斜水清浅，暗香浮动月黄昏。", "A random thought for you."),
    # "直达" tooltip
    ('title="直达"', 'title="Visit"'),
    # ============================================================
    # Website card names (strong tags) - 56 unique
    # ============================================================
    ("<strong>语雀</strong>", "<strong>Yuque</strong>"),
    ("<strong>QQ 邮箱</strong>", "<strong>QQ Mail</strong>"),
    ("<strong>开源中国</strong>", "<strong>OSChina</strong>"),
    ("<strong>公众号平台</strong>", "<strong>WeChat Official</strong>"),
    ("<strong>GitHub</strong>", "<strong>GitHub</strong>"),
    ("<strong>在线ps</strong>", "<strong>Online PS</strong>"),
    ("<strong>房贷计算器</strong>", "<strong>Mortgage Calculator</strong>"),
    ("<strong>m3u8在线播放器</strong>", "<strong>M3U8 Player</strong>"),
    ("<strong>在线工具助手</strong>", "<strong>Online Tool Hub</strong>"),
    ("<strong>远程工作</strong>", "<strong>Remote Work</strong>"),
    ("<strong>阿里云</strong>", "<strong>Alibaba Cloud</strong>"),
    ("<strong>腾讯云</strong>", "<strong>Tencent Cloud</strong>"),
    ("<strong>华为云</strong>", "<strong>Huawei Cloud</strong>"),
    ("<strong>青椒云</strong>", "<strong>Qingjiao Cloud</strong>"),
    ("<strong>云筏科技</strong>", "<strong>Yunfa Tech</strong>"),
    ("<strong>极云普惠云电脑</strong>", "<strong>Jiyun Cloud PC</strong>"),
    ("<strong>优酷</strong>", "<strong>Youku</strong>"),
    ("<strong>爱奇艺</strong>", "<strong>iQiyi</strong>"),
    ("<strong>哔哩哔哩</strong>", "<strong>Bilibili</strong>"),
    ("<strong>腾讯视频</strong>", "<strong>Tencent Video</strong>"),
    ("<strong>QQ音乐</strong>", "<strong>QQ Music</strong>"),
    ("<strong>网易云音乐</strong>", "<strong>NetEase Music</strong>"),
    ("<strong>电影天堂（DYGOD）</strong>", "<strong>DYgod Movies</strong>"),
    ("<strong>电影天堂（DYTT8）</strong>", "<strong>DYTT8 Movies</strong>"),
    ("<strong>台服战地</strong>", "<strong>AVA Battlefield</strong>"),
    ("<strong>百度网盘</strong>", "<strong>Baidu Netdisk</strong>"),
    ("<strong>阿里云盘</strong>", "<strong>Aliyun Drive</strong>"),
    ("<strong>天翼云盘</strong>", "<strong>Tianyi Cloud Drive</strong>"),
    ("<strong>坚果云</strong>", "<strong>Jianguo Cloud</strong>"),
    ("<strong>百度贴吧</strong>", "<strong>Baidu Tieba</strong>"),
    ("<strong>知乎</strong>", "<strong>Zhihu</strong>"),
    ("<strong>书栈网</strong>", "<strong>BookStack</strong>"),
    ("<strong>微信读书</strong>", "<strong>WeChat Read</strong>"),
    ("<strong>慕课网</strong>", "<strong>MOOC</strong>"),
    ("<strong>经管之家</strong>", "<strong>JingGuan Home</strong>"),
    ("<strong>有道翻译</strong>", "<strong>Youdao Translate</strong>"),
    ("<strong>有道词典</strong>", "<strong>Youdao Dictionary</strong>"),
    ("<strong>谷歌翻译</strong>", "<strong>Google Translate</strong>"),
    ("<strong>酷壳</strong>", "<strong>CoolShell</strong>"),
    ("<strong>阮一峰的网络日志</strong>", "<strong>Ruan Yifeng Blog</strong>"),
    ("<strong>base64在线解码</strong>", "<strong>Base64 Codec</strong>"),
    ("<strong>在线图像编辑器</strong>", "<strong>Online Image Editor</strong>"),
    ("<strong>素材中国</strong>", "<strong>SucaiCN</strong>"),
    ("<strong>千图网</strong>", "<strong>Qiantu</strong>"),
    ("<strong>千库网</strong>", "<strong>Qianku</strong>"),
    ("<strong>懒人图库</strong>", "<strong>Lazyren</strong>"),
    ("<strong>我图网</strong>", "<strong>Wotu</strong>"),
    ("<strong>素材搜索</strong>", "<strong>Asset Search</strong>"),
    ("<strong>5百丁</strong>", "<strong>5Baiding</strong>"),
    ("<strong>90 设计</strong>", "<strong>90 Design</strong>"),
    ("<strong>优品PPT</strong>", "<strong>Youpin PPT</strong>"),
    ("<strong>PS 饭团网</strong>", "<strong>PS Fantuan</strong>"),
    ("<strong>私藏字体</strong>", "<strong>Sicang Fonts</strong>"),
    ("<strong>字体传奇网</strong>", "<strong>Font Legend</strong>"),
    ("<strong>方正字库</strong>", "<strong>Founder Fonts</strong>"),
    # ============================================================
    # Card descriptions (data-original-title and p text) - 71 unique
    # ============================================================
    ("专业的云端知识库。", "Professional cloud knowledge base."),
    ("腾讯 QQ 邮箱。", "Tencent QQ email service."),
    ("中文开源技术交流社区。", "Chinese open-source tech community."),
    (
        "再小的个体也有自己的品牌。",
        "Even the smallest individual can have their own brand.",
    ),
    ("GitHub 开源社区。", "GitHub open-source community."),
    ("一键p图抠图工具", "One-click photo editing and background removal"),
    ("房贷利率计算器", "Mortgage rate calculator"),
    ("m3u8/hls在线播放", "M3U8/HLS online player"),
    ("一些常见的开发工具", "Common development tools"),
    ("远程工作搜索，一搜即达。", "Remote job search, find it instantly."),
    ("远程职位搜索，一搜即达。", "Remote job search, find it instantly."),
    ("上云就上阿里云。", "Alibaba Cloud - the cloud of choice."),
    ("产业智变，云启未来。", "Tencent Cloud - empowering industries."),
    (
        "提供云计算服务+智能，见未来-华为云。",
        "Huawei Cloud - computing services + intelligence.",
    ),
    ("云桌面,一站式云电脑服务平台。", "Cloud desktop, all-in-one cloud PC platform."),
    (
        "云电脑-云游戏-手机变电脑软件。",
        "Cloud PC - cloud gaming - phone-to-PC software.",
    ),
    ("云筏 - 科研云。", "Yunfa - research cloud platform."),
    ("优酷 - 这个世界很酷。", "Youku - discover a cool world."),
    ("爱奇艺在线视频。", "iQiyi online video streaming."),
    ("Bilibili 视频弹幕网站。", "Bilibili - video with danmaku comments."),
    ("腾讯视频，海量视频在线观看。", "Tencent Video - massive online video library."),
    ("QQ 音乐，在线听歌。", "QQ Music - listen to music online."),
    ("163 网易云音乐。", "NetEase Music - online music streaming."),
    ("电影天堂（DYGOD），高清电影下载。", "DYgod - HD movie downloads."),
    ("电影天堂（DYTT8），高清电影下载。", "DYTT8 - HD movie downloads."),
    ("台服 AVA 战地之王。", "AVA Battlefield - Taiwan server."),
    ("家庭云|网盘|文件备份|资源分享。", "Cloud storage | backup | file sharing."),
    ("阿里云盘，你的数字世界。", "Aliyun Drive - your digital world."),
    ("天翼云盘，你的个人云盘。", "Tianyi Cloud Drive - your personal cloud."),
    ("坚果云官网。", "Jianguo Cloud official site."),
    ("百度贴吧。", "Baidu Tieba - online community forum."),
    ("知乎社区。", "Zhihu - community Q&A platform."),
    ("IT 互联网开源编程书籍免费阅读与下载。", "Free IT and programming books online."),
    ("微信读书电脑版。", "WeChat Read - desktop version."),
    (
        "程序员的梦工厂（有UI课程）。",
        "MOOC - programmer training platform with UI courses.",
    ),
    (
        "国内活跃的经济、管理、金融、统计在线教育和咨询网站。",
        "Active economics, management, finance and statistics education site.",
    ),
    ("免费，即时的多语种在线翻译。", "Free, instant multilingual online translation."),
    ("有道翻译。", "Youdao translation service."),
    ("谷歌翻译。", "Google translation service."),
    ("酷 壳 – CoolShell。", "CoolShell - tech blog by Chen Hao."),
    ("阮一峰，科技爱好者周刊。", "Ruan Yifeng - tech enthusiast weekly."),
    ("重新掌控你的新闻订阅源。", "Take back control of your news feed."),
    ("base64在线解码与编码", "Online Base64 encode and decode"),
    ("在线图像编辑器", "Online image editor"),
    ("Photoshop不需要解释", "Photoshop needs no explanation"),
    ("矢量图形和插图。", "Vector graphics and illustrations."),
    ("阿里巴巴矢量图标库。", "Alibaba vector icon library."),
    (
        "PNG、ICO、ICNS格式图标搜索、图标下载服务。",
        "PNG, ICO, ICNS icon search and download.",
    ),
    ("免费 png 图片背景素材下载。", "Free PNG image and background downloads."),
    ("免费素材共享平台。", "Free asset sharing platform."),
    ("原创素材共享平台。", "Original asset sharing platform."),
    ("专注免费设计素材下载的网站.", "Free design asset download site."),
    ("懒人图库专注于提供网页素材下载。", "Lazyren - web design asset downloads."),
    (
        "我图网，提供图片素材及模板下载，专注正版设计作品交易。",
        "Wotu - design assets, templates and licensed artwork marketplace.",
    ),
    ("设计素材搜索聚合。", "Design asset search aggregator."),
    (
        "不一样的设计素材库！让自己的设计与众不同！",
        "A unique design asset library! Make your designs stand out!",
    ),
    (
        "电商设计（淘宝美工）千图免费淘宝素材库。",
        "E-commerce design - free Taobao asset library.",
    ),
    ("中国领先的PPT模板共享平台。", "Leading Chinese PPT template sharing platform."),
    (
        "分享高端 ppt 模板与 keynote 模板的数字作品交易平台。",
        "Premium PPT and Keynote template marketplace.",
    ),
    (
        "高质量的模版，而且还有PPT图表，PPT背景图等资源。",
        "High-quality templates, PPT charts and background images.",
    ),
    (
        "OfficePLUS，微软Office官方在线模板网站！",
        "OfficePLUS - official Microsoft Office template site!",
    ),
    (
        "PPT加直播、录制和分享—PPT+语音内容分享平台。",
        "PPT with live stream, recording and sharing platform.",
    ),
    (
        "5百丁，专业的在线PPT设计平台。",
        "5Baiding - professional online PPT design platform.",
    ),
    (
        "90设计 - 电商设计师必备平台。",
        "90 Design - essential platform for e-commerce designers.",
    ),
    (
        "PS饭团网 - Photoshop教程和资源。",
        "PS Fantuan - Photoshop tutorials and resources.",
    ),
    (
        "中国首个字体品牌设计师交流网。",
        "First Chinese font brand and designer community.",
    ),
    ("优质字体免费下载站。", "Quality free font download site."),
    ("方正字库官方网站。", "Founder Fonts official website."),
    ("专业创意软件。", "Professional creative software."),
    ("创意设计软件学习平台。", "Creative design software learning platform."),
    ("WEB UI免费视频公开课。", "Free WEB UI video courses."),
    ("页面设计、布局和出版。", "Page design, layout and publishing."),
    ("无需利用编码即可进行网站设计。", "Design websites without coding."),
    ("文本转语音。", "Text to speech conversion."),
    (
        "一家关于计算机黑客和创业公司的社会化新闻网站。",
        "Social news site about hackers and startups.",
    ),
    ("V2EX 创意工作者的社区。", "V2EX - community for creative professionals."),
]

# Apply all translations to create English version
html_en = html_zh
for old, new in translations:
    html_en = html_en.replace(old, new)

# Insert English switch button into English version
html_en = html_en.replace(
    nav_search_marker,
    switch_btn_en + "\n\n\n                        " + nav_search_marker,
)

# Write Chinese version (with switch button added)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_zh)
print("index.html updated with EN switch button")

# Write English version
with open("index-en.html", "w", encoding="utf-8") as f:
    f.write(html_en)
print("index-en.html created with full English translation + ZH switch button")

# Verify no Chinese remains in index-en.html (check for CJK characters)
cjk_remaining = 0
for i, line in enumerate(html_en.split("\n"), 1):
    for ch in line:
        if "\u4e00" <= ch <= "\u9fff":
            cjk_remaining += 1
            if cjk_remaining <= 20:
                print(f"  CJK at line {i}: {line.strip()[:80]}")
print(f"\nTotal remaining CJK characters: {cjk_remaining}")
