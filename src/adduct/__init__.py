"""adduct — the health check-up for robot-learning datasets (Layer 1).

Point it at your demonstrations and get a plain-language list of the hidden defects before
you train. No simulator, no training, no ground truth, no upload — the data never leaves
the machine.

    import adduct
    report = adduct.scan("./my_teleop_data")
    print(report.score)

See ``docs/`` for the full architecture. Phase 1: reads local LeRobot datasets (v2.1 + v3)
and runs a conformally-calibrated detector battery over the frozen Canonical IR.
"""

from __future__ import annotations

from adduct.api import scan
from adduct.detectors.base import AnalysisContext, Detector, Requirements
from adduct.detectors.registry import register
from adduct.ir.schema import Family, Severity
from adduct.report.model import Cluster, Finding, Report
from adduct.version import REPORT_SCHEMA_VERSION, __version__

__all__ = [
    "REPORT_SCHEMA_VERSION",
    "AnalysisContext",
    "Cluster",
    "Detector",
    "Family",
    "Finding",
    "Report",
    "Requirements",
    "Severity",
    "__version__",
    "register",
    "scan",
]
