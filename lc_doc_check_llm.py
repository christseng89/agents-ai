# lc_doc_check_llm.py
"""
Simulated Agentic AI pipeline for Letter of Credit (LC) document checking using LangChain.

This skeleton shows how you might wire together multiple autonomous agents (each as a LangChain
Tool or Runnable) to execute the full LC checking workflow:

1. LC Extractor Agent          – parse MT700 / PDF LC to JSON terms
2. Document Classifier Agent   – tag each uploaded document type
3. Data Extraction Agent       – pull key fields from each document
4. Compliance Validator Agent  – compare fields against LC terms & ICC rules
5. Discrepancy Identifier Agent– list discrepancies with justification
6. Decision Agent              – recommend accept/reject/waive
7. Report Generator Agent      – compile final PDF / JSON report

Replace each TODO section with concrete logic, e.g. OCR calls, regex/LLM parsing, rule‑based checks, etc.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Any

from langchain.agents import initialize_agent, AgentType, AgentExecutor
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.tools import Tool

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
OPENAI_MODEL = "gpt-4o-mini"  # Or your preferred model
TEMPERATURE = 0.0

# -----------------------------------------------------------------------------
# Helper stubs (you will implement these)
# -----------------------------------------------------------------------------

def load_file_bytes(file_path: Path) -> bytes:
    """Utility: read a file and return its bytes (for OCR or base64)."""
    return file_path.read_bytes()


# 1️⃣ LC Extractor -------------------------------------------------------------

def lc_extractor(file_bytes: bytes) -> Dict[str, Any]:
    """Parse LC (MT700 PDF or SWIFT message) and return structured JSON terms.
    TODO: implement OCR / LLM extraction / regex depending on input format.
    """
    # dummy output
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
            "Certificate of Origin"
        ],
    }


# 2️⃣ Document Classifier ------------------------------------------------------

def doc_classifier(files: List[bytes]) -> Dict[str, List[int]]:
    """Return a mapping: doc_type -> list of index positions within `files`.
    TODO: implement with ML model or LLM few‑shot classification.
    """
    # dummy: assume sequential order
    return {
        "Commercial Invoice": [0],
        "Bill of Lading": [1],
        "Packing List": [2],
        "Certificate of Origin": [3],
    }


# 3️⃣ Data Extraction ----------------------------------------------------------

def data_extractor(classified_files: Dict[str, List[int]], files: List[bytes]) -> Dict[str, Dict[str, Any]]:
    """Extract required fields from each document and return nested JSON.
    TODO: OCR / LLM / rule‑based extraction.
    """
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


# 4️⃣ Compliance Validator -----------------------------------------------------

def compliance_validator(lc_terms: Dict[str, Any], doc_data: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Compare extracted document data with LC terms & ICC rules.
    Return a dict containing pass/fail status and raw details.
    TODO: encode UCP 600 + ISBP logic.
    """
    # dummy compliance example
    discrepancies = []
    if doc_data["Commercial Invoice"]["invoice_value"] > lc_terms["amount"]:
        discrepancies.append({
            "doc": "Commercial Invoice",
            "field": "invoice_value",
            "issue": "Invoice amount exceeds LC amount",
            "rule_ref": "UCP 600 Art. 18(b)"
        })
    return {
        "is_compliant": len(discrepancies) == 0,
        "discrepancies": discrepancies,
    }


# 5️⃣ Discrepancy Identifier ---------------------------------------------------

def discrepancy_identifier(validation_result: Dict[str, Any]) -> List[Dict[str, str]]:
    """Produce human‑readable discrepancy list with ICC justification."""
    return validation_result["discrepancies"]


# 6️⃣ Decision Agent -----------------------------------------------------------

LLM_SYSTEM_PROMPT = (
    "You are a senior LC document checker following UCP 600 and ISBP 821. "
    "Given LC terms and discrepancy list, decide whether to Accept, Reject, or "
    "Request Waiver. Justify your decision concisely citing ICC rules."
)


def decision_agent(lc_terms: Dict[str, Any], discrepancies: List[Dict[str, str]]) -> Dict[str, str]:
    llm = ChatOpenAI(model_name=OPENAI_MODEL, temperature=TEMPERATURE)
    messages = [
        SystemMessage(content=LLM_SYSTEM_PROMPT),
        HumanMessage(content=json.dumps({
            "lc_terms": lc_terms,
            "discrepancies": discrepancies,
        }))
    ]
    response = llm(messages)
    return {"decision": response.content.strip()}


# 7️⃣ Report Generator ---------------------------------------------------------

def report_generator(
    lc_terms: Dict[str, Any],
    doc_data: Dict[str, Dict[str, Any]],
    discrepancies: List[Dict[str, str]],
    decision_summary: Dict[str, str],
) -> str:
    """Generate a simple JSON report (could be extended to PDF)."""
    report = {
        "LC Terms": lc_terms,
        "Document Data": doc_data,
        "Discrepancies": discrepancies,
        "Decision": decision_summary,
    }
    return json.dumps(report, indent=2, ensure_ascii=False)


# -----------------------------------------------------------------------------
# Wrap Agent Functions as LangChain Tools
# -----------------------------------------------------------------------------

lc_extractor_tool = Tool(
    name="lc_extractor",
    func=lambda x: lc_extractor(x),
    description="Extract structured LC terms from an LC PDF or MT700 bytes.",
)

doc_classifier_tool = Tool(
    name="doc_classifier",
    func=lambda x: doc_classifier(x),
    description="Classify list[bytes] into document types required by the LC.",
)

data_extractor_tool = Tool(
    name="data_extractor",
    func=lambda x: data_extractor(x["classified_files"], x["files"]),
    description="Extract key trade data fields from classified documents.",
)

compliance_validator_tool = Tool(
    name="compliance_validator",
    func=lambda x: compliance_validator(x["lc_terms"], x["doc_data"]),
    description="Validate documents against LC terms and ICC rules.",
)

discrepancy_identifier_tool = Tool(
    name="discrepancy_identifier",
    func=lambda x: discrepancy_identifier(x),
    description="Generate discrepancy list with rule justification.",
)

decision_agent_tool = Tool(
    name="decision_agent",
    func=lambda x: decision_agent(x["lc_terms"], x["discrepancies"]),
    description="Decide accept/reject/waive based on discrepancies and LC.",
)

report_generator_tool = Tool(
    name="report_generator",
    func=lambda x: report_generator(
        x["lc_terms"], x["doc_data"], x["discrepancies"], x["decision"]
    ),
    description="Compile final LC checking report in JSON.",
)

# Collect tools in execution order (for OPENAI_FUNCTIONS agent)
TOOLS = [
    lc_extractor_tool,
    doc_classifier_tool,
    data_extractor_tool,
    compliance_validator_tool,
    discrepancy_identifier_tool,
    decision_agent_tool,
    report_generator_tool,
]


# -----------------------------------------------------------------------------
# Orchestrator / Pipeline Execution
# -----------------------------------------------------------------------------

def run_pipeline(lc_file: Path, doc_files: List[Path]) -> str:
    """High‑level wrapper to run the full LC checking pipeline and return report."""
    llm = ChatOpenAI(model_name=OPENAI_MODEL, temperature=TEMPERATURE)

    agent: AgentExecutor = initialize_agent(
        TOOLS,
        llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
    )

    # 1. Read all files into bytes -------------------------------------------
    lc_bytes = load_file_bytes(lc_file)
    docs_bytes = [load_file_bytes(p) for p in doc_files]

    # 2. Agent step 1 – extract LC terms -------------------------------------
    lc_terms = agent.run(tool="lc_extractor", tool_input=lc_bytes)

    # 3. Agent step 2 – classify documents -----------------------------------
    classified_files = agent.run(tool="doc_classifier", tool_input=docs_bytes)

    # 4. Agent step 3 – data extraction --------------------------------------
    doc_data = agent.run(
        tool="data_extractor",
        tool_input={"classified_files": classified_files, "files": docs_bytes},
    )

    # 5. Agent step 4 – compliance validation --------------------------------
    validation_result = agent.run(
        tool="compliance_validator",
        tool_input={"lc_terms": lc_terms, "doc_data": doc_data},
    )

    # 6. Agent step 5 – discrepancy identification ---------------------------
    discrepancies = agent.run(tool="discrepancy_identifier", tool_input=validation_result)

    # 7. Agent step 6 – decision agent ---------------------------------------
    decision = agent.run(
        tool="decision_agent",
        tool_input={"lc_terms": lc_terms, "discrepancies": discrepancies},
    )

    # 8. Agent step 7 – report generation ------------------------------------
    report = agent.run(
        tool="report_generator",
        tool_input={
            "lc_terms": lc_terms,
            "doc_data": doc_data,
            "discrepancies": discrepancies,
            "decision": decision,
        },
    )

    return report


if __name__ == "__main__":
    # Example usage ----------------------------------------------------------
    SAMPLE_LC = Path("sample_mt700.pdf")
    SAMPLE_DOCS = [
        Path("invoice.pdf"),
        Path("bl.pdf"),
        Path("packing_list.pdf"),
        Path("co.pdf"),
    ]

    # For demo purposes, you might stub these files or mock load_file_bytes.
    final_report = run_pipeline(SAMPLE_LC, SAMPLE_DOCS)
    print("\n===== LC CHECKING REPORT =====\n")
    print(final_report)
