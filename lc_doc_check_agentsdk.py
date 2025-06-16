# lc_doc_check_agentsdk.py
"""
Simulated Agentic AI pipeline for LC document checking using **OpenAI Agents SDK**.

The Agents SDK (beta) lets you programmatically define **tool functions** and
invoke them via automatic function‑calling.  This skeleton shows how to expose
seven domain‑specific tools, then orchestrate them step‑by‑step to achieve the
same workflow we outlined earlier (LC Extractor → Document Classifier → … →
Report Generator).

Replace the TODO sections with real OCR / ICC rule logic as needed.  The goal is
clarity on structure, not full production code.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List

import openai

# -----------------------------------------------------------------------------
# 0. OpenAI client setup -------------------------------------------------------
# -----------------------------------------------------------------------------
openai.api_key = os.getenv("OPENAI_API_KEY", "sk‑…REPLACE_ME…")  # noqa: E501
MODEL = "gpt-4o-mini"

# -----------------------------------------------------------------------------
# 1. DOMAIN TOOL DEFINITIONS ---------------------------------------------------
# -----------------------------------------------------------------------------
# Each tool is a normal Python function.  Its signature & docstring become the
# JSON schema that the Agents SDK uses for function‑calling.
# -----------------------------------------------------------------------------

def lc_extractor(lc_bytes_b64: str) -> Dict[str, Any]:
    """Parse an LC (MT700 PDF or Swift message) and return structured terms.

    Args:
        lc_bytes_b64: base64‑encoded binary of the LC document.
    Returns:
        JSON object containing applicant, beneficiary, amount, currency, expiry,
        latest_shipment, and list of required documents.
    """
    # TODO: implement real extraction (OCR + LLM).
    return {
        "applicant": "ABC Importers Ltd.",
        "beneficiary": "XYZ Exporters Inc.",
        "amount": 100000,
        "currency": "USD",
        "expiry_date": "2025-12-31",
        "latest_shipment": "2025-11-30",
        "req_documents": [
            "Commercial Invoice",
            "Bill of Lading",
            "Packing List",
            "Certificate of Origin",
        ],
    }


def doc_classifier(docs_b64: List[str]) -> Dict[str, List[int]]:
    """Classify each uploaded document into trade‑doc types.

    Args:
        docs_b64: list of base64‑encoded binary docs (order preserved).
    Returns:
        Mapping of doc_type → list of indices referring back to docs_b64.
    """
    # TODO: implement ML / LLM classifier.
    return {
        "Commercial Invoice": [0],
        "Bill of Lading": [1],
        "Packing List": [2],
        "Certificate of Origin": [3],
    }


def data_extractor(classified_map: Dict[str, List[int]], docs_b64: List[str]) -> Dict[str, Dict[str, Any]]:
    """Extract key fields from each classified document.

    Args:
        classified_map: output of `doc_classifier`.
        docs_b64: raw files list to extract from.
    Returns:
        Nested JSON of extracted fields by doc_type.
    """
    # TODO: implement custom logic.
    return {
        "Commercial Invoice": {
            "invoice_value": 99999,
            "invoice_date": "2025-10-01",
        },
        "Bill of Lading": {
            "port_of_loading": "Shanghai",
            "port_of_discharge": "New York",
            "on_board_date": "2025-10-15",
        },
        "Packing List": {},
        "Certificate of Origin": {
            "country": "CN",
        },
    }


def compliance_validator(lc_terms: Dict[str, Any], doc_data: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Validate extracted data against LC terms & ICC rules.

    Args:
        lc_terms: structured LC JSON from `lc_extractor`.
        doc_data: field extractions from `data_extractor`.
    Returns:
        Dict with `is_compliant` bool and `discrepancies` list.
    """
    disc = []
    if doc_data["Commercial Invoice"]["invoice_value"] > lc_terms["amount"]:
        disc.append({
            "doc": "Commercial Invoice",
            "field": "invoice_value",
            "issue": "Invoice amount exceeds LC amount",
            "rule_ref": "UCP 600 Art. 18(b)",
        })
    return {"is_compliant": not disc, "discrepancies": disc}


def discrepancy_identifier(validation_result: Dict[str, Any]) -> List[Dict[str, str]]:
    """Return list of discrepancy objects for human review."""
    return validation_result["discrepancies"]


def decision_agent(lc_terms: Dict[str, Any], discrepancies: List[Dict[str, str]]) -> Dict[str, str]:
    """Use GPT‑4o to recommend ACCEPT / REJECT / WAIVE and rationale."""
    sys = (
        "You are an expert trade‑finance document checker following UCP 600 & ISBP. "
        "Review LC terms & discrepancy list, then respond with JSON: {'decision': str, 'reason': str}."
    )
    resp = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": sys},
            {"role": "user", "content": json.dumps({
                "lc_terms": lc_terms,
                "discrepancies": discrepancies,
            })},
        ],
        temperature=0,
    )
    return json.loads(resp.choices[0].message.content)


def report_generator(lc_terms: Dict[str, Any], doc_data: Dict[str, Dict[str, Any]], discrepancies: List[Dict[str, str]], decision: Dict[str, str]) -> str:
    """Compile final LC checking report (JSON string)."""
    report = {
        "LC Terms": lc_terms,
        "Document Data": doc_data,
        "Discrepancies": discrepancies,
        "Decision": decision,
    }
    return json.dumps(report, indent=2, ensure_ascii=False)


# -----------------------------------------------------------------------------
# 2. TOOL REGISTRATION ---------------------------------------------------------
# -----------------------------------------------------------------------------
TOOLS = [
    {
        "type": "function",
        "function": lc_extractor,
    },
    {"type": "function", "function": doc_classifier},
    {"type": "function", "function": data_extractor},
    {"type": "function", "function": compliance_validator},
    {"type": "function", "function": discrepancy_identifier},
    {"type": "function", "function": decision_agent},
    {"type": "function", "function": report_generator},
]

# -----------------------------------------------------------------------------
# 3. ORCHESTRATION LOGIC -------------------------------------------------------
# -----------------------------------------------------------------------------
# In the Agents SDK you usually drive the chain with a while‑loop handling every
# assistant response.  Below is a linear helper (`step_call`) to simplify.
# -----------------------------------------------------------------------------

def step_call(function_name: str, args: Any):
    """Invoke `function_name` via function‑calling and return parsed JSON."""
    chat_resp = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": json.dumps(args),
                "tool_choice": {"name": function_name},
            }
        ],
        tools=TOOLS,
    )
    tool_call = chat_resp.choices[0].message.tool_calls[0]
    return json.loads(tool_call.function.arguments)


# -----------------------------------------------------------------------------
# 4. PIPELINE WRAPPER ----------------------------------------------------------
# -----------------------------------------------------------------------------

def run_pipeline(lc_path: Path, doc_paths: List[Path]) -> str:
    """Execute the full LC checking pipeline and return final JSON report."""
    import base64

    # Load & base64‑encode files so they can be passed as JSON safely.
    lc_b64 = base64.b64encode(lc_path.read_bytes()).decode()
    docs_b64 = [base64.b64encode(p.read_bytes()).decode() for p in doc_paths]

    lc_terms = step_call("lc_extractor", lc_b64)
    classified = step_call("doc_classifier", docs_b64)
    doc_data = step_call("data_extractor", {"classified_map": classified, "docs_b64": docs_b64})
    validation = step_call("compliance_validator", {"lc_terms": lc_terms, "doc_data": doc_data})
    discrepancies = step_call("discrepancy_identifier", validation)
    decision = step_call("decision_agent", {"lc_terms": lc_terms, "discrepancies": discrepancies})
    final_report = step_call(
        "report_generator",
        {
            "lc_terms": lc_terms,
            "doc_data": doc_data,
            "discrepancies": discrepancies,
            "decision": decision,
        },
    )
    return final_report


if __name__ == "__main__":
    SAMPLE_LC = Path("sample_mt700.pdf")
    SAMPLE_DOCS = [
        Path("invoice.pdf"),
        Path("bl.pdf"),
        Path("packing_list.pdf"),
        Path("co.pdf"),
    ]

    report_json = run_pipeline(SAMPLE_LC, SAMPLE_DOCS)
    print("\n========== LC DOCUMENT CHECK REPORT ==========")
    print(report_json)
