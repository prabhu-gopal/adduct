"""Stage ⑥ — the report model and renderers (docs/02 §6, docs/03 §7)."""

from __future__ import annotations

from adduct.report.base import Renderer
from adduct.report.html import HtmlRenderer
from adduct.report.model import (
    BlastRadius,
    Cluster,
    DatasetInfo,
    Evidence,
    Finding,
    Fix,
    Locus,
    Report,
)
from adduct.report.tty import TtyRenderer

__all__ = [
    "BlastRadius",
    "Cluster",
    "DatasetInfo",
    "Evidence",
    "Finding",
    "Fix",
    "HtmlRenderer",
    "Locus",
    "Renderer",
    "Report",
    "TtyRenderer",
]
