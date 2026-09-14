#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create English version of index.html and add language switch buttons to both pages."""

import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ============================================================
# 1. Language switch button HTML (injected into navbar)
# ============================================================
switch_btn_zh = """<li class="nav-item mr-3 mr-lg-0">
                            <a href="./index-en.html" class="nav-link" style="font-size:14px;padding:6px 12px;border:1px solid #ddd;border-radius:20px;color:inherit;">
                                <i class="fas fa-language mr-1"></i>EN
                            </a>
                        </li>"""

switch_btn_en = """<li class="nav-item mr-3 mr-lg-0">
                            <a href="./index.html" class="nav-link" style="font-size:14px;padding:6px 12px;border:1px solid #ddd;border-radius:20px;color:inherit;">
                                <i class="fas fa-language mr-1"></i>中文
                            </a>
                        </li>"""

# Insert switch button before the search icon in navbar
# Find the nav-search li and insert before it
nav_search_marker = '<li class="nav-search ml-3 ml-md-4">'
html_zh = html.replace(
    nav_search_marker,
    switch_btn_zh + "\n\n\n                        " + nav_search_marker,
)

# ============================================================
# 2. Translation dictionary (Chinese -> English)
# ============================================================
translations = [
    # HTML lang attribute
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
    # alt text for logo
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
    # Sidebar bottom links
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
    # Search engine labels (text-muted spans)
    ('<span class="text-muted">百度</span>', '<span class="text-muted">Baidu</span>'),
    ('<span class="text-muted">必应</span>', '<span class="text-muted">Bing</span>'),
    ('<span class="text-muted">谷歌</span>', '<span class="text-muted">Google</span>'),
    (
        '<span class="text-muted">软件</span>',
        '<span class="text-muted">Software</span>',
    ),
    ('<span class="text-muted">文献</span>', '<span class="text-muted">Papers</span>'),
    ('<span class="text-muted">360</span>', '<span class="text-muted">360</span>'),
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
    ('<span class="text-muted">12306</span>', '<span class="text-muted">12306</span>'),
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
    # Search data-placeholder
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
    ('data-placeholder="12306"', 'data-placeholder="12306"'),
    ('data-placeholder="去哪儿"', 'data-placeholder="Qunar"'),
    ('data-placeholder="智联招聘"', 'data-placeholder="Zhaopin"'),
    ('data-placeholder="前程无忧"', 'data-placeholder="51Job"'),
    ('data-placeholder="拉钩网"', 'data-placeholder="Lagou"'),
    ('data-placeholder="猎聘网"', 'data-placeholder="Liepin"'),
    ('data-placeholder="远程职位"', 'data-placeholder="Remote Jobs"'),
    # Category headers (h4 text after the icon span)
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
    # Hitokoto default text
    ("疏影横斜水清浅，暗香浮动月黄昏。", "A random thought for you."),
    # "直达" tooltip on card links
    ('title="直达"', 'title="Visit"'),
    # ============================================================
    # 3. Website card names (strong tags) and descriptions
    # ============================================================
    # Popular Tools section
    ("<strong>语雀</strong>", "<strong>Yuque</strong>"),
    ("专业的云端知识库。", "Professional cloud knowledge base."),
    ("<strong>QQ 邮箱</strong>", "<strong>QQ Mail</strong>"),
    ("腾讯 QQ 邮箱。", "Tencent QQ email service."),
    ("<strong>开源中国</strong>", "<strong>OSChina</strong>"),
    ("中文开源技术交流社区。", "Chinese open-source tech community."),
    ("<strong>公众号平台</strong>", "<strong>WeChat Official Account</strong>"),
    (
        "再小的个体也有自己的品牌。",
        "Even the smallest individual can have their own brand.",
    ),
    ("<strong>GitHub</strong>", "<strong>GitHub</strong>"),
    ("GitHub 开源社区。", "GitHub open-source community."),
    ("<strong>在线ps</strong>", "<strong>Online PS</strong>"),
    ("一键p图抠图工具", "One-click photo editing and background removal"),
    ("<strong>房贷计算器</strong>", "<strong>Mortgage Calculator</strong>"),
    ("房贷利率计算器", "Mortgage rate calculator"),
    ("<strong>m3u8在线播放器</strong>", "<strong>M3U8 Player</strong>"),
    ("m3u8/hls在线播放", "M3U8/HLS online player"),
    ("<strong>在线工具助手</strong>", "<strong>Online Tool Hub</strong>"),
    ("一些常见的开发工具", "Common development tools"),
    ("<strong>远程工作</strong>", "<strong>Remote Work</strong>"),
    ("远程工作搜索，一搜即达。", "Remote job search, find it instantly."),
]

# ============================================================
# 4. Read remaining card data from lines 926+ for full translation
# ============================================================
# I need to read the middle section to get all 149 cards
# For now, let me also handle cards from the rest of the file

# Read the full file to get all card names/descriptions
with open("index.html", "r", encoding="utf-8") as f:
    full_lines = f.readlines()

# Extract all data-original-title and strong text pairs from the full file
card_translations = {}

# Pattern: data-original-title="..." ... <strong>...</strong> ... <p class="overflowClip_1 m-0 text-muted text-xs">...</p>
# Collect all unique Chinese text from strong and p tags
strong_texts = set()
desc_texts = set()
title_texts = set()

for line in full_lines:
    # strong tags
    for m in re.finditer(r"<strong>([^<]+)</strong>", line):
        t = m.group(1).strip()
        if t and any("\u4e00" <= c <= "\u9fff" for c in t):
            strong_texts.add(t)
    # p description tags
    for m in re.finditer(
        r'<p class="overflowClip_1 m-0 text-muted text-xs">([^<]*)</p>', line
    ):
        t = m.group(1).strip()
        if t and any("\u4e00" <= c <= "\u9fff" for c in t):
            desc_texts.add(t)
    # data-original-title
    for m in re.finditer(r'data-original-title="([^"]*)"', line):
        t = m.group(1).strip()
        if t and any("\u4e00" <= c <= "\u9fff" for c in t):
            title_texts.add(t)

# Print summary
print(f"Found {len(strong_texts)} unique Chinese strong texts")
print(f"Found {len(desc_texts)} unique Chinese description texts")
print(f"Found {len(title_texts)} unique Chinese title texts")

# Print them for review
print("\n=== STRONG TEXTS ===")
for t in sorted(strong_texts):
    print(f"  {t}")

print("\n=== DESCRIPTION TEXTS ===")
for t in sorted(desc_texts):
    print(f"  {t}")

print("\n=== TITLE TEXTS ===")
for t in sorted(title_texts):
    print(f"  {t}")
