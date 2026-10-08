# Contributing / 贡献说明

先阅读 [收录标准](docs/curation_policy.md) 与 [来源裁决](docs/research_decisions.md)。请修改 `data/projects.yaml`，不要直接维护生成的两份 README、JSON 和 BibTeX。

1. 确认属于 Agent 环境构建、任务合成、交互数据或领域评测范围，找到一手来源并阅读实质内容。
2. 选择所属大类下的小类，再查询既有 `work_id`，避免将同一论文、配套博客和代码写成独立研究成果。
3. 写中英文机制摘要、边界、证据类型、日期和短证据片段。论文使用完整作者与标题；日期用首次 arXiv 提交日期。
4. 只有核实作者关联后才填写官方代码。对空仓库、部分发布、模拟后端和评测专用任务作出明确说明。
5. 更新 GitHub 元数据，运行生成器和 verifier，检查外链报告。新增字段规则时补充必要的边界测试。
6. 若调整收录原则、分类或消歧结论，更新对应文档并写清一手依据。

```bash
.venv/bin/python scripts/render_readme.py
.venv/bin/python scripts/verify_catalog.py
.venv/bin/python scripts/verify_catalog.py --links
.venv/bin/python -m unittest discover -s tests
```

若使用 Git，提交遵循 Conventional Commits：`<type>(<scope>): <description>`，scope 可选，例如 `docs(catalog): add executable environment research`。分支使用 `docs/`、`feat/`、`fix/` 等标准前缀，不使用 `codex/`。

Do not turn HTTP success into a reproducibility claim, guess official repository names, refresh human review dates automatically, or train on held-out benchmarks merely because their task definitions are public. Third-party sources and software retain their own licenses; this catalog does not grant rights to those materials.
