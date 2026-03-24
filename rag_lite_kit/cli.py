from __future__ import annotations

import argparse
import json

from .loaders import load_documents_from_directory, load_documents_from_json
from .pipeline import RAGPipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="rag-lite-kit CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest_parser = subparsers.add_parser("ingest-json", help="Ingest documents from a JSON file")
    ingest_parser.add_argument("path")

    ingest_dir_parser = subparsers.add_parser("ingest-dir", help="Ingest .txt and .md documents from a directory")
    ingest_dir_parser.add_argument("path")

    ask_parser = subparsers.add_parser("ask", help="Ask a question")
    ask_parser.add_argument("question")
    ask_parser.add_argument("--top-k", type=int, default=4)

    subparsers.add_parser("reset", help="Reset the current vector store")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    pipeline = RAGPipeline()

    if args.command == "ingest-json":
        result = pipeline.ingest(load_documents_from_json(args.path))
        print(result.model_dump_json(indent=2))
        return

    if args.command == "ingest-dir":
        result = pipeline.ingest(load_documents_from_directory(args.path))
        print(result.model_dump_json(indent=2))
        return

    if args.command == "ask":
        result = pipeline.ask(args.question, top_k=args.top_k)
        print(json.dumps(result.model_dump(), ensure_ascii=False, indent=2))
        return

    if args.command == "reset":
        pipeline.reset()
        print('{"status": "ok"}')
        return


if __name__ == "__main__":
    main()
