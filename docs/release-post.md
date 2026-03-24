# 发布文案

## GitHub 仓库简介（短版）

`rag-lite-kit` 是一个轻量级、可扩展的 RAG starter，面向知识库问答 / 内部文档助手 / 大模型应用工程实践。项目提供 ingest → retrieve → answer 的最小闭环，并支持 API / CLI 双入口，适合作为学习、PoC 和求职作品集项目。

## GitHub 发布文案（中文版）

最近整理了一个自己用于 RAG 场景练习和作品集展示的开源项目：**rag-lite-kit**。

它不是只演示概念的一次性 demo，而是尽量把一个知识库问答应用的基础工程骨架搭完整：
- 支持文档入库
- 支持切块、向量化、检索、回答生成
- 提供 FastAPI + CLI 双入口
- 默认可用 hash embedding + memory store 低门槛跑通
- 可继续扩展到 Chroma / sentence-transformers / OpenAI / Ollama

如果你也在做：
- RAG 学习
- 企业知识库问答 PoC
- 大模型应用工程求职作品

欢迎交流，提 issue / PR 也非常欢迎。

## GitHub 发布文案（英文版）

I just open-sourced **rag-lite-kit**, a lightweight yet production-minded RAG starter for knowledge assistant prototypes.

It covers the core flow from ingestion to retrieval and answer generation, while keeping the structure simple enough for learning, demos, and portfolio use:
- document ingestion
- chunking
- pluggable embeddings
- vector retrieval
- FastAPI service
- CLI entrypoint
- low-friction local run path

If you are working on RAG demos, internal knowledge assistants, or LLM application engineering portfolio projects, this repo may be a useful starting point.
