# rag-lite-kit

一个更像真实工程、而不是一次性 demo 的 **轻量级 RAG 开源 starter**。  
它面向“知识库问答 / 内部文档助手 / 行业检索增强应用”场景，提供从 **文档入库、切块、向量化、检索、回答生成，到 API/CLI 调用** 的最小可扩展闭环。

> 适合：
> - 求职作品集 / GitHub 技术名片
> - 大模型应用开发工程师岗位展示
> - 企业知识库问答 PoC
> - RAG 学习与二次开发起点

---

## 项目亮点

- **最小闭环完整**：支持 ingest → retrieve → answer 全流程
- **工程结构清晰**：模块拆分明确，适合作为二次开发骨架
- **双模式可跑**：默认使用纯 Python `hash embedding + memory store`，零外部模型即可本地体验；也支持切换到 `sentence-transformers + Chroma`
- **同时提供 API 与 CLI**：便于演示、联调和集成
- **便于扩展**：后续可平滑接入 OpenAI / DeepSeek / Ollama / reranker / hybrid search
- **开源仓库友好**：包含 CI、Dockerfile、Makefile、Contributing、Roadmap 等基础仓库资产

---

## 核心能力

### 1) 文档入库
- 支持 JSON 文档批量入库
- 支持目录扫描导入 `.txt` / `.md`
- 支持为文档附带 metadata

### 2) 文本切块
- 可配置 `chunk_size` / `chunk_overlap`
- 默认进行空白规范化

### 3) 向量化
- 默认：`hash embedding`（轻量、可测试、无需下载模型）
- 可选：`sentence-transformers`

### 4) 向量检索
- 默认：内存向量库，适合本地 demo / 单测
- 可选：Chroma 持久化向量库

### 5) 生成回答
- 内置 mock LLM，用于无外部依赖的最小闭环演示
- Prompt 层已独立，便于后续替换成真实 LLM Provider

### 6) 服务化
- FastAPI 提供 `/health`、`/ingest`、`/query`、`/reset`
- CLI 支持本地快速测试与脚本化调用

---

## 项目结构

```text
rag-lite-kit/
├── rag_lite_kit/
│   ├── api.py
│   ├── cli.py
│   ├── config.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── loaders.py
│   ├── models.py
│   ├── pipeline.py
│   ├── prompts.py
│   ├── retriever.py
│   ├── splitter.py
│   └── store.py
├── docs/
│   ├── architecture.md
│   ├── project-intro.md
│   ├── release-post.md
│   └── resume-snippets.md
├── examples/
│   └── sample_docs.json
├── tests/
├── .github/workflows/ci.yml
├── CONTRIBUTING.md
├── Dockerfile
├── Makefile
└── README.md
```

---

## 快速开始

### 方案 A：零模型依赖跑通（推荐先体验）

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp .env.example .env
pytest
uvicorn rag_lite_kit.api:app --reload
```

默认配置：
- `EMBEDDING_PROVIDER=hash`
- `VECTOR_STORE=memory`

这意味着你无需下载 embedding 模型，也无需安装 chroma，就能先把项目跑起来。

---

### 方案 B：切换到本地向量检索栈

```bash
pip install -e .[local,dev]
cp .env.example .env
```

然后修改 `.env`：

```env
EMBEDDING_PROVIDER=sentence-transformers
VECTOR_STORE=chroma
```

启动：

```bash
uvicorn rag_lite_kit.api:app --reload
```

---

## API 使用示例

### 1. 健康检查

```bash
curl http://127.0.0.1:8000/health
```

### 2. 导入示例文档

```bash
curl -X POST http://127.0.0.1:8000/ingest \
  -H "Content-Type: application/json" \
  -d @examples/sample_docs.json
```

### 3. 发起问答

```bash
curl -X POST http://127.0.0.1:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What affects retrieval quality?", "top_k": 2}'
```

### 4. 重置向量库

```bash
curl -X POST http://127.0.0.1:8000/reset
```

---

## CLI 使用示例

### 导入 JSON

```bash
rag-lite-kit ingest-json examples/sample_docs.json
```

### 导入目录下的 `.txt` / `.md`

```bash
rag-lite-kit ingest-dir ./knowledge
```

### 进行问答

```bash
rag-lite-kit ask "What affects retrieval quality?" --top-k 2
```

### 重置

```bash
rag-lite-kit reset
```

---

## 设计思路

### 为什么默认不用真实大模型？
因为这个仓库的目标不是“强依赖某个线上 API 才能跑”，而是：
1. **先让项目结构成立**
2. **先让 RAG 闭环可测试、可演示**
3. **再逐步替换成真实 provider**

这对开源项目和求职作品尤其重要：招聘方拉下来以后，应该尽量低门槛跑通。

### 为什么同时保留 memory / chroma 两种向量库？
- `memory`：适合单元测试、Demo、CI
- `chroma`：适合本地持久化 PoC

---

## Roadmap

### v0.3
- [ ] PDF / DOCX Loader
- [ ] metadata filtering
- [ ] reranker interface
- [ ] richer prompt templates
- [ ] better answer synthesis

### v0.4
- [ ] OpenAI / DeepSeek / Ollama providers
- [ ] evaluation dataset and metrics
- [ ] hybrid retrieval (keyword + vector)
- [ ] Docker Compose example

更多说明见：[docs/architecture.md](docs/architecture.md)

---

## 为什么这个项目适合写进简历

因为它对应了 JD 中最常见的几项能力：
- RAG 基础链路搭建
- Python 工程化开发
- API 服务化
- 向量检索与知识库应用
- 技术方案可扩展设计

你可以直接参考：[docs/resume-snippets.md](docs/resume-snippets.md)

---

## GitHub 发布建议

推荐仓库描述：

> A lightweight yet production-minded RAG starter kit for knowledge assistant prototypes, with API/CLI, pluggable embeddings, and vector store backends.

推荐 Topics：

```text
rag llm python fastapi chromadb vector-search knowledge-base ai-agent retrieval-augmented-generation
```

---

## 运行测试

```bash
pytest
```

---

## 贡献

欢迎提 Issue / PR。  
具体见：[CONTRIBUTING.md](CONTRIBUTING.md)

---

## License

MIT
