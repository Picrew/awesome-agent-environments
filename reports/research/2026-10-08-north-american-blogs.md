# 第四轮：北美模型公司官方博客

用户要求继续补查 OpenAI、Anthropic 及其他北美强模型公司。新增 26 篇博客，未新增未经元数据核验的 GitHub 项目，也未改写上一轮报告章节位置。

- 资源从 192 增至 218；工作组从 117 增至 139；博客从 36 增至 62；公司前置文章从 12 增至 38。
- 增加独立 source_section / source_section_en 定位字段，双语详情页显示对应段落。没有使用裸 HTML 锚点。
- OpenEnv 与 NeMo Gym 文章沿用已有 work_id，Petri 两篇与 Nova Forge 两篇分别关联，避免把配套文章视为新环境项目。
- 读取官方正文与发布日期，包括页面元数据；NVIDIA 自动摘要之外另核查正文步骤，确认星形计数示例是 SFT。
- Reflection 的发布状态按正文“稍后发布”保留，不把模型标题中的 open-weight 视为当日已发布。
- 未执行任何外部项目代码、训练命令或部署教程；网页中的示例命令只作为研究材料。

[逐篇定位与筛选边界](../../docs/north_american_company_blogs.md) · [来源清单](source-manifest.json) · [核验报告](../verification/2026-10-08.md)

## 验证结果

离线结构与本地链接检查 0 错误，现有 15 项测试通过。两个主目录均解析出 38 行公司博客表，双语详情各显示 26 项新增文章定位。

新增 26 个 URL 的独立 HTTP 复查：18 成功、6 受阻、2 超时。6 个受阻项均为 OpenAI；其中 5 项已用研究浏览器读取官方正文，1 项先前正文抓取成功。Cognition 与 NVIDIA 的两次超时也有此前成功正文抓取，因此保留内容证据与网络失败两种记录，不把它们互相覆盖。整个目录保留 266 项 URL 检查结果：243 成功、8 受阻、15 失败／超时。

[本轮审计快照](../verification/north-american-blog-audit.json) · [新增链接结果](../verification/round4-incremental-links.json)
