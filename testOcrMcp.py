#!/usr/bin/env python3

import sys
import json
from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image

# Load your Donut model
processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base")
model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base")

def ocr_invoice(image_path):
    """
    Run Donut OCR on an image file path.
    """
    image = Image.open(image_path)
    pixel_values = processor(image, return_tensors="pt").pixel_values
    output = model.generate(pixel_values, max_length=512)
    text = processor.batch_decode(output, skip_special_tokens=True)[0]
    return {"extracted_text": text}

# Main loop for stdio JSON-RPC
for line in sys.stdin:
    try:
        request = json.loads(line)
        method = request.get("method")
        id_ = request.get("id")

        if method == "list_tools":
            tools = [{
                "name": "ocr_invoice",
                "description": "Extract text from an invoice image using Donut OCR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "image_path": {"type": "string"}
                    },
                    "required": ["image_path"]
                }
            }]
            result = tools
        elif method == "tools/call":
            tool_name = request["params"]["name"]
            arguments = request["params"]["arguments"]
            if tool_name == "ocr_invoice":
                result = ocr_invoice(arguments["image_path"])
            else:
                result = {"error": f"Unknown tool: {tool_name}"}
        else:
            result = {"error": f"Unknown method: {method}"}

        response = {
            "jsonrpc": "2.0",
            "id": id_,
            "result": result
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()

    except Exception as e:
        error_response = {
            "jsonrpc": "2.0",
            "id": None,
            "error": str(e)
        }
        sys.stdout.write(json.dumps(error_response) + "\n")
        sys.stdout.flush()
