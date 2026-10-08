# 来源与核验流程

本调研采用来源驱动的策展，而非搜索结果数量驱动的收录。起点是用户指定的 VERA 和 Scale AgentEnv，同时参考本地 awesome-agent-harness、awesome-rsi 的双语目录、主题分类、结构化数据和核验方式。原参考目录没有被修改。

## 检索路径

1. 阅读两个种子的一手页面，拆出环境接口、执行式合成、模拟器、课程、验证器等子问题。
2. 沿论文、官方博客、作者页和仓库 README 扩展；交叉搜索方法名、完整标题、arXiv ID、作者与代码地址。
3. 把高相关新工作向历史依赖追溯，补入领域底座与代表性环境；对只有重名或宣传关系的候选不收录。
4. 为收录项写中英文机制和边界，区分论文、博客、实现，并以 `work_id` 关联。
5. 获取公开 GitHub API 元数据；核验目录结构、生成文件、站内链接和公开外链。

示例检索式见 [检索模板](github_query_templates.md)。候选阅读痕迹见 [来源清单](../reports/research/source-manifest.json)，典型取舍见 [裁决记录](research_decisions.md)。没有宣称检索穷尽所有数据库，也不报告不存在的筛选 PRISMA 数字。

## 四类证据不能混用

| 证据 | 能支持什么 | 不能支持什么 |
| --- | --- | --- |
| 原论文／博客内容 | 作者报告的方法、实验和限制 | 本地复现、独立验证、同行评审状态 |
| 作者页与代码交叉链接 | 实现的作者归属 | 发布完整性、安装成功、许可证兼容性 |
| GitHub API | 观测 star、push、归档、仓库大小、许可标签与规范 URL | 代码质量、有效维护、真实训练可用性 |
| HTTP 链接检查 | 本次检查时 URL 可访问／受阻／失败与重定向 | 内容永不变、来源可信度、论文结论成立 |

代码可用性由人工阅读发布说明补充，不由 HTTP 200 推导。受限网络、反爬、超时分别记录，不能用缓存成功掩盖本次失败。来源抓取缓存用于复核，位于 `.cache/`，不作为公开目录发布；来源清单只保留 URL、标题、时间、状态和内容哈希，避免复制整篇原文。

## 时间与版本

- `catalog.as_of`：本轮研究快照日（Asia/Shanghai）。
- `reviewed_at` / `last_reviewed`：人工内容复核日。
- `metadata_refreshed_at`：最近完整 GitHub 元数据批次；`metadata_incremental_refreshed_at`：新增仓库的增量批次；`github.fetched_at`：每个仓库实际查询时间（UTC）。可与本地日期相差一天，增量批次不表示旧仓库全部重新查询。
- `published`：论文首次 arXiv 提交日期；标题采用本轮看到的当前版本。博客有明确一手日期才填写。
- `link-checks.json`：网络检查自己的 UTC 时间。

当前目录是研究快照，不是锁定 commit 的复现清单。要运行论文实验，应另行锁定代码、容器、数据与依赖版本。未来只更新 stars 时，不得自动宣称重新审查了全部正文。

## 维护命令

在目录根路径执行：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/sync_github_metadata.py
.venv/bin/python scripts/render_readme.py
.venv/bin/python scripts/render_readme.py --check
.venv/bin/python scripts/verify_catalog.py
.venv/bin/python scripts/verify_catalog.py --links
.venv/bin/python -m unittest discover -s tests
```

元数据脚本使用无需凭证的 GitHub 公共 API，受公共速率限制。它先收集全部结果，任一请求失败则不覆盖数据源；错误保存在报告中。网络检查通过系统 `curl` 只读取公开页面，不登录账户、不调用模型、不执行第三方环境。连接限时 3 秒，单次总限时 8 秒；HEAD 收到 HTTP 错误才回退 GET，连接失败不反复请求。超时不能解释为资源已删除。

默认 verifier 检查字段、类别、日期、代码状态、来源、双语生成一致性和本地文件／锚点。`--links` 检查数据与文档中的 HTTP URL，报告成功、被阻止和失败，默认不抓取整页。HTTP 成功并不检查外部网页锚点或语义正确性。

最终结果见 [核验报告](../reports/verification/2026-10-08.md)。本轮没有验证第三方安装、训练复现、云资源可用性或跨许可证再分发条件。

## 本地目录名称

主目录现为 `~/Downloads/awesome-agent-environments`。原 `awesome-agent-training-environments` 路径保留为指向新目录的兼容符号链接，以便先前分享的本地文件链接继续可用。参考目录 `awesome-agent-harness` 与 `awesome-rsi` 未修改。

## 技术报告与展示核验

本轮按指定版本核对环境相关章节，并把章节 URL 与 PDF 页序写入结构化字段。模型报告与环境专题论文分开计数；章节只是报告内定位。HTML 标题 ID 由正文核验，PDF 定位由文本分页与选页渲染交叉检查。详见[第三轮记录](../reports/research/2026-10-08-presentation-and-reports.md)。
