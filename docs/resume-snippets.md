# 简历描述建议

## 简历项目标题

**rag-lite-kit｜轻量级 RAG 知识库问答开源项目**

## 简历描述版本 1（偏工程实现）

独立设计并开发轻量级 RAG 开源项目 `rag-lite-kit`，完成文档入库、文本切块、向量化、相似度检索、Prompt 组装与问答接口服务化的最小闭环；采用 Python + FastAPI 构建 API 层，抽象 Embedding 与 Vector Store 适配接口，支持 Memory/Chroma 双后端切换，便于后续扩展 OpenAI / DeepSeek / Ollama 等模型能力。

## 简历描述版本 2（偏岗位匹配）

围绕行业知识库问答场景，自主实现 RAG 工程骨架，支持 JSON/目录文档导入、可配置切块策略、向量检索、引用返回及 API/CLI 双调用方式；项目强调可运行性与工程扩展性，可快速演进为企业内部知识助手 PoC。

## 简历描述版本 3（偏开源表达）

发布开源项目 `rag-lite-kit`，以“低依赖可跑通 + 可扩展架构”为目标，提供面向知识库问答场景的 RAG starter，内置测试、Docker、CI 与文档体系，适合作为大模型应用工程项目模板。

## 面试可讲亮点

- 为什么默认使用 hash embedding + memory store
- 为什么把 embeddings / vector store / prompt / llm 解耦
- 如何从这个 starter 演进到真实企业 RAG 系统
- 如何加入 PDF、reranker、hybrid retrieval、评测体系
