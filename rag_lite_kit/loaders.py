from __future__ import annotations

import json
from pathlib import Path

from .models import DocumentIn


SUPPORTED_TEXT_EXTENSIONS = {".txt", ".md"}


def load_documents_from_json(path: str | Path) -> list[DocumentIn]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    raw_docs = data["documents"] if isinstance(data, dict) and "documents" in data else data
    return [DocumentIn(**doc) for doc in raw_docs]


def load_documents_from_directory(path: str | Path) -> list[DocumentIn]:
    docs: list[DocumentIn] = []
    base = Path(path)
    for file_path in sorted(base.rglob("*")):
        if not file_path.is_file() or file_path.suffix.lower() not in SUPPORTED_TEXT_EXTENSIONS:
            continue
        text = file_path.read_text(encoding="utf-8")
        docs.append(
            DocumentIn(
                doc_id=str(file_path.relative_to(base)),
                text=text,
                metadata={"source_path": str(file_path.relative_to(base)), "suffix": file_path.suffix.lower()},
            )
        )
    return docs
