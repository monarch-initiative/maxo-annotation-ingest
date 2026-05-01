"""Upstream source version fetcher for maxo-annotation-ingest.

MAxO annotations are tracked from a github master branch (no formal
releases for the annotations file), so the version is the latest
commit SHA on the maxo-annotations repo.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from kozahub_metadata_schema import (
    now_iso,
    urls_from_download_yaml,
    version_from_github_branch,
)


INGEST_DIR = Path(__file__).resolve().parents[1]
DOWNLOAD_YAML = INGEST_DIR / "download.yaml"


def get_source_versions() -> list[dict[str, Any]]:
    ver, method = version_from_github_branch(
        "monarch-initiative/maxo-annotations", branch="master"
    )
    return [
        {
            "id": "infores:maxo-annotations",
            "name": "MAxO (Medical Action Ontology) Annotations",
            "urls": urls_from_download_yaml(DOWNLOAD_YAML),
            "version": ver,
            "version_method": method,
            "retrieved_at": now_iso(),
        }
    ]
