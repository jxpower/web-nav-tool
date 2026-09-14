# Cloudflare Pages 部署指南

## 前置条件

1. 已注册 Cloudflare 账号
2. 已安装 Git
3. 有一个 GitHub 账号（用于关联 Cloudflare Pages）

## 步骤一：将代码推送到 GitHub

1. 登录 GitHub，创建一个新仓库（如 `my-web-tool`）
2. 在本地项目目录执行：

```bash
cd web_tool
git add .
git commit -m "init: web navigation site with AdSense"
git remote add origin https://github.com/你的用户名/my-web-tool.git
git push -u origin main
```

## 步骤二：在 Cloudflare Pages 创建项目

1. 登录 Cloudflare Dashboard: https://dash.cloudflare.com
2. 左侧菜单选择 **Workers & Pages**
3. 点击 **Create application** → **Pages** → **Connect to Git**
4. 授权 Cloudflare 访问你的 GitHub 账号
5. 选择你刚推送的 `my-web-tool` 仓库
6. 配置构建设置：
   - **Project name**: 自定义（如 `my-web-tool`）
   - **Production branch**: `main`
   - **Framework preset**: 选择 `None`
   - **Build command**: 留空
   - **Build output directory**: `/` （根目录）
7. 点击 **Save and Deploy**

部署完成后，Cloudflare 会分配一个域名：`https://my-web-tool.pages.dev`

## 步骤三：绑定自定义域名（可选但推荐）

AdSense 审核通常需要自有域名，建议绑定：

1. 在 Cloudflare Pages 项目设置中，进入 **Custom domains**
2. 添加你的域名（如 `tools.yourdomain.com`）
3. 按提示添加 CNAME 记录
4. Cloudflare 会自动配置 HTTPS 证书

## 步骤四：申请 Google AdSense

1. 访问 https://www.google.com/adsense
2. 用 Google 账号登录并注册
3. 添加你的网站域名
4. 获取 AdSense 代码（包含 `ca-pub-XXXXXXXXXXXXXXXX` 格式的发布商ID）
5. 将 index.html 中所有 `ca-pub-XXXXXXXXXXXXXXXX` 替换为你的真实ID
6. 将 `data-ad-slot` 的数字替换为 AdSense 后台创建的广告单元ID
7. 重新推送到 GitHub，Cloudflare Pages 会自动部署

## 步骤五：AdSense 审核通过后

- 审核通常需要数天到数周
- 确保网站有足够内容（导航链接丰富、页面正常访问）
- 确保域名已绑定且 HTTPS 正常
- 审核通过后广告会自动展示

## 文件结构

```
web_tool/
├── index.html              # 首页（已添加 AdSense 广告位）
├── commit.html             # 网址提交页面
├── 404.html                # 404 页面
├── about/
│   └── index.html          # 关于页面
├── assets/
│   ├── css/               # 样式文件
│   ├── js/                # JavaScript 文件
│   ├── images/            # 图片资源
│   └── fontawesome-5.15.4/ # 图标库
└── DEPLOY.md              # 本部署指南
```

## AdSense 广告位说明

已在 index.html 中预置了 2 个广告位：
1. **顶部横幅** - 页面内容区顶部（728x90 自适应）
2. **底部横幅** - 页脚上方（728x90 自适应）

替换步骤：
1. 全局搜索 `ca-pub-XXXXXXXXXXXXXXXX`，替换为你的 AdSense 发布商ID
2. 将 `data-ad-slot` 的数字（1111111111 / 2222222222）替换为你在 AdSense 后台创建的广告单元ID
